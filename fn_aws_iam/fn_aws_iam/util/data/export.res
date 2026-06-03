{
  "action_order": [],
  "actions": [
    {
      "automations": [
        {
          "scripts_to_run": "scr_aws_iam_add_access_key_as_artifact",
          "type": "run_script",
          "value": null
        }
      ],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.AccessKeyId",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Add Access Key As Artifact",
      "id": 27,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Add Access Key As Artifact",
      "object_type": "aws_iam_access_keys",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "b4296cdf-6a53-47fc-8278-5598607a0a5e",
      "view_items": [],
      "workflows": []
    },
    {
      "automations": [
        {
          "scripts_to_run": "scr_aws_iam_add_user_as_artifact",
          "type": "run_script",
          "value": null
        }
      ],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Add User As Artifact",
      "id": 28,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Add User As Artifact",
      "object_type": "aws_iam_users",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "38fe8eeb-cd21-4b44-a006-82fb4223693d",
      "view_items": [],
      "workflows": []
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.DefaultUser",
          "method": "not_equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Add User To Group",
      "id": 29,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Add User To Group",
      "object_type": "aws_iam_users",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d151b2c5-4faf-4db1-bbd6-acb09f3d91a6",
      "view_items": [
        {
          "content": "6a273ffd-f8b1-4edc-90dd-abc2d4ba7179",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_add_user_to_group"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.DefaultUser",
          "method": "not_equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Attach User Policy",
      "id": 30,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Attach User Policy",
      "object_type": "aws_iam_users",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f86c8f0a-5af1-4989-857f-9a1d7a6b398c",
      "view_items": [
        {
          "content": "7660ab32-6584-4c61-a2d5-6fd42349e658",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_attach_user_policy"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.DefaultUser",
          "method": "not_equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.LoginProfileExists",
          "method": "equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Change Profile Password",
      "id": 31,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Change Profile Password",
      "object_type": "aws_iam_users",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "645f519f-a6dd-461d-873b-4a5e7f88dc58",
      "view_items": [
        {
          "content": "34c2782e-4f1b-4515-8348-7edb2724c037",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "03e32eee-9433-4e65-ae51-1fbe742412b5",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_change_profile_password"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.AccessKeyId",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.DefaultKey",
          "method": "not_equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.Status",
          "method": "equals",
          "type": null,
          "value": "Active"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.Status",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Deactivate Access Key",
      "id": 32,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Deactivate Access Key",
      "object_type": "aws_iam_access_keys",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e76a8697-a5d9-4d0f-b6e9-1f1b50ae2359",
      "view_items": [
        {
          "content": "\u003cdiv\u003e Are you sure that you want to deactivate the access key? \u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_deactivate_access_key"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.AccessKeyId",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.DefaultKey",
          "method": "not_equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Delete Access Key",
      "id": 33,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Delete Access Key",
      "object_type": "aws_iam_access_keys",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "3598bc44-ec2d-40b8-99fa-ff9b23ac985c",
      "view_items": [
        {
          "content": "\u003cdiv\u003e Are you sure that you want to delete the access key? \u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_delete_access_key"
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
          "value": "aws_iam_access_key_id"
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Delete Access Key For Artifact",
      "id": 34,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Delete Access Key For Artifact",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e30b7929-e896-439d-8af3-22576618c9f9",
      "view_items": [
        {
          "content": "\u003cdiv\u003e Are you sure that you want to delete the access key? \u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_delete_access_key_for_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.AccessKeyIds",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.DefaultUser",
          "method": "not_equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Delete Access Keys",
      "id": 35,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Delete Access Keys",
      "object_type": "aws_iam_users",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6d9c639d-115d-4e2a-8b8a-52ddc8665185",
      "view_items": [
        {
          "content": "\u003cdiv\u003e Are you sure that you want to delete the access keys? \u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_delete_access_keys"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.DefaultUser",
          "method": "not_equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.LoginProfileExists",
          "method": "equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Delete Login Profile",
      "id": 36,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Delete Login Profile",
      "object_type": "aws_iam_users",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "a59b1cba-1060-4a27-9bfb-3491964f8571",
      "view_items": [
        {
          "content": "\u003cdiv\u003e Are you sure that you want to delete the user login profile? \u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_delete_login_profile"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.DefaultUser",
          "method": "not_equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Delete User",
      "id": 37,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Delete User",
      "object_type": "aws_iam_users",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "d3e3ee5f-1b56-481a-8d04-db0d0a8c3b95",
      "view_items": [
        {
          "content": "\u003cdiv\u003e Are you sure that you want to delete the user? \u003c/div\u003e\n\u003cdiv\u003e \nNote: The following items in AWS IAM if associated with the user will be removed, de-activated or deleted:\n\u003col\u003e\n   \u003cli\u003eDelete login profile.\u003c/li\u003e\n    \u003cli\u003eDelete access keys.\u003c/li\u003e\n    \u003cli\u003eDelete inline policies.\u003c/li\u003e\n    \u003cli\u003eDetach managed policies.\u003c/li\u003e\n    \u003cli\u003eRemove user from groups.\u003c/li\u003e\n    \u003cli\u003eDelete signing certificates.\u003c/li\u003e\n    \u003cli\u003eDelete SSH public keys.\u003c/li\u003e\n   \u003cli\u003eDelete service specific credentials.\u003c/li\u003e\n   \u003cli\u003eDe-activate MFA devices.\u003c/li\u003e\n \u003cli\u003eDelete virtual MFA devices.\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_delete_user"
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
          "value": "aws_iam_user_name"
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Delete User For Artifact",
      "id": 38,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Delete User For Artifact",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "f9368c9d-6db4-46eb-9515-e8fe0a0bf639",
      "view_items": [
        {
          "content": "\u003cdiv\u003e Are you sure that you want to delete the user? \u003c/div\u003e\n\u003cdiv\u003e \nNote: The following items in AWS IAM if associated with the user will be removed, de-activated or deleted:\n\u003col\u003e\n   \u003cli\u003eDelete login profile.\u003c/li\u003e\n    \u003cli\u003eDelete access keys.\u003c/li\u003e\n    \u003cli\u003eDelete inline policies.\u003c/li\u003e\n    \u003cli\u003eDetach managed policies.\u003c/li\u003e\n    \u003cli\u003eRemove user from groups.\u003c/li\u003e\n    \u003cli\u003eDelete signing certificates.\u003c/li\u003e\n    \u003cli\u003eDelete SSH public keys.\u003c/li\u003e\n   \u003cli\u003eDelete service specific credentials.\u003c/li\u003e\n   \u003cli\u003eDe-activate MFA devices.\u003c/li\u003e\n \u003cli\u003eDelete virtual MFA devices.\u003c/li\u003e\n\u003c/ol\u003e\n\u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_delete_user_for_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.DefaultUser",
          "method": "not_equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Policies",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Detach All User Policies",
      "id": 39,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Detach All User Policies",
      "object_type": "aws_iam_users",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "158da16d-3d1d-4640-a1be-4fa302a9b8b3",
      "view_items": [
        {
          "content": "\u003cdiv\u003e Are you sure that you want to detach all policies for the user? \u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_detach_all_user_policies"
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
          "value": "aws_iam_access_key_id"
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Get access Key For Artifact",
      "id": 40,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Get access Key For Artifact",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "e5330fe4-4c90-4cba-aa00-340b043f476d",
      "view_items": [],
      "workflows": [
        "wf_aws_iam_get_access_key_for_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.AccessKeyIds",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Get Access Keys",
      "id": 41,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Get Access Keys",
      "object_type": "aws_iam_users",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "ae985ccf-eddf-4951-8b11-e5c7eb314b20",
      "view_items": [],
      "workflows": [
        "wf_aws_iam_get_access_keys"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.AccessKeyId",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Get User",
      "id": 42,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Get User",
      "object_type": "aws_iam_access_keys",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "6b505a60-44a6-41d6-9325-0db4eb383d84",
      "view_items": [],
      "workflows": [
        "wf_aws_iam_get_user"
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
          "value": "aws_iam_user_name"
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Get User For Artifact",
      "id": 43,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Get User For Artifact",
      "object_type": "artifact",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "2b14d3c8-3743-42c4-b5cc-0e3b2ecce725",
      "view_items": [],
      "workflows": [
        "wf_aws_iam_get_user_for_artifact"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: AWS IAM: List Access Keys",
      "id": 44,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: List Access Keys",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "616822ef-18ee-4d2b-9b03-8511f1276d4c",
      "view_items": [
        {
          "content": "613f7245-6c9c-4a75-8c9a-2ece77101a0a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3c684c12-49a8-4119-8a02-f7929e5cb69d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_list_access_keys"
      ]
    },
    {
      "automations": [],
      "conditions": [],
      "enabled": true,
      "export_key": "Example: AWS IAM: List Users",
      "id": 45,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: List Users",
      "object_type": "incident",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4e391fa2-37eb-47b5-beb8-35dd01c7ea03",
      "view_items": [
        {
          "content": "613f7245-6c9c-4a75-8c9a-2ece77101a0a",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "9ed0bd41-cb3f-465d-b58e-33e96d7b8c9e",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3c9e9fbd-0f58-41b7-8d7a-92410ff7b1d1",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "3c684c12-49a8-4119-8a02-f7929e5cb69d",
          "element": "field_uuid",
          "field_type": "actioninvocation",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_list_users"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.AccessKeyId",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_access_keys.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Refresh Access Key",
      "id": 46,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Refresh Access Key",
      "object_type": "aws_iam_access_keys",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "1b29b32f-502a-4713-adcd-a18d239cb7fb",
      "view_items": [],
      "workflows": [
        "wf_aws_iam_refresh_access_key"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Refresh User",
      "id": 47,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Refresh User",
      "object_type": "aws_iam_users",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "4ba9c798-783f-40e2-841a-1cf2a18b3084",
      "view_items": [],
      "workflows": [
        "wf_aws_iam_refresh_user"
      ]
    },
    {
      "automations": [],
      "conditions": [
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.DefaultUser",
          "method": "not_equals",
          "type": null,
          "value": "Yes"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Groups",
          "method": "has_a_value",
          "type": null,
          "value": null
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.Status",
          "method": "not_equals",
          "type": null,
          "value": "Deleted"
        },
        {
          "evaluation_id": null,
          "field_name": "aws_iam_users.UserName",
          "method": "has_a_value",
          "type": null,
          "value": null
        }
      ],
      "enabled": true,
      "export_key": "Example: AWS IAM: Remove User From All Groups",
      "id": 48,
      "logic_type": "all",
      "message_destinations": [],
      "name": "Example: AWS IAM: Remove User From All Groups",
      "object_type": "aws_iam_users",
      "tags": [],
      "timeout_seconds": 86400,
      "type": 1,
      "uuid": "8bbd56db-9df9-4959-964e-208e5320182c",
      "view_items": [
        {
          "content": "\u003cdiv\u003e Are you sure that you want to remove the user from all groups? \u003c/div\u003e",
          "element": "html",
          "field_type": null,
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        }
      ],
      "workflows": [
        "wf_aws_iam_remove_user_from_all_groups"
      ]
    }
  ],
  "apps": [],
  "automatic_tasks": [],
  "case_matching_profiles": [],
  "export_date": 1719811198557,
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
      "export_key": "__function/aws_iam_password",
      "hide_notification": false,
      "id": 672,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_password",
      "tooltip": "AWS IAM password for user login profile.",
      "type_id": 11,
      "uuid": "93a81af4-7d79-4de1-a0cb-30000bff6e61",
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
      "export_key": "__function/aws_iam_status",
      "hide_notification": false,
      "id": 673,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_status",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_status",
      "tooltip": "",
      "type_id": 11,
      "uuid": "95e86085-40e3-4dbf-a989-9c2deaa3c1e4",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "Inactive",
          "properties": null,
          "uuid": "7456ec52-5061-4b31-8137-092c9ea29d1a",
          "value": 108
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Active",
          "properties": null,
          "uuid": "ab3b4944-32a0-483b-9973-9d99caae1bda",
          "value": 109
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
      "export_key": "__function/aws_iam_ssh_key_ids",
      "hide_notification": false,
      "id": 674,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_ssh_key_ids",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_ssh_key_ids",
      "tooltip": "",
      "type_id": 11,
      "uuid": "b190100f-4a02-476c-8993-75733bdbcca3",
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
      "export_key": "__function/aws_iam_access_key_filter",
      "hide_notification": false,
      "id": 675,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_access_key_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_access_key_filter",
      "tooltip": "Filter by access key id. Can be a string or regular expression.",
      "type_id": 11,
      "uuid": "b1ac6bbb-8bab-47ac-88a0-028deb661096",
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
      "export_key": "__function/aws_iam_policy_names",
      "hide_notification": false,
      "id": 676,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_policy_names",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_policy_names",
      "tooltip": "Comma separated list of AWS IAM policy names.",
      "type_id": 11,
      "uuid": "cecc9df4-afea-49f7-95b4-f434fb381425",
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
      "export_key": "__function/aws_iam_user_name",
      "hide_notification": false,
      "id": 677,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_user_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "AWS IAM user name",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_user_name",
      "tooltip": "AWS IAM user name.",
      "type_id": 11,
      "uuid": "d7d96d4f-e23e-436c-be00-7204ed33694b",
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
      "export_key": "__function/aws_iam_ssc_ids",
      "hide_notification": false,
      "id": 678,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_ssc_ids",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_ssc_ids",
      "tooltip": "",
      "type_id": 11,
      "uuid": "e867f22c-33f5-470b-bfdf-915af174c8bc",
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
      "export_key": "__function/aws_iam_mfa_serial_nums",
      "hide_notification": false,
      "id": 679,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_mfa_serial_nums",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_mfa_serial_nums",
      "tooltip": "",
      "type_id": 11,
      "uuid": "ed50aaeb-760f-4b76-87c3-b5546e4edf2a",
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
      "export_key": "__function/aws_iam_access_keys",
      "hide_notification": false,
      "id": 680,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_access_keys",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_access_keys",
      "tooltip": "Comma seperated list of AWS IAM access key names.",
      "type_id": 11,
      "uuid": "0c8b7db1-ddd1-4c1d-bb93-98df99153ac2",
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
      "export_key": "__function/aws_iam_query_type",
      "hide_notification": false,
      "id": 681,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_query_type",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_query_type",
      "tooltip": "Type of query to perform for list_users. Can be one of \u0027users\u0027 or \u0027access_keys\u0027.",
      "type_id": 11,
      "uuid": "136e1156-7875-4314-ad4a-729b5026c5ce",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "users",
          "properties": null,
          "uuid": "e85f91d4-3011-4878-950f-a9b96217d3f6",
          "value": 110
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "access_keys",
          "properties": null,
          "uuid": "c9a6c66b-1deb-409b-8d8a-6ef9a98770e2",
          "value": 111
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
      "export_key": "__function/aws_iam_group_names",
      "hide_notification": false,
      "id": 682,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_group_names",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_group_names",
      "tooltip": "Comma separated list of AWS IAM group names.",
      "type_id": 11,
      "uuid": "38083166-fa87-4360-86a5-ca8befac8788",
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
      "export_key": "__function/aws_iam_policy_filter",
      "hide_notification": false,
      "id": 683,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_policy_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_policy_filter",
      "tooltip": "Filter by policy name. Can be a string or regular expression.",
      "type_id": 11,
      "uuid": "389645a9-c932-45a6-9b29-3b422b0ca40e",
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
      "export_key": "__function/aws_iam_access_key_id",
      "hide_notification": false,
      "id": 684,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_access_key_id",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_access_key_id",
      "tooltip": "",
      "type_id": 11,
      "uuid": "458744ef-622f-4a00-8a8f-58545eb2cb6d",
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
      "export_key": "__function/aws_iam_sign_cert_ids",
      "hide_notification": false,
      "id": 685,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_sign_cert_ids",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_sign_cert_ids",
      "tooltip": "",
      "type_id": 11,
      "uuid": "5072b195-f75d-4bc7-a7c2-8986fb372125",
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
      "export_key": "__function/aws_iam_password_reset_required",
      "hide_notification": false,
      "id": 686,
      "input_type": "boolean",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_password_reset_required",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_password_reset_required",
      "tooltip": "Password reset required on next login.",
      "type_id": 11,
      "uuid": "5106b8bf-edf9-460c-bca5-bffbe602fb36",
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
      "export_key": "__function/aws_iam_user_filter",
      "hide_notification": false,
      "id": 687,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_user_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_user_filter",
      "tooltip": "Filter by user name. Can be a string or regular expression.",
      "type_id": 11,
      "uuid": "53d3f14e-3ea3-4333-88b1-0c18af81beab",
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
      "export_key": "__function/aws_iam_group_filter",
      "hide_notification": false,
      "id": 688,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_group_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_group_filter",
      "tooltip": "Filter by group name. Can be a string or regular expression.",
      "type_id": 11,
      "uuid": "54051802-e82c-44c7-aa7b-8c1b2a6ecf45",
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
      "export_key": "__function/aws_iam_arns",
      "hide_notification": false,
      "id": 689,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_arns",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": null,
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "aws_iam_arns",
      "tooltip": "Comma separated list of AWS IAM Amazon Resource Names (ARNs).",
      "type_id": 11,
      "uuid": "70a8baec-9c1e-4b65-a596-6a8b21cbdd25",
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
      "export_key": "actioninvocation/aws_iam_group_filter",
      "hide_notification": false,
      "id": 664,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_group_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "(group1|group2) or group3",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Group filter",
      "tooltip": "Filter by group name. Can be a string or regular expression.",
      "type_id": 6,
      "uuid": "9ed0bd41-cb3f-465d-b58e-33e96d7b8c9e",
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
      "export_key": "actioninvocation/aws_iam_password_reset_required",
      "hide_notification": false,
      "id": 665,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_password_reset_required",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Password reset required",
      "tooltip": "Password reset required on next login.",
      "type_id": 6,
      "uuid": "03e32eee-9433-4e65-ae51-1fbe742412b5",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "No",
          "properties": null,
          "uuid": "ee0aaf6e-b088-475c-aae8-f1bc0e559956",
          "value": 102
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "Yes",
          "properties": null,
          "uuid": "1be56bbf-6b45-4e3b-bee3-3c2eb4e6c8e5",
          "value": 103
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
      "export_key": "actioninvocation/aws_iam_password",
      "hide_notification": false,
      "id": 666,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_password",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Password",
      "tooltip": "The new password needs be minimum 8 characters in length and have at least 1 uppercase and 1 lowercase character.",
      "type_id": 6,
      "uuid": "34c2782e-4f1b-4515-8348-7edb2724c037",
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
      "export_key": "actioninvocation/aws_iam_access_key_filter",
      "hide_notification": false,
      "id": 667,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_access_key_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "ABC123CDE456FGH789IJ",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Access Key filter",
      "tooltip": "Filter by access key id. Can be a string or regular expression.",
      "type_id": 6,
      "uuid": "3c684c12-49a8-4119-8a02-f7929e5cb69d",
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
      "export_key": "actioninvocation/aws_iam_policy_filter",
      "hide_notification": false,
      "id": 668,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_policy_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "(policy1|policy2) or FullAccess",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Policy filter",
      "tooltip": "Filter by policy name. Can be a string or regular expression.",
      "type_id": 6,
      "uuid": "3c9e9fbd-0f58-41b7-8d7a-92410ff7b1d1",
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
      "export_key": "actioninvocation/aws_iam_user_filter",
      "hide_notification": false,
      "id": 669,
      "input_type": "text",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_user_filter",
      "operation_perms": {},
      "operations": [],
      "placeholder": "(name1|name2) or name3",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "User filter",
      "tooltip": "Filter by user name. Can be a string or regular expression.",
      "type_id": 6,
      "uuid": "613f7245-6c9c-4a75-8c9a-2ece77101a0a",
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
      "export_key": "actioninvocation/aws_iam_group",
      "hide_notification": false,
      "id": 670,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_group",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "required": "always",
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Group",
      "tooltip": "AWS IAM group name.",
      "type_id": 6,
      "uuid": "6a273ffd-f8b1-4edc-90dd-abc2d4ba7179",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "\u003cUser_group_name_1\u003e",
          "properties": null,
          "uuid": "3c1870a5-8194-442a-8a26-f2dfd2be5f08",
          "value": 104
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u003cUser_group_name_2\u003e",
          "properties": null,
          "uuid": "100fa4cd-1e4d-44b4-9132-b54650587e4f",
          "value": 105
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
      "export_key": "actioninvocation/aws_iam_policy_name",
      "hide_notification": false,
      "id": 671,
      "input_type": "select",
      "internal": false,
      "is_tracked": false,
      "name": "aws_iam_policy_name",
      "operation_perms": {},
      "operations": [],
      "placeholder": "",
      "prefix": "properties",
      "read_only": false,
      "rich_text": false,
      "tags": [],
      "templates": [],
      "text": "Policy name",
      "tooltip": "",
      "type_id": 6,
      "uuid": "7660ab32-6584-4c61-a2d5-6fd42349e658",
      "values": [
        {
          "default": true,
          "enabled": true,
          "hidden": false,
          "label": "\u003cUser_policy_name_1\u003e",
          "properties": null,
          "uuid": "9918289d-9dba-4fa3-b05a-b798613bb5d4",
          "value": 106
        },
        {
          "default": false,
          "enabled": true,
          "hidden": false,
          "label": "\u003cUser_policy_name_2\u003e",
          "properties": null,
          "uuid": "71de6077-84c6-4ad2-99ff-678277e02369",
          "value": 107
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
      "created_date": 1718964394797,
      "description": {
        "content": "Add the specified IAM user to the specified groups. Parameter aws_iam_user_name is an IAM user name. Parameter aws_iam_group_names is a comma-separated list of IAM group names.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Add User To Groups",
      "export_key": "fn_aws_iam_add_user_to_groups",
      "id": 1,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964394797,
      "name": "fn_aws_iam_add_user_to_groups",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "f460bc26-ba06-4180-9d5e-fb6de5646f42",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "38083166-fa87-4360-86a5-ca8befac8788",
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
          "name": "Example: AWS IAM: Add User To Group",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_add_user_to_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 4
        }
      ]
    },
    {
      "created_date": 1718964394926,
      "description": {
        "content": "Attach the specified managed policies to the specified IAM user. Parameter aws_iam_user_name is an IAM user name. Parameter aws_iam_policy_names (optional) is a comma-separated  list of IAM policy names. Parameter (optional) aws_iam_arns is a comma-separated list of IAM policy arns.\n\nNote: One of parameters aws_iam_policy_names or aws_iam_arns required to be set.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Attach User policies",
      "export_key": "fn_aws_iam_attach_user_policies",
      "id": 2,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964394926,
      "name": "fn_aws_iam_attach_user_policies",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "23f07e6d-8bfd-4762-ac22-fab95a7a2ec3",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "70a8baec-9c1e-4b65-a596-6a8b21cbdd25",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cecc9df4-afea-49f7-95b4-f434fb381425",
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
          "name": "Example: AWS IAM: Attach User Policy",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_attach_user_policy",
          "tags": [],
          "uuid": null,
          "workflow_id": 17
        }
      ]
    },
    {
      "created_date": 1718964395042,
      "description": {
        "content": "Deactivate an MFA device and remove it from association with the user name for which it was originally enabled. Parameter aws_iam_user_name is an IAM user name. Parameter aws_iam_mfa_serial_numbers is a comma-separated list of IAM MFA serial numbers or arns.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Deactivate MFA Devices",
      "export_key": "fn_aws_iam_deactivate_mfa_devices",
      "id": 3,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964395042,
      "name": "fn_aws_iam_deactivate_mfa_devices",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "6c20740b-0696-4e2f-b772-54f74ef049fe",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "ed50aaeb-760f-4b76-87c3-b5546e4edf2a",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964395159,
      "description": {
        "content": "Delete the access key pairs associated with the specified IAM user. Parameter aws_iam_user_name is an IAM user name. Parameter aws_iam_access_keys is a comma-separated list of IAM access key IDs.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Delete Access Keys",
      "export_key": "fn_aws_iam_delete_access_keys",
      "id": 4,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964395159,
      "name": "fn_aws_iam_delete_access_keys",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "6a15d8e2-7472-4460-858e-3ff83221e183",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "0c8b7db1-ddd1-4c1d-bb93-98df99153ac2",
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
          "name": "Example: AWS IAM: Delete Access Key",
          "object_type": "aws_iam_access_keys",
          "programmatic_name": "wf_aws_iam_delete_access_key",
          "tags": [],
          "uuid": null,
          "workflow_id": 3
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete Access Key For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_access_key_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 14
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete Access Keys",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_access_keys",
          "tags": [],
          "uuid": null,
          "workflow_id": 5
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964395272,
      "description": {
        "content": "Delete the password for the specified IAM user, which terminates the user\u0027s ability to access AWS services through the AWS Management Console. Parameter aws_iam_user_name is an IAM user name.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Delete Login Profile",
      "export_key": "fn_aws_iam_delete_login_profile",
      "id": 5,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964395272,
      "name": "fn_aws_iam_delete_login_profile",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "22d5a7a2-9e89-4011-b53d-604a4aeaad2e",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
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
          "name": "Example: AWS IAM: Delete Login Profile",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_login_profile",
          "tags": [],
          "uuid": null,
          "workflow_id": 19
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964395384,
      "description": {
        "content": "Delete a virtual MFA device. Parameter aws_iam_mfa_serial_numbers is a comma-separated list of IAM MFA serial numbers or arns.\n\nNote: You must deactivate a user\u0027s virtual MFA device before you can delete it.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Delete Virtual MFA Devices",
      "export_key": "fn_aws_iam_delete_mfa_devices",
      "id": 6,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964395384,
      "name": "fn_aws_iam_delete_mfa_devices",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "0685a3cf-fdf3-4a68-8574-a8a4dcc112eb",
      "version": 0,
      "view_items": [
        {
          "content": "ed50aaeb-760f-4b76-87c3-b5546e4edf2a",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964395498,
      "description": {
        "content": "Delete signing certificates associated with the specified IAM user. Parameter aws_iam_user_name is an IAM user name. Parameter aws_iam_sign_cert_ids is a comma-separated list of signing certificate IDs.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Delete Signing Certificates",
      "export_key": "fn_aws_iam_delete_signing_certs",
      "id": 7,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964395498,
      "name": "fn_aws_iam_delete_signing_certs",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "8fda0978-9293-4078-9578-c9855ff26f85",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5072b195-f75d-4bc7-a7c2-8986fb372125",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964395607,
      "description": {
        "content": "Delete service-specific credentials associated with the specified IAM user. Parameter aws_iam_user_name is an IAM user name. Parameter aws_iam_ssc_ids is a comma-separated list of service-specific credential IDs.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Delete Service Specific Credentials",
      "export_key": "fn_aws_iam_delete_ss_creds",
      "id": 8,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964395607,
      "name": "fn_aws_iam_delete_ss_creds",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "590079fe-1bb9-47d9-8c3a-7084838232c7",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "e867f22c-33f5-470b-bfdf-915af174c8bc",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964395731,
      "description": {
        "content": "Delete Secure Shell (SSH) public keys associated with the specified IAM user. Parameter aws_iam_user_name is an IAM user name. Parameter aws_iam_ssh_key_ids is a comma-separated list of SSH public key IDs.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Delete SSH Public Keys",
      "export_key": "fn_aws_iam_delete_ssh_keys",
      "id": 9,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964395731,
      "name": "fn_aws_iam_delete_ssh_keys",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "17506b61-ff8f-44b2-937e-15a3ae3d5d0a",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b190100f-4a02-476c-8993-75733bdbcca3",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964395831,
      "description": {
        "content": "Delete the specified IAM user. Parameter aws_iam_user_name is an IAM user name. \n\nNote: When deleting an IAM user programmatically, you must delete the following items attached to the user or the deletion fails:\n\n    Password ( DeleteLoginProfile )\n    Access keys ( DeleteAccessKey )\n    Inline policies ( DeleteUserPolicy )\n    Attached managed policies ( DetachUserPolicy ) \n    Group memberships ( RemoveUserFromGroup )\n    Signing certificate ( DeleteSigningCertificate )\n    SSH public key ( DeleteSSHPublicKey )\n    Git credentials ( DeleteServiceSpecificCredential )\n    Multi-factor authentication (MFA) device ( DeactivateMFADevice , DeleteVirtualMFADevice )",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Delete User",
      "export_key": "fn_aws_iam_delete_user",
      "id": 10,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964395831,
      "name": "fn_aws_iam_delete_user",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "773f48cb-3a55-405e-aef9-73c7938de80f",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964395933,
      "description": {
        "content": "Remove the specified managed policy from the specified IAM user. Parameter aws_iam_user_name is an IAM user name. Parameter aws_iam_policy_names (optional) is  a comma-separated  list of IAM policy names. Parameter (optional) aws_iam_arns is a comma-separated list of IAM policy arns.\n\nNote: A user can also have inline policies embedded with it, this function will delete inline policies associated with the the user. \nNote: one of parameters aws_iam_policy_names or aws_iam_arns required to be set.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Detach User policies",
      "export_key": "fn_aws_iam_detach_user_policies",
      "id": 11,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964395933,
      "name": "fn_aws_iam_detach_user_policies",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "10a78fb7-0c3e-48f3-88b8-2a464dbb0715",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "70a8baec-9c1e-4b65-a596-6a8b21cbdd25",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "cecc9df4-afea-49f7-95b4-f434fb381425",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Detach All User Policies",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_detach_all_user_policies",
          "tags": [],
          "uuid": null,
          "workflow_id": 16
        }
      ]
    },
    {
      "created_date": 1718964396048,
      "description": {
        "content": "List the MFA devices associated with an IAM user also determine which of the associated MFA devices is a virtual device. Parameter aws_iam_user_name is an IAM user name.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: List MFA Devices",
      "export_key": "fn_aws_iam_list_mfa_devices",
      "id": 12,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964396048,
      "name": "fn_aws_iam_list_mfa_devices",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "d85d59b9-b5e1-444e-9b9f-ea2f5dae64ae",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964396149,
      "description": {
        "content": "List the signing certificates  associated with an IAM user. Parameter aws_iam_user_name is an IAM user name.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: List Signing Certificates",
      "export_key": "fn_aws_iam_list_signing_certs",
      "id": 13,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964396149,
      "name": "fn_aws_iam_list_signing_certs",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "28643fbd-6a39-411e-9b67-8507e4a228e7",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964396249,
      "description": {
        "content": "List the service-specific credentials associated with an IAM user. Parameter aws_iam_user_name is an IAM user name.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: List Service Specific Credentials",
      "export_key": "fn_aws_iam_list_ss_creds",
      "id": 14,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964396249,
      "name": "fn_aws_iam_list_ss_creds",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "ec76a52d-94e3-447c-8b0c-f049c365b4f3",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964396350,
      "description": {
        "content": "List the SSH public keys associated with an IAM user. Parameter aws_iam_user_name is an IAM user name.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: List SSH Public Keys",
      "export_key": "fn_aws_iam_list_ssh_keys",
      "id": 15,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964396350,
      "name": "fn_aws_iam_list_ssh_keys",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "a7b28b9e-6a27-44c1-90f2-d4d3d5f54ba9",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        }
      ]
    },
    {
      "created_date": 1718964396451,
      "description": {
        "content": "Get information about the access key IDs associated with the specified IAM user. Parameter aws_iam_user_name is an IAM user name.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: List User Access Key IDs",
      "export_key": "fn_aws_iam_list_user_access_key_ids",
      "id": 16,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964396451,
      "name": "fn_aws_iam_list_user_access_key_ids",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "278f8cba-ff48-4495-93b0-27349c3fec8b",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
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
          "name": "Example: AWS IAM: Delete Access Keys",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_access_keys",
          "tags": [],
          "uuid": null,
          "workflow_id": 5
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Get User",
          "object_type": "aws_iam_access_keys",
          "programmatic_name": "wf_aws_iam_get_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 12
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Get User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_get_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 6
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Refresh Access Key",
          "object_type": "aws_iam_access_keys",
          "programmatic_name": "wf_aws_iam_refresh_access_key",
          "tags": [],
          "uuid": null,
          "workflow_id": 13
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Refresh User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_refresh_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    },
    {
      "created_date": 1718964396555,
      "description": {
        "content": "Get the IAM groups that the specified IAM user belongs to. Parameter aws_iam_user_name is an IAM user name.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: List User Groups",
      "export_key": "fn_aws_iam_list_user_groups",
      "id": 17,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964396555,
      "name": "fn_aws_iam_list_user_groups",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "c8b67eb7-166c-4f5c-8291-1d0e3bd14e68",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
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
          "name": "Example: AWS IAM: Add User To Group",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_add_user_to_group",
          "tags": [],
          "uuid": null,
          "workflow_id": 4
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Get User",
          "object_type": "aws_iam_access_keys",
          "programmatic_name": "wf_aws_iam_get_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 12
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Get User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_get_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 6
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Refresh User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_refresh_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Remove User From All Groups",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_remove_user_from_all_groups",
          "tags": [],
          "uuid": null,
          "workflow_id": 20
        }
      ]
    },
    {
      "created_date": 1718964396661,
      "description": {
        "content": "Get all managed policies and in-line policies that are attached to the specified IAM user. Parameter aws_iam_user_name is an IAM user name.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: List User Policies",
      "export_key": "fn_aws_iam_list_user_policies",
      "id": 18,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964396661,
      "name": "fn_aws_iam_list_user_policies",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "64a30bb5-b539-45d6-b6e5-55674539d411",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
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
          "name": "Example: AWS IAM: Attach User Policy",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_attach_user_policy",
          "tags": [],
          "uuid": null,
          "workflow_id": 17
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Detach All User Policies",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_detach_all_user_policies",
          "tags": [],
          "uuid": null,
          "workflow_id": 16
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Get User",
          "object_type": "aws_iam_access_keys",
          "programmatic_name": "wf_aws_iam_get_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 12
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Get User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_get_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 6
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Refresh User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_refresh_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    },
    {
      "created_date": 1718964396765,
      "description": {
        "content": "Get IAM user or users in the AWS account.  Users can be filtered by user name , group and policy. If the user name is specified get information only for this user. Parameter aws_iam_user_name is an IAM user name. Parameters aws_iam_user_filter, aws_aim_group_filter and aws_aim_policy_filter param (all optional) are filters used to refine user data returned. Parameter aws_iam_query_type (optional) is used to determine type of query to perform users.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: List Users",
      "export_key": "fn_aws_iam_list_users",
      "id": 19,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964396765,
      "name": "fn_aws_iam_list_users",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "7991e057-a564-424d-a6b9-ba806cc549b0",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "53d3f14e-3ea3-4333-88b1-0c18af81beab",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "54051802-e82c-44c7-aa7b-8c1b2a6ecf45",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "389645a9-c932-45a6-9b29-3b422b0ca40e",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "b1ac6bbb-8bab-47ac-88a0-028deb661096",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "136e1156-7875-4314-ad4a-729b5026c5ce",
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
          "name": "Example: AWS IAM: Delete Access Key For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_access_key_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 14
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete Login Profile",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_login_profile",
          "tags": [],
          "uuid": null,
          "workflow_id": 19
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Get Access Key For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_get_access_key_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 15
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Get Access Keys",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_get_access_keys",
          "tags": [],
          "uuid": null,
          "workflow_id": 11
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Get User",
          "object_type": "aws_iam_access_keys",
          "programmatic_name": "wf_aws_iam_get_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 12
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Get User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_get_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 6
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: List Access Keys",
          "object_type": "incident",
          "programmatic_name": "wf_aws_iam_list_access_keys",
          "tags": [],
          "uuid": null,
          "workflow_id": 2
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: List Users",
          "object_type": "incident",
          "programmatic_name": "wf_aws_iam_list_users",
          "tags": [],
          "uuid": null,
          "workflow_id": 18
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Refresh Access Key",
          "object_type": "aws_iam_access_keys",
          "programmatic_name": "wf_aws_iam_refresh_access_key",
          "tags": [],
          "uuid": null,
          "workflow_id": 13
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Refresh User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_refresh_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 1
        }
      ]
    },
    {
      "created_date": 1718964396906,
      "description": {
        "content": "Removes the specified IAM user from the specified groups. Group names is be a comma-separated string of group names. Parameter aws_iam_user_name is an IAM user name. Parameter aws_iam_group_names is  a comma-separated list of IAM group names.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Remove User From Groups",
      "export_key": "fn_aws_iam_remove_user_from_groups",
      "id": 20,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964396906,
      "name": "fn_aws_iam_remove_user_from_groups",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "7efc8616-ed52-4a8f-9f25-5c168b681ba9",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "38083166-fa87-4360-86a5-ca8befac8788",
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
          "name": "Example: AWS IAM: Delete User",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_delete_user",
          "tags": [],
          "uuid": null,
          "workflow_id": 9
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Delete User For Artifact",
          "object_type": "artifact",
          "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
          "tags": [],
          "uuid": null,
          "workflow_id": 10
        },
        {
          "actions": [],
          "description": null,
          "name": "Example: AWS IAM: Remove User From All Groups",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_remove_user_from_all_groups",
          "tags": [],
          "uuid": null,
          "workflow_id": 20
        }
      ]
    },
    {
      "created_date": 1718964397024,
      "description": {
        "content": "Change the status of an access key from Active to Inactive, or vice versa. Parameter aws_iam_user_name is an IAM user name. Parameter aws_iam_access_key_id is an IAM user access key ID. Parameter aws_iam_status is be set to \"Active\" or \"Inactive\" to change the status of the access key.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Update Access Key",
      "export_key": "fn_aws_iam_update_access_key",
      "id": 21,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964397024,
      "name": "fn_aws_iam_update_access_key",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "045fe24b-3eb8-4a2a-885d-62f36e2d4b10",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "458744ef-622f-4a00-8a8f-58545eb2cb6d",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "95e86085-40e3-4dbf-a989-9c2deaa3c1e4",
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
          "name": "Example: AWS IAM: Deactivate Access Key",
          "object_type": "aws_iam_access_keys",
          "programmatic_name": "wf_aws_iam_deactivate_access_key",
          "tags": [],
          "uuid": null,
          "workflow_id": 8
        }
      ]
    },
    {
      "created_date": 1718964397137,
      "description": {
        "content": "Change the password for the specified IAM user.Parameter aws_iam_user_name is an IAM user name. Parameter aws_iam_password is a new password value fro an IAM user. Parameter aws_iam_password_reset_required is a boolean value to determine whether a password reset should be required on change.",
        "format": "text"
      },
      "destination_handle": "fn_aws_iam",
      "display_name": "AWS IAM: Update Login Profile",
      "export_key": "fn_aws_iam_update_login_profile",
      "id": 22,
      "last_modified_by": {
        "display_name": "SOAR_Apps_Dev",
        "id": 8,
        "name": "0624e4db-d2fa-4b7b-a678-77e3fe3edac2",
        "type": "apikey"
      },
      "last_modified_time": 1718964397137,
      "name": "fn_aws_iam_update_login_profile",
      "output_description": {
        "content": null,
        "format": "text"
      },
      "tags": [],
      "uuid": "5b37eab0-39a9-4ecf-bfd9-4ec53e30f233",
      "version": 0,
      "view_items": [
        {
          "content": "d7d96d4f-e23e-436c-be00-7204ed33694b",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "93a81af4-7d79-4de1-a0cb-30000bff6e61",
          "element": "field_uuid",
          "field_type": "__function",
          "show_if": null,
          "show_link_header": false,
          "step_label": null
        },
        {
          "content": "5106b8bf-edf9-460c-bca5-bffbe602fb36",
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
          "name": "Example: AWS IAM: Change Profile Password",
          "object_type": "aws_iam_users",
          "programmatic_name": "wf_aws_iam_change_profile_password",
          "tags": [],
          "uuid": null,
          "workflow_id": 7
        }
      ]
    }
  ],
  "geos": null,
  "groups": null,
  "id": 38,
  "inbound_destinations": [],
  "inbound_mailboxes": null,
  "incident_artifact_types": [
    {
      "default_scan_option": "unsupported",
      "desc": "Amazon Web Services (AWS) IAM access key id.",
      "enabled": true,
      "export_key": "aws_iam_access_key_id",
      "file": false,
      "id": 0,
      "multi_aware": false,
      "name": "AWS IAM Access Key ID",
      "parse_as_csv": false,
      "programmatic_name": "aws_iam_access_key_id",
      "reg_exp": null,
      "system": false,
      "tags": [],
      "use_for_relationships": true,
      "uuid": "a33a1971-162c-4417-b344-8708f9d25644",
      "version": 0
    },
    {
      "default_scan_option": "unsupported",
      "desc": "Amazon Web Services (AWS) IAM user name.",
      "enabled": true,
      "export_key": "aws_iam_user_name",
      "file": false,
      "id": 0,
      "multi_aware": false,
      "name": "AWS IAM User Name",
      "parse_as_csv": false,
      "programmatic_name": "aws_iam_user_name",
      "reg_exp": null,
      "system": false,
      "tags": [],
      "use_for_relationships": true,
      "uuid": "3a0a5309-ba33-47cb-92df-c8a506f87317",
      "version": 0
    }
  ],
  "incident_types": [
    {
      "create_date": 1719811195650,
      "description": "Customization Packages (internal)",
      "enabled": false,
      "export_key": "Customization Packages (internal)",
      "hidden": false,
      "id": 0,
      "name": "Customization Packages (internal)",
      "parent_id": null,
      "system": false,
      "update_date": 1719811195650,
      "uuid": "bfeec2d4-3770-11e8-ad39-4a0004044aa0"
    }
  ],
  "layouts": [],
  "locale": null,
  "message_destinations": [
    {
      "api_keys": [
        "0624e4db-d2fa-4b7b-a678-77e3fe3edac2"
      ],
      "destination_type": 0,
      "expect_ack": true,
      "export_key": "fn_aws_iam",
      "name": "AWS IAM",
      "programmatic_name": "fn_aws_iam",
      "tags": [],
      "users": [],
      "uuid": "36584fb3-0d31-4000-954f-509dc1ea270f"
    }
  ],
  "notifications": null,
  "overrides": null,
  "phases": [],
  "playbooks": [],
  "regulators": null,
  "roles": [],
  "scripts": [
    {
      "actions": [],
      "created_date": 1718964393673,
      "description": "Add an AWS IAM access key from data table \"AWS IAM Users\" as a Resilient artifact .",
      "enabled": false,
      "export_key": "scr_aws_iam_add_access_key_as_artifact",
      "id": 5,
      "language": "python3",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719375101714,
      "name": "scr_aws_iam_add_access_key_as_artifact",
      "object_type": "aws_iam_access_keys",
      "playbook_handle": null,
      "programmatic_name": "scr_aws_iam_add_access_key_as_artifact",
      "script_text": "# Create a Resilient artifact based on username from the corresponding data-table field.\nARTIFACT_TYPE = \"aws_iam_access_key_id\"\nSCRIPT_NAME = \"scr_aws_iam_add_access_key_as_artifact\"\n\n\ndef addArtifact(artifact_type, artifact_value, description):\n    \"\"\"This method adds new artifacts to the incident derived from matches of the the regular expression\n\n    :param artifact_type: The type of the artifact.\n    :param artifact_value: - The value of the artifact.\n    :param description: - the description of the artifact.\n    \"\"\"\n    incident.addArtifact(artifact_type, artifact_value, description)\n\ndef main():\n\n    desc = \"AWS IAM access key associated with username \u0027{0}\u0027 was detected by an AWS IAM query and added as an artifact \" \\\n           \"by script \u0027{1}\u0027 from data table \u0027{2}\u0027 for the AWS IAM Resilient integration.\"\\\n        .format(row.UserName, SCRIPT_NAME, \"AWS IAM Access Keys\")\n\n    addArtifact(ARTIFACT_TYPE, row.AccessKeyId, desc)\n\n\n# Script execution starts here\nif __name__ == \"__main__\":\n    main()",
      "tags": [],
      "uuid": "ba06e1b2-a6a7-44e3-a19c-a6d4d9fdfcb0"
    },
    {
      "actions": [],
      "created_date": 1718964393712,
      "description": "Add an AWS IAM user from data table \"AWS IAM Users\" as a Resilient artifact .",
      "enabled": false,
      "export_key": "scr_aws_iam_add_user_as_artifact",
      "id": 6,
      "language": "python3",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719375117241,
      "name": "scr_aws_iam_add_user_as_artifact",
      "object_type": "aws_iam_users",
      "playbook_handle": null,
      "programmatic_name": "scr_aws_iam_add_user_as_artifact",
      "script_text": "# Create a Resilient artifact based on username from the corresponding data-table field.\nARTIFACT_TYPE = \"aws_iam_user_name\"\nSCRIPT_NAME = \"scr_aws_iam_add_user_as_artifact\"\n\n\ndef addArtifact(artifact_type, artifact_value, description):\n    \"\"\"This method adds new artifacts to the incident derived from matches of the the regular expression\n\n    :param artifact_type: The type of the artifact.\n    :param artifact_value: - The value of the artifact.\n    :param description: - the description of the artifact.\n    \"\"\"\n    incident.addArtifact(artifact_type, artifact_value, description)\n\ndef main():\n\n    desc = \"AWS IAM user was detected by an AWS IAM query and added as an artifact by script \u0027{0}\u0027 from \" \\\n           \"data table \u0027{1}\u0027 for the AWS IAM Resilient integration.\".format(SCRIPT_NAME, \"AWS IAM Users\")\n    addArtifact(ARTIFACT_TYPE, row.UserName, desc)\n\n\n# Script execution starts here\nif __name__ == \"__main__\":\n    main()",
      "tags": [],
      "uuid": "0ed6bba7-dd50-4a2e-b35c-b37ba5e8d8b4"
    }
  ],
  "server_version": {
    "build_number": 9340,
    "f": 0,
    "m": 0,
    "major": 0,
    "minor": 0,
    "r": 0,
    "v": 51,
    "version": "51.0.0.0.9340"
  },
  "tags": [],
  "task_order": [],
  "timeframes": null,
  "types": [
    {
      "actions": [],
      "display_name": "AWS IAM Access Keys",
      "export_key": "aws_iam_access_keys",
      "fields": {
        "AccessKeyId": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_access_keys/AccessKeyId",
          "hide_notification": false,
          "id": 644,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "AccessKeyId",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Access key id",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "24fc2e57-3549-4047-9d59-76ca2da25698",
          "values": [],
          "width": 168
        },
        "CreateDate": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_access_keys/CreateDate",
          "hide_notification": false,
          "id": 645,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "CreateDate",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Create date",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "5e1d55eb-6dc2-4276-bf55-9fea1fd61f43",
          "values": [],
          "width": 141
        },
        "DefaultKey": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_access_keys/DefaultKey",
          "hide_notification": false,
          "id": 646,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "DefaultKey",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Default key",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "54d43bd2-6bb4-42d5-b51e-3a4b2d0de8fc",
          "values": [],
          "width": 38
        },
        "LastUsedDate": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_access_keys/LastUsedDate",
          "hide_notification": false,
          "id": 647,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "LastUsedDate",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Last used date",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "46a60584-e33b-4d17-a313-df7b5708c932",
          "values": [],
          "width": 72
        },
        "Region": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_access_keys/Region",
          "hide_notification": false,
          "id": 648,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Region",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Region",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "dccfe966-9402-44e0-b27b-e427764e2097",
          "values": [],
          "width": 35
        },
        "ServiceName": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_access_keys/ServiceName",
          "hide_notification": false,
          "id": 649,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "ServiceName",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Service name",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "a5bcb947-95c9-47c3-a1ea-b32644dd5a72",
          "values": [],
          "width": 69
        },
        "Status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_access_keys/Status",
          "hide_notification": false,
          "id": 650,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Status",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "c00dac53-3e36-4e8e-a277-7512d57da1b6",
          "values": [],
          "width": 102
        },
        "UserName": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_access_keys/UserName",
          "hide_notification": false,
          "id": 651,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "UserName",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "User name",
          "tooltip": "",
          "type_id": 1000,
          "uuid": "69d9f265-2bcc-4c24-aaf7-5a71d623557d",
          "values": [],
          "width": 131
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": false,
          "calculated": false,
          "changeable": true,
          "chosen": false,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_access_keys/query_execution_date",
          "hide_notification": false,
          "id": 652,
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
          "type_id": 1000,
          "uuid": "bcf946ec-47d4-4697-a5ab-9ed392512a71",
          "values": [],
          "width": 129
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
      "type_name": "aws_iam_access_keys",
      "uuid": "f496b94c-1b86-477a-88ed-94b2d10ce61b"
    },
    {
      "actions": [],
      "display_name": "AWS IAM Users",
      "export_key": "aws_iam_users",
      "fields": {
        "AccessKeyIds": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_users/AccessKeyIds",
          "hide_notification": false,
          "id": 653,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "AccessKeyIds",
          "operation_perms": {},
          "operations": [],
          "order": 3,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Access key ids",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "30ba9503-014c-4804-94d0-be9998bb9a41",
          "values": [],
          "width": 123
        },
        "Arn": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_users/Arn",
          "hide_notification": false,
          "id": 654,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Arn",
          "operation_perms": {},
          "operations": [],
          "order": 7,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "User Arn",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "53d69c02-dce3-47f5-87d5-f97c5b178a49",
          "values": [],
          "width": 164
        },
        "CreateDate": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_users/CreateDate",
          "hide_notification": false,
          "id": 655,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "CreateDate",
          "operation_perms": {},
          "operations": [],
          "order": 8,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Create date",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "ff213f93-db27-4286-abcc-3cd6c57d3166",
          "values": [],
          "width": 68
        },
        "DefaultUser": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_users/DefaultUser",
          "hide_notification": false,
          "id": 656,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "DefaultUser",
          "operation_perms": {},
          "operations": [],
          "order": 9,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Default user",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "c550c795-fc97-45af-97e7-0a2ef2f8085a",
          "values": [],
          "width": 38
        },
        "Groups": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_users/Groups",
          "hide_notification": false,
          "id": 657,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Groups",
          "operation_perms": {},
          "operations": [],
          "order": 4,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Groups",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "7452a53a-c4a8-494c-abb9-0c6033759a08",
          "values": [],
          "width": 109
        },
        "LoginProfileExists": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_users/LoginProfileExists",
          "hide_notification": false,
          "id": 658,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "LoginProfileExists",
          "operation_perms": {},
          "operations": [],
          "order": 2,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Login Profile exists",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "25dfc73d-de36-4235-8717-89563da2d261",
          "values": [],
          "width": 34
        },
        "Policies": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_users/Policies",
          "hide_notification": false,
          "id": 659,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Policies",
          "operation_perms": {},
          "operations": [],
          "order": 5,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Policies",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "6aa3faed-3dc0-4c0a-8852-12896a18b789",
          "values": [],
          "width": 95
        },
        "Status": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_users/Status",
          "hide_notification": false,
          "id": 660,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Status",
          "operation_perms": {},
          "operations": [],
          "order": 10,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Status",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "7f864212-ac6f-4753-90bf-7a3c2b36e47e",
          "values": [],
          "width": 51
        },
        "Tags": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_users/Tags",
          "hide_notification": false,
          "id": 661,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "Tags",
          "operation_perms": {},
          "operations": [],
          "order": 6,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "Tags",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "504b2002-aefa-4f6d-91b4-754c971f9d92",
          "values": [],
          "width": 114
        },
        "UserName": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_users/UserName",
          "hide_notification": false,
          "id": 662,
          "input_type": "text",
          "internal": false,
          "is_tracked": false,
          "name": "UserName",
          "operation_perms": {},
          "operations": [],
          "order": 1,
          "placeholder": "",
          "prefix": null,
          "read_only": false,
          "rich_text": false,
          "tags": [],
          "templates": [],
          "text": "User name",
          "tooltip": "",
          "type_id": 1001,
          "uuid": "c819c6b8-3e36-439e-bd30-b91594a19691",
          "values": [],
          "width": 164
        },
        "query_execution_date": {
          "allow_default_value": false,
          "blank_option": true,
          "calculated": false,
          "changeable": true,
          "chosen": true,
          "default_chosen_by_server": false,
          "deprecated": false,
          "export_key": "aws_iam_users/query_execution_date",
          "hide_notification": false,
          "id": 663,
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
          "type_id": 1001,
          "uuid": "96de2e81-bbee-4717-bd32-35a2354595db",
          "values": [],
          "width": 78
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
      "type_name": "aws_iam_users",
      "uuid": "78c24adc-c532-470b-a907-30a25c05c76a"
    }
  ],
  "workflows": [
    {
      "actions": [],
      "content": {
        "version": 11,
        "workflow_id": "wf_aws_iam_refresh_user",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_refresh_user\" isExecutable=\"true\" name=\"Example: AWS IAM: Refresh User\"\u003e\u003cdocumentation\u003eRefresh an IAM users information in the data table. The User is assigned from a field in the selected data table row. The data table row will be refreshed with updated values for the selected user.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0ct4iz2\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1w1y93n\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n            \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n            \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User\u0027, \u0027CreateDate\u0027: \u00272019-11-05 15:54:43\u0027},\\n                        {\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User_2\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User_2\u0027,\\n                         \u0027CreateDate\u0027: \u00272019-10-31 16:23:07\u0027, \u0027PasswordLastUsed\u0027: \u00272019-11-12 10:55:42\u0027}\\n                       ],\\n            \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::12345:user/iam_test_User\\\", \\\"CreateDate\\\": \\\"2019-11-05 15:54:43\\\"}, {\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User_2\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::12345:user/iam_test_User_2\\\", \\\"CreateDate\\\": \\\"2019-10-31 16:23:07\\\"}]\u0027,\\n            \u0027inputs\u0027: {},\\n            \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                        \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 7951,\\n                        \u0027timestamp\u0027: \u00272019-11-14 13:48:30\u0027\\n                       }\\n}\\n\\n\\\"\\\"\\\"\\nimport re\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_users script\\nDATA_TBL_FIELDS = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"Arn\\\", \\\"DefaultUser\\\", \\\"CreateDate\\\", \\\"LoginProfileExists\\\",\\n                   \\\"Tags\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"Refresh User\\\"\\n# Processing\\nINPUTS = results.inputs\\nCONTENT = results.content\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef check_add_quotes(tag_name):\\n    # Using regex\\n    # If spaces in tag name add quotes\\n    if re.search(r\\\"\\\\s\\\", tag_name):\\n        return \\\"\u0027\\\"+tag_name+\\\"\u0027\\\"\\n    else:\\n        return tag_name\\n\\ndef process_tags(tag_list, row):\\n    tags = []\\n    for tag in tag_list:\\n        if tag[\\\"Key\\\"]:\\n            tags.append(tag[\\\"Key\\\"])\\n    row.Tags = \u0027,\u0027.join(check_add_quotes(t) for t in tags)\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        if isinstance(CONTENT, dict) and CONTENT.get(\\\"Status\\\") == \\\"NoSuchEntity\\\":\\n            note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; does not exist \\\" \\\\\\n                         \\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.Status = \\\"Deleted\\\"\\n        elif len(CONTENT) == 1:\\n            note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was found \\\" \\\\\\n                         \\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            note_text += \\\"\u0026lt;br\u0026gt;Refreshing data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\u0026lt;/br\u0026gt;\\\"\\\\\\n                .format(\\\"AWS IAM Users\\\", INPUTS[\\\"aws_iam_user_name\\\"])\\n            workflow.addProperty(\\\"user_exists\\\", {})\\n            u = CONTENT.pop()\\n            row.query_execution_date = QUERY_EXECUTION_DATE\\n            for f in DATA_TBL_FIELDS:\\n                if u[f] is not None:\\n                    if isinstance(u[f], unicode) or isinstance(u[f], int) \\\\\\n                            or isinstance(u[f], long) or len(u[f]) == 0:\\n                        if f == \\\"DefaultUser\\\" and not u[f]:\\n                            pass\\n                        else:\\n                            row[f] = u[f]\\n                    else:\\n                        if f == \\\"Tags\\\" and len(u[f]) \u0026gt; 0:\\n                            process_tags(u[f], row)\\n                        else:\\n                            row[f] = \u0027,\u0027.join(u[f])\\n        else:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Too many results \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned for user \\\" \\\\\\n                        \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.LoginProfileExists = \\\"No\\\"\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned for user \\\" \\\\\\n                     \\\"\u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if note_text:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ct4iz2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_028hlbn\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ct4iz2\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1w1y93n\"/\u003e\u003cserviceTask id=\"ServiceTask_0kgpvcj\" name=\"AWS IAM: List User Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8b67eb7-166c-4f5c-8291-1d0e3bd14e68\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027GroupName\u0027: \u0027system-admins\u0027, \u0027GroupId\u0027: \u0027ABCDEFG\u0027,\\n                      \u0027Arn\u0027: \u0027arn:aws:iam::12345:group/system-admins\u0027, \u0027CreateDate\u0027: \u00272017-05-29 20:37:53\u0027}],\\n                      \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"GroupName\\\": \\\"system-admins\\\", \\\"GroupId\\\": \\\"ABCDEFG\\\",\\n                      \\\"Arn\\\": \\\"arn:aws:iam::12345:group/system-admins\\\", \\\"CreateDate\\\": \\\"2017-05-29 20:37:53\\\"\\n                      }\\n                    ]\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                     \u0027execution_time_ms\u0027: 1070, \u0027timestamp\u0027: \u00272019-11-18 10:19:19\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_groups script\\nDATA_TBL_FIELDS = [\\\"Groups\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_groups\\\"\\nWF_NAME = \\\"Refresh User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef main():\\n\\n    if CONTENT:\\n        groups = []\\n        for grp in CONTENT:\\n            if grp[\\\"GroupName\\\"] is not None:\\n                groups.append(grp[\\\"GroupName\\\"])\\n        row.Groups = \\\",\\\".join(groups)\\n    else:\\n        row.Groups = \\\"\\\"\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ejnpiu\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1g5pbvs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_1v6mnzk\" name=\"AWS IAM: List User Policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"64a30bb5-b539-45d6-b6e5-55674539d411\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyName\u0027: \u0027test_pol\u0027},\\n                      {\u0027PolicyName\u0027: \u0027test_pol_2\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::12345:policy/test_pol_2\u0027},\\n                      {\u0027PolicyName\u0027: \u0027AmazonRoute53ReadOnlyAccess\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\u0027}],\\n          \u0027raw\u0027: \u0027[{\\\"PolicyName\\\": \\\"test_pol\\\"}, {\\\"PolicyName\\\": \\\"test_pol_2\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::12345:policy/test_pol_2\\\"},\\n                    {\\\"PolicyName\\\": \\\"AmazonRoute53ReadOnlyAccess\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 87423, \u0027timestamp\u0027: \u00272019-11-21 11:55:29\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_groups script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_policies\\\"\\nWF_NAME = \\\"Refresh User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        policy_names = []\\n        for pol in CONTENT:\\n            if  pol[\\\"PolicyName\\\"] is not None:\\n                policy_names.append( pol[\\\"PolicyName\\\"])\\n        row.Policies = \\\",\\\".join(policy_names)\\n    else:\\n        row.Policies = \\\"\\\"\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0xhsu0d\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1kw0jo5\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_0uo0u4h\" name=\"AWS IAM: List User Access Key IDs\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"278f8cba-ff48-4495-93b0-27349c3fec8b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027,\\n                       \u0027Status\u0027: \u0027Active\u0027, \u0027CreateDate\u0027: \u00272019-11-12 11:09:38\u0027\\n                       }],\\n          \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_User\\\", \\\"AccessKeyId\\\": \\\"ABCDEFG\\\",\\n                  \\\"Status\\\": \\\"Active\\\", \\\"CreateDate\\\": \\\"2019-11-12 11:09:38\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 5365, \u0027timestamp\u0027: \u00272019-11-21 10:41:22\u0027}}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_access_keys script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_access_keys\\\"\\nWF_NAME = \\\"Refresh User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nnote_text = \u0027\u0027\\n\\ndef main():\\n\\n    if CONTENT:\\n        access_key_ids = []\\n        for ak_id in CONTENT:\\n            if ak_id[\\\"AccessKeyId\\\"] is not None:\\n                access_key_ids.append(ak_id[\\\"AccessKeyId\\\"])\\n        row.AccessKeyIds = \\\",\\\".join(access_key_ids)\\n    else:\\n        row.AccessKeyIds = \\\"\\\"\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1kw0jo5\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ejnpiu\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1kw0jo5\" sourceRef=\"ServiceTask_1v6mnzk\" targetRef=\"ServiceTask_0uo0u4h\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0ejnpiu\" sourceRef=\"ServiceTask_0uo0u4h\" targetRef=\"ServiceTask_0kgpvcj\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1g5pbvs\" sourceRef=\"ServiceTask_0kgpvcj\" targetRef=\"EndEvent_1j00fc7\"/\u003e\u003cendEvent id=\"EndEvent_1j00fc7\"\u003e\u003cincoming\u003eSequenceFlow_1g5pbvs\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1bx7nce\u003c/incoming\u003e\u003c/endEvent\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0brvsys\"\u003e\u003cincoming\u003eSequenceFlow_028hlbn\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0xhsu0d\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1bx7nce\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_028hlbn\" sourceRef=\"ServiceTask_1w1y93n\" targetRef=\"ExclusiveGateway_0brvsys\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0xhsu0d\" name=\"User exists.\" sourceRef=\"ExclusiveGateway_0brvsys\" targetRef=\"ServiceTask_1v6mnzk\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_1bx7nce\" name=\"User doesn\u0027t exist.\" sourceRef=\"ExclusiveGateway_0brvsys\" targetRef=\"EndEvent_1j00fc7\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_17ojiev\"\u003e\u003ctext\u003eList all users to\u00a0 determine if user\u00a0 exists. Update data table row.\u00a0 Username assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0rwnp9z\" sourceRef=\"ServiceTask_1w1y93n\" targetRef=\"TextAnnotation_17ojiev\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0gim1kb\"\u003e\u003ctext\u003eGet policy list for user. Update data table row for Policies.\n\u00a0Username assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ctxxoa\" sourceRef=\"ServiceTask_1v6mnzk\" targetRef=\"TextAnnotation_0gim1kb\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1rbc2uo\"\u003e\u003ctext\u003eGet access key list for user. Update data table row for access key ids.\n\u00a0Username assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0zs27ox\" sourceRef=\"ServiceTask_0uo0u4h\" targetRef=\"TextAnnotation_1rbc2uo\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1xbz71r\"\u003e\u003ctext\u003eGet group list for user. Update data table row.\n\u00a0Username assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0jvyanh\" sourceRef=\"ServiceTask_0kgpvcj\" targetRef=\"TextAnnotation_1xbz71r\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1w1y93n\" id=\"ServiceTask_1w1y93n_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"263\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ct4iz2\" id=\"SequenceFlow_0ct4iz2_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"263\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"230.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0kgpvcj\" id=\"ServiceTask_0kgpvcj_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"991\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1v6mnzk\" id=\"ServiceTask_1v6mnzk_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"544\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0uo0u4h\" id=\"ServiceTask_0uo0u4h_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"761\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1kw0jo5\" id=\"SequenceFlow_1kw0jo5_di\"\u003e\u003comgdi:waypoint x=\"644\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"761\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"657.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ejnpiu\" id=\"SequenceFlow_0ejnpiu_di\"\u003e\u003comgdi:waypoint x=\"861\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"991\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"881\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1g5pbvs\" id=\"SequenceFlow_1g5pbvs_di\"\u003e\u003comgdi:waypoint x=\"1091\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1211\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"1106\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1j00fc7\" id=\"EndEvent_1j00fc7_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1211\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"1184\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0brvsys\" id=\"ExclusiveGateway_0brvsys_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"423\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"448\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_028hlbn\" id=\"SequenceFlow_028hlbn_di\"\u003e\u003comgdi:waypoint x=\"363\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"423\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"393\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0xhsu0d\" id=\"SequenceFlow_0xhsu0d_di\"\u003e\u003comgdi:waypoint x=\"473\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"544\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"60\" x=\"481\" y=\"166\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1bx7nce\" id=\"SequenceFlow_1bx7nce_di\"\u003e\u003comgdi:waypoint x=\"448\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"448\" y=\"273\"/\u003e\u003comgdi:waypoint x=\"1229\" y=\"273\"/\u003e\u003comgdi:waypoint x=\"1229\" y=\"224\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"67\" x=\"806\" y=\"252\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_17ojiev\" id=\"TextAnnotation_17ojiev_di\"\u003e\u003comgdc:Bounds height=\"67\" width=\"215\" x=\"205\" y=\"52\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0rwnp9z\" id=\"Association_0rwnp9z_di\"\u003e\u003comgdi:waypoint x=\"314\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"314\" y=\"119\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0gim1kb\" id=\"TextAnnotation_0gim1kb_di\"\u003e\u003comgdc:Bounds height=\"66\" width=\"178\" x=\"502\" y=\"41\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ctxxoa\" id=\"Association_0ctxxoa_di\"\u003e\u003comgdi:waypoint x=\"593\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"593\" y=\"107\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1rbc2uo\" id=\"TextAnnotation_1rbc2uo_di\"\u003e\u003comgdc:Bounds height=\"46\" width=\"168\" x=\"727\" y=\"63\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0zs27ox\" id=\"Association_0zs27ox_di\"\u003e\u003comgdi:waypoint x=\"811\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"811\" y=\"109\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1xbz71r\" id=\"TextAnnotation_1xbz71r_di\"\u003e\u003comgdc:Bounds height=\"42\" width=\"170\" x=\"956\" y=\"65\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0jvyanh\" id=\"Association_0jvyanh_di\"\u003e\u003comgdi:waypoint x=\"1041\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"1041\" y=\"107\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 11,
      "description": "Refresh an IAM users information in the data table. The User is assigned from a field in the selected data table row. The data table row will be refreshed with updated values for the selected user.",
      "export_key": "wf_aws_iam_refresh_user",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719811157540,
      "name": "Example: AWS IAM: Refresh User",
      "object_type": "aws_iam_users",
      "programmatic_name": "wf_aws_iam_refresh_user",
      "tags": [],
      "uuid": "6b186ba1-453e-47d2-9da4-d751abd9ca94",
      "workflow_id": 1
    },
    {
      "actions": [],
      "content": {
        "version": 6,
        "workflow_id": "wf_aws_iam_refresh_access_key",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_refresh_access_key\" isExecutable=\"true\" name=\"Example: AWS IAM: Refresh Access Key\"\u003e\u003cdocumentation\u003eRefresh an IAM access key information in the data table. The access key id and user is assigned from  fields in the selected data table row. The data table row will be refreshed with updated values for the selected access key id.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1t31ltd\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1m2x2fw\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n            \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n            \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User\u0027, \u0027CreateDate\u0027: \u00272019-11-05 15:54:43\u0027},\\n                        {\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User_2\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User_2\u0027,\\n                         \u0027CreateDate\u0027: \u00272019-10-31 16:23:07\u0027, \u0027PasswordLastUsed\u0027: \u00272019-11-12 10:55:42\u0027}\\n                       ],\\n            \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User\\\", \\\"CreateDate\\\": \\\"2019-11-05 15:54:43\\\"}, {\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User_2\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User_2\\\", \\\"CreateDate\\\": \\\"2019-10-31 16:23:07\\\"}]\u0027,\\n            \u0027inputs\u0027: {},\\n            \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                        \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 7951,\\n                        \u0027timestamp\u0027: \u00272019-11-14 13:48:30\u0027\\n                       }\\n}\\n\\n\\\"\\\"\\\"\\nimport re\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_users script\\nDATA_TBL_FIELDS = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"UserId\\\", \\\"Arn\\\", \\\"DefaultUser\\\", \\\"CreateDate\\\", \\\"LoginProfileExists\\\",\\n                   \\\"PasswordLastUsed\\\", \\\"Tags\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"Refresh Access Key\\\"\\n# Processing\\nINPUTS = results.inputs\\nCONTENT = results.content\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        if isinstance(CONTENT, dict) and CONTENT.get(\\\"Status\\\") == \\\"NoSuchEntity\\\":\\n            note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; does not exist \\\" \\\\\\n                         \\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.Status = \\\"Deleted\\\"\\n        elif len(CONTENT) == 1:\\n            workflow.addProperty(\\\"user_exists\\\", {})\\n        else:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Too many results \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned for user \\\" \\\\\\n                        \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.Status = \\\"Deleted\\\"\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned for user \\\" \\\\\\n                     \\\"\u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if note_text:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1t31ltd\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ggoj87\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1t31ltd\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1m2x2fw\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1hpgmd9\"\u003e\u003cincoming\u003eSequenceFlow_1ggoj87\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0o5ggse\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1k2glej\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1ggoj87\" sourceRef=\"ServiceTask_1m2x2fw\" targetRef=\"ExclusiveGateway_1hpgmd9\"/\u003e\u003cserviceTask id=\"ServiceTask_076mskh\" name=\"AWS IAM: List User Access Key IDs\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"278f8cba-ff48-4495-93b0-27349c3fec8b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFGH\u0027,\\n                       \u0027Status\u0027: \u0027Active\u0027, \u0027CreateDate\u0027: \u00272019-11-12 11:09:38\u0027\\n                       }],\\n          \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_User\\\", \\\"AccessKeyId\\\": \\\"ABCDEFGH\\\",\\n                  \\\"Status\\\": \\\"Active\\\", \\\"CreateDate\\\": \\\"2019-11-12 11:09:38\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 5365, \u0027timestamp\u0027: \u00272019-11-21 10:41:22\u0027}}\\n\\\"\\\"\\\"\\n#  Globals\\nDATA_TBL_FIELDS = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"AccessKeyId\\\", \\\"CreateDate\\\", \\\"Status\\\", \\\"DefaultKey\\\"]\\n# List of fields in datatable fn_aws_iam_list_users script last used access keys.\\nDATA_TBL_FIELDS_LUAK = [\\\"LastUsedDate\\\", \\\"ServiceName\\\", \\\"Region\\\"]\\n\\nFN_NAME = \\\"fn_aws_iam_list_user_access_keys\\\"\\nWF_NAME = \\\"Refresh Access Key\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\ndef process_access_key(ak_id, user_name):\\n    row.query_execution_date = QUERY_EXECUTION_DATE\\n    for f in DATA_TBL_FIELDS[2:]:\\n        if ak_id[f] is not None:\\n            row[f] = ak_id[f]\\n        # Add key last used data if it exists.\\n        if ak_id[\\\"key_last_used\\\"] is not None:\\n            luak = ak_id[\\\"key_last_used\\\"]\\n            for l in DATA_TBL_FIELDS_LUAK:\\n                if luak[l] is not None:\\n                    row[l] = luak[l]\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        for ak_id in CONTENT:\\n            if ak_id[\\\"AccessKeyId\\\"] and ak_id[\\\"AccessKeyId\\\"] == row.AccessKeyId:\\n                note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Access key \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; found for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                    .format(WF_NAME, row.AccessKeyId, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n                note_text += \\\"\u0026lt;br\u0026gt;Refreshing data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; and access key \\\" \\\\\\n                             \\\"id \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\u0026lt;/br\u0026gt;\\\"\\\\\\n                    .format(\\\"AWS IAM Access Keys\\\", INPUTS[\\\"aws_iam_user_name\\\"], row.AccessKeyId)\\n                user_name = ak_id[\\\"UserName\\\"]\\n                process_access_key(ak_id, user_name)\\n            else:\\n                note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Access key \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; not found for user \\\" \\\\\\n                            \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n                    .format(WF_NAME, row.AccessKeyId, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n                row.Status = \\\"Deleted\\\"\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; Access key \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; not found \\\" \\\\\\n                    \\\"for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, row.AccessKeyId, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        row.Status = \\\"Deleted\\\"\\n        \\n    if note_text:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0o5ggse\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1rov5ou\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0o5ggse\" name=\"User exists.\" sourceRef=\"ExclusiveGateway_1hpgmd9\" targetRef=\"ServiceTask_076mskh\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cendEvent id=\"EndEvent_08r1do3\"\u003e\u003cincoming\u003eSequenceFlow_1rov5ou\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1k2glej\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1rov5ou\" sourceRef=\"ServiceTask_076mskh\" targetRef=\"EndEvent_08r1do3\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1k2glej\" name=\"User doesn\u0027t exist.\" sourceRef=\"ExclusiveGateway_1hpgmd9\" targetRef=\"EndEvent_08r1do3\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0lc7xyh\"\u003e\u003ctext\u003eList users to\u00a0 determine if user\u00a0 exists. Username assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0dd72al\" sourceRef=\"ServiceTask_1m2x2fw\" targetRef=\"TextAnnotation_0lc7xyh\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1b0wwev\"\u003e\u003ctext\u003eGet access key for user. Update data table row for access key.\n\u00a0Username and access key id assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1o1gdt0\" sourceRef=\"ServiceTask_076mskh\" targetRef=\"TextAnnotation_1b0wwev\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1m2x2fw\" id=\"ServiceTask_1m2x2fw_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"258\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1t31ltd\" id=\"SequenceFlow_1t31ltd_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"258\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"228\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1hpgmd9\" id=\"ExclusiveGateway_1hpgmd9_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"402\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"427\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ggoj87\" id=\"SequenceFlow_1ggoj87_di\"\u003e\u003comgdi:waypoint x=\"358\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"402\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"380\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_076mskh\" id=\"ServiceTask_076mskh_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"507\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0o5ggse\" id=\"SequenceFlow_0o5ggse_di\"\u003e\u003comgdi:waypoint x=\"452\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"507\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"60\" x=\"450\" y=\"176\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_08r1do3\" id=\"EndEvent_08r1do3_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"663\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"681\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1rov5ou\" id=\"SequenceFlow_1rov5ou_di\"\u003e\u003comgdi:waypoint x=\"607\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"663\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"635\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1k2glej\" id=\"SequenceFlow_1k2glej_di\"\u003e\u003comgdi:waypoint x=\"427\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"427\" y=\"17\"/\u003e\u003comgdi:waypoint x=\"681\" y=\"17\"/\u003e\u003comgdi:waypoint x=\"681\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"67\" x=\"521\" y=\"-4\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0lc7xyh\" id=\"TextAnnotation_0lc7xyh_di\"\u003e\u003comgdc:Bounds height=\"71\" width=\"119\" x=\"250\" y=\"52\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0dd72al\" id=\"Association_0dd72al_di\"\u003e\u003comgdi:waypoint x=\"309\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"309\" y=\"123\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1b0wwev\" id=\"TextAnnotation_1b0wwev_di\"\u003e\u003comgdc:Bounds height=\"79\" width=\"163\" x=\"475\" y=\"53\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1o1gdt0\" id=\"Association_1o1gdt0_di\"\u003e\u003comgdi:waypoint x=\"557\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"557\" y=\"132\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 6,
      "description": "Refresh an IAM access key information in the data table. The access key id and user is assigned from  fields in the selected data table row. The data table row will be refreshed with updated values for the selected access key id.",
      "export_key": "wf_aws_iam_refresh_access_key",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719810953026,
      "name": "Example: AWS IAM: Refresh Access Key",
      "object_type": "aws_iam_access_keys",
      "programmatic_name": "wf_aws_iam_refresh_access_key",
      "tags": [],
      "uuid": "feab52e5-30c2-47e7-98a5-cf3093c7fdfe",
      "workflow_id": 13
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "wf_aws_iam_delete_access_key",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_delete_access_key\" isExecutable=\"true\" name=\"Example: AWS IAM: Delete Access Key\"\u003e\u003cdocumentation\u003eDelete an access key pair. The user and access key names are assigned from fields in the selected data table row. The data table row will be refreshed with updated status for the selected access key id.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1k4ay0g\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0u6ls9r\" name=\"AWS IAM: Delete Access Keys\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6a15d8e2-7472-4460-858e-3ff83221e183\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: [{\u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027OK\u0027}],\\n         \u0027raw\u0027: \u0027[{\\\"AccessKeyId\\\": \\\"ABCDEFG\\\", \\\"Status\\\": \\\"OK\\\"}]\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User_1\u0027, \u0027aws_iam_access_keys\u0027: \u0027ABCDEFG\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                     \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 752, \u0027timestamp\u0027: \u00272020-01-16 13:47:07\u0027\\n                    }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_access_keys  script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_access_keys\\\"\\nWF_NAME = \\\"Delete Access Key\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nEXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_keys = []\\n    no_such_entity_keys = []\\n    if CONTENT:\\n        for ak_stat in CONTENT:\\n            if ak_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_keys.append(ak_stat[\\\"AccessKeyId\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_keys.append(ak_stat[\\\"AccessKeyId\\\"])\\n        if deleted_keys:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The Access Key Id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was deleted \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, \u0027,\u0027.join(deleted_keys), INPUTS[\\\"aws_iam_user_name\\\"],  FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Access keyId id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; does not exist \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, \u0027,\u0027.join(no_such_entity_keys), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        row.Status = \\\"Deleted\\\"\\n        row.query_execution_date = EXECUTION_DATE\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were no results returned for \\\" \\\\\\n        \\\"access key id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; access key  Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_access_keys\\\"], FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ninputs.aws_iam_access_keys = row.AccessKeyId\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1k4ay0g\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_13wjqhq\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1k4ay0g\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0u6ls9r\"/\u003e\u003cendEvent id=\"EndEvent_0ima94h\"\u003e\u003cincoming\u003eSequenceFlow_13wjqhq\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_13wjqhq\" sourceRef=\"ServiceTask_0u6ls9r\" targetRef=\"EndEvent_0ima94h\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1jc17xg\"\u003e\u003ctext\u003eDelete access key of a user. Username and access key id are assigned from data table rows.\u00a0 Data table row is updated for access key \"Status\".\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1udfkkp\" sourceRef=\"ServiceTask_0u6ls9r\" targetRef=\"TextAnnotation_1jc17xg\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0u6ls9r\" id=\"ServiceTask_0u6ls9r_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"227\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1k4ay0g\" id=\"SequenceFlow_1k4ay0g_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"227\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"212.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0ima94h\" id=\"EndEvent_0ima94h_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"367\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"385\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13wjqhq\" id=\"SequenceFlow_13wjqhq_di\"\u003e\u003comgdi:waypoint x=\"327\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"367\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"347\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1jc17xg\" id=\"TextAnnotation_1jc17xg_di\"\u003e\u003comgdc:Bounds height=\"100\" width=\"201\" x=\"176\" y=\"26\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1udfkkp\" id=\"Association_1udfkkp_di\"\u003e\u003comgdi:waypoint x=\"277\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"278\" y=\"126\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Delete an access key pair. The user and access key names are assigned from fields in the selected data table row. The data table row will be refreshed with updated status for the selected access key id.",
      "export_key": "wf_aws_iam_delete_access_key",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719372852812,
      "name": "Example: AWS IAM: Delete Access Key",
      "object_type": "aws_iam_access_keys",
      "programmatic_name": "wf_aws_iam_delete_access_key",
      "tags": [],
      "uuid": "72d888d0-07de-434d-8c4d-95f44cbed6d5",
      "workflow_id": 3
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "wf_aws_iam_delete_access_keys",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_delete_access_keys\" isExecutable=\"true\" name=\"Example: AWS IAM: Delete Access Keys\"\u003e\u003cdocumentation\u003eDelete access key pairs associated an IAM user. The user and access key names are assigned from fields in the selected data table row.  The data table row will be refreshed with updated access key values for the selected user.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1fhrgfm\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_00rux21\" name=\"AWS IAM: Delete Access Keys\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6a15d8e2-7472-4460-858e-3ff83221e183\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: [{\u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027OK\u0027}],\\n         \u0027raw\u0027: \u0027[{\\\"AccessKeyId\\\": \\\"ABCDEFG\\\", \\\"Status\\\": \\\"OK\\\"}]\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User_1\u0027, \u0027aws_iam_access_keys\u0027: \u0027ABCDEFG\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                     \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 752, \u0027timestamp\u0027: \u00272020-01-16 13:47:07\u0027\\n                    }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_access_keys  script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_access_keys\\\"\\nWF_NAME = \\\"Delete Access Key\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_keys = []\\n    no_such_entity_keys = []\\n    if CONTENT:\\n        for ak_stat in CONTENT:\\n            if ak_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_keys.append(ak_stat[\\\"AccessKeyId\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_keys.append(ak_stat[\\\"AccessKeyId\\\"])\\n        if deleted_keys:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The Access Key Ids \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; were deleted \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, \u0027,\u0027.join(deleted_keys), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Access keyId ids \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; does not exist \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, \u0027,\u0027.join(no_such_entity), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were no results returned for \\\" \\\\\\n        \\\"access key id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; access key  Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_access_keys\\\"], FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ninputs.aws_iam_access_keys = row.AccessKeyIds\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1fhrgfm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1yykevw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1fhrgfm\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_00rux21\"/\u003e\u003cserviceTask id=\"ServiceTask_0y1inlq\" name=\"AWS IAM: List User Access Key IDs\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"278f8cba-ff48-4495-93b0-27349c3fec8b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027,\\n                       \u0027Status\u0027: \u0027Active\u0027, \u0027CreateDate\u0027: \u00272019-11-12 11:09:38\u0027\\n                       }],\\n          \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_User\\\", \\\"AccessKeyId\\\": \\\"ABCDEFG\\\",\\n                  \\\"Status\\\": \\\"Active\\\", \\\"CreateDate\\\": \\\"2019-11-12 11:09:38\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 5365, \u0027timestamp\u0027: \u00272019-11-21 10:41:22\u0027}}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_groups script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_access_keys\\\"\\nWF_NAME = \\\"Delete Access Keys\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nnote_text = \u0027\u0027\\n\\ndef main():\\n\\n    if CONTENT:\\n        access_key_ids = []\\n        for ak in CONTENT:\\n            if ak[\\\"AccessKeyId\\\"] is not None:\\n                access_key_ids.append(ak[\\\"AccessKeyId\\\"])\\n        row.AccessKeyIds = \\\",\\\".join(access_key_ids)\\n    else:\\n        row.AccessKeyIds = \\\"\\\"\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1yykevw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1rnv05r\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1yykevw\" sourceRef=\"ServiceTask_00rux21\" targetRef=\"ServiceTask_0y1inlq\"/\u003e\u003cendEvent id=\"EndEvent_17sukhf\"\u003e\u003cincoming\u003eSequenceFlow_1rnv05r\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1rnv05r\" sourceRef=\"ServiceTask_0y1inlq\" targetRef=\"EndEvent_17sukhf\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1mrd9a1\"\u003e\u003ctext\u003eDelete all access keys of\u00a0 a user. Username and access key ids assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1y68sqr\" sourceRef=\"ServiceTask_00rux21\" targetRef=\"TextAnnotation_1mrd9a1\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1y23yvn\"\u003e\u003ctext\u003eGet updated access key list for user\u00a0 and update data table.\n\u00a0Username assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0dckrky\" sourceRef=\"ServiceTask_0y1inlq\" targetRef=\"TextAnnotation_1y23yvn\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_00rux21\" id=\"ServiceTask_00rux21_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"235\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1fhrgfm\" id=\"SequenceFlow_1fhrgfm_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"235\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"216.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0y1inlq\" id=\"ServiceTask_0y1inlq_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"453\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1yykevw\" id=\"SequenceFlow_1yykevw_di\"\u003e\u003comgdi:waypoint x=\"335\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"453\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"349\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_17sukhf\" id=\"EndEvent_17sukhf_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"611\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"584\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1rnv05r\" id=\"SequenceFlow_1rnv05r_di\"\u003e\u003comgdi:waypoint x=\"553\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"611\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"537\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1mrd9a1\" id=\"TextAnnotation_1mrd9a1_di\"\u003e\u003comgdc:Bounds height=\"71\" width=\"177\" x=\"196\" y=\"45\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1y68sqr\" id=\"Association_1y68sqr_di\"\u003e\u003comgdi:waypoint x=\"285\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"285\" y=\"116\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1y23yvn\" id=\"TextAnnotation_1y23yvn_di\"\u003e\u003comgdc:Bounds height=\"57\" width=\"214\" x=\"396\" y=\"52\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0dckrky\" id=\"Association_0dckrky_di\"\u003e\u003comgdi:waypoint x=\"503\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"503\" y=\"109\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Delete access key pairs associated an IAM user. The user and access key names are assigned from fields in the selected data table row.  The data table row will be refreshed with updated access key values for the selected user.",
      "export_key": "wf_aws_iam_delete_access_keys",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719373033504,
      "name": "Example: AWS IAM: Delete Access Keys",
      "object_type": "aws_iam_users",
      "programmatic_name": "wf_aws_iam_delete_access_keys",
      "tags": [],
      "uuid": "995c0e27-b48a-4f38-840f-647ab972c2c8",
      "workflow_id": 5
    },
    {
      "actions": [],
      "content": {
        "version": 23,
        "workflow_id": "wf_aws_iam_delete_user",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_delete_user\" isExecutable=\"true\" name=\"Example: AWS IAM: Delete User\"\u003e\u003cdocumentation\u003eDelete the selected IAM user. The User is assigned from a field in the selected data table row. The data table row will be refreshed will updated values for the selected user.\n\nNote: Unlike the AWS Management Console, when you delete a user programmatically, you must delete the items attached to the user or the deletion fails. Before attempting to delete a user, the following items if associated with the user will be removed, de-activated or deleted.:\n\n    Password ( DeleteLoginProfile )\n    Access keys ( DeleteAccessKey )\n    Inline policies ( DeleteUserPolicy )\n    Attached managed policies ( DetachUserPolicy ) \n    Group memberships ( RemoveUserFromGroup )\n    Signing certificate ( DeleteSigningCertificate )\n    SSH public key ( DeleteSSHPublicKey )\n    Git credentials ( DeleteServiceSpecificCredential )\n    Multi-factor authentication (MFA) device ( DeactivateMFADevice , DeleteVirtualMFADevice )\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1izc3u0\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0s76zua\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n            \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n            \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User\u0027, \u0027CreateDate\u0027: \u00272019-11-05 15:54:43\u0027},\\n                        {\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User_2\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User_2\u0027,\\n                         \u0027CreateDate\u0027: \u00272019-10-31 16:23:07\u0027, \u0027PasswordLastUsed\u0027: \u00272019-11-12 10:55:42\u0027}\\n                       ],\\n            \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User\\\", \\\"CreateDate\\\": \\\"2019-11-05 15:54:43\\\"}, \\n            {\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User_2\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User_2\\\", \\\"CreateDate\\\": \\\"2019-10-31 16:23:07\\\"}]\u0027,\\n            \u0027inputs\u0027: {},\\n            \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                        \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 7951,\\n                        \u0027timestamp\u0027: \u00272019-11-14 13:48:30\u0027\\n                       }\\n}\\n\\n\\\"\\\"\\\"\\nimport re\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_users script\\nDATA_TBL_FIELDS = [\\\"UserName\\\", \\\"LoginProfileExists\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nINPUTS = results.inputs\\nCONTENT = results.content\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        if isinstance(CONTENT, dict) and CONTENT.get(\\\"Status\\\") == \\\"NoSuchEntity\\\":\\n            note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was not found for Resilient \\\" \\\\\\n                         \\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.Status = \\\"Deleted\\\"\\n        elif len(CONTENT) == 1:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was found \\\" \\\\\\n                        \\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            workflow.addProperty(\\\"user_exists\\\", {})\\n            u = CONTENT.pop()\\n            if u[\\\"LoginProfileExists\\\"] is not None and u[\\\"LoginProfileExists\\\"].lower() == \\\"yes\\\":\\n                 workflow.addProperty(\\\"has_login_profile\\\", {})\\n            if u[\\\"DefaultUser\\\"] is not None and u[\\\"DefaultUser\\\"].lower() == \\\"yes\\\":\\n                workflow.addProperty(\\\"is_default_user\\\", {})\\n                note_text += \\\"\u0026lt;br\u0026gt;This is the default user and therefore will not be deleted.\u0026lt;/br\u0026gt;\\\"\\n        else:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Too many results \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.LoginProfileExists = \\\"No\\\"\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \\\" \\\\\\n                     \\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    \\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1izc3u0\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0536rkw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1izc3u0\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0s76zua\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0do5med\"\u003e\u003cincoming\u003eSequenceFlow_1gsn1ap\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1fky00t\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0x9sjg9\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003cserviceTask id=\"ServiceTask_1civ9g8\" name=\"AWS IAM: Delete Login Profile\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"22d5a7a2-9e89-4011-b53d-604a4aeaad2e\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_login_profile script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: \u0027NoSuchEntity\u0027, \u0027raw\u0027: \u0027\\\"NoSuchEntity\\\"\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                     \u0027host\u0027: \u0027myhost.ie.ibm.com\u0027, \u0027execution_time_ms\u0027: 9170, \u0027timestamp\u0027: \u00272019-11-18 16:24:17\u0027\\n                     }\\n}\\nNosuchEntity\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: \u0027OK\u0027, \u0027raw\u0027: \u0027\\\"OK\\\"\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                     \u0027host\u0027: \u0027myhost.ie.ibm.com\u0027, \u0027execution_time_ms\u0027: 9170, \u0027timestamp\u0027: \u00272019-11-18 16:24:17\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_delete_login_profile  script\\nDATA_TBL_FIELDS = [\\\"LoginProfileExists\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_login_profile\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT=False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        if CONTENT == \\\"OK\\\":\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Login profile deleted for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.LoginProfileExists = \\\"No\\\"\\n        elif CONTENT == \\\"NoSuchEntity\\\":\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Login profile does not exist for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.LoginProfileExists = \\\"No\\\"\\n\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1fky00t\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_06178d2\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1fky00t\" name=\"Has a login profile.\" sourceRef=\"ExclusiveGateway_0do5med\" targetRef=\"ServiceTask_1civ9g8\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_login_profile\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_1izll8i\" name=\"AWS IAM: List User Access Key IDs\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"278f8cba-ff48-4495-93b0-27349c3fec8b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027,\\n                       \u0027Status\u0027: \u0027Active\u0027, \u0027CreateDate\u0027: \u00272019-11-12 11:09:38\u0027\\n                       }],\\n          \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_User\\\", \\\"AccessKeyId\\\": \\\"ABCDEFG\\\",\\n                  \\\"Status\\\": \\\"Active\\\", \\\"CreateDate\\\": \\\"2019-11-12 11:09:38\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 5365, \u0027timestamp\u0027: \u00272019-11-21 10:41:22\u0027}}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_access_keys script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_access_keys\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT=False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Access key\u0027 result(s) returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        access_key_ids = []\\n        for ak in CONTENT:\\n            if ak[\\\"AccessKeyId\\\"] is not None:\\n                workflow.addProperty(\\\"has_access_keys\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Access key\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_user_access_keys_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0x9sjg9\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_06178d2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_01ws640\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0x9sjg9\" name=\"Doesn\u0027t have a login profile.\" sourceRef=\"ExclusiveGateway_0do5med\" targetRef=\"ServiceTask_1izll8i\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_login_profile\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_06178d2\" sourceRef=\"ServiceTask_1civ9g8\" targetRef=\"ServiceTask_1izll8i\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_119mcb9\"\u003e\u003cincoming\u003eSequenceFlow_01ws640\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_11hmndb\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1wpyrsg\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_01ws640\" sourceRef=\"ServiceTask_1izll8i\" targetRef=\"ExclusiveGateway_119mcb9\"/\u003e\u003cserviceTask id=\"ServiceTask_15sjdh5\" name=\"AWS IAM: Delete Access Keys\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6a15d8e2-7472-4460-858e-3ff83221e183\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027OK\u0027},\\n                      {\u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\\\"AccessKeyId\\\": \\\"ABCDEFG\\\", \\\"Status\\\": \\\"OK\\\"},\\n                  {\\\"AccessKeyId\\\": \\\"ABCDEFG\\\", \\\"Status\\\": \\\"NoSuchEntity\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027test_User\u0027, \u0027aws_iam_access_keys\u0027: \u0027ABCDEFG,ABCDEFG\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 37199, \u0027timestamp\u0027: \u00272019-11-21 14:31:13\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_access_keys  script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_access_keys\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT=False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_keys = []\\n    no_such_entity_keys = []\\n    if CONTENT:\\n        for ak_status in CONTENT:\\n            if ak_status[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_keys.append(ak_status[\\\"AccessKeyId\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_keys.append(ak_status[\\\"AccessKeyId\\\"])\\n        if deleted_keys:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Access Key Ids \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; deleted \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_keys), deleted_keys, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Access Key Ids \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_keys), no_such_entity_keys, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        row.AccessKeyIds = \\\"\\\"\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ncontent = workflow.properties.list_user_access_keys_results.content\\naccess_key_ids = []\\nfor ak_id in content:\\n    if ak_id[\\\"AccessKeyId\\\"] is not None:\\n        access_key_ids.append(ak_id[\\\"AccessKeyId\\\"])\\ninputs.aws_iam_access_keys = \\\",\\\".join(access_key_ids)\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_11hmndb\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1fzhdg0\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_11hmndb\" name=\"Has access keys.\" sourceRef=\"ExclusiveGateway_119mcb9\" targetRef=\"ServiceTask_15sjdh5\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_access_keys\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_13tmpe4\" name=\"AWS IAM: List User Policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"64a30bb5-b539-45d6-b6e5-55674539d411\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyName\u0027: \u0027test_pol\u0027},\\n                      {\u0027PolicyName\u0027: \u0027test_pol_2\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::123456789123:policy/test_pol_2\u0027},\\n                      {\u0027PolicyName\u0027: \u0027AmazonRoute53ReadOnlyAccess\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\u0027}],\\n          \u0027raw\u0027: \u0027[{\\\"PolicyName\\\": \\\"test_pol\\\"}, {\\\"PolicyName\\\": \\\"test_pol_2\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::123456789123:policy/test_pol_2\\\"},\\n                    {\\\"PolicyName\\\": \\\"AmazonRoute53ReadOnlyAccess\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 87423, \u0027timestamp\u0027: \u00272019-11-21 11:55:29\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_groups script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_policies\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT=False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Policy name\u0027 result(s) returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        policy_names = []\\n        for pol in CONTENT:\\n            if pol[\\\"PolicyName\\\"] is not None:\\n                workflow.addProperty(\\\"has_policies\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Policy name\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n    \\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_user_policies_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1wpyrsg\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1fzhdg0\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1qac2f4\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1wpyrsg\" name=\"Doesn\u0027t have access keys.\" sourceRef=\"ExclusiveGateway_119mcb9\" targetRef=\"ServiceTask_13tmpe4\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_access_keys\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_1fzhdg0\" sourceRef=\"ServiceTask_15sjdh5\" targetRef=\"ServiceTask_13tmpe4\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_03xbdyk\"\u003e\u003cincoming\u003eSequenceFlow_1qac2f4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0m4qiat\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0h90voj\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1qac2f4\" sourceRef=\"ServiceTask_13tmpe4\" targetRef=\"ExclusiveGateway_03xbdyk\"/\u003e\u003cserviceTask id=\"ServiceTask_0whqlz7\" name=\"AWS IAM: Detach User policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"10a78fb7-0c3e-48f3-88b8-2a464dbb0715\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_detach_user_policies script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyName\u0027: \u0027AWSDenyAll\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027PolicyName\u0027: \u0027AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027PolicyName\u0027: \\\"AWSDenyAll\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027PolicyName\u0027: \u0027AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_arns\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User_1\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_detach_user_policies  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_detach_user_policies\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    detached = 0\\n    no_such_entity = 0\\n    detached_policies = []\\n    no_such_entity_policies = []\\n    if CONTENT:\\n        for pol_stat in CONTENT:\\n            if pol_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                detached += 1\\n                detached_policies.append(pol_stat[\\\"PolicyName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_policies.append(pol_stat[\\\"PolicyName\\\"])\\n        if detached_policies:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Policies \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; detached \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(detached_policies), \\\", \\\".join(str(i) for i in detached_policies), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Policies \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_policies), \\\", \\\".join(str(i) for i in no_such_entity_policies), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ncontent = workflow.properties.list_user_policies_results.content\\npolicy_names = []\\nfor pol in content:\\n    if pol[\\\"PolicyName\\\"] is not None:\\n        policy_names.append(pol[\\\"PolicyName\\\"])\\ninputs.aws_iam_policy_names = \\\",\\\".join(policy_names)\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0m4qiat\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0qlvv4k\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0m4qiat\" name=\"Has attached policies.\" sourceRef=\"ExclusiveGateway_03xbdyk\" targetRef=\"ServiceTask_0whqlz7\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_policies\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_0iyqm1d\" name=\"AWS IAM: List User Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8b67eb7-166c-4f5c-8291-1d0e3bd14e68\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027GroupName\u0027: \u0027system-admins\u0027, \u0027GroupId\u0027: \u0027ABCDEFG\u0027,\\n                      \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:group/system-admins\u0027, \u0027CreateDate\u0027: \u00272017-05-29 20:37:53\u0027}],\\n                      \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"GroupName\\\": \\\"system-admins\\\", \\\"GroupId\\\": \\\"ABCDEFG\\\",\\n                      \\\"Arn\\\": \\\"arn:aws:iam::123456789123:group/system-admins\\\", \\\"CreateDate\\\": \\\"2017-05-29 20:37:53\\\"\\n                      }\\n                    ]\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                     \u0027execution_time_ms\u0027: 1070, \u0027timestamp\u0027: \u00272019-11-18 10:19:19\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_groups script\\nDATA_TBL_FIELDS = [\\\"Groups\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_groups\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT=False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Group\u0027 result(s) returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        groups = []\\n        for grp in CONTENT:\\n            if grp[\\\"GroupName\\\"]:\\n                workflow.addProperty(\\\"is_group_member\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Group\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_user_groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0h90voj\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0qlvv4k\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_03cfb0e\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0h90voj\" name=\"Does not have attached policies.\" sourceRef=\"ExclusiveGateway_03xbdyk\" targetRef=\"ServiceTask_0iyqm1d\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_policies\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0qlvv4k\" sourceRef=\"ServiceTask_0whqlz7\" targetRef=\"ServiceTask_0iyqm1d\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1e1nnri\"\u003e\u003cincoming\u003eSequenceFlow_03cfb0e\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1doiaom\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1vxmza3\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_03cfb0e\" sourceRef=\"ServiceTask_0iyqm1d\" targetRef=\"ExclusiveGateway_1e1nnri\"/\u003e\u003cserviceTask id=\"ServiceTask_0iuu80s\" name=\"AWS IAM: Remove User From Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7efc8616-ed52-4a8f-9f25-5c168b681ba9\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_detach_user_policies script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027PolicyArn\u0027: \\\"arn:aws:iam::aws:policy/AWSDenyAll\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_arns\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User_1\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_detach_user_policies  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_remove_user_from_groups\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_groups = []\\n    no_such_entity_groups = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_groups.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_groups.append(grp_stat[\\\"GroupName\\\"])\\n        if deleted_groups:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Groups \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; removed \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_groups), \\\", \\\".join(str(i) for i in deleted_groups), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Groups \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_groups), \\\", \\\".join(str(i) for i in no_such_entity_groups), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        row.Groups = \u0027\u0027\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ncontent = workflow.properties.list_user_groups_results.content\\ngroups = []\\nfor grp in content:\\n    if grp[\\\"GroupName\\\"] is not None:\\n        groups.append(grp[\\\"GroupName\\\"])\\ninputs.aws_iam_group_names = \\\",\\\".join(groups)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1doiaom\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0uvp3da\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1doiaom\" name=\"Is a group member.\" sourceRef=\"ExclusiveGateway_1e1nnri\" targetRef=\"ServiceTask_0iuu80s\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_group_member\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_1vxmza3\" name=\"Is not a group member.\" sourceRef=\"ExclusiveGateway_1e1nnri\" targetRef=\"ServiceTask_032rb9j\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_group_member\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0uvp3da\" sourceRef=\"ServiceTask_0iuu80s\" targetRef=\"ServiceTask_032rb9j\"/\u003e\u003cendEvent id=\"EndEvent_0domjpp\"\u003e\u003cincoming\u003eSequenceFlow_1goxcss\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0dll6hk\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_17q0k1j\u003c/incoming\u003e\u003c/endEvent\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1mqg0j9\"\u003e\u003cincoming\u003eSequenceFlow_0536rkw\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1goxcss\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1yelc0d\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1goxcss\" name=\"User doesn\u0027t exist.\" sourceRef=\"ExclusiveGateway_1mqg0j9\" targetRef=\"EndEvent_0domjpp\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0536rkw\" sourceRef=\"ServiceTask_0s76zua\" targetRef=\"ExclusiveGateway_1mqg0j9\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_19z8tdz\"\u003e\u003cincoming\u003eSequenceFlow_1yelc0d\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1gsn1ap\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0dll6hk\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1yelc0d\" name=\"User exists.\" sourceRef=\"ExclusiveGateway_1mqg0j9\" targetRef=\"ExclusiveGateway_19z8tdz\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_1gsn1ap\" name=\"Is not default user.\" sourceRef=\"ExclusiveGateway_19z8tdz\" targetRef=\"ExclusiveGateway_0do5med\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_default_user\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0dll6hk\" name=\"Is default user.\" sourceRef=\"ExclusiveGateway_19z8tdz\" targetRef=\"EndEvent_0domjpp\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_default_user\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_032rb9j\" name=\"AWS IAM: List SSH Public Keys\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a7b28b9e-6a27-44c1-90f2-d4d3d5f54ba9\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_ssh_public_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n          \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027SSHPublicKeyId\u0027: \u0027ABCDEFG\u0027, \\n                       \u0027Status\u0027: \u0027Active\u0027, \u0027UploadDate\u0027: \u00272020-02-25 11:05:17\u0027\\n                      }\\n                     ], \\n          \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_user_10\\\", \\\"SSHPublicKeyId\\\": \\\"ABCDEFG\\\", \\n                  \\\"Status\\\": \\\"Active\\\", \\\"UploadDate\\\": \\\"2020-02-25 11:05:17\\\"}]\u0027, \\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user\u0027}, \\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027, \\n                      \u0027execution_time_ms\u0027: 657, \u0027timestamp\u0027: \u00272020-02-25 16:11:28\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_ssh_public_keys script\\nDATA_TBL_FIELDS = [\\\"SSHPublicKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_ssh_public_keys\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT=False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027SSH Public keys\u0027 returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        access_key_ids = []\\n        for sshk_id in CONTENT:\\n            if sshk_id[\\\"SSHPublicKeyId\\\"] is not None:\\n                workflow.addProperty(\\\"has_ssh_public_keys\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027SSH Public keys\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_ssh_keys_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1vxmza3\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0uvp3da\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1d54zar\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_1vqtsd1\" name=\"AWS IAM: Delete SSH Public Keys\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"17506b61-ff8f-44b2-937e-15a3ae3d5d0a\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_ssh_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027SSHPublicKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027SSHPublicKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027SSHPublicKeyId\u0027: \\\"ABCDEFG\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027SSHPublicKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_ssh_keys_ids\u0027: \u0027ABCDEFG\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_ssh_keys  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_ssh_keys\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_keys = []\\n    no_such_entity_keys = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_keys.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_keys.append(grp_stat[\\\"GroupName\\\"])\\n        if deleted_keys:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027SSH Public keys\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; removed \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_keys), \\\", \\\".join(str(i) for i in deleted_keys), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027SSH Public keys\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_keys), \\\", \\\".join(str(i) for i in no_such_entity_keys), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ncontent = workflow.properties.list_ssh_keys_results.content\\nssh_key_ids = []\\nfor ssh_key_id in content:\\n    if ssh_key_id[\\\"SSHPublicKeyId\\\"] is not None:\\n        ssh_key_ids.append(ssh_key_id[\\\"SSHPublicKeyId\\\"])\\ninputs.aws_iam_ssh_key_ids = \\\",\\\".join(ssh_key_ids)\\n\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1c8w1el\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1tmswh1\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_094k23t\"\u003e\u003cincoming\u003eSequenceFlow_1d54zar\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1c8w1el\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0q6a3at\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1d54zar\" sourceRef=\"ServiceTask_032rb9j\" targetRef=\"ExclusiveGateway_094k23t\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1c8w1el\" name=\"User has SSH public keys.\" sourceRef=\"ExclusiveGateway_094k23t\" targetRef=\"ServiceTask_1vqtsd1\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_ssh_public_keys\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0q6a3at\" name=\"User doesn\u0027t have SSH public keys.\" sourceRef=\"ExclusiveGateway_094k23t\" targetRef=\"ServiceTask_0x796wp\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_ssh_public_keys\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_0x796wp\" name=\"AWS IAM: List Service Specific Cr...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ec76a52d-94e3-447c-8b0c-f049c365b4f3\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_service_specific_credentials script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n         \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027Status\u0027: \u0027Active\u0027, \u0027ServiceUserName\u0027: \u0027iam_test_user\u0027, \\n                      \u0027CreateDate\u0027: \u00272020-02-25 10:43:24\u0027, \u0027ServiceSpecificCredentialId\u0027: \u0027ABCDEFG\u0027, \\n                      \u0027ServiceName\u0027: \u0027codecommit.amazonaws.com\u0027\\n                     },\\n                     {\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027Status\u0027: \u0027Active\u0027, \u0027ServiceUserName\u0027: \u0027iam_test_user_10\u0027,\\n                      \u0027CreateDate\u0027: \u00272020-02-26 11:50:52\u0027, \u0027ServiceSpecificCredentialId\u0027: \u0027ABCDEFG\u0027, \\n                      \u0027ServiceName\u0027: \u0027cassandra.amazonaws.com\u0027}], \\n         \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_user\\\", \\\"Status\\\": \\\"Active\\\", \\\"ServiceUserName\\\": \\\"iam_test_user_10\\\", \\n                   \\\"CreateDate\\\": \\\"2020-02-25 10:43:24\\\", \\\"ServiceSpecificCredentialId\\\": \\\"ABCDEFG\\\", \\\"ServiceName\\\": \\\"codecommit.amazonaws.com\\\"}, \\n                   {\\\"UserName\\\": \\\"iam_test_user_10\\\", \\\"Status\\\": \\\"Active\\\", \\\"ServiceUserName\\\": \\\"iam_test_user_10\\\", \\n                   \\\"CreateDate\\\": \\\"2020-02-26 11:50:52\\\", \\\"ServiceSpecificCredentialId\\\": \\\"ABCDEFG\\\", \\\"ServiceName\\\": \\\"cassandra.amazonaws.com\\\"}]\u0027, \\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user\u0027}, \\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027, \\n                     \u0027execution_time_ms\u0027: 982, \u0027timestamp\u0027: \u00272020-02-26 11:56:51\u0027\\n                    }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_service_specific_credentials script\\nDATA_TBL_FIELDS = [\\\"ServiceSpecificCredentialIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_service_specific_credentials\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Service specific credentials\u0027 returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        for ssc_id in CONTENT:\\n            if ssc_id[\\\"ServiceSpecificCredentialId\\\"] is not None:\\n                workflow.addProperty(\\\"has_srv_creds\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Service specific credentials\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_srv_specific_creds_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tmswh1\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0q6a3at\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0onuhu7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tmswh1\" sourceRef=\"ServiceTask_1vqtsd1\" targetRef=\"ServiceTask_0x796wp\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1dcgog4\"\u003e\u003cincoming\u003eSequenceFlow_0onuhu7\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0idkipc\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1uhivst\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0onuhu7\" sourceRef=\"ServiceTask_0x796wp\" targetRef=\"ExclusiveGateway_1dcgog4\"/\u003e\u003cserviceTask id=\"ServiceTask_1um41mk\" name=\"AWS IAM: Delete Service Specific ...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"590079fe-1bb9-47d9-8c3a-7084838232c7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_ss_creds script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027ServiceSpecificCredentialId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027ServiceSpecificCredentialId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027ServiceSpecificCredentialId: \\\"ABCDEFG\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027ServiceSpecificCredentialId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_ssc_ids\u0027: \u0027ABCDEFG\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_ss_creds  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_ss_creds\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_creds = []\\n    no_such_entity_creds = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_creds.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_creds.append(grp_stat[\\\"GroupName\\\"])\\n        if deleted_creds:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Service specific credentials\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; removed \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_creds), \\\", \\\".join(str(i) for i in deleted_creds), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Service specific credentials\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_creds), \\\", \\\".join(str(i) for i in no_such_entity_creds), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ncontent = workflow.properties.list_srv_specific_creds_results.content\\nsrv_specific_cred_ids = []\\nfor ssc_id in content:\\n    if ssc_id[\\\"ServiceSpecificCredentialId\\\"] is not None:\\n        srv_specific_cred_ids.append(ssc_id[\\\"ServiceSpecificCredentialId\\\"])\\ninputs.aws_iam_ssc_ids = \\\",\\\".join(srv_specific_cred_ids)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0idkipc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1uemn5i\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0idkipc\" name=\"User has service specific credentials.\" sourceRef=\"ExclusiveGateway_1dcgog4\" targetRef=\"ServiceTask_1um41mk\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_srv_creds\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_1uhivst\" name=\"User doesn\u0027t have service specific credentials.\" sourceRef=\"ExclusiveGateway_1dcgog4\" targetRef=\"ServiceTask_182s08y\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_srv_creds\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_182s08y\" name=\"AWS IAM: List Signing Certificate...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"28643fbd-6a39-411e-9b67-8507e4a228e7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_signing_certificates script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n         \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027CertificateId\u0027: \u0027ABCDEFGH1234567\u0027, \\n                      \u0027CertificateBody\u0027: \u0027-----BEGIN CERTIFICATE-----\\\\nMIID...Apg=\\\\n-----END CERTIFICATE-----\u0027, \\n                      \u0027Status\u0027: \u0027Active\u0027, \u0027UploadDate\u0027: \u00272020-02-26 12:25:27\u0027}], \\n         \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_user\\\", \\\"CertificateId\\\": \\\"ABCDEFGH1234567\\\", \\\"CertificateBody\\\": \\n                 \\\"-----BEGIN CERTIFICATE-----\\\\\\\\nMIID...Apg=\\\\\\\\n-----END CERTIFICATE-----\\\", \\\"Status\\\": \\\"Active\\\", \\\"UploadDate\\\": \\\"2020-02-26 12:25:27\\\"}]\u0027, \\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user\u0027}, \\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 729, \u0027timestamp\u0027: \u00272020-02-26 12:33:57\u0027\\n        }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_signing_certificates script\\nDATA_TBL_FIELDS = [\\\"CertificateIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_signing_certificates\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT=False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Signing Certificates\u0027 returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        for scert_id in CONTENT:\\n            if scert_id[\\\"CertificateId\\\"] is not None:\\n                workflow.addProperty(\\\"has_sign_certs\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Signing Certificates\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_signing_certs_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1uemn5i\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1uhivst\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1af0uxz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1uemn5i\" sourceRef=\"ServiceTask_1um41mk\" targetRef=\"ServiceTask_182s08y\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1gfuqq8\"\u003e\u003cincoming\u003eSequenceFlow_1af0uxz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1i0yldd\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_01agcix\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1af0uxz\" sourceRef=\"ServiceTask_182s08y\" targetRef=\"ExclusiveGateway_1gfuqq8\"/\u003e\u003cserviceTask id=\"ServiceTask_02vzvwx\" name=\"AWS IAM: Delete Signing Certifica...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8fda0978-9293-4078-9578-c9855ff26f85\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_signing_certs script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027CertificateId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027OK\u0027},\\n                      {\u0027CertificateId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027CertificateId: \\\"ABCDEFG\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027CertificateId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_sign_cert_ids\u0027: \u0027ABCDEFG\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_list_signing_certs  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_signing_certs\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_certs = []\\n    no_such_entity_certs = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_certs.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_certs.append(grp_stat[\\\"GroupName\\\"])\\n        if deleted_certs:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Signing Certificates\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; removed \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_certs), \\\", \\\".join(str(i) for i in deleted_certs), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Signing Certificates\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_certs), \\\", \\\".join(str(i) for i in no_such_entity_certs), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ncontent = workflow.properties.list_signing_certs_results.content\\nsign_cert_ids = []\\nfor scert_id in content:\\n    if scert_id[\\\"CertificateId\\\"] is not None:\\n        sign_cert_ids.append(scert_id[\\\"CertificateId\\\"])\\ninputs.aws_iam_sign_cert_ids = \\\",\\\".join(sign_cert_ids)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1i0yldd\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10ezp90\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1i0yldd\" name=\"User has signing certificates.\" sourceRef=\"ExclusiveGateway_1gfuqq8\" targetRef=\"ServiceTask_02vzvwx\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_sign_certs\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_01agcix\" name=\"User doesn\u0027t have siging certificates.\" sourceRef=\"ExclusiveGateway_1gfuqq8\" targetRef=\"ServiceTask_0z95wxx\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_sign_certs\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_0z95wxx\" name=\"AWS IAM: List MFA Devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d85d59b9-b5e1-444e-9b9f-ea2f5dae64ae\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_mfa_devices script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n         \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \\n                      \u0027EnableDate\u0027: \u00272020-02-26 16:55:05\u0027, \u0027is_virtual\u0027: True}], \\n         \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_user_10\\\", \\\"SerialNumber\\\": \\\"arn:aws:iam::123456789123:mfa/iam_test_user_10\\\", \\n                 \\\"EnableDate\\\": \\\"2020-02-26 16:55:05\\\", \u0027is_virtual\u0027: True}]\u0027, \\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user_10\u0027}, \\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ie.ibm.com\u0027, \\n                     \u0027execution_time_ms\u0027: 5644, \u0027timestamp\u0027: \u00272020-02-26 17:37:48\u0027\\n                    }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_mfa_devices script\\nDATA_TBL_FIELDS = [\\\"SerialNumbers\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_mfa_devices\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT=False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Active NFA devices\u0027 returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        for mfa_ser_num in CONTENT:\\n            if mfa_ser_num[\\\"SerialNumber\\\"] is not None:\\n                workflow.addProperty(\\\"has_active_mfa\\\", {})\\n            if mfa_ser_num.get(\\\"is_virtual\\\", None):\\n                workflow.addProperty(\\\"is_virtual_mfa\\\", {})\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Active NFA devices\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_mfa_devices_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_10ezp90\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_01agcix\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0a4v7ma\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_10ezp90\" sourceRef=\"ServiceTask_02vzvwx\" targetRef=\"ServiceTask_0z95wxx\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1ix2tyr\"\u003e\u003cincoming\u003eSequenceFlow_0a4v7ma\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1aaggt1\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0r25rrv\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0a4v7ma\" sourceRef=\"ServiceTask_0z95wxx\" targetRef=\"ExclusiveGateway_1ix2tyr\"/\u003e\u003cserviceTask id=\"ServiceTask_1hjsbrx\" name=\"AWS IAM: Deactivate MFA Devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6c20740b-0696-4e2f-b772-54f74ef049fe\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_deactivate_mfa_devices script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027SerialNumber: \\\"arn:aws:iam::123456789123:mfa/iam_test_user\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_mfa_serial_nums\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_deactivate_mfa_devices  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_deactivate_mfa_devices\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deactivated = 0\\n    no_such_entity = 0\\n    deactivated_mfas = []\\n    no_such_entity_mfas = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deactivated += 1\\n                deactivated_mfas.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_mfas.append(grp_stat[\\\"GroupName\\\"])\\n        if deactivated_mfas:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027MFA devices\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; de-activated \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deactivated_mfas), \\\", \\\".join(str(i) for i in deactivated_mfas), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027MFA devices\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_mfas), \\\", \\\".join(str(i) for i in no_such_entity_mfas), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ncontent = workflow.properties.list_mfa_devices_results.content\\nmfa_serial_nums = []\\nfor mfa_ser_num in content:\\n    if mfa_ser_num[\\\"SerialNumber\\\"] is not None:\\n        mfa_serial_nums.append(mfa_ser_num[\\\"SerialNumber\\\"])\\ninputs.aws_iam_mfa_serial_nums = \\\",\\\".join(mfa_serial_nums)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1aaggt1\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0b6qabt\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1aaggt1\" name=\"User has activated mfa device.\" sourceRef=\"ExclusiveGateway_1ix2tyr\" targetRef=\"ServiceTask_1hjsbrx\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_active_mfa\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0r25rrv\" name=\"User doesn\u0027t have activated mfa device.\" sourceRef=\"ExclusiveGateway_1ix2tyr\" targetRef=\"ServiceTask_0w0we39\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_active_mfa\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1uufj8s\"\u003e\u003cincoming\u003eSequenceFlow_0b6qabt\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0xdhsvf\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1ipz0w2\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0b6qabt\" sourceRef=\"ServiceTask_1hjsbrx\" targetRef=\"ExclusiveGateway_1uufj8s\"/\u003e\u003cserviceTask id=\"ServiceTask_1k7neej\" name=\"AWS IAM: Delete Virtual MFA Devic...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0685a3cf-fdf3-4a68-8574-a8a4dcc112eb\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_mfa_devices script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027SerialNumber: \\\"arn:aws:iam::123456789123:mfa/iam_test_user\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_mfa_serial_nums\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_mfa_devices  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_mfa_devices\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_mfas = []\\n    no_such_entity_mfas = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_mfas.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_mfas.append(grp_stat[\\\"GroupName\\\"])\\n        if deleted_mfas:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027MFA devices\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; deleted\\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_mfas), \\\", \\\".join(str(i) for i in deleted_mfas), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027MFA devices\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_mfas), \\\", \\\".join(str(i) for i in no_such_entity_mfas), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"content = workflow.properties.list_mfa_devices_results.content\\nmfa_serial_nums = []\\nfor mfa_ser_num in content:\\n    if mfa_ser_num[\\\"SerialNumber\\\"] is not None and mfa_ser_num.get(\\\"is_virtual\\\", None):\\n        mfa_serial_nums.append(mfa_ser_num[\\\"SerialNumber\\\"])\\ninputs.aws_iam_mfa_serial_nums = \\\",\\\".join(mfa_serial_nums)\\n\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0xdhsvf\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0r5gn32\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0xdhsvf\" name=\"User mfs is a virtual mfa.\" sourceRef=\"ExclusiveGateway_1uufj8s\" targetRef=\"ServiceTask_1k7neej\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_virtual_mfa\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_1ipz0w2\" name=\"User mfa ss not a virtual mfa.\" sourceRef=\"ExclusiveGateway_1uufj8s\" targetRef=\"ServiceTask_0w0we39\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_virtual_mfa\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_0w0we39\" name=\"AWS IAM: Delete User\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"773f48cb-3a55-405e-aef9-73c7938de80f\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: { \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n          \u0027content\u0027: \u0027OK\u0027, \\n          \u0027raw\u0027: \u0027\\\"OK\\\"\u0027, \\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user\u0027}, \\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027, \\n                      \u0027execution_time_ms\u0027: 689, \u0027timestamp\u0027: \u00272020-01-15 10:27:48\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_user  script\\nDATA_TBL_FIELDS = [\\\"Status\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_user\\\"\\nWF_NAME = \\\"Delete User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nEXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        if CONTENT == \\\"OK\\\":\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: User \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was successfully deleted for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.Status = \\\"Deleted\\\"\\n            row.Tags = \\\"\\\"\\n            row.query_execution_date = EXECUTION_DATE\\n        else:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Unexpected delete status \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for delete\\\" \\\\\\n                        \\\" user operation \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, CONTENT, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0r5gn32\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0r25rrv\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1ipz0w2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_17q0k1j\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0r5gn32\" sourceRef=\"ServiceTask_1k7neej\" targetRef=\"ServiceTask_0w0we39\"/\u003e\u003csequenceFlow id=\"SequenceFlow_17q0k1j\" sourceRef=\"ServiceTask_0w0we39\" targetRef=\"EndEvent_0domjpp\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0lu4nwx\"\u003e\u003ctext\u003eList all users to\u00a0 determine if 1) user exists ,\u00a0 2) is not a default user and 3) has a login profile. Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0hx7fal\" sourceRef=\"ServiceTask_0s76zua\" targetRef=\"TextAnnotation_0lu4nwx\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0ohm0c0\"\u003e\u003ctext\u003eDelete user login profile. Update data table row for user login profile.\n\u00a0Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0t97ren\" sourceRef=\"ServiceTask_1civ9g8\" targetRef=\"TextAnnotation_0ohm0c0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0gf2um5\"\u003e\u003ctext\u003eDetermine if any access keys assigned to user.\u00a0 Update workflow result.\n\u00a0Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1c1n6mm\" sourceRef=\"ServiceTask_1izll8i\" targetRef=\"TextAnnotation_0gf2um5\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1pn6ygc\"\u003e\u003ctext\u003eDelete user access keys. Update data table row for user access keys.\n\u00a0Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1rgbbp6\" sourceRef=\"ServiceTask_15sjdh5\" targetRef=\"TextAnnotation_1pn6ygc\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1t14m3g\"\u003e\u003ctext\u003eDetermine if any policies attached to user. Update workflow result.\n\u00a0Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_082tdee\" sourceRef=\"ServiceTask_13tmpe4\" targetRef=\"TextAnnotation_1t14m3g\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_13kowcg\"\u003e\u003ctext\u003eDetach (managed) or delete (in-line) all policies for user. Update data table row for user policies.\n\u00a0Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_100352u\" sourceRef=\"ServiceTask_0whqlz7\" targetRef=\"TextAnnotation_13kowcg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1h4tvl2\"\u003e\u003ctext\u003eDetermine if\u00a0 user is a member of any groups. Update workflow result.\n\u00a0Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_17n97i0\" sourceRef=\"ServiceTask_0iyqm1d\" targetRef=\"TextAnnotation_1h4tvl2\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_148mg8e\"\u003e\u003ctext\u003eRemove user from all groups. Update data table row for user groups.\n\u00a0Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ourg5n\" sourceRef=\"ServiceTask_0iuu80s\" targetRef=\"TextAnnotation_148mg8e\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0q8gzch\"\u003e\u003ctext\u003eRemove user. Set data table row \"Status\" field to \"Deleted\".\n\u00a0Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0h5n3s5\" sourceRef=\"ServiceTask_0w0we39\" targetRef=\"TextAnnotation_0q8gzch\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0urmhbe\"\u003e\u003ctext\u003eDetermine ssh public keys for user. Update workflow result.\nUsername is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1051knh\" sourceRef=\"ServiceTask_032rb9j\" targetRef=\"TextAnnotation_0urmhbe\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1rel8ll\"\u003e\u003ctext\u003eDelete ssh public keys for user.\nUsername is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ljvg3q\" sourceRef=\"ServiceTask_1vqtsd1\" targetRef=\"TextAnnotation_1rel8ll\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_14o6f19\"\u003e\u003ctext\u003eDetermine if\u00a0 user has any service-specific credentials.\nUpdate workflow result. Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1d6ehb4\" sourceRef=\"ServiceTask_0x796wp\" targetRef=\"TextAnnotation_14o6f19\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0lhi3vt\"\u003e\u003ctext\u003eDelete service specific credentials for user.\nUsername is assigned from an artifact value. Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0aka1l0\" sourceRef=\"ServiceTask_1um41mk\" targetRef=\"TextAnnotation_0lhi3vt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0oe5fei\"\u003e\u003ctext\u003eDetermine if\u00a0 user has any signing certificates. Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1eeqo2h\" sourceRef=\"ServiceTask_182s08y\" targetRef=\"TextAnnotation_0oe5fei\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1bv3jme\"\u003e\u003ctext\u003eDelete signing certificates for user.\nUsername is assigned from an artifact value. Username is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1fauokf\" sourceRef=\"ServiceTask_02vzvwx\" targetRef=\"TextAnnotation_1bv3jme\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1y3wek6\"\u003e\u003ctext\u003eDetermine if\u00a0 user has any MFA devices and which are virtual. Update workflow result.\nUsername is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_18mudda\" sourceRef=\"ServiceTask_0z95wxx\" targetRef=\"TextAnnotation_1y3wek6\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0x4l807\"\u003e\u003ctext\u003eDe-activate virtual MFA devices for user.\nUsername is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ik0tfp\" sourceRef=\"ServiceTask_1hjsbrx\" targetRef=\"TextAnnotation_0x4l807\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1os2f99\"\u003e\u003ctext\u003eDelete virtual MFA devices for user.\nUsername is assigned from a data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0dpk1v9\" sourceRef=\"ServiceTask_1k7neej\" targetRef=\"TextAnnotation_1os2f99\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"-33\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"-38\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"-111\" y=\"263\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"-27\" y=\"218\"/\u003e\u003comgdi:waypoint x=\"-55\" y=\"263\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0s76zua\" id=\"ServiceTask_0s76zua_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"61\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1izc3u0\" id=\"SequenceFlow_1izc3u0_di\"\u003e\u003comgdi:waypoint x=\"3\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"61\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"-13\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0do5med\" id=\"ExclusiveGateway_0do5med_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"414\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"394\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1civ9g8\" id=\"ServiceTask_1civ9g8_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"515\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1fky00t\" id=\"SequenceFlow_1fky00t_di\"\u003e\u003comgdi:waypoint x=\"464\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"515\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"61\" x=\"452\" y=\"170\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1izll8i\" id=\"ServiceTask_1izll8i_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"728\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0x9sjg9\" id=\"SequenceFlow_0x9sjg9_di\"\u003e\u003comgdi:waypoint x=\"439\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"439\" y=\"112\"/\u003e\u003comgdi:waypoint x=\"778\" y=\"112\"/\u003e\u003comgdi:waypoint x=\"778\" y=\"166\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"79\" x=\"572\" y=\"91\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_06178d2\" id=\"SequenceFlow_06178d2_di\"\u003e\u003comgdi:waypoint x=\"615\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"728\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"626.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_119mcb9\" id=\"ExclusiveGateway_119mcb9_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"863\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"843\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01ws640\" id=\"SequenceFlow_01ws640_di\"\u003e\u003comgdi:waypoint x=\"828\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"863\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"800.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_15sjdh5\" id=\"ServiceTask_15sjdh5_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"947\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11hmndb\" id=\"SequenceFlow_11hmndb_di\"\u003e\u003comgdi:waypoint x=\"913\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"947\" y=\"205\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"89\" x=\"887\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_13tmpe4\" id=\"ServiceTask_13tmpe4_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"1159\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1wpyrsg\" id=\"SequenceFlow_1wpyrsg_di\"\u003e\u003comgdi:waypoint x=\"888\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"888\" y=\"115\"/\u003e\u003comgdi:waypoint x=\"1209\" y=\"115\"/\u003e\u003comgdi:waypoint x=\"1209\" y=\"162\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"70\" x=\"1014\" y=\"94\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1fzhdg0\" id=\"SequenceFlow_1fzhdg0_di\"\u003e\u003comgdi:waypoint x=\"1047\" y=\"204\"/\u003e\u003comgdi:waypoint x=\"1120\" y=\"204\"/\u003e\u003comgdi:waypoint x=\"1120\" y=\"204\"/\u003e\u003comgdi:waypoint x=\"1159\" y=\"204\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1090\" y=\"197.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_03xbdyk\" id=\"ExclusiveGateway_03xbdyk_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"1328\" y=\"177\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1308\" y=\"230\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qac2f4\" id=\"SequenceFlow_1qac2f4_di\"\u003e\u003comgdi:waypoint x=\"1259\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1285\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1285\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1328\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1255\" y=\"195.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0whqlz7\" id=\"ServiceTask_0whqlz7_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"1444\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0m4qiat\" id=\"SequenceFlow_0m4qiat_di\"\u003e\u003comgdi:waypoint x=\"1378\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1411\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1411\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1444\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"70\" x=\"1352\" y=\"228\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0iyqm1d\" id=\"ServiceTask_0iyqm1d_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"1668\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0h90voj\" id=\"SequenceFlow_0h90voj_di\"\u003e\u003comgdi:waypoint x=\"1353\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1353\" y=\"109\"/\u003e\u003comgdi:waypoint x=\"1718\" y=\"109\"/\u003e\u003comgdi:waypoint x=\"1718\" y=\"162\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"88\" x=\"1493\" y=\"88\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0qlvv4k\" id=\"SequenceFlow_0qlvv4k_di\"\u003e\u003comgdi:waypoint x=\"1544\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1668\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1561\" y=\"180.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1e1nnri\" id=\"ExclusiveGateway_1e1nnri_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"1825\" y=\"177\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1805\" y=\"230\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_03cfb0e\" id=\"SequenceFlow_03cfb0e_di\"\u003e\u003comgdi:waypoint x=\"1768\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1825\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1751.5\" y=\"180.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0iuu80s\" id=\"ServiceTask_0iuu80s_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"1946\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1doiaom\" id=\"SequenceFlow_1doiaom_di\"\u003e\u003comgdi:waypoint x=\"1875\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1910\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1910\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"1946\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"54\" x=\"1860\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1vxmza3\" id=\"SequenceFlow_1vxmza3_di\"\u003e\u003comgdi:waypoint x=\"1850\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"1850\" y=\"114\"/\u003e\u003comgdi:waypoint x=\"2197\" y=\"114\"/\u003e\u003comgdi:waypoint x=\"2197\" y=\"162\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"73\" x=\"1989\" y=\"93\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0uvp3da\" id=\"SequenceFlow_0uvp3da_di\"\u003e\u003comgdi:waypoint x=\"2046\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2096\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2096\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2147\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"2066\" y=\"195.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0domjpp\" id=\"EndEvent_0domjpp_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"4501\" y=\"184\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"4474\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1mqg0j9\" id=\"ExclusiveGateway_1mqg0j9_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"187\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"167\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1goxcss\" id=\"SequenceFlow_1goxcss_di\"\u003e\u003comgdi:waypoint x=\"212\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"212\" y=\"359\"/\u003e\u003comgdi:waypoint x=\"4519\" y=\"359\"/\u003e\u003comgdi:waypoint x=\"4519\" y=\"220\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"67\" x=\"2336\" y=\"338\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0536rkw\" id=\"SequenceFlow_0536rkw_di\"\u003e\u003comgdi:waypoint x=\"161\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"187\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"129\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_19z8tdz\" id=\"ExclusiveGateway_19z8tdz_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"294\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"319\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1yelc0d\" id=\"SequenceFlow_1yelc0d_di\"\u003e\u003comgdi:waypoint x=\"237\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"294\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"60\" x=\"236\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1gsn1ap\" id=\"SequenceFlow_1gsn1ap_di\"\u003e\u003comgdi:waypoint x=\"344\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"414\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"69\" x=\"346\" y=\"171\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0dll6hk\" id=\"SequenceFlow_0dll6hk_di\"\u003e\u003comgdi:waypoint x=\"319\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"319\" y=\"297\"/\u003e\u003comgdi:waypoint x=\"1823\" y=\"285\"/\u003e\u003comgdi:waypoint x=\"4519\" y=\"285\"/\u003e\u003comgdi:waypoint x=\"4519\" y=\"220\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"75\" x=\"3085\" y=\"265\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0lu4nwx\" id=\"TextAnnotation_0lu4nwx_di\"\u003e\u003comgdc:Bounds height=\"67\" width=\"259\" x=\"116\" y=\"30\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0hx7fal\" id=\"Association_0hx7fal_di\"\u003e\u003comgdi:waypoint x=\"149\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"215\" y=\"97\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0ohm0c0\" id=\"TextAnnotation_0ohm0c0_di\"\u003e\u003comgdc:Bounds height=\"32\" width=\"204\" x=\"463\" y=\"30\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0t97ren\" id=\"Association_0t97ren_di\"\u003e\u003comgdi:waypoint x=\"565\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"566\" y=\"62\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0gf2um5\" id=\"TextAnnotation_0gf2um5_di\"\u003e\u003comgdc:Bounds height=\"59\" width=\"187\" x=\"684\" y=\"15\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1c1n6mm\" id=\"Association_1c1n6mm_di\"\u003e\u003comgdi:waypoint x=\"778\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"778\" y=\"74\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1pn6ygc\" id=\"TextAnnotation_1pn6ygc_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"181\" x=\"906\" y=\"15\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1rgbbp6\" id=\"Association_1rgbbp6_di\"\u003e\u003comgdi:waypoint x=\"997\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"997\" y=\"75\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1t14m3g\" id=\"TextAnnotation_1t14m3g_di\"\u003e\u003comgdc:Bounds height=\"45\" width=\"252\" x=\"1103\" y=\"22\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_082tdee\" id=\"Association_082tdee_di\"\u003e\u003comgdi:waypoint x=\"1209\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"1209\" y=\"67\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_13kowcg\" id=\"TextAnnotation_13kowcg_di\"\u003e\u003comgdc:Bounds height=\"61\" width=\"216\" x=\"1386\" y=\"15\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_100352u\" id=\"Association_100352u_di\"\u003e\u003comgdi:waypoint x=\"1494\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"1494\" y=\"76\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1h4tvl2\" id=\"TextAnnotation_1h4tvl2_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"223\" x=\"1619\" y=\"16\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_17n97i0\" id=\"Association_17n97i0_di\"\u003e\u003comgdi:waypoint x=\"1718\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"1718\" y=\"76\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_148mg8e\" id=\"TextAnnotation_148mg8e_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"219\" x=\"1886\" y=\"22\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ourg5n\" id=\"Association_1ourg5n_di\"\u003e\u003comgdi:waypoint x=\"1996\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"1995\" y=\"70\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_032rb9j\" id=\"ServiceTask_032rb9j_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"2147\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1vqtsd1\" id=\"ServiceTask_1vqtsd1_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"2448\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_094k23t\" id=\"ExclusiveGateway_094k23t_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"2318\" y=\"177\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"2298\" y=\"230\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1d54zar\" id=\"SequenceFlow_1d54zar_di\"\u003e\u003comgdi:waypoint x=\"2247\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2318\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"2237.5\" y=\"180.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1c8w1el\" id=\"SequenceFlow_1c8w1el_di\"\u003e\u003comgdi:waypoint x=\"2368\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2408\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2408\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2448\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"75\" x=\"2362\" y=\"163\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0q6a3at\" id=\"SequenceFlow_0q6a3at_di\"\u003e\u003comgdi:waypoint x=\"2343\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"2343\" y=\"101\"/\u003e\u003comgdi:waypoint x=\"2707\" y=\"101\"/\u003e\u003comgdi:waypoint x=\"2707\" y=\"162\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"40\" width=\"87\" x=\"2484\" y=\"80\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0x796wp\" id=\"ServiceTask_0x796wp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"2657\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tmswh1\" id=\"SequenceFlow_1tmswh1_di\"\u003e\u003comgdi:waypoint x=\"2548\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2598\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2598\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2657\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"2568\" y=\"195.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1dcgog4\" id=\"ExclusiveGateway_1dcgog4_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"2786\" y=\"177\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"2766\" y=\"230\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0onuhu7\" id=\"SequenceFlow_0onuhu7_di\"\u003e\u003comgdi:waypoint x=\"2757\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2786\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"2726.5\" y=\"180.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1um41mk\" id=\"ServiceTask_1um41mk_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"2926\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0idkipc\" id=\"SequenceFlow_0idkipc_di\"\u003e\u003comgdi:waypoint x=\"2836\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2878\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2878\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"2926\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"40\" width=\"88\" x=\"2813\" y=\"181\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1uhivst\" id=\"SequenceFlow_1uhivst_di\"\u003e\u003comgdi:waypoint x=\"2811\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"2811\" y=\"93\"/\u003e\u003comgdi:waypoint x=\"3178\" y=\"93\"/\u003e\u003comgdi:waypoint x=\"3178\" y=\"162\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"53\" width=\"67\" x=\"2962\" y=\"72\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_182s08y\" id=\"ServiceTask_182s08y_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"3128\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1uemn5i\" id=\"SequenceFlow_1uemn5i_di\"\u003e\u003comgdi:waypoint x=\"3026\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3076\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3076\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3128\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3046\" y=\"195.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1gfuqq8\" id=\"ExclusiveGateway_1gfuqq8_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"3267\" y=\"177\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3247\" y=\"230\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1af0uxz\" id=\"SequenceFlow_1af0uxz_di\"\u003e\u003comgdi:waypoint x=\"3228\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3267\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3202.5\" y=\"180.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_02vzvwx\" id=\"ServiceTask_02vzvwx_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"3365\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1i0yldd\" id=\"SequenceFlow_1i0yldd_di\"\u003e\u003comgdi:waypoint x=\"3317\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3339\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3339\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3365\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"88\" x=\"3283\" y=\"159\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01agcix\" id=\"SequenceFlow_01agcix_di\"\u003e\u003comgdi:waypoint x=\"3292\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"3292\" y=\"113\"/\u003e\u003comgdi:waypoint x=\"3564\" y=\"113\"/\u003e\u003comgdi:waypoint x=\"3564\" y=\"162\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"40\" width=\"67\" x=\"3396\" y=\"92\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0z95wxx\" id=\"ServiceTask_0z95wxx_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"3514\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10ezp90\" id=\"SequenceFlow_10ezp90_di\"\u003e\u003comgdi:waypoint x=\"3465\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3488\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3488\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3514\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3458\" y=\"195.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1ix2tyr\" id=\"ExclusiveGateway_1ix2tyr_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"3680\" y=\"177\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3660\" y=\"230\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0a4v7ma\" id=\"SequenceFlow_0a4v7ma_di\"\u003e\u003comgdi:waypoint x=\"3614\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3637\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3637\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3680\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3607\" y=\"195.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1hjsbrx\" id=\"ServiceTask_1hjsbrx_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"3811\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1aaggt1\" id=\"SequenceFlow_1aaggt1_di\"\u003e\u003comgdi:waypoint x=\"3730\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3769\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3769\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3811\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"40\" width=\"71\" x=\"3714\" y=\"181\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0r25rrv\" id=\"SequenceFlow_0r25rrv_di\"\u003e\u003comgdi:waypoint x=\"3705\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"3705\" y=\"97\"/\u003e\u003comgdi:waypoint x=\"4387\" y=\"97\"/\u003e\u003comgdi:waypoint x=\"4387\" y=\"162\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"40\" width=\"77\" x=\"4009\" y=\"76\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1uufj8s\" id=\"ExclusiveGateway_1uufj8s_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"3970\" y=\"177\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3950\" y=\"230\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0b6qabt\" id=\"SequenceFlow_0b6qabt_di\"\u003e\u003comgdi:waypoint x=\"3911\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3942\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3942\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"3970\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3912\" y=\"195.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1k7neej\" id=\"ServiceTask_1k7neej_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"4127\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0xdhsvf\" id=\"SequenceFlow_0xdhsvf_di\"\u003e\u003comgdi:waypoint x=\"4020\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"4072\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"4072\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"4127\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"70\" x=\"4011\" y=\"181\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ipz0w2\" id=\"SequenceFlow_1ipz0w2_di\"\u003e\u003comgdi:waypoint x=\"3995\" y=\"177\"/\u003e\u003comgdi:waypoint x=\"3995\" y=\"118\"/\u003e\u003comgdi:waypoint x=\"4364\" y=\"118\"/\u003e\u003comgdi:waypoint x=\"4364\" y=\"162\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"89\" x=\"4136\" y=\"97\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0w0we39\" id=\"ServiceTask_0w0we39_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"4337\" y=\"162\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0r5gn32\" id=\"SequenceFlow_0r5gn32_di\"\u003e\u003comgdi:waypoint x=\"4227\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"4337\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"4237\" y=\"180.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_17q0k1j\" id=\"SequenceFlow_17q0k1j_di\"\u003e\u003comgdi:waypoint x=\"4437\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"4473\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"4473\" y=\"202\"/\u003e\u003comgdi:waypoint x=\"4501\" y=\"202\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"4443\" y=\"195.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0q8gzch\" id=\"TextAnnotation_0q8gzch_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"166\" x=\"4392\" y=\"6\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0h5n3s5\" id=\"Association_0h5n3s5_di\"\u003e\u003comgdi:waypoint x=\"4409\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"4453\" y=\"86\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0urmhbe\" id=\"TextAnnotation_0urmhbe_di\"\u003e\u003comgdc:Bounds height=\"61\" width=\"179\" x=\"2107\" y=\"15\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1051knh\" id=\"Association_1051knh_di\"\u003e\u003comgdi:waypoint x=\"2197\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"2197\" y=\"76\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1rel8ll\" id=\"TextAnnotation_1rel8ll_di\"\u003e\u003comgdc:Bounds height=\"44\" width=\"194\" x=\"2401\" y=\"24\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ljvg3q\" id=\"Association_1ljvg3q_di\"\u003e\u003comgdi:waypoint x=\"2498\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"2498\" y=\"68\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_14o6f19\" id=\"TextAnnotation_14o6f19_di\"\u003e\u003comgdc:Bounds height=\"69\" width=\"175\" x=\"2619\" y=\"11\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1d6ehb4\" id=\"Association_1d6ehb4_di\"\u003e\u003comgdi:waypoint x=\"2707\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"2707\" y=\"80\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0lhi3vt\" id=\"TextAnnotation_0lhi3vt_di\"\u003e\u003comgdc:Bounds height=\"63\" width=\"177\" x=\"2887\" y=\"-5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0aka1l0\" id=\"Association_0aka1l0_di\"\u003e\u003comgdi:waypoint x=\"2976\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"2976\" y=\"58\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0oe5fei\" id=\"TextAnnotation_0oe5fei_di\"\u003e\u003comgdc:Bounds height=\"75\" width=\"160\" x=\"3098\" y=\"-1\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1eeqo2h\" id=\"Association_1eeqo2h_di\"\u003e\u003comgdi:waypoint x=\"3178\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"3179\" y=\"74\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1bv3jme\" id=\"TextAnnotation_1bv3jme_di\"\u003e\u003comgdc:Bounds height=\"70\" width=\"148\" x=\"3341\" y=\"11\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1fauokf\" id=\"Association_1fauokf_di\"\u003e\u003comgdi:waypoint x=\"3415\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"3416\" y=\"81\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1y3wek6\" id=\"TextAnnotation_1y3wek6_di\"\u003e\u003comgdc:Bounds height=\"64\" width=\"175\" x=\"3523\" y=\"14\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_18mudda\" id=\"Association_18mudda_di\"\u003e\u003comgdi:waypoint x=\"3576\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"3601\" y=\"78\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0x4l807\" id=\"TextAnnotation_0x4l807_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"183\" x=\"3769\" y=\"20\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ik0tfp\" id=\"Association_0ik0tfp_di\"\u003e\u003comgdi:waypoint x=\"3861\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"3861\" y=\"72\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1os2f99\" id=\"TextAnnotation_1os2f99_di\"\u003e\u003comgdc:Bounds height=\"42\" width=\"190\" x=\"4082\" y=\"25\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0dpk1v9\" id=\"Association_0dpk1v9_di\"\u003e\u003comgdi:waypoint x=\"4177\" y=\"162\"/\u003e\u003comgdi:waypoint x=\"4177\" y=\"67\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 23,
      "description": "Delete the selected IAM user. The User is assigned from a field in the selected data table row. The data table row will be refreshed will updated values for the selected user.\n\nNote: Unlike the AWS Management Console, when you delete a user programmatically, you must delete the items attached to the user or the deletion fails. Before attempting to delete a user, the following items if associated with the user will be removed, de-activated or deleted.:\n\n    Password ( DeleteLoginProfile )\n    Access keys ( DeleteAccessKey )\n    Inline policies ( DeleteUserPolicy )\n    Attached managed policies ( DetachUserPolicy ) \n    Group memberships ( RemoveUserFromGroup )\n    Signing certificate ( DeleteSigningCertificate )\n    SSH public key ( DeleteSSHPublicKey )\n    Git credentials ( DeleteServiceSpecificCredential )\n    Multi-factor authentication (MFA) device ( DeactivateMFADevice , DeleteVirtualMFADevice )",
      "export_key": "wf_aws_iam_delete_user",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719810112354,
      "name": "Example: AWS IAM: Delete User",
      "object_type": "aws_iam_users",
      "programmatic_name": "wf_aws_iam_delete_user",
      "tags": [],
      "uuid": "0a5e656c-cb36-4d05-a322-4cd901da67ec",
      "workflow_id": 9
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "wf_aws_iam_change_profile_password",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_change_profile_password\" isExecutable=\"true\" name=\"Example: AWS IAM: Change Profile Password\"\u003e\u003cdocumentation\u003eChange the password for an IAM user. The User is assigned from a field in the selected data table row.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0zbr81g\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0da0mtx\" name=\"AWS IAM: Update Login Profile\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"5b37eab0-39a9-4ecf-bfd9-4ec53e30f233\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_update_login_profile script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n         \u0027content\u0027: \u0027OK\u0027, \u0027raw\u0027: \u0027\\\"OK\\\"\u0027, \\n                     \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user_1\u0027, \\n                                \u0027aws_iam_password\u0027: \u0027***\u0027, \u0027aws_iam_password_reset_required\u0027: False}, \\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027, \\n                     \u0027execution_time_ms\u0027: 4300, \u0027timestamp\u0027: \u00272020-03-13 17:35:48\u0027\\n                    }\\n}\\n\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_update_login_profile  script\\nFN_NAME = \\\"fn_aws_iam_update_login_profile\\\"\\nWF_NAME = \\\"Change Profile Password\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        if CONTENT == \\\"OK\\\":\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Login profile password was updated for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        elif CONTENT == \\\"PasswordPolicyViolation\\\":\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Login profile password got policy violation ERROR updating user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        elif CONTENT == \\\"ValidationError\\\":\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Login profile password got validation ERROR updating user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        else:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Login profile password got unexpected ERROR updating user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\n# Test password to see it complies with basic password policy.\\nerr_msg_validation = \\\"The new password needs be minimum 8 characters in length and have at least 1 uppercase and 1 lowercase character.\\\"\\nerr_msg_ascii = \\\"The new password must contain only printable ASCII characters.\\\"\\nif len(rule.properties.aws_iam_password) \u0026lt; 8:\\n    raise ValueError(err_msg_validation)\\nif not any(c.isupper() for c in rule.properties.aws_iam_password):\\n    raise ValueError(err_msg_validation)\\nif not any(c.islower() for c in rule.properties.aws_iam_password):\\n    raise ValueError(err_msg_validation)\\ntry:\\n    rule.properties.aws_iam_password.decode(\u0027ascii\u0027)\\nexcept:\\n    raise ValueError(err_msg_ascii)\\ninputs.aws_iam_password = rule.properties.aws_iam_password\\ninputs.aws_iam_password_reset_required = False\\nif rule.properties.aws_iam_password_reset_required.lower() == \\\"yes\\\":\\n    inputs.aws_iam_password_reset_required = True\\n\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0zbr81g\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1e39lhn\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0zbr81g\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0da0mtx\"/\u003e\u003cendEvent id=\"EndEvent_0hb3ows\"\u003e\u003cincoming\u003eSequenceFlow_1e39lhn\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1e39lhn\" sourceRef=\"ServiceTask_0da0mtx\" targetRef=\"EndEvent_0hb3ows\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kk3rwe\"\u003e\u003ctext\u003eChange profile password for user. Username assigned from data table row. New password name assigned from activity field.\n\u00a0Password reset required boolean assigned from activity field.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_02xao30\" sourceRef=\"ServiceTask_0da0mtx\" targetRef=\"TextAnnotation_1kk3rwe\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0da0mtx\" id=\"ServiceTask_0da0mtx_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"237\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0zbr81g\" id=\"SequenceFlow_0zbr81g_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"237\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"217.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0hb3ows\" id=\"EndEvent_0hb3ows_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"377\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"395\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e39lhn\" id=\"SequenceFlow_1e39lhn_di\"\u003e\u003comgdi:waypoint x=\"337\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"357\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"357\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"377\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"372\" y=\"199.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kk3rwe\" id=\"TextAnnotation_1kk3rwe_di\"\u003e\u003comgdc:Bounds height=\"94\" width=\"256\" x=\"159\" y=\"30\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_02xao30\" id=\"Association_02xao30_di\"\u003e\u003comgdi:waypoint x=\"287\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"288\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Change the password for an IAM user. The User is assigned from a field in the selected data table row.",
      "export_key": "wf_aws_iam_change_profile_password",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719372005897,
      "name": "Example: AWS IAM: Change Profile Password",
      "object_type": "aws_iam_users",
      "programmatic_name": "wf_aws_iam_change_profile_password",
      "tags": [],
      "uuid": "95679dbf-1999-4c42-aeb8-a2934ecd6fa8",
      "workflow_id": 7
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "wf_aws_iam_deactivate_access_key",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_deactivate_access_key\" isExecutable=\"true\" name=\"Example: AWS IAM: Deactivate Access Key\"\u003e\u003cdocumentation\u003eDeactivate an access key id for a user. The user and access key ids  are assigned from fields in the selected data table row. The target status is set to \"Inactive\". The data table row will be refreshed with updated access key \"Status\" for the selected access key.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0m2uut8\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0q1j3fd\" name=\"AWS IAM: Update Access Key\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"045fe24b-3eb8-4a2a-885d-62f36e2d4b10\"\u003e{\"inputs\":{\"95e86085-40e3-4dbf-a989-9c2deaa3c1e4\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"7456ec52-5061-4b31-8137-092c9ea29d1a\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_update_access_key script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\u0027inputs\u0027: {u\u0027aws_iam_user_name\u0027: u\u0027iam_test_user\u0027, u\u0027aws_iam_access_key_id\u0027: u\u0027ABCDEFG\u0027, u\u0027aws_iam_status\u0027: u\u0027Inactive\u0027},\\n         \u0027metrics\u0027: {\u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027timestamp\u0027: \u00272020-02-19 12:53:48\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                     \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027version\u0027: \u00271.0\u0027, \u0027execution_time_ms\u0027: 3023},\\n         \u0027success\u0027: True,\\n         \u0027content\u0027: \u0027OK\u0027,\\n         \u0027raw\u0027: \u0027\\\"OK\\\"\u0027,\\n         \u0027reason\u0027: None,\\n         \u0027version\u0027: \u00271.0\u0027\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_access_keys  script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_update_access_key\\\"\\nWF_NAME = \\\"Deactivate Access Key\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        if CONTENT == \\\"OK\\\":\\n            note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The Access Key Id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was deactivated \\\" \\\\\\n                        u\\\"for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_access_key_id\\\"], INPUTS[\\\"aws_iam_user_name\\\"],  FN_NAME)\\n            row.Status = \\\"Inactive\\\"\\n        elif CONTENT == u\\\"NoSuchEntity\\\":\\n            note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The Access Key Id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Not found \\\" \\\\\\n                        u\\\"for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_access_key_id\\\"], INPUTS[\\\"aws_iam_user_name\\\"],  FN_NAME)\\n            row.Status = \\\"NoSuchEntity\\\"\\n    else:\\n        note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were no results returned for \\\" \\\\\\n                     u\\\"access key id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; access key  Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_access_keys\\\"], FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_access_key_id = row.AccessKeyId\\ninputs.aws_iam_user_name = row.UserName\\ninputs.aws_iam_status = \\\"Inactive\\\"\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0m2uut8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0anuzaa\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0m2uut8\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0q1j3fd\"/\u003e\u003cendEvent id=\"EndEvent_1qb13sw\"\u003e\u003cincoming\u003eSequenceFlow_0anuzaa\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0anuzaa\" sourceRef=\"ServiceTask_0q1j3fd\" targetRef=\"EndEvent_1qb13sw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0944q03\"\u003e\u003ctext\u003eDeactivate an access key of a user. Username and access key id are assigned from data table rows. Target status is set to \"Inactive\". Data table row is updated for access key status.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1azpril\" sourceRef=\"ServiceTask_0q1j3fd\" targetRef=\"TextAnnotation_0944q03\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0q1j3fd\" id=\"ServiceTask_0q1j3fd_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"243\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0m2uut8\" id=\"SequenceFlow_0m2uut8_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"243\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"220.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1qb13sw\" id=\"EndEvent_1qb13sw_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"383\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"401\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0anuzaa\" id=\"SequenceFlow_0anuzaa_di\"\u003e\u003comgdi:waypoint x=\"343\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"383\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"363\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0944q03\" id=\"TextAnnotation_0944q03_di\"\u003e\u003comgdc:Bounds height=\"112\" width=\"180\" x=\"203\" y=\"3\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1azpril\" id=\"Association_1azpril_di\"\u003e\u003comgdi:waypoint x=\"293\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"293\" y=\"115\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Deactivate an access key id for a user. The user and access key ids  are assigned from fields in the selected data table row. The target status is set to \"Inactive\". The data table row will be refreshed with updated access key \"Status\" for the selected access key.",
      "export_key": "wf_aws_iam_deactivate_access_key",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719372059543,
      "name": "Example: AWS IAM: Deactivate Access Key",
      "object_type": "aws_iam_access_keys",
      "programmatic_name": "wf_aws_iam_deactivate_access_key",
      "tags": [],
      "uuid": "3b470629-556d-4cc7-9ccc-c9ff3ee4b5b0",
      "workflow_id": 8
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "wf_aws_iam_get_user",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_get_user\" isExecutable=\"true\" name=\"Example: AWS IAM: Get User\"\u003e\u003cdocumentation\u003eGet an IAM users information. The User is assigned from a field in the selected data table row. A new row will be created in the data table \u0027AWS IAM users\u0027 for the user if it exists for the AWS IAM account.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_13yvmpq\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0cmuuzc\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n            \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n            \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User\u0027, \u0027CreateDate\u0027: \u00272019-11-05 15:54:43\u0027},\\n                        {\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User_2\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User_2\u0027,\\n                         \u0027CreateDate\u0027: \u00272019-10-31 16:23:07\u0027, \u0027PasswordLastUsed\u0027: \u00272019-11-12 10:55:42\u0027}\\n                       ],\\n            \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User\\\", \\\"CreateDate\\\": \\\"2019-11-05 15:54:43\\\"}, {\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User_2\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User_2\\\", \\\"CreateDate\\\": \\\"2019-10-31 16:23:07\\\"}]\u0027,\\n            \u0027inputs\u0027: {},\\n            \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                        \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 7951,\\n                        \u0027timestamp\u0027: \u00272019-11-14 13:48:30\u0027\\n                       }\\n}\\n\\n\\\"\\\"\\\"\\nimport re\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_users script\\nDATA_TBL_FIELDS = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"Arn\\\", \\\"DefaultUser\\\", \\\"CreateDate\\\", \\\"LoginProfileExists\\\",\\n                   \\\"Tags\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"Get User\\\"\\n# Processing\\nINPUTS = results.inputs\\nCONTENT = results.content\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        if isinstance(CONTENT, dict) and CONTENT.get(\\\"Status\\\") == \\\"NoSuchEntity\\\":\\n            note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; does not exist \\\" \\\\\\n                         \\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        elif isinstance(CONTENT, dict) and CONTENT.get(\\\"Status\\\") == \\\"ValidationError\\\":\\n            note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The username \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; is invalid \\\" \\\\\\n                         \\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        elif len(CONTENT) == 1:\\n            note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was found for Resilient \\\" \\\\\\n                        u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            note_text += \\\"\u0026lt;br\u0026gt;Adding new row to data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\u0026lt;/br\u0026gt;\\\"\\\\\\n                .format(\\\"AWS IAM Users\\\", INPUTS[\\\"aws_iam_user_name\\\"])\\n            workflow.addProperty(\\\"user_exists\\\", {})\\n        else:\\n            note_text = u\\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Too many results \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned for user \\\" \\\\\\n                        \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned for Resilient \\\" \\\\\\n                     \\\"function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_users_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_13yvmpq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0po4uxe\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_13yvmpq\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0cmuuzc\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0usw774\"\u003e\u003cincoming\u003eSequenceFlow_0po4uxe\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0q9gutq\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1iz6w0q\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0po4uxe\" sourceRef=\"ServiceTask_0cmuuzc\" targetRef=\"ExclusiveGateway_0usw774\"/\u003e\u003cserviceTask id=\"ServiceTask_0yvxpb1\" name=\"AWS IAM: List User Policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"64a30bb5-b539-45d6-b6e5-55674539d411\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_policies script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyName\u0027: \u0027test_pol\u0027},\\n                      {\u0027PolicyName\u0027: \u0027test_pol_2\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::123456789123:policy/test_pol_2\u0027},\\n                      {\u0027PolicyName\u0027: \u0027AmazonRoute53ReadOnlyAccess\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\u0027}],\\n          \u0027raw\u0027: \u0027[{\\\"PolicyName\\\": \\\"test_pol\\\"}, {\\\"PolicyName\\\": \\\"test_pol_2\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::123456789123:policy/test_pol_2\\\"},\\n                    {\\\"PolicyName\\\": \\\"AmazonRoute53ReadOnlyAccess\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 87423, \u0027timestamp\u0027: \u00272019-11-21 11:55:29\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_policies script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_policies\\\"\\nWF_NAME = \\\"Get User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; policies found for user \\\" \\\\\\n                    u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; policies found for \\\" \\\\\\n                    u\\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_user_policies_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0q9gutq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10y1yjd\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0q9gutq\" name=\"User exists.\" sourceRef=\"ExclusiveGateway_0usw774\" targetRef=\"ServiceTask_0yvxpb1\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_0nxglzg\" name=\"AWS IAM: List User Access Key IDs\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"278f8cba-ff48-4495-93b0-27349c3fec8b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027,\\n                       \u0027Status\u0027: \u0027Active\u0027, \u0027CreateDate\u0027: \u00272019-11-12 11:09:38\u0027\\n                       }],\\n          \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_User\\\", \\\"AccessKeyId\\\": \\\"ABCDEFG\\\",\\n                  \\\"Status\\\": \\\"Active\\\", \\\"CreateDate\\\": \\\"2019-11-12 11:09:38\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 5365, \u0027timestamp\u0027: \u00272019-11-21 10:41:22\u0027}}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_access_keys script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_access_keys\\\"\\nWF_NAME = \\\"Get User\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    newrow = workflow.properties.newrow\\n    if CONTENT:\\n        note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; access key ids found for user \\\" \\\\\\n                    u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; access key id found for \\\" \\\\\\n                    u\\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_user_access_key_ids_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_10y1yjd\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0rsf28y\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_10y1yjd\" sourceRef=\"ServiceTask_0yvxpb1\" targetRef=\"ServiceTask_0nxglzg\"/\u003e\u003cserviceTask id=\"ServiceTask_0ehxfue\" name=\"AWS IAM: List User Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8b67eb7-166c-4f5c-8291-1d0e3bd14e68\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027GroupName\u0027: \u0027system-admins\u0027, \u0027GroupId\u0027: \u0027ABCDEFG\u0027,\\n                      \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:group/system-admins\u0027, \u0027CreateDate\u0027: \u00272017-05-29 20:37:53\u0027}],\\n                      \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"GroupName\\\": \\\"system-admins\\\", \\\"GroupId\\\": \\\"ABCDEFG\\\",\\n                      \\\"Arn\\\": \\\"arn:aws:iam::123456789123:group/system-admins\\\", \\\"CreateDate\\\": \\\"2017-05-29 20:37:53\\\"\\n                      }\\n                    ]\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                     \u0027execution_time_ms\u0027: 1070, \u0027timestamp\u0027: \u00272019-11-18 10:19:19\u0027\\n                     }\\n}\\nUse this step to get user groups and also to process previous steps in workflow for dtat-table addition.\\n\\n\\\"\\\"\\\"\\n#  Globals\\nimport re\\n# List of fields in datatable fn_aws_iam_list_user_groups script\\nDATA_TBL_FIELDS_USER = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"Arn\\\", \\\"DefaultUser\\\", \\\"CreateDate\\\", \\\"LoginProfileExists\\\",\\n                        \\\"Tags\\\"]\\nDATA_TBL_FIELDS_GROUPS = [\\\"Groups\\\"]\\nDATA_TBL_FIELDS_POLICIES = [\\\"Policies\\\"]\\n\\nFN_NAME = \\\"fn_aws_iam_list_user_groups\\\"\\nWF_NAME = \\\"Get User\\\"\\n# Processing\\nUSER_CONTENT = workflow.properties.list_users_results.content\\nPOLICY_CONTENT = workflow.properties.list_user_policies_results.content\\nACCESS_KEY_ID_CONTENT = workflow.properties.list_user_access_key_ids_result.content\\nGROUP_CONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef check_add_quotes(tag_name):\\n    # Using regex\\n    # If spaces in tag name add quotes\\n    if re.search(r\\\"\\\\s\\\", tag_name):\\n        return \\\"\u0027\\\"+tag_name+\\\"\u0027\\\"\\n    else:\\n        return tag_name\\n\\ndef process_access_key_ids(access_key_id_list, row):\\n    access_key_ids = []\\n    for ak_id in access_key_id_list:\\n        if ak_id[\\\"AccessKeyId\\\"] is not None:\\n            access_key_ids.append(ak_id[\\\"AccessKeyId\\\"])\\n    row.AccessKeyIds = \u0027,\u0027.join(access_key_ids)\\n\\ndef process_policies(policy_list, row):\\n    policies = []\\n    for pol in policy_list:\\n        if pol[\\\"PolicyName\\\"] is not None:\\n            policies.append(pol[\\\"PolicyName\\\"])\\n    row.Policies = \u0027,\u0027.join(policies)\\n\\ndef process_groups(group_list, row):\\n    groups = []\\n    for grp in group_list:\\n        if grp[\\\"GroupName\\\"] is not None:\\n            groups.append(grp[\\\"GroupName\\\"])\\n    row.Groups = \\\",\\\".join(groups)\\n\\n\\ndef process_tags(tag_list, row):\\n    tags = []\\n    for tag in tag_list:\\n        if tag[\\\"Key\\\"] is not None:\\n            tags.append(tag[\\\"Key\\\"])\\n    row.Tags = \u0027,\u0027.join(check_add_quotes(t) for t in tags)\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    if USER_CONTENT:\\n        u = USER_CONTENT.pop()\\n        newrow = incident.addRow(\\\"aws_iam_users\\\")\\n        newrow.query_execution_date = QUERY_EXECUTION_DATE\\n        for f in DATA_TBL_FIELDS_USER:\\n            if u[f] is not None:\\n                if isinstance(u[f], unicode) or isinstance(u[f], int) \\\\\\n                        or isinstance(u[f], long) or len(u[f]) == 0:\\n                    if f == \\\"DefaultUser\\\" and not u[f]:\\n                        pass\\n                    else:\\n                        newrow[f] = u[f]\\n                else:\\n                    if f == \\\"Tags\\\" and len(u[f]) \u0026gt; 0:\\n                        process_tags(u[f], newrow)\\n                    else:\\n                        newrow[f] = \u0027,\u0027.join(u[f])\\n        if POLICY_CONTENT:\\n            process_policies(POLICY_CONTENT, newrow)\\n        if ACCESS_KEY_ID_CONTENT:\\n            process_access_key_ids(ACCESS_KEY_ID_CONTENT, newrow)\\n        if GROUP_CONTENT:\\n            note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; groups found for user \\\" \\\\\\n                        u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(GROUP_CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            process_groups(GROUP_CONTENT, newrow)\\n        else:\\n            note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; group found for \\\" \\\\\\n                        u\\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n    \\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0rsf28y\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1wz90oc\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0rsf28y\" sourceRef=\"ServiceTask_0nxglzg\" targetRef=\"ServiceTask_0ehxfue\"/\u003e\u003cendEvent id=\"EndEvent_0eydfmd\"\u003e\u003cincoming\u003eSequenceFlow_1wz90oc\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1iz6w0q\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1wz90oc\" sourceRef=\"ServiceTask_0ehxfue\" targetRef=\"EndEvent_0eydfmd\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1iz6w0q\" name=\"User does not exist.\" sourceRef=\"ExclusiveGateway_0usw774\" targetRef=\"EndEvent_0eydfmd\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1o5b37d\"\u003e\u003ctext\u003eList all users to\u00a0 determine if user exists. Username assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0y4nujf\" sourceRef=\"ServiceTask_0cmuuzc\" targetRef=\"TextAnnotation_1o5b37d\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_05mnv7z\"\u003e\u003ctext\u003eGet policy list for user, add to workflow result.\n\u00a0Username assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1n1db7c\" sourceRef=\"ServiceTask_0yvxpb1\" targetRef=\"TextAnnotation_05mnv7z\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0lyr0gz\"\u003e\u003ctext\u003eGet access key list for user, add to workflow result.\n\u00a0Username\u00a0 assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_115i84p\" sourceRef=\"ServiceTask_0nxglzg\" targetRef=\"TextAnnotation_0lyr0gz\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0xxm26j\"\u003e\u003ctext\u003eGet group list for user. Add new row to data table\u00a0 \"AWS IAM Users\" with all workflow results.\n\u00a0Username assigned\u00a0 from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1a5y5pi\" sourceRef=\"ServiceTask_0ehxfue\" targetRef=\"TextAnnotation_0xxm26j\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0cmuuzc\" id=\"ServiceTask_0cmuuzc_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"238\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13yvmpq\" id=\"SequenceFlow_13yvmpq_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"238\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"218\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0usw774\" id=\"ExclusiveGateway_0usw774_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"387\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"412\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0po4uxe\" id=\"SequenceFlow_0po4uxe_di\"\u003e\u003comgdi:waypoint x=\"338\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"387\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"362.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0yvxpb1\" id=\"ServiceTask_0yvxpb1_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"492\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0q9gutq\" id=\"SequenceFlow_0q9gutq_di\"\u003e\u003comgdi:waypoint x=\"437\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"492\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"60\" x=\"435\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0nxglzg\" id=\"ServiceTask_0nxglzg_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"703\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10y1yjd\" id=\"SequenceFlow_10y1yjd_di\"\u003e\u003comgdi:waypoint x=\"592\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"703\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"647.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0ehxfue\" id=\"ServiceTask_0ehxfue_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"887\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0rsf28y\" id=\"SequenceFlow_0rsf28y_di\"\u003e\u003comgdi:waypoint x=\"803\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"887\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"845\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0eydfmd\" id=\"EndEvent_0eydfmd_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1072\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"1090\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1wz90oc\" id=\"SequenceFlow_1wz90oc_di\"\u003e\u003comgdi:waypoint x=\"987\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1072\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"1029.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1iz6w0q\" id=\"SequenceFlow_1iz6w0q_di\"\u003e\u003comgdi:waypoint x=\"412\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"412\" y=\"22\"/\u003e\u003comgdi:waypoint x=\"1090\" y=\"22\"/\u003e\u003comgdi:waypoint x=\"1090\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"74\" x=\"715\" y=\"1\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1o5b37d\" id=\"TextAnnotation_1o5b37d_di\"\u003e\u003comgdc:Bounds height=\"77\" width=\"156\" x=\"210\" y=\"17\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0y4nujf\" id=\"Association_0y4nujf_di\"\u003e\u003comgdi:waypoint x=\"288\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"288\" y=\"94\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_05mnv7z\" id=\"TextAnnotation_05mnv7z_di\"\u003e\u003comgdc:Bounds height=\"65\" width=\"158\" x=\"463\" y=\"56\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1n1db7c\" id=\"Association_1n1db7c_di\"\u003e\u003comgdi:waypoint x=\"542\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"542\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0lyr0gz\" id=\"TextAnnotation_0lyr0gz_di\"\u003e\u003comgdc:Bounds height=\"82\" width=\"153\" x=\"685\" y=\"48\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_115i84p\" id=\"Association_115i84p_di\"\u003e\u003comgdi:waypoint x=\"756\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"759\" y=\"130\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0xxm26j\" id=\"TextAnnotation_0xxm26j_di\"\u003e\u003comgdc:Bounds height=\"78\" width=\"153\" x=\"860\" y=\"50\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1a5y5pi\" id=\"Association_1a5y5pi_di\"\u003e\u003comgdi:waypoint x=\"937\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"937\" y=\"128\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "description": "Get an IAM users information. The User is assigned from a field in the selected data table row. A new row will be created in the data table \u0027AWS IAM users\u0027 for the user if it exists for the AWS IAM account.",
      "export_key": "wf_aws_iam_get_user",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719810778868,
      "name": "Example: AWS IAM: Get User",
      "object_type": "aws_iam_access_keys",
      "programmatic_name": "wf_aws_iam_get_user",
      "tags": [],
      "uuid": "0a17de5b-773a-4d9f-825d-42995d2d6038",
      "workflow_id": 12
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "wf_aws_iam_attach_user_policy",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_attach_user_policy\" isExecutable=\"true\" name=\"Example: AWS IAM: Attach User Policy\"\u003e\u003cdocumentation\u003eAttach a managed policy to an IAM user. The user is assigned from a field in the selected data table row. A policy name is assigned from an activity field drop-down list. The data table row will be refreshed with updated policy values for the selected user.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_15q5g12\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0n56nhl\" name=\"AWS IAM: Attach User policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"23f07e6d-8bfd-4762-ac22-fab95a7a2ec3\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_attach_user_policies script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll\u0027, \u0027Status\u0027: \u0027OK\u0027},\\n                      {\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027PolicyArn\u0027: \\\"arn:aws:iam::aws:policy/AWSDenyAll\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_arns\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User_1\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_attach_user_policies  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_attach_user_policies\\\"\\nWF_NAME = \\\"Attach User Policy\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    added = 0\\n    no_such_entity = 0\\n    added_policies = []\\n    no_such_entity_policies = []\\n    if CONTENT:\\n        for pol_stat in CONTENT:\\n            if pol_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                added += 1\\n                added_policies.append(pol_stat[\\\"PolicyName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_policies.append(pol_stat[\\\"PolicyName\\\"])\\n        if added_policies:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The Policy \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was attached to user \\\" \\\\\\n                        \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, \\\", \\\".join(str(i) for i in added_policies), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            note_text += \\\"\u0026lt;br\u0026gt;Refreshing data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; row for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with updated policy data.\\\"\\\\\\n                .format(\\\"AWS IAM Users\\\", INPUTS[\\\"aws_iam_user_name\\\"])\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Policies \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_policies), \\\", \\\".join(str(i) for i in no_such_entity_policies), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ninputs.aws_iam_policy_names = rule.properties.aws_iam_policy_name\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_15q5g12\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1m2sevz\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_15q5g12\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0n56nhl\"/\u003e\u003cserviceTask id=\"ServiceTask_144xxvp\" name=\"AWS IAM: List User Policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"64a30bb5-b539-45d6-b6e5-55674539d411\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_policies script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyName\u0027: \u0027test_pol\u0027},\\n                      {\u0027PolicyName\u0027: \u0027test_pol_2\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::123456789123:policy/test_pol_2\u0027},\\n                      {\u0027PolicyName\u0027: \u0027AmazonRoute53ReadOnlyAccess\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\u0027}],\\n          \u0027raw\u0027: \u0027[{\\\"PolicyName\\\": \\\"test_pol\\\"}, {\\\"PolicyName\\\": \\\"test_pol_2\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::123456789123:policy/test_pol_2\\\"},\\n                    {\\\"PolicyName\\\": \\\"AmazonRoute53ReadOnlyAccess\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 87423, \u0027timestamp\u0027: \u00272019-11-21 11:55:29\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_list_user_policies script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_policies\\\"\\nWF_NAME = \\\"Example: AWS IAM: Attach User Policy\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        policy_names = []\\n        for pol in CONTENT:\\n            if pol[\\\"PolicyName\\\"] is not None:\\n                policy_names.append(pol[\\\"PolicyName\\\"])\\n        row.Policies = \\\",\\\".join(policy_names)\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; attached Policy names found for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        row.Policies = \\\"\\\"\\n    if note_text:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1m2sevz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0uind2d\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1m2sevz\" sourceRef=\"ServiceTask_0n56nhl\" targetRef=\"ServiceTask_144xxvp\"/\u003e\u003cendEvent id=\"EndEvent_1y0k3as\"\u003e\u003cincoming\u003eSequenceFlow_0uind2d\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0uind2d\" sourceRef=\"ServiceTask_144xxvp\" targetRef=\"EndEvent_1y0k3as\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_06v91ix\"\u003e\u003ctext\u003eAttach policy to a user. Username assigned from data table row. Policy name assigned from activity field drop-down.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1uvvvjg\" sourceRef=\"ServiceTask_0n56nhl\" targetRef=\"TextAnnotation_06v91ix\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0t386xu\"\u003e\u003ctext\u003eGet updated policy list for user\u00a0 and update data table.\n\u00a0Username assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_11fa0cv\" sourceRef=\"ServiceTask_144xxvp\" targetRef=\"TextAnnotation_0t386xu\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0n56nhl\" id=\"ServiceTask_0n56nhl_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"229\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_15q5g12\" id=\"SequenceFlow_15q5g12_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"229\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"213.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_144xxvp\" id=\"ServiceTask_144xxvp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"450\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1m2sevz\" id=\"SequenceFlow_1m2sevz_di\"\u003e\u003comgdi:waypoint x=\"329\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"450\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"344.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1y0k3as\" id=\"EndEvent_1y0k3as_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"615\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"588\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0uind2d\" id=\"SequenceFlow_0uind2d_di\"\u003e\u003comgdi:waypoint x=\"550\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"615\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"537.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_06v91ix\" id=\"TextAnnotation_06v91ix_di\"\u003e\u003comgdc:Bounds height=\"70\" width=\"177\" x=\"190\" y=\"50\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1uvvvjg\" id=\"Association_1uvvvjg_di\"\u003e\u003comgdi:waypoint x=\"279\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"279\" y=\"120\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0t386xu\" id=\"TextAnnotation_0t386xu_di\"\u003e\u003comgdc:Bounds height=\"65\" width=\"183\" x=\"408\" y=\"52\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_11fa0cv\" id=\"Association_11fa0cv_di\"\u003e\u003comgdi:waypoint x=\"500\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"500\" y=\"117\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "description": "Attach a managed policy to an IAM user. The user is assigned from a field in the selected data table row. A policy name is assigned from an activity field drop-down list. The data table row will be refreshed with updated policy values for the selected user.",
      "export_key": "wf_aws_iam_attach_user_policy",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719372020451,
      "name": "Example: AWS IAM: Attach User Policy",
      "object_type": "aws_iam_users",
      "programmatic_name": "wf_aws_iam_attach_user_policy",
      "tags": [],
      "uuid": "201a69ad-b2a9-4193-814f-4ab4f1e7de6d",
      "workflow_id": 17
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "wf_aws_iam_delete_login_profile",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_delete_login_profile\" isExecutable=\"true\" name=\"Example: AWS IAM: Delete Login Profile\"\u003e\u003cdocumentation\u003eDelete the password for an IAM user, which terminates the user\u0027s ability to access AWS services through the AWS Management Console. The User is assigned from a field in the selected data table row. The data table row will be refreshed will updated values for the selected user.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1km05if\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0tn7e22\" name=\"AWS IAM: Delete Login Profile\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"22d5a7a2-9e89-4011-b53d-604a4aeaad2e\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_login_profile script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: \u0027NoSuchEntity\u0027, \u0027raw\u0027: \u0027\\\"NoSuchEntity\\\"\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                     \u0027host\u0027: \u0027myhost.ie.ibm.com\u0027, \u0027execution_time_ms\u0027: 9170, \u0027timestamp\u0027: \u00272019-11-18 16:24:17\u0027\\n                     }\\n}\\nNosuchEntity\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: \u0027OK\u0027, \u0027raw\u0027: \u0027\\\"OK\\\"\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                     \u0027host\u0027: \u0027myhost.ie.ibm.com\u0027, \u0027execution_time_ms\u0027: 9170, \u0027timestamp\u0027: \u00272019-11-18 16:24:17\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_delete_login_profile  script\\nDATA_TBL_FIELDS = [\\\"Groups\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_login_profile\\\"\\nWF_NAME = \\\"Delete Login Profile\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        if CONTENT == \\\"OK\\\":\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Login profile deleted for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.LoginProfileExists = \\\"No\\\"\\n        elif CONTENT == \\\"NoSuchEntity\\\":\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Login profile does not exist for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.LoginProfileExists = \\\"No\\\"\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1km05if\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0luxs5e\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1km05if\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0tn7e22\"/\u003e\u003cserviceTask id=\"ServiceTask_0uc614t\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n            \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n            \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User\u0027, \u0027CreateDate\u0027: \u00272019-11-05 15:54:43\u0027},\\n                        {\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User_2\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User_2\u0027,\\n                         \u0027CreateDate\u0027: \u00272019-10-31 16:23:07\u0027, \u0027PasswordLastUsed\u0027: \u00272019-11-12 10:55:42\u0027}\\n                       ],\\n            \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User\\\", \\\"CreateDate\\\": \\\"2019-11-05 15:54:43\\\"}, {\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User_2\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User_2\\\", \\\"CreateDate\\\": \\\"2019-10-31 16:23:07\\\"}]\u0027,\\n            \u0027inputs\u0027: {},\\n            \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                        \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 7951,\\n                        \u0027timestamp\u0027: \u00272019-11-14 13:48:30\u0027\\n                       }\\n}\\n\\n\\\"\\\"\\\"\\nimport re\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_users script\\nDATA_TBL_FIELDS = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"UserId\\\", \\\"Arn\\\", \\\"DefaultUser\\\", \\\"CreateDate\\\", \\\"LoginProfileExists\\\",\\n                   \\\"PasswordLastUsed\\\", \\\"Tags\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"Delete Login Profile\\\"\\n# Processing\\nINPUTS = results.inputs\\nCONTENT = results.content\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef check_add_quotes(tag_name):\\n    # Using regex\\n    # If spaces in tag name add quotes\\n    if re.search(r\\\"\\\\s\\\", tag_name):\\n        return \\\"\u0027\\\"+tag_name+\\\"\u0027\\\"\\n    else:\\n        return tag_name\\n\\ndef process_tags(tag_list, row):\\n    tags = []\\n    for i in range(len(tag_list)):\\n        if tag_list[i][\\\"Key\\\"] is not None:\\n            tags.append(tag_list[i][\\\"Key\\\"])\\n    row.Tags = \u0027,\u0027.join(check_add_quotes(t) for t in tags)\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        if len(CONTENT) == 1:\\n            u = CONTENT.pop()\\n            row.query_execution_date = QUERY_EXECUTION_DATE\\n            for f in DATA_TBL_FIELDS:\\n                if u[f] is not None:\\n                    if isinstance(u[f], unicode) or isinstance(u[f], int) \\\\\\n                            or isinstance(u[f], long) or len(u[f]) == 0:\\n                        if f == \\\"DefaultUser\\\" and not u[f]:\\n                            pass\\n                        else:\\n                            row[f] = u[f]\\n                    else:\\n                        if f == \\\"Tags\\\" and len(u[f]) \u0026gt; 0:\\n                            process_tags(u[f], row)\\n                        else:\\n                            row[f] = \u0027,\u0027.join(u[f])\\n        else:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Too many results \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            row.LoginProfileExists = \\\"No\\\"\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned for Resilient function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if note_text:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0luxs5e\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1e5a8hy\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0luxs5e\" sourceRef=\"ServiceTask_0tn7e22\" targetRef=\"ServiceTask_0uc614t\"/\u003e\u003cendEvent id=\"EndEvent_0wrh41r\"\u003e\u003cincoming\u003eSequenceFlow_1e5a8hy\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1e5a8hy\" sourceRef=\"ServiceTask_0uc614t\" targetRef=\"EndEvent_0wrh41r\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0s7m0lm\"\u003e\u003ctext\u003eDelete login profile of\u00a0 a user. Username assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1x263ie\" sourceRef=\"ServiceTask_0tn7e22\" targetRef=\"TextAnnotation_0s7m0lm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1vjjhan\"\u003e\u003ctext\u003eGet updated user properties and update data table. Username from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0l695cw\" sourceRef=\"ServiceTask_0uc614t\" targetRef=\"TextAnnotation_1vjjhan\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0tn7e22\" id=\"ServiceTask_0tn7e22_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"250\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1km05if\" id=\"SequenceFlow_1km05if_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"250\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"90\" x=\"179\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0uc614t\" id=\"ServiceTask_0uc614t_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"506\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0luxs5e\" id=\"SequenceFlow_0luxs5e_di\"\u003e\u003comgdi:waypoint x=\"350\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"506\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"383\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0wrh41r\" id=\"EndEvent_0wrh41r_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"675\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"648\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1e5a8hy\" id=\"SequenceFlow_1e5a8hy_di\"\u003e\u003comgdi:waypoint x=\"606\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"675\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"595.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0s7m0lm\" id=\"TextAnnotation_0s7m0lm_di\"\u003e\u003comgdc:Bounds height=\"65\" width=\"150\" x=\"225\" y=\"38\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1x263ie\" id=\"Association_1x263ie_di\"\u003e\u003comgdi:waypoint x=\"300\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"300\" y=\"103\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1vjjhan\" id=\"TextAnnotation_1vjjhan_di\"\u003e\u003comgdc:Bounds height=\"74\" width=\"147\" x=\"482\" y=\"34\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0l695cw\" id=\"Association_0l695cw_di\"\u003e\u003comgdi:waypoint x=\"556\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"556\" y=\"108\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "description": "Delete the password for an IAM user, which terminates the user\u0027s ability to access AWS services through the AWS Management Console. The User is assigned from a field in the selected data table row. The data table row will be refreshed will updated values for the selected user.",
      "export_key": "wf_aws_iam_delete_login_profile",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719373147461,
      "name": "Example: AWS IAM: Delete Login Profile",
      "object_type": "aws_iam_users",
      "programmatic_name": "wf_aws_iam_delete_login_profile",
      "tags": [],
      "uuid": "9993334b-a79c-4b9a-bb04-f0a80f4a180e",
      "workflow_id": 19
    },
    {
      "actions": [],
      "content": {
        "version": 10,
        "workflow_id": "wf_aws_iam_get_user_for_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_get_user_for_artifact\" isExecutable=\"true\" name=\"Example: AWS IAM: Get User For Artifact\"\u003e\u003cdocumentation\u003eGet an IAM users information. The User is assigned from the artifact value (of type \"AWS IAM User Name\").  A new row will be created in the data table \u0027AWS IAM users\u0027  for the user if it exists for the AWS IAM account.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_11zamar\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_05ucju9\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n            \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n            \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User\u0027, \u0027CreateDate\u0027: \u00272019-11-05 15:54:43\u0027},\\n                        {\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User_2\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User_2\u0027,\\n                         \u0027CreateDate\u0027: \u00272019-10-31 16:23:07\u0027, \u0027PasswordLastUsed\u0027: \u00272019-11-12 10:55:42\u0027}\\n                       ],\\n            \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User\\\", \\\"CreateDate\\\": \\\"2019-11-05 15:54:43\\\"}, {\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User_2\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User_2\\\", \\\"CreateDate\\\": \\\"2019-10-31 16:23:07\\\"}]\u0027,\\n            \u0027inputs\u0027: {},\\n            \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                        \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 7951,\\n                        \u0027timestamp\u0027: \u00272019-11-14 13:48:30\u0027\\n                       }\\n}\\n\\n\\\"\\\"\\\"\\nimport re\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_users script\\nDATA_TBL_FIELDS = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"Arn\\\", \\\"DefaultUser\\\", \\\"CreateDate\\\", \\\"LoginProfileExists\\\",\\n                   \\\"Tags\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"Get User For Artifact\\\"\\n# Processing\\nINPUTS = results.inputs\\nCONTENT = results.content\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        if isinstance(CONTENT, dict) and CONTENT.get(\\\"Status\\\") == \\\"NoSuchEntity\\\":\\n            note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; does not exist \\\" \\\\\\n                         \\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        elif isinstance(CONTENT, dict) and CONTENT.get(\\\"Status\\\") == \\\"ValidationError\\\":\\n            note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The username \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; is invalid \\\" \\\\\\n                         \\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        elif len(CONTENT) == 1:\\n            note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was found for Resilient \\\" \\\\\\n                        u\\\"function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            workflow.addProperty(\\\"user_exists\\\", {})\\n        else:\\n            note_text = u\\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Too many results \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned for user \\\" \\\\\\n                        \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned for Resilient \\\" \\\\\\n                     \\\"function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_users_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_11zamar\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1dmgt76\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_11zamar\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_05ucju9\"/\u003e\u003cserviceTask id=\"ServiceTask_1x8lxiw\" name=\"AWS IAM: List User Policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"64a30bb5-b539-45d6-b6e5-55674539d411\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_policies script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyName\u0027: \u0027test_pol\u0027},\\n                      {\u0027PolicyName\u0027: \u0027test_pol_2\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::123456789123:policy/test_pol_2\u0027},\\n                      {\u0027PolicyName\u0027: \u0027AmazonRoute53ReadOnlyAccess\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\u0027}],\\n          \u0027raw\u0027: \u0027[{\\\"PolicyName\\\": \\\"test_pol\\\"}, {\\\"PolicyName\\\": \\\"test_pol_2\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::834299573936:policy/test_pol_2\\\"},\\n                    {\\\"PolicyName\\\": \\\"AmazonRoute53ReadOnlyAccess\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 87423, \u0027timestamp\u0027: \u00272019-11-21 11:55:29\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_policies script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_policies\\\"\\nWF_NAME = \\\"Get User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; policies found for user \\\" \\\\\\n                    u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; policies found for \\\" \\\\\\n                    u\\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_user_policies_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1x3ivl6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1tsqqbn\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_1w96any\" name=\"AWS IAM: List User Access Key IDs\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"278f8cba-ff48-4495-93b0-27349c3fec8b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027,\\n                       \u0027Status\u0027: \u0027Active\u0027, \u0027CreateDate\u0027: \u00272019-11-12 11:09:38\u0027\\n                       }],\\n          \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_User\\\", \\\"AccessKeyId\\\": \\\"ABCDEFG\\\",\\n                  \\\"Status\\\": \\\"Active\\\", \\\"CreateDate\\\": \\\"2019-11-12 11:09:38\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 5365, \u0027timestamp\u0027: \u00272019-11-21 10:41:22\u0027}}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_access_keys script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_access_keys\\\"\\nWF_NAME = \\\"Get User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    newrow = workflow.properties.newrow\\n    if CONTENT:\\n        note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; access key ids found for user \\\" \\\\\\n                    u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; access key id found for \\\" \\\\\\n                    u\\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_user_access_key_ids_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tsqqbn\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1kpg8k6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cserviceTask id=\"ServiceTask_1n98qcs\" name=\"AWS IAM: List User Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8b67eb7-166c-4f5c-8291-1d0e3bd14e68\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027GroupName\u0027: \u0027system-admins\u0027, \u0027GroupId\u0027: \u0027ABCDEFG\u0027,\\n                      \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:group/system-admins\u0027, \u0027CreateDate\u0027: \u00272017-05-29 20:37:53\u0027}],\\n                      \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"GroupName\\\": \\\"system-admins\\\", \\\"GroupId\\\": \\\"ABCDEFG\\\",\\n                      \\\"Arn\\\": \\\"arn:aws:iam::123456789123:group/system-admins\\\", \\\"CreateDate\\\": \\\"2017-05-29 20:37:53\\\"\\n                      }\\n                    ]\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                     \u0027execution_time_ms\u0027: 1070, \u0027timestamp\u0027: \u00272019-11-18 10:19:19\u0027\\n                     }\\n}\\nUse this step to get user groups and also to process previous steps in workflow for dtat-table addition.\\n\\n\\\"\\\"\\\"\\n#  Globals\\nimport re\\n# List of fields in datatable fn_aws_iam_list_user_groups script\\nDATA_TBL_FIELDS_USER = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"Arn\\\", \\\"DefaultUser\\\", \\\"CreateDate\\\", \\\"LoginProfileExists\\\",\\n                        \\\"Tags\\\"]\\nDATA_TBL_FIELDS_GROUPS = [\\\"Groups\\\"]\\nDATA_TBL_FIELDS_POLICIES = [\\\"Policies\\\"]\\n\\nFN_NAME = \\\"fn_aws_iam_list_user_groups\\\"\\nWF_NAME = \\\"Get User For Artifact\\\"\\n# Processing\\nUSER_CONTENT = workflow.properties.list_users_results.content\\nPOLICY_CONTENT = workflow.properties.list_user_policies_results.content\\nACCESS_KEY_ID_CONTENT = workflow.properties.list_user_access_key_ids_result.content\\nGROUP_CONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef check_add_quotes(tag_name):\\n    # Using regex\\n    # If spaces in tag name add quotes\\n    if re.search(r\\\"\\\\s\\\", tag_name):\\n        return \\\"\u0027\\\"+tag_name+\\\"\u0027\\\"\\n    else:\\n        return tag_name\\n\\ndef process_access_key_ids(access_key_id_list, row):\\n    access_key_ids = []\\n    for ak_id in access_key_id_list:\\n        if ak_id[\\\"AccessKeyId\\\"] is not None:\\n            access_key_ids.append(ak_id[\\\"AccessKeyId\\\"])\\n    row.AccessKeyIds = \u0027,\u0027.join(access_key_ids)\\n\\ndef process_policies(policy_list, row):\\n    policies = []\\n    for pol in policy_list:\\n        if pol[\\\"PolicyName\\\"] is not None:\\n            policies.append(pol[\\\"PolicyName\\\"])\\n    row.Policies = \u0027,\u0027.join(policies)\\n\\ndef process_groups(group_list, row):\\n    groups = []\\n    for grp in group_list:\\n        if grp[\\\"GroupName\\\"] is not None:\\n            groups.append(grp[\\\"GroupName\\\"])\\n    row.Groups = \\\",\\\".join(groups)\\n\\n\\ndef process_tags(tag_list, row):\\n    tags = []\\n    for tag in tag_list:\\n        if tag[\\\"Key\\\"] is not None:\\n            tags.append(tag[\\\"Key\\\"])\\n    row.Tags = \u0027,\u0027.join(check_add_quotes(t) for t in tags)\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    if USER_CONTENT:\\n        u = USER_CONTENT.pop()\\n        newrow = incident.addRow(\\\"aws_iam_users\\\")\\n        newrow.query_execution_date = QUERY_EXECUTION_DATE\\n        for f in DATA_TBL_FIELDS_USER:\\n            if u[f] is not None:\\n                if isinstance(u[f], unicode) or isinstance(u[f], int) \\\\\\n                        or isinstance(u[f], long) or len(u[f]) == 0:\\n                    if f == \\\"DefaultUser\\\" and not u[f]:\\n                        pass\\n                    else:\\n                        newrow[f] = u[f]\\n                else:\\n                    if f == \\\"Tags\\\" and len(u[f]) \u0026gt; 0:\\n                        process_tags(u[f], newrow)\\n                    else:\\n                        newrow[f] = \u0027,\u0027.join(u[f])\\n        if POLICY_CONTENT:\\n            process_policies(POLICY_CONTENT, newrow)\\n        if ACCESS_KEY_ID_CONTENT:\\n            process_access_key_ids(ACCESS_KEY_ID_CONTENT, newrow)\\n        if GROUP_CONTENT:\\n            note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; groups found for user \\\" \\\\\\n                        u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(GROUP_CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            process_groups(GROUP_CONTENT, newrow)\\n        else:\\n            note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; group found for \\\" \\\\\\n                        u\\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_user_groups_result\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1kpg8k6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1qzv99x\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_16afr9l\"\u003e\u003cincoming\u003eSequenceFlow_0wv1eq5\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1qzv99x\u003c/incoming\u003e\u003c/endEvent\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0abtu8n\"\u003e\u003cincoming\u003eSequenceFlow_1dmgt76\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1x3ivl6\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0wv1eq5\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1dmgt76\" sourceRef=\"ServiceTask_05ucju9\" targetRef=\"ExclusiveGateway_0abtu8n\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1x3ivl6\" name=\"User exists.\" sourceRef=\"ExclusiveGateway_0abtu8n\" targetRef=\"ServiceTask_1x8lxiw\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0wv1eq5\" name=\"User does not exist.\" sourceRef=\"ExclusiveGateway_0abtu8n\" targetRef=\"EndEvent_16afr9l\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_1qzv99x\" sourceRef=\"ServiceTask_1n98qcs\" targetRef=\"EndEvent_16afr9l\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1tsqqbn\" sourceRef=\"ServiceTask_1x8lxiw\" targetRef=\"ServiceTask_1w96any\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1kpg8k6\" sourceRef=\"ServiceTask_1w96any\" targetRef=\"ServiceTask_1n98qcs\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1xeokqm\"\u003e\u003ctext\u003eList all users to\u00a0 determine if user exists. Username assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1b5ca4t\" sourceRef=\"ServiceTask_05ucju9\" targetRef=\"TextAnnotation_1xeokqm\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0fa8u08\"\u003e\u003ctext\u003eGet policy list for user, add to workflow result.\n\u00a0Username assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ratvhr\" sourceRef=\"ServiceTask_1x8lxiw\" targetRef=\"TextAnnotation_0fa8u08\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1vpmifz\"\u003e\u003ctext\u003eGet access key list for user, add to workflow result.\n\u00a0Username\u00a0 assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0xj0g01\" sourceRef=\"ServiceTask_1w96any\" targetRef=\"TextAnnotation_1vpmifz\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1oxs8nk\"\u003e\u003ctext\u003eGet group list for user. Add new row to data table\u00a0 \"AWS IAM Users\" with all workflow results.\n\u00a0Username assigned\u00a0 from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0xfnepu\" sourceRef=\"ServiceTask_1n98qcs\" targetRef=\"TextAnnotation_1oxs8nk\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_05ucju9\" id=\"ServiceTask_05ucju9_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"238\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11zamar\" id=\"SequenceFlow_11zamar_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"238\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"218\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1x8lxiw\" id=\"ServiceTask_1x8lxiw_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"470\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1w96any\" id=\"ServiceTask_1w96any_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"701\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1n98qcs\" id=\"ServiceTask_1n98qcs_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"958\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_16afr9l\" id=\"EndEvent_16afr9l_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"1152\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1125\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0abtu8n\" id=\"ExclusiveGateway_0abtu8n_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"374\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"399\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1dmgt76\" id=\"SequenceFlow_1dmgt76_di\"\u003e\u003comgdi:waypoint x=\"338\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"374\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"356\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1x3ivl6\" id=\"SequenceFlow_1x3ivl6_di\"\u003e\u003comgdi:waypoint x=\"424\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"470\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"60\" x=\"417\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0wv1eq5\" id=\"SequenceFlow_0wv1eq5_di\"\u003e\u003comgdi:waypoint x=\"399\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"399\" y=\"27\"/\u003e\u003comgdi:waypoint x=\"1170\" y=\"27\"/\u003e\u003comgdi:waypoint x=\"1170\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"74\" x=\"749\" y=\"6\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qzv99x\" id=\"SequenceFlow_1qzv99x_di\"\u003e\u003comgdi:waypoint x=\"1058\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1152\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1060\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tsqqbn\" id=\"SequenceFlow_1tsqqbn_di\"\u003e\u003comgdi:waypoint x=\"570\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"701\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"635.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1kpg8k6\" id=\"SequenceFlow_1kpg8k6_di\"\u003e\u003comgdi:waypoint x=\"801\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"958\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"834.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1xeokqm\" id=\"TextAnnotation_1xeokqm_di\"\u003e\u003comgdc:Bounds height=\"74\" width=\"186\" x=\"197\" y=\"42\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1b5ca4t\" id=\"Association_1b5ca4t_di\"\u003e\u003comgdi:waypoint x=\"289\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"290\" y=\"116\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0fa8u08\" id=\"TextAnnotation_0fa8u08_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"192\" x=\"423\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ratvhr\" id=\"Association_1ratvhr_di\"\u003e\u003comgdi:waypoint x=\"520\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"520\" y=\"134\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1vpmifz\" id=\"TextAnnotation_1vpmifz_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"212\" x=\"645\" y=\"79\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0xj0g01\" id=\"Association_0xj0g01_di\"\u003e\u003comgdi:waypoint x=\"751\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"751\" y=\"130\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1oxs8nk\" id=\"TextAnnotation_1oxs8nk_di\"\u003e\u003comgdc:Bounds height=\"57\" width=\"274\" x=\"871\" y=\"76\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0xfnepu\" id=\"Association_0xfnepu_di\"\u003e\u003comgdi:waypoint x=\"1009\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"1009\" y=\"133\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 10,
      "description": "Get an IAM users information. The User is assigned from the artifact value (of type \"AWS IAM User Name\").  A new row will be created in the data table \u0027AWS IAM users\u0027  for the user if it exists for the AWS IAM account.",
      "export_key": "wf_aws_iam_get_user_for_artifact",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719810844322,
      "name": "Example: AWS IAM: Get User For Artifact",
      "object_type": "artifact",
      "programmatic_name": "wf_aws_iam_get_user_for_artifact",
      "tags": [],
      "uuid": "6ff0bc5a-9c31-498b-91fc-7e89ce619e0f",
      "workflow_id": 6
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "wf_aws_iam_detach_all_user_policies",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_detach_all_user_policies\" isExecutable=\"true\" name=\"Example: AWS IAM: Detach All User Policies\"\u003e\u003cdocumentation\u003eRemove a managed policy from an IAM user. The User and policy names are assigned from fields in the selected data table row.  The data table row will be refreshed with updated values for the selected user.\n\nNote: A user can also have inline policies embedded with it, this function will also delete inline policies associated with the user.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1kl9bv7\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1kdyvrg\" name=\"AWS IAM: Detach User policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"10a78fb7-0c3e-48f3-88b8-2a464dbb0715\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_detach_user_policies script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyName\u0027: \u0027AWSDenyAll\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027PolicyName\u0027: \u0027AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027PolicyName\u0027: \\\"AWSDenyAll\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027PolicyName\u0027: \u0027AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_arns\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User_1\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_detach_user_policies  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_detach_user_policies\\\"\\nWF_NAME = \\\"Detach All User Policies\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    added = 0\\n    no_such_entity = 0\\n    detached_policies = []\\n    no_such_entity_policies = []\\n    if CONTENT:\\n        for pol_stat in CONTENT:\\n            if pol_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                added += 1\\n                detached_policies.append(pol_stat[\\\"PolicyName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_policies.append(pol_stat[\\\"PolicyName\\\"])\\n        if detached_policies:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The Policies \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; were detached and/or deleted \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, \\\", \\\".join(str(i) for i in detached_policies), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Policies \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_policies), \\\", \\\".join(str(i) for i in no_such_entity_policies), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ninputs.aws_iam_policy_names = row.Policies\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1kl9bv7\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_10wzgnm\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1kl9bv7\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1kdyvrg\"/\u003e\u003cserviceTask id=\"ServiceTask_1u9130g\" name=\"AWS IAM: List User Policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"64a30bb5-b539-45d6-b6e5-55674539d411\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_policies script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyName\u0027: \u0027test_pol\u0027},\\n                      {\u0027PolicyName\u0027: \u0027test_pol_2\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::12345:policy/test_pol_2\u0027},\\n                      {\u0027PolicyName\u0027: \u0027AmazonRoute53ReadOnlyAccess\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\u0027}],\\n          \u0027raw\u0027: \u0027[{\\\"PolicyName\\\": \\\"test_pol\\\"}, {\\\"PolicyName\\\": \\\"test_pol_2\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::12345:policy/test_pol_2\\\"},\\n                    {\\\"PolicyName\\\": \\\"AmazonRoute53ReadOnlyAccess\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 87423, \u0027timestamp\u0027: \u00272019-11-21 11:55:29\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_list_user_policies script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_policies\\\"\\nWF_NAME = \\\"Detach All User Policies\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    if CONTENT:\\n        policy_names = []\\n        for pol in CONTENT:\\n            if pol[\\\"PolicyName\\\"] is not None:\\n                policy_names.append(pol[\\\"PolicyName\\\"])\\n        row.Policies = \\\",\\\".join(policy_names)\\n    else:\\n        row.Policies = \\\"\\\"\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_10wzgnm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_152lkp7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_10wzgnm\" sourceRef=\"ServiceTask_1kdyvrg\" targetRef=\"ServiceTask_1u9130g\"/\u003e\u003cendEvent id=\"EndEvent_0fsvymn\"\u003e\u003cincoming\u003eSequenceFlow_152lkp7\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_152lkp7\" sourceRef=\"ServiceTask_1u9130g\" targetRef=\"EndEvent_0fsvymn\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1x4zzq9\"\u003e\u003ctext\u003eDetach (managed) or delete (inline) all policies of\u00a0 a user. Username and policy names assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_14iqnam\" sourceRef=\"ServiceTask_1kdyvrg\" targetRef=\"TextAnnotation_1x4zzq9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1v7gpao\"\u003e\u003ctext\u003eGet updated policy list for user\u00a0 and update data table.\n\u00a0Username assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0ts01e1\" sourceRef=\"ServiceTask_1u9130g\" targetRef=\"TextAnnotation_1v7gpao\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1kdyvrg\" id=\"ServiceTask_1kdyvrg_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"241\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1kl9bv7\" id=\"SequenceFlow_1kl9bv7_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"241\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"219.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1u9130g\" id=\"ServiceTask_1u9130g_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"464\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10wzgnm\" id=\"SequenceFlow_10wzgnm_di\"\u003e\u003comgdi:waypoint x=\"341\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"464\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"357.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0fsvymn\" id=\"EndEvent_0fsvymn_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"653\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"626\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_152lkp7\" id=\"SequenceFlow_152lkp7_di\"\u003e\u003comgdi:waypoint x=\"564\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"653\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"563.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1x4zzq9\" id=\"TextAnnotation_1x4zzq9_di\"\u003e\u003comgdc:Bounds height=\"92\" width=\"187\" x=\"194\" y=\"21\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_14iqnam\" id=\"Association_14iqnam_di\"\u003e\u003comgdi:waypoint x=\"290\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"290\" y=\"113\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1v7gpao\" id=\"TextAnnotation_1v7gpao_di\"\u003e\u003comgdc:Bounds height=\"73\" width=\"186\" x=\"421\" y=\"30\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0ts01e1\" id=\"Association_0ts01e1_di\"\u003e\u003comgdi:waypoint x=\"515\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"515\" y=\"103\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "description": "Remove a managed policy from an IAM user. The User and policy names are assigned from fields in the selected data table row.  The data table row will be refreshed with updated values for the selected user.\n\nNote: A user can also have inline policies embedded with it, this function will also delete inline policies associated with the user.",
      "export_key": "wf_aws_iam_detach_all_user_policies",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719374236095,
      "name": "Example: AWS IAM: Detach All User Policies",
      "object_type": "aws_iam_users",
      "programmatic_name": "wf_aws_iam_detach_all_user_policies",
      "tags": [],
      "uuid": "5bb46b0d-c613-4f0d-b2eb-464b6d1fda5c",
      "workflow_id": 16
    },
    {
      "actions": [],
      "content": {
        "version": 9,
        "workflow_id": "wf_aws_iam_delete_access_key_for_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_delete_access_key_for_artifact\" isExecutable=\"true\" name=\"Example: AWS IAM: Delete Access Key For Artifact\"\u003e\u003cdocumentation\u003eDelete an access key pair. The access key name is assigned from the artifact value. The user name is assigned from  result returned from the list users query. A  comment will be added to the artifact.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1tgik9o\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cendEvent id=\"EndEvent_0k33rav\"\u003e\u003cincoming\u003eSequenceFlow_1j0jsa4\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_046khc3\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1m5rg76\u003c/incoming\u003e\u003c/endEvent\u003e\u003cserviceTask id=\"ServiceTask_0c3lk1i\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n         \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_user\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027, \\n                      \u0027Arn\u0027: \u0027arn:aws:iam::123456789012:user/UserName\u0027, \u0027CreateDate\u0027: \u00272019-10-31 16:23:07\u0027, \\n                      \u0027PasswordLastUsed\u0027: \u00272020-01-22 11:22:39\u0027, \u0027LoginProfileExists\u0027: \u0027Yes\u0027, \u0027DefaultUser\u0027: \u0027Yes\u0027, \\n                      \u0027AccessKeyIds\u0027: [{\u0027UserName\u0027: \u0027iam_user\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027, \\n                                        \u0027Status\u0027: \u0027Active\u0027, \u0027CreateDate\u0027: \u00272019-11-04 11:33:33\u0027, \u0027DefaultKey\u0027: \u0027Yes\u0027, \\n                                        \u0027key_last_used\u0027: {\u0027LastUsedDate\u0027: \u00272020-01-24 12:36:00\u0027, \u0027ServiceName\u0027: \u0027iam\u0027, \\n                                                          \u0027Region\u0027: \u0027us-east-1\u0027}\\n                                       }\\n                                      ]\\n                     }\\n                    ], \\n         \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_user\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\n                \\\"arn:aws:iam::123456789012:user/iam_user\\\", \\\"CreateDate\\\": \\\"2019-10-31 16:23:07\\\", \\\"PasswordLastUsed\\\": \\n                \\\"2020-01-22 11:22:39\\\", \\\"LoginProfileExists\\\": \\\"Yes\\\", \\\"DefaultUser\\\": \\\"Yes\\\",\\n                \\\"AccessKeyIds\\\": [{\\\"UserName\\\": \\\"iam_user\\\", \\\"AccessKeyId\\\": \\\"ABCDEFG\\\", \\\"Status\\\": \\\"Active\\\", \\n                \\\"CreateDate\\\": \\\"2019-11-04 11:33:33\\\", \\\"DefaultKey\\\": \\\"Yes\\\", \\\"key_last_used\\\": {\\\"LastUsedDate\\\": \\\"2020-01-24 12:36:00\\\", \\n                \\\"ServiceName\\\": \\\"iam\\\", \\\"Region\\\": \\\"us-east-1\\\"}}]}]\u0027, \\n         \u0027inputs\u0027: {\u0027aws_iam_query_type\u0027: \u0027access_keys\u0027, \u0027aws_iam_access_key_filter\u0027: \u0027ABCDEFG\u0027}, \\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ie.ibm.com\u0027, \u0027execution_time_ms\u0027: 33209, \u0027timestamp\u0027: \u00272020-01-24 12:45:59\u0027\\n\\n         }}\\n\\n\\\"\\\"\\\"\\nimport re\\n\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_users script\\nDATA_TBL_FIELDS = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"UserId\\\", \\\"Arn\\\", \\\"DefaultUser\\\", \\\"CreateDate\\\",\\n                   \\\"LoginProfileExists\\\",\\n                   \\\"PasswordLastUsed\\\", \\\"Tags\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete Access Key For Artifact\\\"\\n# Processing\\nINPUTS = results.inputs\\nCONTENT = results.content\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    note_text_2 = u\u0027\u0027\\n    if CONTENT:\\n        if len(CONTENT) == 1:\\n            workflow.addProperty(\\\"user_exists\\\", {})\\n            u = CONTENT.pop()\\n            if u:\\n                ak_list = u[\\\"AccessKeyIds\\\"]\\n                if len(ak_list) == 1:\\n                    ak = ak_list.pop()\\n                    if \\\"DefaultKey\\\" in ak and ak[\\\"DefaultKey\\\"].lower() == \\\"yes\\\":\\n                        # Property to ensure we don\u0027t delete the default key for the integration.\\n                        workflow.addProperty(\\\"is_default_key\\\", {})\\n                        note_text += u\\\"\u0026lt;br\u0026gt;This is the default access key and therefore will not be deleted.\u0026lt;/br\u0026gt;\\\"\\n                else:\\n                    note_text_2 = u\\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Too many access keys \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned \\\" \\\\\\n                                  u\\\"for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                        .format(WF_NAME, len(CONTENT), len(ak), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        else:\\n            note_text = u\\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Too many results \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned for user \\\" \\\\\\n                        u\\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n\\n    else:\\n        note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The access key \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; not found \\\" \\\\\\n                     u\\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n          .format(WF_NAME, INPUTS[\\\"aws_iam_access_key_filter\\\"], FN_NAME)\\n    if note_text:\\n        incident.addNote(helper.createRichText(note_text))\\n    if note_text_2:\\n        incident.addNote(helper.createRichText(note_text_2))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_access_key_filter = artifact.value\\ninputs.aws_iam_query_type = \\\"access_keys\\\"\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_users_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1tgik9o\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0hz63pu\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1tgik9o\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0c3lk1i\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1n200w7\"\u003e\u003cincoming\u003eSequenceFlow_0hz63pu\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1j0jsa4\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0w1xcne\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0hz63pu\" sourceRef=\"ServiceTask_0c3lk1i\" targetRef=\"ExclusiveGateway_1n200w7\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1j0jsa4\" name=\"User does not exist.\" sourceRef=\"ExclusiveGateway_1n200w7\" targetRef=\"EndEvent_0k33rav\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_05tfidj\"\u003e\u003cincoming\u003eSequenceFlow_0w1xcne\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1cm7a60\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1m5rg76\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0w1xcne\" name=\"User exists.\" sourceRef=\"ExclusiveGateway_1n200w7\" targetRef=\"ExclusiveGateway_05tfidj\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_1cm7a60\" name=\"Is not default key.\" sourceRef=\"ExclusiveGateway_05tfidj\" targetRef=\"ServiceTask_1425olx\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_default_key\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_1m5rg76\" name=\"Is default key.\" sourceRef=\"ExclusiveGateway_05tfidj\" targetRef=\"EndEvent_0k33rav\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_default_key\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_1425olx\" name=\"AWS IAM: Delete Access Keys\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6a15d8e2-7472-4460-858e-3ff83221e183\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: [{\u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027OK\u0027}],\\n         \u0027raw\u0027: \u0027[{\\\"AccessKeyId\\\": \\\"ABCDEFG\\\", \\\"Status\\\": \\\"OK\\\"}]\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User_1\u0027, \u0027aws_iam_access_keys\u0027: \u0027ABCDEFG\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                     \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 752, \u0027timestamp\u0027: \u00272020-01-16 13:47:07\u0027\\n                    }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_access_keys  script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_access_keys\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete Access Key For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nEXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_keys = []\\n    no_such_entity_keys = []\\n    if CONTENT:\\n        for ak_stat in CONTENT:\\n            if ak_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_keys.append(ak_stat[\\\"AccessKeyId\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_keys.append(ak_stat[\\\"AccessKeyId\\\"])\\n        if deleted_keys:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The Access Key Id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; deleted \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n                .format(WF_NAME, \\\", \\\".join(str(i) for i in deleted_keys), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n\\n            artifact_desc_content = artifact.description[\\\"content\\\"]\\n            artifact_desc_sep = \\\"===============\\\"\\n            artifact_desc_upd = \\\"{0}: Access key \u0027{1}\u0027 deleted for AWS IAM user \u0027{2}\u0027 by Workflow \u0027{3}\u0027 and Function \u0027{4}\u0027.\\\"\\\\\\n              .format(EXECUTION_DATE, CONTENT[0][\\\"AccessKeyId\\\"], INPUTS[\\\"aws_iam_user_name\\\"], WF_NAME, FN_NAME)\\n            artifact_desc_upd = artifact_desc_content + \\\"\\\\n\\\" + artifact_desc_sep + \\\"\\\\n\\\" + artifact_desc_upd + \\\"\\\\n\\\" \\\\\\n                                + artifact_desc_sep\\n            artifact.description = \\\"{}\\\".format(artifact_desc_upd)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The Access Key Id \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"did not exist for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\" \\\\\\n                .format(WF_NAME, \\\", \\\".join(str(i) for i in no_such_entity_keys), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\" \\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"user_content = workflow.properties.list_users_results.content\\ninputs.aws_iam_user_name = user_content[0][\\\"UserName\\\"]\\ninputs.aws_iam_access_keys = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1cm7a60\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_046khc3\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_046khc3\" sourceRef=\"ServiceTask_1425olx\" targetRef=\"EndEvent_0k33rav\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_12hu9hw\"\u003e\u003ctext\u003eList all users to\u00a0 determine if access key\u00a0 exists for a user. Access key id assigned from an artifact value.\n\u00a0include username in result.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0bkmdy1\" sourceRef=\"ServiceTask_0c3lk1i\" targetRef=\"TextAnnotation_12hu9hw\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1mo574r\"\u003e\u003ctext\u003eDelete access key of a user and update artifact description.\n\u00a0Access key id assigned from artifact value, username assigned from result of previous step.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0sugzkx\" sourceRef=\"ServiceTask_1425olx\" targetRef=\"TextAnnotation_1mo574r\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0k33rav\" id=\"EndEvent_0k33rav_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"901\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"874\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0c3lk1i\" id=\"ServiceTask_0c3lk1i_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"289\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1tgik9o\" id=\"SequenceFlow_1tgik9o_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"289\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"243.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1n200w7\" id=\"ExclusiveGateway_1n200w7_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"450\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"430\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hz63pu\" id=\"SequenceFlow_0hz63pu_di\"\u003e\u003comgdi:waypoint x=\"389\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"450\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"374.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1j0jsa4\" id=\"SequenceFlow_1j0jsa4_di\"\u003e\u003comgdi:waypoint x=\"475\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"475\" y=\"119\"/\u003e\u003comgdi:waypoint x=\"915\" y=\"119\"/\u003e\u003comgdi:waypoint x=\"915\" y=\"189\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"74\" x=\"655\" y=\"90\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_05tfidj\" id=\"ExclusiveGateway_05tfidj_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"583\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"563\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0w1xcne\" id=\"SequenceFlow_0w1xcne_di\"\u003e\u003comgdi:waypoint x=\"500\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"583\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"60\" x=\"505\" y=\"186\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1cm7a60\" id=\"SequenceFlow_1cm7a60_di\"\u003e\u003comgdi:waypoint x=\"633\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"752\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"89\" x=\"648\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1m5rg76\" id=\"SequenceFlow_1m5rg76_di\"\u003e\u003comgdi:waypoint x=\"608\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"608\" y=\"336\"/\u003e\u003comgdi:waypoint x=\"919\" y=\"336\"/\u003e\u003comgdi:waypoint x=\"919\" y=\"224\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"70\" x=\"734\" y=\"317\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1425olx\" id=\"ServiceTask_1425olx_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"752\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_046khc3\" id=\"SequenceFlow_046khc3_di\"\u003e\u003comgdi:waypoint x=\"852\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"901\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"876.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_12hu9hw\" id=\"TextAnnotation_12hu9hw_di\"\u003e\u003comgdc:Bounds height=\"68\" width=\"187\" x=\"245\" y=\"10\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0bkmdy1\" id=\"Association_0bkmdy1_di\"\u003e\u003comgdi:waypoint x=\"339\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"339\" y=\"78\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1mo574r\" id=\"TextAnnotation_1mo574r_di\"\u003e\u003comgdc:Bounds height=\"83\" width=\"236\" x=\"791\" y=\"10\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0sugzkx\" id=\"Association_0sugzkx_di\"\u003e\u003comgdi:waypoint x=\"830\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"881\" y=\"93\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 9,
      "description": "Delete an access key pair. The access key name is assigned from the artifact value. The user name is assigned from  result returned from the list users query. A  comment will be added to the artifact.",
      "export_key": "wf_aws_iam_delete_access_key_for_artifact",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719806145806,
      "name": "Example: AWS IAM: Delete Access Key For Artifact",
      "object_type": "artifact",
      "programmatic_name": "wf_aws_iam_delete_access_key_for_artifact",
      "tags": [],
      "uuid": "4218ab65-6d1f-459a-997a-62680ee8d694",
      "workflow_id": 14
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "wf_aws_iam_get_access_keys",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_get_access_keys\" isExecutable=\"true\" name=\"Example: AWS IAM: Get Access Keys\"\u003e\u003cdocumentation\u003eGet the IAM access keys for a user in the AWS account. New row(s) will be created in the data table \u0027AWS IAM Access Keys\u0027 if key(s) are found for the user.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0fn4x8h\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0b2mn0d\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n         \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027, \\n                      \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_user\u0027, \\n                      \u0027CreateDate\u0027: \u00272020-02-19 17:17:00\u0027, \u0027LoginProfileExists\u0027: \u0027Yes\u0027, \\n                      \u0027AccessKeyIds\u0027: [{\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027Active\u0027,\\n                                        \u0027CreateDate\u0027: \u00272020-02-20 09:56:19\u0027, \u0027key_last_used\u0027: {\u0027ServiceName\u0027: \u0027N/A\u0027, \u0027Region\u0027: \u0027N/A\u0027}}, \\n                                       {\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027Active\u0027, \\n                                        \u0027CreateDate\u0027: \u00272020-02-20 09:56:34\u0027, \u0027key_last_used\u0027: {\u0027ServiceName\u0027: \u0027N/A\u0027, \u0027Region\u0027: \u0027N/A\u0027}}]}\\n                                      ], \\n         \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_user\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\n                   \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_user\\\", \\\"CreateDate\\\": \\\"2020-02-19 17:17:00\\\", \\n                   \\\"LoginProfileExists\\\": \\\"Yes\\\", \\\"AccessKeyIds\\\": [{\\\"UserName\\\": \\\"iam_test_user\\\", \\\"AccessKeyId\\\": \\n                   \\\"ABCDEFG\\\", \\\"Status\\\": \\\"Active\\\", \\\"CreateDate\\\": \\\"2020-02-20 09:56:19\\\", \\\"key_last_used\\\": \\n                   {\\\"ServiceName\\\": \\\"N/A\\\", \\\"Region\\\": \\\"N/A\\\"}}, {\\\"UserName\\\": \\\"iam_test_user\\\", \\\"AccessKeyId\\\": \\n                   \\\"ABCDEFG\\\", \\\"Status\\\": \\\"Active\\\", \\\"CreateDate\\\": \\\"2020-02-20 09:56:34\\\", \\\"key_last_used\\\": \\n                   {\\\"ServiceName\\\": \\\"N/A\\\", \\\"Region\\\": \\\"N/A\\\"}}]}]\u0027, \\n          \u0027inputs\u0027: {\u0027aws_iam_query_type\u0027: \u0027access_keys\u0027, \u0027aws_iam_user_filter\u0027: \u0027iam_test_user\u0027}, \\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027, \\n                      \u0027execution_time_ms\u0027: 2000, \u0027timestamp\u0027: \u00272020-02-21 15:34:08\u0027\\n                     }\\n}\\n\\n\\\"\\\"\\\"\\n#  Globals\\nimport re\\n# List of fields in datatable fn_aws_iam_list_users script main\\nDATA_TBL_FIELDS = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"AccessKeyId\\\", \\\"CreateDate\\\", \\\"Status\\\", \\\"DefaultKey\\\"]\\n# List of fields in datatable fn_aws_iam_list_users script last used access keys.\\nDATA_TBL_FIELDS_LUAK = [\\\"LastUsedDate\\\", \\\"ServiceName\\\", \\\"Region\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"Get access Keys\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef process_access_keys(access_key_id_list, user_name):\\n    access_key_ids = []\\n    for ak_id in access_key_id_list:\\n        newrow = incident.addRow(\\\"aws_iam_access_keys\\\")\\n        newrow.query_execution_date = QUERY_EXECUTION_DATE\\n        newrow.UserName = user_name\\n        for f in DATA_TBL_FIELDS[2:]:\\n            if ak_id[f] is not None:\\n                newrow[f] = ak_id[f]\\n        # Add key last used data if it exists.\\n        if ak_id[\\\"key_last_used\\\"] is not None:\\n            luak = ak_id[\\\"key_last_used\\\"]\\n            for l in DATA_TBL_FIELDS_LUAK:\\n                if luak[l] is not None:\\n                    newrow[l] = luak[l]\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    key_count = 0\\n    if CONTENT:\\n        if len(CONTENT) == 1:\\n            u = CONTENT.pop()\\n            access_key_ids = []\\n            if u[\\\"AccessKeyIds\\\"]:\\n                for k in u[\\\"AccessKeyIds\\\"]:\\n                    access_key_ids.append(k[\\\"AccessKeyId\\\"])\\n                    key_count += 1\\n            note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; access keys(s) \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; returned for \\\" \\\\\\n                        u\\\"user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, key_count, \u0027,\u0027.join(access_key_ids), INPUTS[\\\"aws_iam_user_filter\\\"], FN_NAME)\\n            if key_count:\\n                note_text += u\\\"\u0026lt;br\u0026gt;Adding new row(s) to data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; for access keys(s) \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\u0026lt;/br\u0026gt;\\\"\\\\\\n                    .format(\\\"AWS IAM Access Keys\\\", \u0027,\u0027.join(access_key_ids), key_count)\\n                user_name = u[\\\"UserName\\\"]\\n                process_access_keys(u[\\\"AccessKeyIds\\\"], user_name)\\n        else:\\n            note_text = u\\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Too many results \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        u\\\"Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_filter\\\"], FN_NAME)\\n    else:\\n        note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned returned for \\\" \\\\\\n                     u\\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_access_key_filter\\\"], FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_filter = row.UserName\\ninputs.aws_iam_query_type = \\\"access_keys\\\"\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0fn4x8h\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_01fo61w\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0fn4x8h\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0b2mn0d\"/\u003e\u003cendEvent id=\"EndEvent_0i7hu5z\"\u003e\u003cincoming\u003eSequenceFlow_01fo61w\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_01fo61w\" sourceRef=\"ServiceTask_0b2mn0d\" targetRef=\"EndEvent_0i7hu5z\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1tu1uqs\"\u003e\u003ctext\u003eList all users to\u00a0 determine if a user exists and has access keys. User filter assigned from the selected data table row. Add new rows to data table\u00a0 \"AWS IAM Access Keys\" for access key ids.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1jz3nq2\" sourceRef=\"ServiceTask_0b2mn0d\" targetRef=\"TextAnnotation_1tu1uqs\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0b2mn0d\" id=\"ServiceTask_0b2mn0d_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"233\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fn4x8h\" id=\"SequenceFlow_0fn4x8h_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"233\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"215.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0i7hu5z\" id=\"EndEvent_0i7hu5z_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"370\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"388\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_01fo61w\" id=\"SequenceFlow_01fo61w_di\"\u003e\u003comgdi:waypoint x=\"333\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"370\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"351.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1tu1uqs\" id=\"TextAnnotation_1tu1uqs_di\"\u003e\u003comgdc:Bounds height=\"131\" width=\"179\" x=\"193\" y=\"-7\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1jz3nq2\" id=\"Association_1jz3nq2_di\"\u003e\u003comgdi:waypoint x=\"283\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"283\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Get the IAM access keys for a user in the AWS account. New row(s) will be created in the data table \u0027AWS IAM Access Keys\u0027 if key(s) are found for the user.",
      "export_key": "wf_aws_iam_get_access_keys",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719374309193,
      "name": "Example: AWS IAM: Get Access Keys",
      "object_type": "aws_iam_users",
      "programmatic_name": "wf_aws_iam_get_access_keys",
      "tags": [],
      "uuid": "ba1c87aa-df6b-45a0-8aa8-52046690a141",
      "workflow_id": 11
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "wf_aws_iam_list_users",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_list_users\" isExecutable=\"true\" name=\"Example: AWS IAM: List Users\"\u003e\u003cdocumentation\u003eGet all the IAM users in the AWS account.  Users can be filtered by user name , group, policy and access key id. If the user name is specified get only information for this user. New rows will be created in the data table \u0027AWS IAM Users\u0027  for all users found based on the filtering criteria.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0slknrp\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0glvddf\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n            \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n            \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User\u0027, \u0027CreateDate\u0027: \u00272019-11-05 15:54:43\u0027},\\n                        {\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User_2\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User_2\u0027,\\n                         \u0027CreateDate\u0027: \u00272019-10-31 16:23:07\u0027, \u0027PasswordLastUsed\u0027: \u00272019-11-12 10:55:42\u0027}\\n                       ],\\n            \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User\\\", \\\"CreateDate\\\": \\\"2019-11-05 15:54:43\\\"}, {\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User_2\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User_2\\\", \\\"CreateDate\\\": \\\"2019-10-31 16:23:07\\\"}]\u0027,\\n            \u0027inputs\u0027: {},\\n            \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                        \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 7951,\\n                        \u0027timestamp\u0027: \u00272019-11-14 13:48:30\u0027\\n                       }\\n}\\n\\n\\\"\\\"\\\"\\n#  Globals\\nimport re\\n# List of fields in datatable fn_aws_iam_list_users script\\nDATA_TBL_FIELDS = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"Arn\\\", \\\"DefaultUser\\\", \\\"CreateDate\\\", \\\"LoginProfileExists\\\", \\n                   \\\"AccessKeyIds\\\", \\\"Policies\\\", \\\"Tags\\\", \\\"Groups\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"List Users\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef check_add_quotes(tag_name):\\n    # Using regex\\n    # If spaces in tag name add quotes\\n    if re.search(r\\\"\\\\s\\\", tag_name):\\n        return \\\"\u0027\\\"+tag_name+\\\"\u0027\\\"\\n    else:\\n        return tag_name\\n\\ndef process_access_key_ids(access_key_id_list, row):\\n    access_key_ids = []\\n    for ak_id in access_key_id_list:\\n        if ak_id[\\\"AccessKeyId\\\"] is not None:\\n            access_key_ids.append(ak_id[\\\"AccessKeyId\\\"])\\n    row.AccessKeyIds = \u0027,\u0027.join(access_key_ids)\\n\\ndef process_policies(policy_list, row):\\n    policies = []\\n    for pol in policy_list:\\n        if pol[\\\"PolicyName\\\"] is not None:\\n            policies.append(pol[\\\"PolicyName\\\"])\\n    row.Policies = \u0027,\u0027.join(policies)\\n\\ndef process_groups(group_list, row):\\n    groups = []\\n    for grp in group_list:\\n        if grp[\\\"GroupName\\\"] is not None:\\n            groups.append(grp[\\\"GroupName\\\"])\\n    row.Groups = \\\",\\\".join(groups)\\n\\ndef process_tags(tag_list, row):\\n    tags = []\\n    for tag in tag_list:\\n        if tag[\\\"Key\\\"] is not None:\\n            tags.append(tag[\\\"Key\\\"])\\n    row.Tags = \u0027,\u0027.join(check_add_quotes(t) for t in tags)\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    filters = [f for f in [INPUTS[\\\"aws_iam_user_filter\\\"], INPUTS[\\\"aws_iam_group_filter\\\"],  \\n                           INPUTS[\\\"aws_iam_policy_filter\\\"], INPUTS[\\\"aws_iam_access_key_filter\\\"]] \\n               if f is not None]\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; user(s) returned for Resilient function \\\" \\\\\\n                   \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(CONTENT), FN_NAME)\\n        note_text += \\\"\u0026lt;br\u0026gt;Adding new row(s) to data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; for \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; user(s).\u0026lt;/br\u0026gt;\\\".format(\\\"AWS IAM Users\\\", len(CONTENT))\\n        for u in CONTENT:\\n            newrow = incident.addRow(\\\"aws_iam_users\\\")\\n            newrow.query_execution_date = QUERY_EXECUTION_DATE\\n            for f in DATA_TBL_FIELDS:\\n                newrow.Status = \\\"Active\\\"\\n                if u[f] is not None:\\n                    if isinstance(u[f], unicode) or isinstance(u[f], int) \\\\\\n                            or isinstance(u[f], long) or len(u[f]) == 0:\\n                        if f == \\\"DefaultUser\\\" and not u[f]:\\n                            pass\\n                        else:\\n                          newrow[f] = u[f]\\n                    else:\\n                        if f == \\\"AccessKeyIds\\\" and len(u[f]) \u0026gt; 0:\\n                            process_access_key_ids(u[f], newrow)\\n                        elif f == \\\"Policies\\\" and len(u[f]) \u0026gt; 0:\\n                            process_policies(u[f], newrow)\\n                        elif f == \\\"Groups\\\" and len(u[f]) \u0026gt; 0:\\n                            process_groups(u[f], newrow)\\n                        elif f == \\\"Tags\\\" and len(u[f]) \u0026gt; 0:\\n                            process_tags(u[f], newrow)\\n                        else:\\n                            newrow[f] = \u0027,\u0027.join(u[f])\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned for Resilient function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if filters:\\n        note_text += \\\"\u0026lt;br\u0026gt;Query Filters:\u0026lt;/br\u0026gt;\\\"\\n        if INPUTS.get(\\\"aws_iam_user_filter\\\"): \\n            note_text += u\\\"\u0026lt;br\u0026gt;aws_iam_user_filter: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\".format(INPUTS[\\\"aws_iam_user_filter\\\"])\\n        if INPUTS.get(\\\"aws_iam_group_filter\\\"): \\n            note_text += u\\\"\u0026lt;br\u0026gt;aws_iam_group_filter: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\".format(INPUTS[\\\"aws_iam_group_filter\\\"])\\n        if INPUTS.get(\\\"aws_iam_policy_filter\\\"): \\n            note_text += u\\\"\u0026lt;br\u0026gt;aws_iam_policy_filter: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\".format(INPUTS[\\\"aws_iam_policy_filter\\\"])\\n        if INPUTS.get(\\\"aws_iam_access_key_filter\\\"):   \\n            note_text += u\\\"\u0026lt;br\u0026gt;aws_iam_access_key_filter: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\".format(INPUTS[\\\"aws_iam_access_key_filter\\\"])\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"import re\\n\\n# Get a list of all enabled filters.\\nENABLED_FILTERS = [f for f in [rule.properties.aws_iam_user_filter, rule.properties.aws_iam_group_filter, \\n                               rule.properties.aws_iam_policy_filter, rule.properties.aws_iam_access_key_filter] \\n                   if f is not None]\\n\\n\\ndef is_regex(regex_str):\\n    \\\"\\\"\\\"\\\"Test if sting is a correctly formed regular expression.\\n\\n    :param regex_str: Regular expression string.\\n    :return: Boolean.\\n    \\\"\\\"\\\"\\n    try:\\n        re.compile(regex_str)\\n        return True\\n    except re.error:\\n        return False\\n\\n\\ndef main():\\n    # Test any enabled filters to ensure they are valid regular expressions.\\n    for ef in (ENABLED_FILTERS):\\n        if not is_regex(ef):\\n            raise ValueError(\\\"The query filter \u0027{}\u0027 is not a valid regular expression.\\\".format(unicode(ef)))\\n\\n    inputs.aws_iam_user_filter = rule.properties.aws_iam_user_filter\\n    inputs.aws_iam_group_filter = rule.properties.aws_iam_group_filter\\n    inputs.aws_iam_policy_filter = rule.properties.aws_iam_policy_filter\\n    inputs.aws_iam_access_key_filter = rule.properties.aws_iam_access_key_filter\\n    inputs.aws_iam_query_type = \\\"users\\\"\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0slknrp\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1vac54r\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003cendEvent id=\"EndEvent_028k2ov\"\u003e\u003cincoming\u003eSequenceFlow_1vac54r\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1vac54r\" sourceRef=\"ServiceTask_0glvddf\" targetRef=\"EndEvent_028k2ov\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0slknrp\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0glvddf\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0jp9sz5\"\u003e\u003ctext\u003eList all users and get all user properties (Login profile, Access keys, Policies, Groups and Tags) .\u00a0Create row in data table \"AWS IAM Users\" for each user.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0x03oqf\" sourceRef=\"ServiceTask_0glvddf\" targetRef=\"TextAnnotation_0jp9sz5\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0glvddf\" id=\"ServiceTask_0glvddf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"261\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_028k2ov\" id=\"EndEvent_028k2ov_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"437\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"410\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1vac54r\" id=\"SequenceFlow_1vac54r_di\"\u003e\u003comgdi:waypoint x=\"361\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"437\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"354\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0slknrp\" id=\"SequenceFlow_0slknrp_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"261\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"184.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0jp9sz5\" id=\"TextAnnotation_0jp9sz5_di\"\u003e\u003comgdc:Bounds height=\"94\" width=\"208\" x=\"207\" y=\"28\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0x03oqf\" id=\"Association_0x03oqf_di\"\u003e\u003comgdi:waypoint x=\"311\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"311\" y=\"122\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Get all the IAM users in the AWS account.  Users can be filtered by user name , group, policy and access key id. If the user name is specified get only information for this user. New rows will be created in the data table \u0027AWS IAM Users\u0027  for all users found based on the filtering criteria.",
      "export_key": "wf_aws_iam_list_users",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719374591701,
      "name": "Example: AWS IAM: List Users",
      "object_type": "incident",
      "programmatic_name": "wf_aws_iam_list_users",
      "tags": [],
      "uuid": "7c8f586e-b637-4590-a8de-3a71a408225c",
      "workflow_id": 18
    },
    {
      "actions": [],
      "content": {
        "version": 5,
        "workflow_id": "wf_aws_iam_remove_user_from_all_groups",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_remove_user_from_all_groups\" isExecutable=\"true\" name=\"Example: AWS IAM: Remove User From All Groups\"\u003e\u003cdocumentation\u003eRemove an  IAM user from IAM groups. The user and groups names are assigned from fields in the selected data table row. The data table row will be refreshed with updated group values for the selected user.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_023djl6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0gupful\" name=\"AWS IAM: Remove User From Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7efc8616-ed52-4a8f-9f25-5c168b681ba9\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_detach_user_policies script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027OK\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027PolicyArn\u0027: \\\"arn:aws:iam::aws:policy/AWSDenyAll\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027OK\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_arns\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User_1\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_detach_user_policies  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_remove_user_from_groups\\\"\\nWF_NAME = \\\"Remove User From All Groups\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    added = 0\\n    no_such_entity = 0\\n    added_groups = []\\n    no_such_entity_groups = []\\n    if CONTENT:\\n        for pol_stat in CONTENT:\\n            if pol_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                added += 1\\n                added_groups.append(pol_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_groups.append(pol_stat[\\\"GroupName\\\"])\\n        if added_groups:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was removed from the \\\" \\\\\\n                        \\\"following groups \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], \\\", \\\".join(str(i) for i in added_groups), FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Groups \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_groups), \\\", \\\".join(str(i) for i in no_such_entity_groups), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ninputs.aws_iam_group_names = row.Groups\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_023djl6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0hl8fkr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_023djl6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0gupful\"/\u003e\u003cserviceTask id=\"ServiceTask_0fqrcsa\" name=\"AWS IAM: List User Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8b67eb7-166c-4f5c-8291-1d0e3bd14e68\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027GroupName\u0027: \u0027system-admins\u0027, \u0027GroupId\u0027: \u0027ABCDEFG\u0027,\\n                      \u0027Arn\u0027: \u0027arn:aws:iam::12345:group/system-admins\u0027, \u0027CreateDate\u0027: \u00272017-05-29 20:37:53\u0027}],\\n                      \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"GroupName\\\": \\\"system-admins\\\", \\\"GroupId\\\": \\\"ABCDEFG\\\",\\n                      \\\"Arn\\\": \\\"arn:aws:iam::12345:group/system-admins\\\", \\\"CreateDate\\\": \\\"2017-05-29 20:37:53\\\"\\n                      }\\n                    ]\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                     \u0027execution_time_ms\u0027: 1070, \u0027timestamp\u0027: \u00272019-11-18 10:19:19\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_groups script\\nDATA_TBL_FIELDS = [\\\"Groups\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_groups\\\"\\nWF_NAME = \\\"Remove User From All Groups\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef check_add_quotes(tag_name):\\n    # Using regex\\n    # If spaces in tag name add quotes\\n    if re.search(r\\\"\\\\s\\\", tag_name):\\n        return \\\"\u0027\\\"+tag_name+\\\"\u0027\\\"\\n    else:\\n        return tag_name\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        groups = []\\n        for grp in CONTENT:\\n            if grp[\\\"GroupName\\\"] is not None:\\n                groups.append(grp[\\\"GroupName\\\"])\\n        row.Groups = \\\",\\\".join(groups)\\n    else:\\n        row.Groups = \\\"\\\"\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0hl8fkr\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0c6ifje\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0hl8fkr\" sourceRef=\"ServiceTask_0gupful\" targetRef=\"ServiceTask_0fqrcsa\"/\u003e\u003cendEvent id=\"EndEvent_0thby2p\"\u003e\u003cincoming\u003eSequenceFlow_0c6ifje\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0c6ifje\" sourceRef=\"ServiceTask_0fqrcsa\" targetRef=\"EndEvent_0thby2p\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ly0o1r\"\u003e\u003ctext\u003eRemove user from all groups. Username and group names assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1a38ikv\" sourceRef=\"ServiceTask_0gupful\" targetRef=\"TextAnnotation_1ly0o1r\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0h12krq\"\u003e\u003ctext\u003eGet updated group list for user\u00a0 and update data table.\n\u00a0Username assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0wzeg29\" sourceRef=\"ServiceTask_0fqrcsa\" targetRef=\"TextAnnotation_0h12krq\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0gupful\" id=\"ServiceTask_0gupful_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"238\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_023djl6\" id=\"SequenceFlow_023djl6_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"238\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"218\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0fqrcsa\" id=\"ServiceTask_0fqrcsa_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"430\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hl8fkr\" id=\"SequenceFlow_0hl8fkr_di\"\u003e\u003comgdi:waypoint x=\"338\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"430\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"339\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0thby2p\" id=\"EndEvent_0thby2p_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"614\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"587\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0c6ifje\" id=\"SequenceFlow_0c6ifje_di\"\u003e\u003comgdi:waypoint x=\"530\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"614\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"527\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ly0o1r\" id=\"TextAnnotation_1ly0o1r_di\"\u003e\u003comgdc:Bounds height=\"62\" width=\"175\" x=\"200\" y=\"62\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1a38ikv\" id=\"Association_1a38ikv_di\"\u003e\u003comgdi:waypoint x=\"288\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"288\" y=\"124\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0h12krq\" id=\"TextAnnotation_0h12krq_di\"\u003e\u003comgdc:Bounds height=\"57\" width=\"195\" x=\"382\" y=\"64\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0wzeg29\" id=\"Association_0wzeg29_di\"\u003e\u003comgdi:waypoint x=\"480\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"480\" y=\"121\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 5,
      "description": "Remove an  IAM user from IAM groups. The user and groups names are assigned from fields in the selected data table row. The data table row will be refreshed with updated group values for the selected user.",
      "export_key": "wf_aws_iam_remove_user_from_all_groups",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719375071680,
      "name": "Example: AWS IAM: Remove User From All Groups",
      "object_type": "aws_iam_users",
      "programmatic_name": "wf_aws_iam_remove_user_from_all_groups",
      "tags": [],
      "uuid": "bd99a002-7768-4d52-844b-e10a540ecbda",
      "workflow_id": 20
    },
    {
      "actions": [],
      "content": {
        "version": 22,
        "workflow_id": "wf_aws_iam_delete_user_for_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_delete_user_for_artifact\" isExecutable=\"true\" name=\"Example: AWS IAM: Delete User For Artifact\"\u003e\u003cdocumentation\u003eDelete the selected IAM user. The User is assigned from an artifact value for an artifact of type \"AWS IAM User Name\". The artifact description will be updated  on successful user deletion.\n\nNote: Unlike the AWS Management Console, when you delete a user programmatically, you must delete the items attached to the user or the deletion fails. Before attempting to delete a user, the following items if associated with the user will be removed, de-activated or deleted.:\n\n    Password ( DeleteLoginProfile )\n    Access keys ( DeleteAccessKey )\n    Inline policies ( DeleteUserPolicy )\n    Attached managed policies ( DetachUserPolicy ) \n    Group memberships ( RemoveUserFromGroup )\n    Signing certificate ( DeleteSigningCertificate )\n    SSH public key ( DeleteSSHPublicKey )\n    Git credentials ( DeleteServiceSpecificCredential )\n    Multi-factor authentication (MFA) device ( DeactivateMFADevice , DeleteVirtualMFADevice )\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1vcyete\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1khyagr\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n            \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n            \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User\u0027, \u0027CreateDate\u0027: \u00272019-11-05 15:54:43\u0027},\\n                        {\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User_2\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User_2\u0027,\\n                         \u0027CreateDate\u0027: \u00272019-10-31 16:23:07\u0027, \u0027PasswordLastUsed\u0027: \u00272019-11-12 10:55:42\u0027}\\n                       ],\\n            \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User\\\", \\\"CreateDate\\\": \\\"2019-11-05 15:54:43\\\"},\\n            {\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User_2\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User_2\\\", \\\"CreateDate\\\": \\\"2019-10-31 16:23:07\\\"}]\u0027,\\n            \u0027inputs\u0027: {},\\n            \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                        \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 7951,\\n                        \u0027timestamp\u0027: \u00272019-11-14 13:48:30\u0027\\n                       }\\n}\\n\\n\\\"\\\"\\\"\\nimport re\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_users script\\nDATA_TBL_FIELDS = [\\\"UserName\\\", \\\"LoginProfileExists\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete User For Artifact\\\"\\n# Processing\\nINPUTS = results.inputs\\nCONTENT = results.content\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = u\u0027\u0027\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        if isinstance(CONTENT, dict) and CONTENT.get(\\\"Status\\\") == \\\"NoSuchEntity\\\":\\n            note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was not found \\\" \\\\\\n                         u\\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        elif isinstance(CONTENT, dict) and CONTENT.get(\\\"Status\\\") == \\\"ValidationError\\\":\\n            note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The username \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; is invalid \\\" \\\\\\n                         u\\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        elif len(CONTENT) == 1:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was found \\\" \\\\\\n                        \\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            workflow.addProperty(\\\"user_exists\\\", {})\\n            u = CONTENT.pop()\\n            if u[\\\"LoginProfileExists\\\"] is not None and u[\\\"LoginProfileExists\\\"].lower() == \\\"yes\\\":\\n                workflow.addProperty(\\\"has_login_profile\\\", {})\\n            if u[\\\"DefaultUser\\\"] is not None and u[\\\"DefaultUser\\\"].lower() == \\\"yes\\\":\\n                workflow.addProperty(\\\"is_default_user\\\", {})\\n                note_text += u\\\"\u0026lt;br\u0026gt;This is the default user and therefore will not be deleted.\u0026lt;/br\u0026gt;\\\"\\n        else:\\n            note_text = u\\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Too many results \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        u\\\"Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned  user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \\\" \\\\\\n                     u\\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n\\n\\n    incident.addNote(helper.createRichText(note_text))\\n        \\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1vcyete\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_08c963g\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1vcyete\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1khyagr\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_08q7k8k\"\u003e\u003cincoming\u003eSequenceFlow_08c963g\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0vv91su\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1qmdyjx\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_08c963g\" sourceRef=\"ServiceTask_1khyagr\" targetRef=\"ExclusiveGateway_08q7k8k\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_13jlzao\"\u003e\u003cincoming\u003eSequenceFlow_0vv91su\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_09pioh6\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_08dlm5e\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0vv91su\" name=\"User exists.\" sourceRef=\"ExclusiveGateway_08q7k8k\" targetRef=\"ExclusiveGateway_13jlzao\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0cudkvl\"\u003e\u003cincoming\u003eSequenceFlow_09pioh6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1cvgahq\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_08nnle9\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_09pioh6\" name=\"Is not default user.\" sourceRef=\"ExclusiveGateway_13jlzao\" targetRef=\"ExclusiveGateway_0cudkvl\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_default_user\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cendEvent id=\"EndEvent_0opl7i1\"\u003e\u003cincoming\u003eSequenceFlow_1qmdyjx\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_08dlm5e\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_11q5lkh\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1qmdyjx\" name=\"User doesn\u0027t exist.\" sourceRef=\"ExclusiveGateway_08q7k8k\" targetRef=\"EndEvent_0opl7i1\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"user_exists\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_08dlm5e\" name=\"Is default user.\" sourceRef=\"ExclusiveGateway_13jlzao\" targetRef=\"EndEvent_0opl7i1\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_default_user\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_0e1bj00\" name=\"AWS IAM: Delete Login Profile\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"22d5a7a2-9e89-4011-b53d-604a4aeaad2e\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_login_profile script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: \u0027NoSuchEntity\u0027, \u0027raw\u0027: \u0027\\\"NoSuchEntity\\\"\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                     \u0027host\u0027: \u0027myhost.ie.ibm.com\u0027, \u0027execution_time_ms\u0027: 9170, \u0027timestamp\u0027: \u00272019-11-18 16:24:17\u0027\\n                     }\\n}\\nNosuchEntity\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: \u0027OK\u0027, \u0027raw\u0027: \u0027\\\"OK\\\"\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                     \u0027host\u0027: \u0027myhost.ie.ibm.com\u0027, \u0027execution_time_ms\u0027: 9170, \u0027timestamp\u0027: \u00272019-11-18 16:24:17\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_delete_login_profile  script\\nDATA_TBL_FIELDS = [\\\"LoginProfileExists\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_login_profile\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        if CONTENT == \\\"OK\\\":\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Login profile deleted for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        elif CONTENT == \\\"NoSuchEntity\\\":\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Login profile does not exist for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1cvgahq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0fp5atw\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1cvgahq\" name=\"Has a login profile.\" sourceRef=\"ExclusiveGateway_0cudkvl\" targetRef=\"ServiceTask_0e1bj00\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_login_profile\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_1n1bl4y\" name=\"AWS IAM: List User Access Key IDs\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"278f8cba-ff48-4495-93b0-27349c3fec8b\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027,\\n                       \u0027Status\u0027: \u0027Active\u0027, \u0027CreateDate\u0027: \u00272019-11-12 11:09:38\u0027\\n                       }],\\n          \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_User\\\", \\\"AccessKeyId\\\": \\\"ABCDEFG\\\",\\n                  \\\"Status\\\": \\\"Active\\\", \\\"CreateDate\\\": \\\"2019-11-12 11:09:38\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 5365, \u0027timestamp\u0027: \u00272019-11-21 10:41:22\u0027}}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_access_keys script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_access_keys\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Access key\u0027 result(s) returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        access_key_ids = []\\n        for ak in CONTENT:\\n            if ak[\\\"AccessKeyId\\\"] is not None:\\n                workflow.addProperty(\\\"has_access_keys\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Access key\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_user_access_keys_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0fp5atw\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_08nnle9\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0b1w6zu\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0fp5atw\" sourceRef=\"ServiceTask_0e1bj00\" targetRef=\"ServiceTask_1n1bl4y\"/\u003e\u003csequenceFlow id=\"SequenceFlow_08nnle9\" name=\"Doesn\u0027t have a login profile.\" sourceRef=\"ExclusiveGateway_0cudkvl\" targetRef=\"ServiceTask_1n1bl4y\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_login_profile\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0lfuuy8\"\u003e\u003cincoming\u003eSequenceFlow_0b1w6zu\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_11a6hxl\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0fbb8nd\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0b1w6zu\" sourceRef=\"ServiceTask_1n1bl4y\" targetRef=\"ExclusiveGateway_0lfuuy8\"/\u003e\u003cserviceTask id=\"ServiceTask_1hzhb3p\" name=\"AWS IAM: Delete Access Keys\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6a15d8e2-7472-4460-858e-3ff83221e183\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027OK\u0027},\\n                      {\u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\\\"AccessKeyId\\\": \\\"ABCDEFG\\\", \\\"Status\\\": \\\"OK\\\"},\\n                  {\\\"AccessKeyId\\\": \\\"ABCDEFG\\\", \\\"Status\\\": \\\"NoSuchEntity\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027TEST_USER\u0027, \u0027aws_iam_access_keys\u0027: \u0027ABCDEFG,ABCDEFG\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 37199, \u0027timestamp\u0027: \u00272019-11-21 14:31:13\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_access_keys  script\\nDATA_TBL_FIELDS = [\\\"AccessKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_access_keys\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_keys = []\\n    no_such_entity_keys = []\\n    if CONTENT:\\n        for ak_stat in CONTENT:\\n            if ak_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_keys.append(ak_stat[\\\"AccessKeyId\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_keys.append(ak_stat[\\\"AccessKeyId\\\"])\\n        if deleted_keys:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Access Key Ids \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; deleted \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_keys), deleted_keys, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Access Key Ids \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_keys), no_such_entity_keys, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\\ncontent = workflow.properties.list_user_access_keys_results.content\\naccess_key_ids = []\\nfor ak_id in content:\\n    if ak_id[\\\"AccessKeyId\\\"] is not None:\\n        access_key_ids.append(ak_id[\\\"AccessKeyId\\\"])\\ninputs.aws_iam_access_keys = \\\",\\\".join(access_key_ids)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_11a6hxl\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1xhovti\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_11a6hxl\" name=\"Has access keys.\" sourceRef=\"ExclusiveGateway_0lfuuy8\" targetRef=\"ServiceTask_1hzhb3p\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_access_keys\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_0fudggi\" name=\"AWS IAM: List User Policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"64a30bb5-b539-45d6-b6e5-55674539d411\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyName\u0027: \u0027test_pol\u0027},\\n                      {\u0027PolicyName\u0027: \u0027test_pol_2\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::123456789123:policy/test_pol_2\u0027},\\n                      {\u0027PolicyName\u0027: \u0027AmazonRoute53ReadOnlyAccess\u0027,\\n                       \u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\u0027}],\\n          \u0027raw\u0027: \u0027[{\\\"PolicyName\\\": \\\"test_pol\\\"}, {\\\"PolicyName\\\": \\\"test_pol_2\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::123456789123:policy/test_pol_2\\\"},\\n                    {\\\"PolicyName\\\": \\\"AmazonRoute53ReadOnlyAccess\\\",\\n                    \\\"PolicyArn\\\": \\\"arn:aws:iam::aws:policy/AmazonRoute53ReadOnlyAccess\\\"}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                      \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 87423, \u0027timestamp\u0027: \u00272019-11-21 11:55:29\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_groups script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_policies\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Policy name\u0027 result(s) returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        policy_names = []\\n        for pol in CONTENT:\\n            if pol[\\\"PolicyName\\\"] is not None:\\n                workflow.addProperty(\\\"has_policies\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Policy name\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_user_policies_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1xhovti\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0fbb8nd\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1buspu6\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1xhovti\" sourceRef=\"ServiceTask_1hzhb3p\" targetRef=\"ServiceTask_0fudggi\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0fbb8nd\" name=\"Doesn\u0027t have access keys.\" sourceRef=\"ExclusiveGateway_0lfuuy8\" targetRef=\"ServiceTask_0fudggi\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_access_keys\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_064jb3p\"\u003e\u003cincoming\u003eSequenceFlow_1buspu6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0hfhx0n\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_1k3cbi4\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1buspu6\" sourceRef=\"ServiceTask_0fudggi\" targetRef=\"ExclusiveGateway_064jb3p\"/\u003e\u003cserviceTask id=\"ServiceTask_0tw2w9u\" name=\"AWS IAM: Detach User policies\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"10a78fb7-0c3e-48f3-88b8-2a464dbb0715\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_detach_user_policies script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyName\u0027: \u0027AWSDenyAll\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027PolicyName\u0027: \u0027AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027PolicyName\u0027: \\\"AWSDenyAll\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027PolicyName\u0027: \u0027AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_arns\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User_1\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_detach_user_policies  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_detach_user_policies\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    detached = 0\\n    no_such_entity = 0\\n    detached_policies = []\\n    no_such_entity_policies = []\\n    if CONTENT:\\n        for pol_stat in CONTENT:\\n            if pol_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                detached += 1\\n                detached_policies.append(pol_stat[\\\"PolicyName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_policies.append(pol_stat[\\\"PolicyName\\\"])\\n        if detached_policies:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Policies \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; detached \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(detached_policies), \\\", \\\".join(str(i) for i in detached_policies), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Policies \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_policies), \\\", \\\".join(str(i) for i in no_such_entity_policies), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\\ncontent = workflow.properties.list_user_policies_results.content\\npolicy_names = []\\nfor pol in content:\\n    if pol[\\\"PolicyName\\\"] is not None:\\n        policy_names.append(pol[\\\"PolicyName\\\"])\\ninputs.aws_iam_policy_names = \\\",\\\".join(policy_names)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0hfhx0n\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1n26lsr\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0hfhx0n\" name=\"Has attached policies.\" sourceRef=\"ExclusiveGateway_064jb3p\" targetRef=\"ServiceTask_0tw2w9u\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_policies\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_0logngp\" name=\"AWS IAM: List User Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8b67eb7-166c-4f5c-8291-1d0e3bd14e68\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n         \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027GroupName\u0027: \u0027system-admins\u0027, \u0027GroupId\u0027: \u0027ABCDEFG\u0027,\\n                      \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:group/system-admins\u0027, \u0027CreateDate\u0027: \u00272017-05-29 20:37:53\u0027}],\\n                      \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"GroupName\\\": \\\"system-admins\\\", \\\"GroupId\\\": \\\"ABCDEFG\\\",\\n                      \\\"Arn\\\": \\\"arn:aws:iam::123456789123:group/system-admins\\\", \\\"CreateDate\\\": \\\"2017-05-29 20:37:53\\\"\\n                      }\\n                    ]\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                     \u0027execution_time_ms\u0027: 1070, \u0027timestamp\u0027: \u00272019-11-18 10:19:19\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_groups script\\nDATA_TBL_FIELDS = [\\\"Groups\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_groups\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Group\u0027 result(s) returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        groups = []\\n        for grp in CONTENT:\\n            if grp[\\\"GroupName\\\"] is not None:\\n                workflow.addProperty(\\\"is_group_member\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Group\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_user_groups_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1n26lsr\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_1k3cbi4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_13e8y9v\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1n26lsr\" sourceRef=\"ServiceTask_0tw2w9u\" targetRef=\"ServiceTask_0logngp\"/\u003e\u003csequenceFlow id=\"SequenceFlow_1k3cbi4\" name=\"Does not have attached policies.\" sourceRef=\"ExclusiveGateway_064jb3p\" targetRef=\"ServiceTask_0logngp\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_policies\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0f9j4hk\"\u003e\u003cincoming\u003eSequenceFlow_13e8y9v\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0uhexmc\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0fnwhv2\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_13e8y9v\" sourceRef=\"ServiceTask_0logngp\" targetRef=\"ExclusiveGateway_0f9j4hk\"/\u003e\u003cserviceTask id=\"ServiceTask_17vw09q\" name=\"AWS IAM: Remove User From Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7efc8616-ed52-4a8f-9f25-5c168b681ba9\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_detach_user_policies script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027PolicyArn\u0027: \\\"arn:aws:iam::aws:policy/AWSDenyAll\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027PolicyArn\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll_2\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_arns\u0027: \u0027arn:aws:iam::aws:policy/AWSDenyAll\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User_1\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_detach_user_policies  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_remove_user_from_groups\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_groups = []\\n    no_such_entity_groups = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_groups.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_groups.append(grp_stat[\\\"GroupName\\\"])\\n        if deleted_groups:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Groups \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; removed \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_groups), \\\", \\\".join(str(i) for i in deleted_groups), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; Groups \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_groups), \\\", \\\".join(str(i) for i in no_such_entity_groups), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\\ncontent = workflow.properties.list_user_groups_results.content\\ngroups = []\\nfor grp in content:\\n    if grp[\\\"GroupName\\\"] is not None:\\n        groups.append(grp[\\\"GroupName\\\"])\\ninputs.aws_iam_group_names = \\\",\\\".join(groups)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0uhexmc\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0q3qxox\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0uhexmc\" name=\"Is a group member.\" sourceRef=\"ExclusiveGateway_0f9j4hk\" targetRef=\"ServiceTask_17vw09q\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_group_member\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_0dk9bos\" name=\"AWS IAM: Delete User\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"773f48cb-3a55-405e-aef9-73c7938de80f\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_access_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: { \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n          \u0027content\u0027: \u0027OK\u0027, \\n          \u0027raw\u0027: \u0027\\\"OK\\\"\u0027, \\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user\u0027}, \\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027, \\n                      \u0027execution_time_ms\u0027: 689, \u0027timestamp\u0027: \u00272020-01-15 10:27:48\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_user  script\\nDATA_TBL_FIELDS = [\\\"Status\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_user\\\"\\nWF_NAME = \\\"Example: AWS IAM: Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nEXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        if CONTENT == \\\"OK\\\":\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: User \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; was successfully deleted for \\\" \\\\\\n                        \\\"Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n            if artifact.description:\\n                artifact_desc_content = artifact.description[\\\"content\\\"] + \\\"\\\\n\\\"\\n            else:\\n              artifact_desc_content = \u0027\u0027\\n            artifact_desc_sep = \\\"===============\\\"\\n            artifact_desc_upd = \\\"{0}: AWS IAM User \u0027{1}\u0027 deleted by Workflow \u0027{2}\u0027 and Function \u0027{3}\u0027.\\\"\\\\\\n              .format(EXECUTION_DATE, INPUTS[\\\"aws_iam_user_name\\\"], WF_NAME, FN_NAME)\\n            artifact_desc_upd = artifact_desc_content + artifact_desc_sep + \\\"\\\\n\\\" + artifact_desc_upd + \\\"\\\\n\\\" \\\\\\n                                + artifact_desc_sep\\n            artifact.description = \\\"{}\\\".format(artifact_desc_upd)\\n        else:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Unexpected delete status \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for delete\\\" \\\\\\n                        \\\" user operation \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, CONTENT, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0r12hry\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_10r7rg5\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0757cr2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_11q5lkh\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_11q5lkh\" sourceRef=\"ServiceTask_0dk9bos\" targetRef=\"EndEvent_0opl7i1\"/\u003e\u003csequenceFlow id=\"SequenceFlow_0fnwhv2\" name=\"Is not a group member.\" sourceRef=\"ExclusiveGateway_0f9j4hk\" targetRef=\"ServiceTask_1mccj8q\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_group_member\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_1mccj8q\" name=\"AWS IAM: List SSH Public Keys\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"a7b28b9e-6a27-44c1-90f2-d4d3d5f54ba9\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_ssh_public_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n          \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027SSHPublicKeyId\u0027: \u0027ABCDEFG\u0027, \\n                       \u0027Status\u0027: \u0027Active\u0027, \u0027UploadDate\u0027: \u00272020-02-25 11:05:17\u0027\\n                      }\\n                     ], \\n          \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_user_10\\\", \\\"SSHPublicKeyId\\\": \\\"ABCDEFG\\\", \\n                  \\\"Status\\\": \\\"Active\\\", \\\"UploadDate\\\": \\\"2020-02-25 11:05:17\\\"}]\u0027, \\n          \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user\u0027}, \\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027, \\n                      \u0027execution_time_ms\u0027: 657, \u0027timestamp\u0027: \u00272020-02-25 16:11:28\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_ssh_public_keys script\\nDATA_TBL_FIELDS = [\\\"SSHPublicKeyIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_ssh_public_keys\\\"\\nWF_NAME = \\\"Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT=False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027SSH Public keys\u0027 returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        access_key_ids = []\\n        for sshk_id in CONTENT:\\n            if sshk_id[\\\"SSHPublicKeyId\\\"] is not None:\\n                workflow.addProperty(\\\"has_ssh_public_keys\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027SSH Public keys\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_ssh_keys_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0q3qxox\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0fnwhv2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_12h0te8\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0q3qxox\" sourceRef=\"ServiceTask_17vw09q\" targetRef=\"ServiceTask_1mccj8q\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1i3oeih\"\u003e\u003cincoming\u003eSequenceFlow_12h0te8\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1206qiz\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_06e1mhe\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_12h0te8\" sourceRef=\"ServiceTask_1mccj8q\" targetRef=\"ExclusiveGateway_1i3oeih\"/\u003e\u003cserviceTask id=\"ServiceTask_0y2v3g3\" name=\"AWS IAM: Delete SSH Public Keys\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"17506b61-ff8f-44b2-937e-15a3ae3d5d0a\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_ssh_keys script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027SSHPublicKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027SSHPublicKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027SSHPublicKeyId\u0027: \\\"ABCDEFG\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027SSHPublicKeyId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_ssh_keys_ids\u0027: \u0027ABCDEFG\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_ssh_keys  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_ssh_keys\\\"\\nWF_NAME = \\\"Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_keys = []\\n    no_such_entity_keys = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_keys.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_keys.append(grp_stat[\\\"GroupName\\\"])\\n        if deleted_keys:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027SSH Public keys\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; removed \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_keys), \\\", \\\".join(str(i) for i in deleted_keys), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027SSH Public keys\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_keys), \\\", \\\".join(str(i) for i in no_such_entity_keys), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\\ncontent = workflow.properties.list_ssh_keys_results.content\\nssh_key_ids = []\\nfor ssh_key_id in content:\\n    if ssh_key_id[\\\"SSHPublicKeyId\\\"] is not None:\\n        ssh_key_ids.append(ssh_key_id[\\\"SSHPublicKeyId\\\"])\\ninputs.aws_iam_ssh_key_ids = \\\",\\\".join(ssh_key_ids)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1206qiz\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0l3v69q\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1206qiz\" name=\"User has SSH public keys.\" sourceRef=\"ExclusiveGateway_1i3oeih\" targetRef=\"ServiceTask_0y2v3g3\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_ssh_public_keys\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_06e1mhe\" name=\"User doesn\u0027t have SSH public keys.\" sourceRef=\"ExclusiveGateway_1i3oeih\" targetRef=\"ServiceTask_1sgmi99\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_ssh_public_keys\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_1sgmi99\" name=\"AWS IAM: List Service Specific Cr...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"ec76a52d-94e3-447c-8b0c-f049c365b4f3\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_service_specific_credentials script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n         \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027Status\u0027: \u0027Active\u0027, \u0027ServiceUserName\u0027: \u0027iam_test_user-at-123456789123\u0027, \\n                      \u0027CreateDate\u0027: \u00272020-02-25 10:43:24\u0027, \u0027ServiceSpecificCredentialId\u0027: \u0027ABCDEFG\u0027, \\n                      \u0027ServiceName\u0027: \u0027codecommit.amazonaws.com\u0027\\n                     },\\n                     {\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027Status\u0027: \u0027Active\u0027, \u0027ServiceUserName\u0027: \u0027iam_test_user_10-at-123456789123\u0027,\\n                      \u0027CreateDate\u0027: \u00272020-02-26 11:50:52\u0027, \u0027ServiceSpecificCredentialId\u0027: \u0027ABCDEFG\u0027, \\n                      \u0027ServiceName\u0027: \u0027cassandra.amazonaws.com\u0027}], \\n         \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_user\\\", \\\"Status\\\": \\\"Active\\\", \\\"ServiceUserName\\\": \\\"iam_test_user_10-at-123456789123\\\", \\n                   \\\"CreateDate\\\": \\\"2020-02-25 10:43:24\\\", \\\"ServiceSpecificCredentialId\\\": \\\"ABCDEFG\\\", \\\"ServiceName\\\": \\\"codecommit.amazonaws.com\\\"}, \\n                   {\\\"UserName\\\": \\\"iam_test_user_10\\\", \\\"Status\\\": \\\"Active\\\", \\\"ServiceUserName\\\": \\\"iam_test_user_10-at-123456789123\\\", \\n                   \\\"CreateDate\\\": \\\"2020-02-26 11:50:52\\\", \\\"ServiceSpecificCredentialId\\\": \\\"ABCDEFG\\\", \\\"ServiceName\\\": \\\"cassandra.amazonaws.com\\\"}]\u0027, \\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user\u0027}, \\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027, \\n                     \u0027execution_time_ms\u0027: 982, \u0027timestamp\u0027: \u00272020-02-26 11:56:51\u0027\\n                    }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_service_specific_credentials script\\nDATA_TBL_FIELDS = [\\\"ServiceSpecificCredentialIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_service_specific_credentials\\\"\\nWF_NAME = \\\"Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Service specific credentials\u0027 returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        for ssc_id in CONTENT:\\n            if ssc_id[\\\"ServiceSpecificCredentialId\\\"] is not None:\\n                workflow.addProperty(\\\"has_srv_creds\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Service specific credentials\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_srv_specific_creds_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0l3v69q\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_06e1mhe\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0cghy2n\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0l3v69q\" sourceRef=\"ServiceTask_0y2v3g3\" targetRef=\"ServiceTask_1sgmi99\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1bgxyws\"\u003e\u003cincoming\u003eSequenceFlow_0cghy2n\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0kpv5qx\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_02g7g9j\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0cghy2n\" sourceRef=\"ServiceTask_1sgmi99\" targetRef=\"ExclusiveGateway_1bgxyws\"/\u003e\u003cserviceTask id=\"ServiceTask_0j2b73x\" name=\"AWS IAM: Delete Service Specific ...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"590079fe-1bb9-47d9-8c3a-7084838232c7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_ss_creds script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027ServiceSpecificCredentialId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027ServiceSpecificCredentialId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027ServiceSpecificCredentialId: \\\"ABCDEFG\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027ServiceSpecificCredentialId\u0027: \u0027ABCDEFG\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_ssc_ids\u0027: \u0027ABCDEFG\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_ss_creds  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_ss_creds\\\"\\nWF_NAME = \\\"Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_creds = []\\n    no_such_entity_creds = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_creds.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_creds.append(grp_stat[\\\"GroupName\\\"])\\n        if deleted_creds:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Service specific credentials\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; removed \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_creds), \\\", \\\".join(str(i) for i in deleted_creds), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Service specific credentials\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_creds), \\\", \\\".join(str(i) for i in no_such_entity_creds), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\\ncontent = workflow.properties.list_srv_specific_creds_results.content\\nsrv_specific_cred_ids = []\\nfor ssc_id in content:\\n    if ssc_id[\\\"ServiceSpecificCredentialId\\\"] is not None:\\n        srv_specific_cred_ids.append(ssc_id[\\\"ServiceSpecificCredentialId\\\"])\\ninputs.aws_iam_ssc_ids = \\\",\\\".join(srv_specific_cred_ids)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0kpv5qx\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0krx7f7\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0kpv5qx\" name=\"User has service specific credentials.\" sourceRef=\"ExclusiveGateway_1bgxyws\" targetRef=\"ServiceTask_0j2b73x\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_srv_creds\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_02g7g9j\" name=\"User doesn\u0027t have service specific credentials.\" sourceRef=\"ExclusiveGateway_1bgxyws\" targetRef=\"ServiceTask_0wb3a6o\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_srv_creds\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_0wb3a6o\" name=\"AWS IAM: List Signing Certificate...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"28643fbd-6a39-411e-9b67-8507e4a228e7\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_signing_certificates script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n         \u0027content\u0027: [{\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027CertificateId\u0027: \u0027WM6U3NNR5JH3AOTNJY44CUI6I6EYXTLD\u0027, \\n                      \u0027CertificateBody\u0027: \u0027-----BEGIN CERTIFICATE-----\\\\nMIID...Apg=\\\\n-----END CERTIFICATE-----\u0027, \\n                      \u0027Status\u0027: \u0027Active\u0027, \u0027UploadDate\u0027: \u00272020-02-26 12:25:27\u0027}], \\n         \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_user\\\", \\\"CertificateId\\\": \\\"WM6U3NNR5JH3AOTNJY44CUI6I6EYXTLD\\\", \\\"CertificateBody\\\": \\n                 \\\"-----BEGIN CERTIFICATE-----\\\\\\\\nMIID...Apg=\\\\\\\\n-----END CERTIFICATE-----\\\", \\\"Status\\\": \\\"Active\\\", \\\"UploadDate\\\": \\\"2020-02-26 12:25:27\\\"}]\u0027, \\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user\u0027}, \\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 729, \u0027timestamp\u0027: \u00272020-02-26 12:33:57\u0027\\n        }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_signing_certificates script\\nDATA_TBL_FIELDS = [\\\"CertificateIds\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_signing_certificates\\\"\\nWF_NAME = \\\"Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT=False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Signing Certificates\u0027 returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        for scert_id in CONTENT:\\n            if scert_id[\\\"CertificateId\\\"] is not None:\\n                workflow.addProperty(\\\"has_sign_certs\\\", {})\\n                break\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Signing Certificates\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_signing_certs_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0krx7f7\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_02g7g9j\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1y5642u\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0krx7f7\" sourceRef=\"ServiceTask_0j2b73x\" targetRef=\"ServiceTask_0wb3a6o\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0srueur\"\u003e\u003cincoming\u003eSequenceFlow_1y5642u\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0f07hag\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0953ew2\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_1y5642u\" sourceRef=\"ServiceTask_0wb3a6o\" targetRef=\"ExclusiveGateway_0srueur\"/\u003e\u003cserviceTask id=\"ServiceTask_1dn9z35\" name=\"AWS IAM: Delete Signing Certifica...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"8fda0978-9293-4078-9578-c9855ff26f85\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_signing_certs script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027CertificateId\u0027: \u0027WM6U3NNR5JH3AOTNJY44CUI6I6EYXTLD\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027CertificateId\u0027: \u0027WM6U3NNR5JH3AOTNJY44CUI6I6EYXTLD\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027CertificateId: \\\"WM6U3NNR5JH3AOTNJY44CUI6I6EYXTLD\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027CertificateId\u0027: \u0027WM6U3NNR5JH3AOTNJY44CUI6I6EYXTLD\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_sign_cert_ids\u0027: \u0027WM6U3NNR5JH3AOTNJY44CUI6I6EYXTLD\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_list_signing_certs  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_signing_certs\\\"\\nWF_NAME = \\\"Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_certs = []\\n    no_such_entity_certs = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_certs.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_certs.append(grp_stat[\\\"GroupName\\\"])\\n        if deleted_certs:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Signing Certificates\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; removed \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_certs), \\\", \\\".join(str(i) for i in deleted_certs), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Signing Certificates\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_certs), \\\", \\\".join(str(i) for i in no_such_entity_certs), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\\ncontent = workflow.properties.list_signing_certs_results.content\\nsign_cert_ids = []\\nfor scert_id in content:\\n    if scert_id[\\\"CertificateId\\\"] is not None:\\n        sign_cert_ids.append(scert_id[\\\"CertificateId\\\"])\\ninputs.aws_iam_sign_cert_ids = \\\",\\\".join(sign_cert_ids)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0f07hag\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0no9ecs\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0f07hag\" name=\"User has signing certificates.\" sourceRef=\"ExclusiveGateway_0srueur\" targetRef=\"ServiceTask_1dn9z35\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_sign_certs\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0953ew2\" name=\"User doesn\u0027t have siging certificates.\" sourceRef=\"ExclusiveGateway_0srueur\" targetRef=\"ServiceTask_1d33ieu\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_sign_certs\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cserviceTask id=\"ServiceTask_1d33ieu\" name=\"AWS IAM: List MFA Devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"d85d59b9-b5e1-444e-9b9f-ea2f5dae64ae\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_mfa_devices script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n         \u0027content\u0027: [{\u0027UserName\u0027a: \u0027iam_test_user\u0027, \u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \\n                      \u0027EnableDate\u0027: \u00272020-02-26 16:55:05\u0027}, \u0027is_virtual\u0027: True], \\n         \u0027raw\u0027: \u0027[{\\\"UserName\\\": \\\"iam_test_user_10\\\", \\\"SerialNumber\\\": \\\"arn:aws:iam::123456789123:mfa/iam_test_user_10\\\", \\n                 \\\"EnableDate\\\": \\\"2020-02-26 16:55:05\\\"}, \u0027is_virtual\u0027: True]\u0027, \\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user_10\u0027}, \\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ie.ibm.com\u0027, \\n                     \u0027execution_time_ms\u0027: 5644, \u0027timestamp\u0027: \u00272020-02-26 17:37:48\u0027\\n                    }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_mfa_devices script\\nDATA_TBL_FIELDS = [\\\"SerialNumbers\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_mfa_devices\\\"\\nWF_NAME = \\\"Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nDEBUG_SCRIPT=False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027Active NFA devices\u0027 returned for user \\\" \\\\\\n                    \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        for mfa_ser_num in CONTENT:\\n            if mfa_ser_num[\\\"SerialNumber\\\"] is not None:\\n                workflow.addProperty(\\\"has_active_mfa\\\", {})\\n            if mfa_ser_num.get(\\\"is_virtual\\\", None):\\n                workflow.addProperty(\\\"is_virtual_mfa\\\", {})\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; \u0027Active NFA devices\u0027 result(s) returned for \\\" \\\\\\n                    \\\"user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\n\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\",\"pre_processing_script_language\":\"python3\",\"result_name\":\"list_mfa_devices_results\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0no9ecs\u003c/incoming\u003e\u003cincoming\u003eSequenceFlow_0953ew2\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0c22kfv\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0no9ecs\" sourceRef=\"ServiceTask_1dn9z35\" targetRef=\"ServiceTask_1d33ieu\"/\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_1nizxai\"\u003e\u003cincoming\u003eSequenceFlow_0c22kfv\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1b3itqq\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_0r12hry\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_0c22kfv\" sourceRef=\"ServiceTask_1d33ieu\" targetRef=\"ExclusiveGateway_1nizxai\"/\u003e\u003cserviceTask id=\"ServiceTask_0fkvwlu\" name=\"AWS IAM: Deactivate MFA Devices\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"6c20740b-0696-4e2f-b772-54f74ef049fe\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_deactivate_mfa_devices script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027SerialNumber: \\\"arn:aws:iam::123456789123:mfa/iam_test_user\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_mfa_serial_nums\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_deactivate_mfa_devices  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_deactivate_mfa_devices\\\"\\nWF_NAME = \\\"Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deactivated = 0\\n    no_such_entity = 0\\n    deactivated_mfas = []\\n    no_such_entity_mfas = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deactivated += 1\\n                deactivated_mfas.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_mfas.append(grp_stat[\\\"GroupName\\\"])\\n        if deactivated_mfas:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027MFA devices\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; de-activated \\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deactivated_mfas), \\\", \\\".join(str(i) for i in deactivated_mfas), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027MFA devices\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_mfas), \\\", \\\".join(str(i) for i in no_such_entity_mfas), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = artifact.value\\ncontent = workflow.properties.list_mfa_devices_results.content\\nmfa_serial_nums = []\\nfor mfa_ser_num in content:\\n    if mfa_ser_num[\\\"SerialNumber\\\"] is not None:\\n        mfa_serial_nums.append(mfa_ser_num[\\\"SerialNumber\\\"])\\ninputs.aws_iam_mfa_serial_nums = \\\",\\\".join(mfa_serial_nums)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1b3itqq\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_14ei8hm\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1b3itqq\" name=\"User has activated mfa device.\" sourceRef=\"ExclusiveGateway_1nizxai\" targetRef=\"ServiceTask_0fkvwlu\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_active_mfa\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0r12hry\" name=\"User doesn\u0027t have activated mfa device.\" sourceRef=\"ExclusiveGateway_1nizxai\" targetRef=\"ServiceTask_0dk9bos\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"has_active_mfa\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003cexclusiveGateway id=\"ExclusiveGateway_0r4px7c\"\u003e\u003cincoming\u003eSequenceFlow_14ei8hm\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0ps0kve\u003c/outgoing\u003e\u003coutgoing\u003eSequenceFlow_10r7rg5\u003c/outgoing\u003e\u003c/exclusiveGateway\u003e\u003csequenceFlow id=\"SequenceFlow_14ei8hm\" sourceRef=\"ServiceTask_0fkvwlu\" targetRef=\"ExclusiveGateway_0r4px7c\"/\u003e\u003cserviceTask id=\"ServiceTask_0cxgrrf\" name=\"AWS IAM: Delete Virtual MFA Devic...\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"0685a3cf-fdf3-4a68-8574-a8a4dcc112eb\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_delete_mfa_devices script ##\\n# Example result:\\n\\\"\\\"\\\"\\nOK\\nResult: {\\n          \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n          \u0027content\u0027: [{\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027OK\u0027}\\n                      {\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}],\\n          \u0027raw\u0027: \u0027[{\u0027SerialNumber: \\\"arn:aws:iam::123456789123:mfa/iam_test_user\\\", \u0027Status\\\": \u0027OK\u0027},\\n                  {\u0027SerialNumber\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027Status\u0027: \u0027NoSuchEntity\u0027}]\u0027,\\n          \u0027inputs\u0027: {\u0027aws_iam_mfa_serial_nums\u0027: \u0027arn:aws:iam::123456789123:mfa/iam_test_user\u0027, \u0027aws_iam_user_name\u0027: \u0027iam_test_User\u0027},\\n          \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                      \u0027execution_time_ms\u0027: 790, \u0027timestamp\u0027: \u00272019-11-29 12:18:30\u0027\\n                     }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_delete_mfa_devices  script\\nDATA_TBL_FIELDS = [\\\"Policies\\\"]\\nFN_NAME = \\\"fn_aws_iam_delete_mfa_devices\\\"\\nWF_NAME = \\\"Delete User For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nDEBUG_SCRIPT = False\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    deleted = 0\\n    no_such_entity = 0\\n    deleted_mfas = []\\n    no_such_entity_mfas = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                deleted += 1\\n                deleted_mfas.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_mfas.append(grp_stat[\\\"GroupName\\\"])\\n        if deleted_mfas:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027MFA devices\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; deleted\\\" \\\\\\n                        \\\"for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(deleted_mfas), \\\", \\\".join(str(i) for i in deleted_mfas), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \u0027MFA devices\u0027 \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"which did not exist for user \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{4}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(no_such_entity_mfas), \\\", \\\".join(str(i) for i in no_such_entity_mfas), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n    if DEBUG_SCRIPT:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"content = workflow.properties.list_mfa_devices_results.content\\nmfa_serial_nums = []\\nfor mfa_ser_num in content:\\n    if mfa_ser_num[\\\"SerialNumber\\\"] is not None and mfa_ser_num.get(\\\"is_virtual\\\", None):\\n        mfa_serial_nums.append(mfa_ser_num[\\\"SerialNumber\\\"])\\ninputs.aws_iam_mfa_serial_nums = \\\",\\\".join(mfa_serial_nums)\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0ps0kve\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0757cr2\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0ps0kve\" name=\"User mfa device is a virtual mfa.\" sourceRef=\"ExclusiveGateway_0r4px7c\" targetRef=\"ServiceTask_0cxgrrf\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_virtual_mfa\\\", None) != None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_10r7rg5\" name=\"User mfa device not a virtual mfa.\" sourceRef=\"ExclusiveGateway_0r4px7c\" targetRef=\"ServiceTask_0dk9bos\"\u003e\u003cconditionExpression language=\"resilient-conditions\" xsi:type=\"tFormalExpression\"\u003e{\"conditions\":[{\"evaluation_id\":1,\"field_name\":null,\"method\":\"script\",\"type\":null,\"value\":{\"final_expression_text\":\"workflow.properties.get(\\\"is_virtual_mfa\\\", None) == None\",\"language\":\"python3\"}}],\"custom_condition\":\"\",\"logic_type\":\"all\",\"script_language\":\"python3\"}\u003c/conditionExpression\u003e\u003c/sequenceFlow\u003e\u003csequenceFlow id=\"SequenceFlow_0757cr2\" sourceRef=\"ServiceTask_0cxgrrf\" targetRef=\"ServiceTask_0dk9bos\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kmg6ls\"\u003e\u003ctext\u003eList all users to\u00a0 determine if 1) user exists ,\u00a0 2) is not a default user and 3) has a login profile. Username is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_180o2zs\" sourceRef=\"ServiceTask_1khyagr\" targetRef=\"TextAnnotation_1kmg6ls\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_102jwbz\"\u003e\u003ctext\u003eDelete user login profile. Update data table row for user login profile.\n\u00a0Username is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_19au57w\" sourceRef=\"ServiceTask_0e1bj00\" targetRef=\"TextAnnotation_102jwbz\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0qshsw7\"\u003e\u003ctext\u003eDetermine if any access keys assigned to user.\u00a0 Update workflow result.\n\u00a0Username is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_17b6nsq\" sourceRef=\"ServiceTask_1n1bl4y\" targetRef=\"TextAnnotation_0qshsw7\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1lsup12\"\u003e\u003ctext\u003eDelete user access keys. Update data table row for user access keys.\n\u00a0Username is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1d67hdx\" sourceRef=\"ServiceTask_1hzhb3p\" targetRef=\"TextAnnotation_1lsup12\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0kf69sl\"\u003e\u003ctext\u003eDetermine if any policies attached to user. Update workflow result.\n\u00a0Username is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1rosae2\" sourceRef=\"ServiceTask_0fudggi\" targetRef=\"TextAnnotation_0kf69sl\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1nrl0ze\"\u003e\u003ctext\u003eDetach (managed) or delete (in-line) all policies for user. Update data table row for user policies.\n\u00a0 Username is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0cgzuy2\" sourceRef=\"ServiceTask_0tw2w9u\" targetRef=\"TextAnnotation_1nrl0ze\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0e8o6m0\"\u003e\u003ctext\u003eDetermine if\u00a0 user is a member of any groups. Update workflow result.\nUsername is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ojlrh3\" sourceRef=\"ServiceTask_0logngp\" targetRef=\"TextAnnotation_0e8o6m0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_05w5ivy\"\u003e\u003ctext\u003eRemove user from all groups. Update data table row for user groups.\nUsername is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1mola69\" sourceRef=\"ServiceTask_17vw09q\" targetRef=\"TextAnnotation_05w5ivy\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_16k5i43\"\u003e\u003ctext\u003eRemove user. Set data table row \"Status\" field to \"Deleted\".\n\u00a0Username is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0rpgbfd\" sourceRef=\"ServiceTask_0dk9bos\" targetRef=\"TextAnnotation_16k5i43\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_14857iu\"\u003e\u003ctext\u003eDelete ssh public keys for user.\nUsername is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_18g2asq\" sourceRef=\"ServiceTask_0y2v3g3\" targetRef=\"TextAnnotation_14857iu\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0dqyx79\"\u003e\u003ctext\u003eDetermine if\u00a0 user has any service-specific credentials. Update workflow result.\nUsername is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_11h8o5d\" sourceRef=\"ServiceTask_1sgmi99\" targetRef=\"TextAnnotation_0dqyx79\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0emdyjs\"\u003e\u003ctext\u003eDelete service specific credentials for user.\nUsername is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1al869u\" sourceRef=\"ServiceTask_0j2b73x\" targetRef=\"TextAnnotation_0emdyjs\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_11zvps9\"\u003e\u003ctext\u003eDetermine if\u00a0 user has any signing certificates. Update workflow result.\nUsername is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0u27wvv\" sourceRef=\"ServiceTask_0wb3a6o\" targetRef=\"TextAnnotation_11zvps9\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_05r56ww\"\u003e\u003ctext\u003eDelete signing certificates for user.\nUsername is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1uk4zt2\" sourceRef=\"ServiceTask_1dn9z35\" targetRef=\"TextAnnotation_05r56ww\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1rlgubg\"\u003e\u003ctext\u003eDetermine if\u00a0 user has any MFA devices and which are virtual. Update workflow result.\nUsername is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1vyroir\" sourceRef=\"ServiceTask_1d33ieu\" targetRef=\"TextAnnotation_1rlgubg\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_12v4unb\"\u003e\u003ctext\u003eDe-activate virtual MFA devices for user.\nUsername is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_0eqcuko\" sourceRef=\"ServiceTask_0fkvwlu\" targetRef=\"TextAnnotation_12v4unb\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ektof0\"\u003e\u003ctext\u003eDelete virtual MFA devices for user.\nUsername is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1fiuewu\" sourceRef=\"ServiceTask_0cxgrrf\" targetRef=\"TextAnnotation_1ektof0\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0mi8n0i\"\u003e\u003ctext\u003eDetermine ssh public keys for user. Update workflow result.\nUsername is assigned from an artifact value.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_07pgk15\" sourceRef=\"ServiceTask_1mccj8q\" targetRef=\"TextAnnotation_0mi8n0i\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"123\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"118\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"49\" y=\"253\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"129\" y=\"219\"/\u003e\u003comgdi:waypoint x=\"114\" y=\"243\"/\u003e\u003comgdi:waypoint x=\"107\" y=\"253\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1khyagr\" id=\"ServiceTask_1khyagr_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"185\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1vcyete\" id=\"SequenceFlow_1vcyete_di\"\u003e\u003comgdi:waypoint x=\"159\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"185\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"127\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_08q7k8k\" id=\"ExclusiveGateway_08q7k8k_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"346\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"371\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08c963g\" id=\"SequenceFlow_08c963g_di\"\u003e\u003comgdi:waypoint x=\"285\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"346\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"315.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_13jlzao\" id=\"ExclusiveGateway_13jlzao_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"465\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"490\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0vv91su\" id=\"SequenceFlow_0vv91su_di\"\u003e\u003comgdi:waypoint x=\"396\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"465\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"60\" x=\"401\" y=\"185\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0cudkvl\" id=\"ExclusiveGateway_0cudkvl_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"573\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"598\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_09pioh6\" id=\"SequenceFlow_09pioh6_di\"\u003e\u003comgdi:waypoint x=\"515\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"573\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"69\" x=\"509\" y=\"165\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_0opl7i1\" id=\"EndEvent_0opl7i1_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"4719\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"4692\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1qmdyjx\" id=\"SequenceFlow_1qmdyjx_di\"\u003e\u003comgdi:waypoint x=\"371\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"371\" y=\"359\"/\u003e\u003comgdi:waypoint x=\"4737\" y=\"359\"/\u003e\u003comgdi:waypoint x=\"4737\" y=\"224\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"67\" x=\"2524\" y=\"338\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08dlm5e\" id=\"SequenceFlow_08dlm5e_di\"\u003e\u003comgdi:waypoint x=\"490\" y=\"231\"/\u003e\u003comgdi:waypoint x=\"490\" y=\"314\"/\u003e\u003comgdi:waypoint x=\"4737\" y=\"314\"/\u003e\u003comgdi:waypoint x=\"4737\" y=\"224\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"75\" x=\"455\" y=\"266\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0e1bj00\" id=\"ServiceTask_0e1bj00_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"681\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1cvgahq\" id=\"SequenceFlow_1cvgahq_di\"\u003e\u003comgdi:waypoint x=\"623\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"681\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"61\" x=\"624\" y=\"165\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1n1bl4y\" id=\"ServiceTask_1n1bl4y_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"886\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fp5atw\" id=\"SequenceFlow_0fp5atw_di\"\u003e\u003comgdi:waypoint x=\"781\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"886\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"788.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_08nnle9\" id=\"SequenceFlow_08nnle9_di\"\u003e\u003comgdi:waypoint x=\"598\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"598\" y=\"100\"/\u003e\u003comgdi:waypoint x=\"936\" y=\"100\"/\u003e\u003comgdi:waypoint x=\"936\" y=\"166\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"79\" x=\"728\" y=\"79\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0lfuuy8\" id=\"ExclusiveGateway_0lfuuy8_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"1050\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1030\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0b1w6zu\" id=\"SequenceFlow_0b1w6zu_di\"\u003e\u003comgdi:waypoint x=\"986\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1050\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"973\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1hzhb3p\" id=\"ServiceTask_1hzhb3p_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"1187\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11a6hxl\" id=\"SequenceFlow_11a6hxl_di\"\u003e\u003comgdi:waypoint x=\"1100\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1187\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"14\" width=\"89\" x=\"1096\" y=\"187\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0fudggi\" id=\"ServiceTask_0fudggi_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"1411\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1xhovti\" id=\"SequenceFlow_1xhovti_di\"\u003e\u003comgdi:waypoint x=\"1287\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1411\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1304\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fbb8nd\" id=\"SequenceFlow_0fbb8nd_di\"\u003e\u003comgdi:waypoint x=\"1075\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"1075\" y=\"100\"/\u003e\u003comgdi:waypoint x=\"1461\" y=\"100\"/\u003e\u003comgdi:waypoint x=\"1461\" y=\"166\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"70\" x=\"1234\" y=\"79\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_064jb3p\" id=\"ExclusiveGateway_064jb3p_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"1559\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1539\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1buspu6\" id=\"SequenceFlow_1buspu6_di\"\u003e\u003comgdi:waypoint x=\"1511\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1559\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1490\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0tw2w9u\" id=\"ServiceTask_0tw2w9u_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"1730\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0hfhx0n\" id=\"SequenceFlow_0hfhx0n_di\"\u003e\u003comgdi:waypoint x=\"1609\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1730\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"70\" x=\"1638\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0logngp\" id=\"ServiceTask_0logngp_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"1962\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1n26lsr\" id=\"SequenceFlow_1n26lsr_di\"\u003e\u003comgdi:waypoint x=\"1830\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"1962\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"1851\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1k3cbi4\" id=\"SequenceFlow_1k3cbi4_di\"\u003e\u003comgdi:waypoint x=\"1584\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"1584\" y=\"96\"/\u003e\u003comgdi:waypoint x=\"2012\" y=\"96\"/\u003e\u003comgdi:waypoint x=\"2012\" y=\"166\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"88\" x=\"1755\" y=\"75\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0f9j4hk\" id=\"ExclusiveGateway_0f9j4hk_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"2093\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"2073\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_13e8y9v\" id=\"SequenceFlow_13e8y9v_di\"\u003e\u003comgdi:waypoint x=\"2062\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"2093\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"2032.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_17vw09q\" id=\"ServiceTask_17vw09q_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"2233\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0uhexmc\" id=\"SequenceFlow_0uhexmc_di\"\u003e\u003comgdi:waypoint x=\"2143\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"2233\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"54\" x=\"2157\" y=\"171\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0dk9bos\" id=\"ServiceTask_0dk9bos_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"4533\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_11q5lkh\" id=\"SequenceFlow_11q5lkh_di\"\u003e\u003comgdi:waypoint x=\"4633\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"4719\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"4631\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0fnwhv2\" id=\"SequenceFlow_0fnwhv2_di\"\u003e\u003comgdi:waypoint x=\"2118\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"2118\" y=\"99\"/\u003e\u003comgdi:waypoint x=\"2442\" y=\"99\"/\u003e\u003comgdi:waypoint x=\"2442\" y=\"157\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"73\" x=\"2244\" y=\"78\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kmg6ls\" id=\"TextAnnotation_1kmg6ls_di\"\u003e\u003comgdc:Bounds height=\"79\" width=\"191\" x=\"137\" y=\"31\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_180o2zs\" id=\"Association_180o2zs_di\"\u003e\u003comgdi:waypoint x=\"234\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"234\" y=\"110\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_102jwbz\" id=\"TextAnnotation_102jwbz_di\"\u003e\u003comgdc:Bounds height=\"54\" width=\"209\" x=\"626\" y=\"7\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_19au57w\" id=\"Association_19au57w_di\"\u003e\u003comgdi:waypoint x=\"731\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"731\" y=\"61\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0qshsw7\" id=\"TextAnnotation_0qshsw7_di\"\u003e\u003comgdc:Bounds height=\"39\" width=\"180\" x=\"846\" y=\"14\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_17b6nsq\" id=\"Association_17b6nsq_di\"\u003e\u003comgdi:waypoint x=\"936\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"937\" y=\"53\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1lsup12\" id=\"TextAnnotation_1lsup12_di\"\u003e\u003comgdc:Bounds height=\"48\" width=\"228\" x=\"1123\" y=\"10\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1d67hdx\" id=\"Association_1d67hdx_di\"\u003e\u003comgdi:waypoint x=\"1237\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"1238\" y=\"58\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0kf69sl\" id=\"TextAnnotation_0kf69sl_di\"\u003e\u003comgdc:Bounds height=\"57\" width=\"213\" x=\"1354\" y=\"5\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1rosae2\" id=\"Association_1rosae2_di\"\u003e\u003comgdi:waypoint x=\"1461\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"1461\" y=\"62\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1nrl0ze\" id=\"TextAnnotation_1nrl0ze_di\"\u003e\u003comgdc:Bounds height=\"56\" width=\"246\" x=\"1657\" y=\"6\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0cgzuy2\" id=\"Association_0cgzuy2_di\"\u003e\u003comgdi:waypoint x=\"1780\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"1780\" y=\"62\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0e8o6m0\" id=\"TextAnnotation_0e8o6m0_di\"\u003e\u003comgdc:Bounds height=\"52\" width=\"242\" x=\"1907\" y=\"-1\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ojlrh3\" id=\"Association_1ojlrh3_di\"\u003e\u003comgdi:waypoint x=\"2012\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"2012\" y=\"51\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_05w5ivy\" id=\"TextAnnotation_05w5ivy_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"261\" x=\"2152\" y=\"-9\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1mola69\" id=\"Association_1mola69_di\"\u003e\u003comgdi:waypoint x=\"2283\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"2283\" y=\"42\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_16k5i43\" id=\"TextAnnotation_16k5i43_di\"\u003e\u003comgdc:Bounds height=\"66\" width=\"256\" x=\"4535\" y=\"7\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0rpgbfd\" id=\"Association_0rpgbfd_di\"\u003e\u003comgdi:waypoint x=\"4578\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"4642\" y=\"73\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1mccj8q\" id=\"ServiceTask_1mccj8q_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"2392\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0q3qxox\" id=\"SequenceFlow_0q3qxox_di\"\u003e\u003comgdi:waypoint x=\"2333\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"2392\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"2362.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1i3oeih\" id=\"ExclusiveGateway_1i3oeih_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"2545\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"2570\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_12h0te8\" id=\"SequenceFlow_12h0te8_di\"\u003e\u003comgdi:waypoint x=\"2492\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"2545\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"2518.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0y2v3g3\" id=\"ServiceTask_0y2v3g3_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"2669\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1206qiz\" id=\"SequenceFlow_1206qiz_di\"\u003e\u003comgdi:waypoint x=\"2595\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"2669\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"75\" x=\"2600\" y=\"168\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_06e1mhe\" id=\"SequenceFlow_06e1mhe_di\"\u003e\u003comgdi:waypoint x=\"2570\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"2570\" y=\"99\"/\u003e\u003comgdi:waypoint x=\"2955\" y=\"99\"/\u003e\u003comgdi:waypoint x=\"2955\" y=\"166\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"40\" width=\"87\" x=\"2720\" y=\"78\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1sgmi99\" id=\"ServiceTask_1sgmi99_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"2905\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0l3v69q\" id=\"SequenceFlow_0l3v69q_di\"\u003e\u003comgdi:waypoint x=\"2769\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"2905\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"2792\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1bgxyws\" id=\"ExclusiveGateway_1bgxyws_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"3035\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3015\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0cghy2n\" id=\"SequenceFlow_0cghy2n_di\"\u003e\u003comgdi:waypoint x=\"3005\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"3035\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"2975\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0j2b73x\" id=\"ServiceTask_0j2b73x_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"3167\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0kpv5qx\" id=\"SequenceFlow_0kpv5qx_di\"\u003e\u003comgdi:waypoint x=\"3085\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"3167\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"40\" width=\"88\" x=\"3080\" y=\"154\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_02g7g9j\" id=\"SequenceFlow_02g7g9j_di\"\u003e\u003comgdi:waypoint x=\"3060\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"3060\" y=\"106\"/\u003e\u003comgdi:waypoint x=\"3372\" y=\"106\"/\u003e\u003comgdi:waypoint x=\"3372\" y=\"166\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"53\" width=\"67\" x=\"3198\" y=\"96\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0wb3a6o\" id=\"ServiceTask_0wb3a6o_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"3322\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0krx7f7\" id=\"SequenceFlow_0krx7f7_di\"\u003e\u003comgdi:waypoint x=\"3267\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"3322\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3249.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0srueur\" id=\"ExclusiveGateway_0srueur_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"3468\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3448\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1y5642u\" id=\"SequenceFlow_1y5642u_di\"\u003e\u003comgdi:waypoint x=\"3422\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"3468\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3400\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1dn9z35\" id=\"ServiceTask_1dn9z35_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"3615\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0f07hag\" id=\"SequenceFlow_0f07hag_di\"\u003e\u003comgdi:waypoint x=\"3518\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"3615\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"88\" x=\"3526\" y=\"169\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0953ew2\" id=\"SequenceFlow_0953ew2_di\"\u003e\u003comgdi:waypoint x=\"3493\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"3493\" y=\"106\"/\u003e\u003comgdi:waypoint x=\"3816\" y=\"106\"/\u003e\u003comgdi:waypoint x=\"3816\" y=\"166\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"40\" width=\"67\" x=\"3622\" y=\"85\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1d33ieu\" id=\"ServiceTask_1d33ieu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"3766\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0no9ecs\" id=\"SequenceFlow_0no9ecs_di\"\u003e\u003comgdi:waypoint x=\"3715\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"3766\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3695.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_1nizxai\" id=\"ExclusiveGateway_1nizxai_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"3913\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3893\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0c22kfv\" id=\"SequenceFlow_0c22kfv_di\"\u003e\u003comgdi:waypoint x=\"3866\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"3913\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"3844.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0fkvwlu\" id=\"ServiceTask_0fkvwlu_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"4052\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1b3itqq\" id=\"SequenceFlow_1b3itqq_di\"\u003e\u003comgdi:waypoint x=\"3963\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"4052\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"40\" width=\"71\" x=\"3968\" y=\"159\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0r12hry\" id=\"SequenceFlow_0r12hry_di\"\u003e\u003comgdi:waypoint x=\"3938\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"3938\" y=\"104\"/\u003e\u003comgdi:waypoint x=\"4580\" y=\"104\"/\u003e\u003comgdi:waypoint x=\"4580\" y=\"166\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"40\" width=\"77\" x=\"4221\" y=\"83\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ExclusiveGateway_0r4px7c\" id=\"ExclusiveGateway_0r4px7c_di\" isMarkerVisible=\"true\"\u003e\u003comgdc:Bounds height=\"50\" width=\"50\" x=\"4199\" y=\"181\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"4179\" y=\"234\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_14ei8hm\" id=\"SequenceFlow_14ei8hm_di\"\u003e\u003comgdi:waypoint x=\"4152\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"4199\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"4130.5\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0cxgrrf\" id=\"ServiceTask_0cxgrrf_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"4355\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0ps0kve\" id=\"SequenceFlow_0ps0kve_di\"\u003e\u003comgdi:waypoint x=\"4249\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"4355\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"86\" x=\"4255\" y=\"163\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_10r7rg5\" id=\"SequenceFlow_10r7rg5_di\"\u003e\u003comgdi:waypoint x=\"4224\" y=\"181\"/\u003e\u003comgdi:waypoint x=\"4224\" y=\"132\"/\u003e\u003comgdi:waypoint x=\"4558\" y=\"132\"/\u003e\u003comgdi:waypoint x=\"4558\" y=\"166\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"27\" width=\"86\" x=\"4349\" y=\"111\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0757cr2\" id=\"SequenceFlow_0757cr2_di\"\u003e\u003comgdi:waypoint x=\"4455\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"4533\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"4449\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_14857iu\" id=\"TextAnnotation_14857iu_di\"\u003e\u003comgdc:Bounds height=\"45\" width=\"258\" x=\"2579\" y=\"2\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_18g2asq\" id=\"Association_18g2asq_di\"\u003e\u003comgdi:waypoint x=\"2717\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"2709\" y=\"47\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0dqyx79\" id=\"TextAnnotation_0dqyx79_di\"\u003e\u003comgdc:Bounds height=\"57\" width=\"227\" x=\"2841\" y=\"-4\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_11h8o5d\" id=\"Association_11h8o5d_di\"\u003e\u003comgdi:waypoint x=\"2955\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"2955\" y=\"53\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0emdyjs\" id=\"TextAnnotation_0emdyjs_di\"\u003e\u003comgdc:Bounds height=\"74\" width=\"148\" x=\"3091\" y=\"-3\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1al869u\" id=\"Association_1al869u_di\"\u003e\u003comgdi:waypoint x=\"3205\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"3177\" y=\"71\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_11zvps9\" id=\"TextAnnotation_11zvps9_di\"\u003e\u003comgdc:Bounds height=\"69\" width=\"185\" x=\"3279\" y=\"-1\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0u27wvv\" id=\"Association_0u27wvv_di\"\u003e\u003comgdi:waypoint x=\"3372\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"3372\" y=\"68\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_05r56ww\" id=\"TextAnnotation_05r56ww_di\"\u003e\u003comgdc:Bounds height=\"70\" width=\"169\" x=\"3485\" y=\"-1\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1uk4zt2\" id=\"Association_1uk4zt2_di\"\u003e\u003comgdi:waypoint x=\"3643\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"3589\" y=\"69\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1rlgubg\" id=\"TextAnnotation_1rlgubg_di\"\u003e\u003comgdc:Bounds height=\"69\" width=\"237\" x=\"3697\" y=\"-1\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1vyroir\" id=\"Association_1vyroir_di\"\u003e\u003comgdi:waypoint x=\"3816\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"3816\" y=\"68\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_12v4unb\" id=\"TextAnnotation_12v4unb_di\"\u003e\u003comgdc:Bounds height=\"51\" width=\"119\" x=\"4042\" y=\"14\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_0eqcuko\" id=\"Association_0eqcuko_di\"\u003e\u003comgdi:waypoint x=\"4102\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"4102\" y=\"65\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ektof0\" id=\"TextAnnotation_1ektof0_di\"\u003e\u003comgdc:Bounds height=\"60\" width=\"126\" x=\"4342\" y=\"10\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1fiuewu\" id=\"Association_1fiuewu_di\"\u003e\u003comgdi:waypoint x=\"4405\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"4405\" y=\"70\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0mi8n0i\" id=\"TextAnnotation_0mi8n0i_di\"\u003e\u003comgdc:Bounds height=\"72\" width=\"161\" x=\"2401\" y=\"-11\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_07pgk15\" id=\"Association_07pgk15_di\"\u003e\u003comgdi:waypoint x=\"2451\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"2474\" y=\"61\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 22,
      "description": "Delete the selected IAM user. The User is assigned from an artifact value for an artifact of type \"AWS IAM User Name\". The artifact description will be updated  on successful user deletion.\n\nNote: Unlike the AWS Management Console, when you delete a user programmatically, you must delete the items attached to the user or the deletion fails. Before attempting to delete a user, the following items if associated with the user will be removed, de-activated or deleted.:\n\n    Password ( DeleteLoginProfile )\n    Access keys ( DeleteAccessKey )\n    Inline policies ( DeleteUserPolicy )\n    Attached managed policies ( DetachUserPolicy ) \n    Group memberships ( RemoveUserFromGroup )\n    Signing certificate ( DeleteSigningCertificate )\n    SSH public key ( DeleteSSHPublicKey )\n    Git credentials ( DeleteServiceSpecificCredential )\n    Multi-factor authentication (MFA) device ( DeactivateMFADevice , DeleteVirtualMFADevice )",
      "export_key": "wf_aws_iam_delete_user_for_artifact",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719810669346,
      "name": "Example: AWS IAM: Delete User For Artifact",
      "object_type": "artifact",
      "programmatic_name": "wf_aws_iam_delete_user_for_artifact",
      "tags": [],
      "uuid": "4b76c62f-ad40-4d30-8263-1c4d5b662b34",
      "workflow_id": 10
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "wf_aws_iam_list_access_keys",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_list_access_keys\" isExecutable=\"true\" name=\"Example: AWS IAM: List Access Keys\"\u003e\u003cdocumentation\u003eGet the IAM access keys for all users in the AWS account.  Access keys can be filtered by user name and access key id. New rows will be created in the data table \u0027AWS IAM Access Keys\u0027  for all keys found based on the filtering criteria.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_0rp2yc4\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_1uqgo1o\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\\n            \u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n            \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User\u0027, \u0027CreateDate\u0027: \u00272019-11-05 15:54:43\u0027},\\n                        {\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_User_2\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                         \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_User_2\u0027,\\n                         \u0027CreateDate\u0027: \u00272019-10-31 16:23:07\u0027, \u0027PasswordLastUsed\u0027: \u00272019-11-12 10:55:42\u0027}\\n                       ],\\n            \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User\\\", \\\"CreateDate\\\": \\\"2019-11-05 15:54:43\\\"}, {\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_User_2\\\", \\\"UserId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_User_2\\\", \\\"CreateDate\\\": \\\"2019-10-31 16:23:07\\\"}]\u0027,\\n            \u0027inputs\u0027: {},\\n            \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027,\\n                        \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 7951,\\n                        \u0027timestamp\u0027: \u00272019-11-14 13:48:30\u0027\\n                       }\\n}\\n\\n\\\"\\\"\\\"\\n#  Globals\\nimport re\\n# List of fields in datatable fn_aws_iam_list_users script main\\nDATA_TBL_FIELDS = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"AccessKeyId\\\", \\\"CreateDate\\\", \\\"Status\\\", \\\"DefaultKey\\\"]\\n# List of fields in datatable fn_aws_iam_list_users script last used access keys.\\nDATA_TBL_FIELDS_LUAK = [\\\"LastUsedDate\\\", \\\"ServiceName\\\", \\\"Region\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"List Access Keys\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\n\\ndef process_access_keys(access_key_id_list, user_name):\\n    access_key_ids = []\\n    for ak_id in access_key_id_list:\\n        newrow = incident.addRow(\\\"aws_iam_access_keys\\\")\\n        newrow.query_execution_date = QUERY_EXECUTION_DATE\\n        newrow.UserName = user_name\\n        for f in DATA_TBL_FIELDS[2:]:\\n            if ak_id[f] is not None:\\n                newrow[f] = ak_id[f]\\n        # Add key last used data if it exists.\\n        if ak_id[\\\"key_last_used\\\"] is not None:\\n            luak = ak_id[\\\"key_last_used\\\"]\\n            for l in DATA_TBL_FIELDS_LUAK:\\n                if luak[l] is not None:\\n                    newrow[l] = luak[l]\\ndef main():\\n    note_text = u\u0027\u0027\\n    filters = [f for f in [INPUTS[\\\"aws_iam_user_filter\\\"], INPUTS[\\\"aws_iam_group_filter\\\"],\\n                           INPUTS[\\\"aws_iam_policy_filter\\\"], INPUTS[\\\"aws_iam_access_key_filter\\\"]]\\n               if f is not None]\\n    if CONTENT:\\n        key_count = 0\\n        for u in CONTENT:\\n           if u[\\\"AccessKeyIds\\\"]:\\n                for k in  u[\\\"AccessKeyIds\\\"]:\\n                    key_count += 1\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; access keys(s) returned for Resilient function \\\" \\\\\\n                   \\\"\u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, key_count, FN_NAME)\\n        note_text += \\\"\u0026lt;br\u0026gt;Adding new rows to data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; for \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; access keys(s).\u0026lt;/br\u0026gt;\\\".format(\\\"AWS IAM Access Keys\\\", key_count)\\n        for u in CONTENT:\\n           if u[\\\"AccessKeyIds\\\"]:\\n                user_name = u[\\\"UserName\\\"]\\n                process_access_keys(u[\\\"AccessKeyIds\\\"], user_name)\\n\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned for Resilient function \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    if filters:\\n        note_text += \\\"\u0026lt;br\u0026gt;Query Filters:\u0026lt;/br\u0026gt;\\\"\\n        if INPUTS.get(\\\"aws_iam_user_filter\\\"):\\n            note_text += u\\\"\u0026lt;br\u0026gt;aws_iam_user_filter: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\".format(INPUTS[\\\"aws_iam_user_filter\\\"])\\n        if INPUTS.get(\\\"aws_iam_access_key_filter\\\"):\\n            note_text += u\\\"\u0026lt;br\u0026gt;aws_iam_access_key_filter: \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;\u0026lt;/br\u0026gt;\\\".format(INPUTS[\\\"aws_iam_access_key_filter\\\"])\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_access_key_filter = rule.properties.aws_iam_access_key_filter\\ninputs.aws_iam_user_filter = rule.properties.aws_iam_user_filter\\ninputs.aws_iam_query_type = \\\"access_keys\\\"\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_0rp2yc4\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0os8yk2\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_0rp2yc4\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_1uqgo1o\"/\u003e\u003cendEvent id=\"EndEvent_01vdhx8\"\u003e\u003cincoming\u003eSequenceFlow_0os8yk2\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0os8yk2\" sourceRef=\"ServiceTask_1uqgo1o\" targetRef=\"EndEvent_01vdhx8\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1qc7rx8\"\u003e\u003ctext\u003eList all users to\u00a0 determine all access key ids for all users.\u00a0Create row in data table \"AWS IAM Access Keys\" for each access key.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1b3y3tu\" sourceRef=\"ServiceTask_1uqgo1o\" targetRef=\"TextAnnotation_1qc7rx8\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1uqgo1o\" id=\"ServiceTask_1uqgo1o_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"236\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0rp2yc4\" id=\"SequenceFlow_0rp2yc4_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"236\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"217\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_01vdhx8\" id=\"EndEvent_01vdhx8_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"371\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"389\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0os8yk2\" id=\"SequenceFlow_0os8yk2_di\"\u003e\u003comgdi:waypoint x=\"336\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"371\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"353.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1qc7rx8\" id=\"TextAnnotation_1qc7rx8_di\"\u003e\u003comgdc:Bounds height=\"78\" width=\"247\" x=\"162\" y=\"33\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1b3y3tu\" id=\"Association_1b3y3tu_di\"\u003e\u003comgdi:waypoint x=\"286\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"286\" y=\"111\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Get the IAM access keys for all users in the AWS account.  Access keys can be filtered by user name and access key id. New rows will be created in the data table \u0027AWS IAM Access Keys\u0027  for all keys found based on the filtering criteria.",
      "export_key": "wf_aws_iam_list_access_keys",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719374543306,
      "name": "Example: AWS IAM: List Access Keys",
      "object_type": "incident",
      "programmatic_name": "wf_aws_iam_list_access_keys",
      "tags": [],
      "uuid": "4bb62010-a035-4825-bed1-c760a226a5d0",
      "workflow_id": 2
    },
    {
      "actions": [],
      "content": {
        "version": 3,
        "workflow_id": "wf_aws_iam_get_access_key_for_artifact",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_get_access_key_for_artifact\" isExecutable=\"true\" name=\"Example: AWS IAM: Get Access Key For Artifact\"\u003e\u003cdocumentation\u003eGet the IAM access keys for all users in the AWS account and filter by access key id specified by the artifact value. A new row will be created in the data table \u0027AWS IAM Access Keys\u0027 if a matching key is found.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_1o0jpb6\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0imi8c0\" name=\"AWS IAM: List Users\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"7991e057-a564-424d-a6b9-ba806cc549b0\"\u003e{\"inputs\":{\"136e1156-7875-4314-ad4a-729b5026c5ce\":{\"input_type\":\"static\",\"static_input\":{\"multiselect_value\":[],\"select_value\":\"e85f91d4-3011-4878-950f-a9b96217d3f6\"}}},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_users script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None,\\n         \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027UserId\u0027: \u0027ABCDEFG\u0027,\\n                      \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:user/iam_test_user\u0027, \u0027CreateDate\u0027: \u00272019-11-18 18:11:33\u0027,\\n                      \u0027LoginProfileExists\u0027: \u0027No\u0027,\\n                      \u0027Groups\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027GroupName\u0027: \u0027group\u0027, \u0027GroupId\u0027: \u0027ABCDEFG\u0027,\\n                                  \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:group/group\u0027, \u0027CreateDate\u0027: \u00272019-11-29 15:49:34\u0027}],\\n                      \u0027AccessKeyIds\u0027: [{\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027,\\n                                        \u0027Status\u0027: \u0027Active\u0027, \u0027CreateDate\u0027: \u00272019-12-10 14:20:19\u0027},\\n                                       {\u0027UserName\u0027: \u0027iam_test_user\u0027, \u0027AccessKeyId\u0027: \u0027ABCDEFG\u0027,\\n                                        \u0027Status\u0027: \u0027Active\u0027, \u0027CreateDate\u0027: \u00272020-01-07 17:10:19\u0027}]}],\\n         \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"UserName\\\": \\\"iam_test_user\\\", \\\"UserId\\\": \\\"ABCDEFGH\\\", \u0027\\n                \u0027\\\"Arn\\\": \\\"arn:aws:iam::123456789123:user/iam_test_user\\\", \\\"CreateDate\\\": \\\"2019-11-18 18:11:33\\\", \\\"LoginProfileExists\\\": \\\"No\\\", \u0027\\n                \u0027\\\"Groups\\\": [{\\\"Path\\\": \\\"/\\\", \\\"GroupName\\\": \\\"group\\\", \\\"GroupId\\\": \\\"ABCDEFG\\\", \\\"Arn\\\": \\\"arn:aws:iam::123456789123:group/group\\\", \u0027\\n                \u0027\\\"CreateDate\\\": \\\"2019-11-29 15:49:34\\\"}], \\\"AccessKeyIds\\\": [{\\\"UserName\\\": \\\"iam_test_user\\\", \\\"AccessKeyId\\\": \\\"ABCDEFG\\\", \u0027\\n                \u0027\\\"Status\\\": \\\"Active\\\", \\\"CreateDate\\\": \\\"2019-12-10 14:20:19\\\"}, {\\\"UserName\\\": \\\"iam_test_user\\\", \\\"AccessKeyId\\\": \\\"ABCDEFG\\\", \u0027\\n                \u0027\\\"Status\\\": \\\"Active\\\", \\\"CreateDate\\\": \\\"2020-01-07 17:10:19\\\"}]}]\u0027,\\n         \u0027inputs\u0027: {\u0027aws_iam_access_key_filter\u0027: \u0027ABCDEFG\u0027},\\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ibm.com\u0027,\\n                     \u0027execution_time_ms\u0027: 6222, \u0027timestamp\u0027: \u00272020-01-13 14:54:50\u0027}\\n         }\\n}\\n\\n\\\"\\\"\\\"\\n#  Globals\\nimport re\\n# List of fields in datatable fn_aws_iam_list_users script main\\nDATA_TBL_FIELDS = [\\\"query_execution_time\\\", \\\"UserName\\\", \\\"AccessKeyId\\\", \\\"CreateDate\\\", \\\"Status\\\", \\\"DefaultKey\\\"]\\n# List of fields in datatable fn_aws_iam_list_users script last used access keys.\\nDATA_TBL_FIELDS_LUAK = [\\\"LastUsedDate\\\", \\\"ServiceName\\\", \\\"Region\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_users\\\"\\nWF_NAME = \\\"Get access Key For Artifact\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef process_access_keys(access_key_id_list, user_name):\\n    access_key_ids = []\\n    for ak_id in access_key_id_list:\\n        newrow = incident.addRow(\\\"aws_iam_access_keys\\\")\\n        newrow.query_execution_date = QUERY_EXECUTION_DATE\\n        newrow.UserName = user_name\\n        for f in DATA_TBL_FIELDS[2:]:\\n            if ak_id[f] is not None:\\n                newrow[f] = ak_id[f]\\n        # Add key last used data if it exists.\\n        if ak_id[\\\"key_last_used\\\"] is not None:\\n            luak = ak_id[\\\"key_last_used\\\"]\\n            for l in DATA_TBL_FIELDS_LUAK:\\n                if luak[l] is not None:\\n                    newrow[l] = luak[l]\\n\\n\\ndef main():\\n    note_text = u\u0027\u0027\\n    if CONTENT:\\n        if len(CONTENT) == 1:\\n            note_text = u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; results returned for access \\\" \\\\\\n                        \\\"key(s) matching \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;  for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_access_key_filter\\\"], FN_NAME)\\n            u = CONTENT.pop()\\n            if u[\\\"AccessKeyIds\\\"] is not None:\\n                user_name = u[\\\"UserName\\\"]\\n                process_access_keys(u[\\\"AccessKeyIds\\\"], user_name)\\n        else:\\n            note_text = u\\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: Too many results \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; returned for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for \\\" \\\\\\n                        u\\\"Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\".format(WF_NAME, len(CONTENT), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += u\\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There were \u0026lt;b\u0026gt;no\u0026lt;/b\u0026gt; results returned returned for access key \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \\\" \\\\\\n                     u\\\"for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_access_key_filter\\\"], FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_access_key_filter = artifact.value\\ninputs.aws_iam_query_type = \\\"access_keys\\\"\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1o0jpb6\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_0g6k4yb\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1o0jpb6\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0imi8c0\"/\u003e\u003cendEvent id=\"EndEvent_1yt60tf\"\u003e\u003cincoming\u003eSequenceFlow_0g6k4yb\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_0g6k4yb\" sourceRef=\"ServiceTask_0imi8c0\" targetRef=\"EndEvent_1yt60tf\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1db3r06\"\u003e\u003ctext\u003eList all users to\u00a0 determine if access key\u00a0 exists for a user. Access key id filter assigned from an artifact value. Add new row to data table\u00a0 \"AWS IAM Access Keys\" for access key id.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1qgisvi\" sourceRef=\"ServiceTask_0imi8c0\" targetRef=\"TextAnnotation_1db3r06\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0imi8c0\" id=\"ServiceTask_0imi8c0_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"230\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1o0jpb6\" id=\"SequenceFlow_1o0jpb6_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"230\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"214\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1yt60tf\" id=\"EndEvent_1yt60tf_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"364\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"382\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_0g6k4yb\" id=\"SequenceFlow_0g6k4yb_di\"\u003e\u003comgdi:waypoint x=\"330\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"364\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"347\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1db3r06\" id=\"TextAnnotation_1db3r06_di\"\u003e\u003comgdc:Bounds height=\"87\" width=\"278\" x=\"141\" y=\"19\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1qgisvi\" id=\"Association_1qgisvi_di\"\u003e\u003comgdi:waypoint x=\"281\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"281\" y=\"106\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 3,
      "description": "Get the IAM access keys for all users in the AWS account and filter by access key id specified by the artifact value. A new row will be created in the data table \u0027AWS IAM Access Keys\u0027 if a matching key is found.",
      "export_key": "wf_aws_iam_get_access_key_for_artifact",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719374267617,
      "name": "Example: AWS IAM: Get Access Key For Artifact",
      "object_type": "artifact",
      "programmatic_name": "wf_aws_iam_get_access_key_for_artifact",
      "tags": [],
      "uuid": "315f2dc0-afec-48c3-9c96-c322394920da",
      "workflow_id": 15
    },
    {
      "actions": [],
      "content": {
        "version": 4,
        "workflow_id": "wf_aws_iam_add_user_to_group",
        "xml": "\u003c?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?\u003e\u003cdefinitions xmlns=\"http://www.omg.org/spec/BPMN/20100524/MODEL\" xmlns:bpmndi=\"http://www.omg.org/spec/BPMN/20100524/DI\" xmlns:omgdc=\"http://www.omg.org/spec/DD/20100524/DC\" xmlns:omgdi=\"http://www.omg.org/spec/DD/20100524/DI\" xmlns:resilient=\"http://resilient.ibm.com/bpmn\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" targetNamespace=\"http://www.camunda.org/test\"\u003e\u003cprocess id=\"wf_aws_iam_add_user_to_group\" isExecutable=\"true\" name=\"Example: AWS IAM: Add User To Group\"\u003e\u003cdocumentation\u003eAdd an IAM user to an IAM group. The user is assigned from a field in the selected data table row. A group name is assigned from an activity field drop-down list.  The data table row will be refreshed with updated group values for the selected user.\u003c/documentation\u003e\u003cstartEvent id=\"StartEvent_155asxm\"\u003e\u003coutgoing\u003eSequenceFlow_005w2go\u003c/outgoing\u003e\u003c/startEvent\u003e\u003cserviceTask id=\"ServiceTask_0l8gfqa\" name=\"AWS IAM: Add User To Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"f460bc26-ba06-4180-9d5e-fb6de5646f42\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_add_user_to_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n         \u0027content\u0027: [{\u0027GroupName\u0027: \u0027denyall_group\u0027, \u0027Status\u0027: \u0027OK\u0027}], \\n         \u0027raw\u0027: \u0027[{\\\"GroupName\\\": \\\"denyall_group\\\", \\\"Status\\\": \\\"OK\\\"}]\u0027, \\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user_1\u0027, \u0027aws_iam_group_names\u0027: \u0027denyall_group\u0027}, \\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \\n                     \u0027host\u0027: \u0027myhost.ibm.com\u0027, \u0027execution_time_ms\u0027: 4303, \u0027timestamp\u0027: \u00272020-03-16 15:43:17\u0027\\n           \\n        }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable for fn_aws_iam_add_user_to_groups  script\\nDATA_TBL_FIELDS = [\\\"Groups\\\"]\\nFN_NAME = \\\"fn_aws_iam_add_user_to_groups\\\"\\nWF_NAME = \\\"Add User To Group\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    added = 0\\n    no_such_entity = 0\\n    added_groups = []\\n    no_such_entity_groups = []\\n    if CONTENT:\\n        for grp_stat in CONTENT:\\n            if grp_stat[\\\"Status\\\"] == \\\"OK\\\":\\n                added += 1\\n                added_groups.append(grp_stat[\\\"GroupName\\\"])\\n            else:\\n                no_such_entity += 1\\n                no_such_entity_groups.append(grp_stat[\\\"GroupName\\\"])\\n        if added_groups:\\n            note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: User \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; added to group \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], \\\", \\\".join(str(i) for i in added_groups), FN_NAME)\\n            note_text += \\\"\u0026lt;br\u0026gt;Refreshing data table \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt; row for user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; with updated group data.\\\"\\\\\\n                .format(\\\"AWS IAM Users\\\", INPUTS[\\\"aws_iam_user_name\\\"])\\n        if no_such_entity:\\n            note_text = \\\"AWS IAM Integration: : Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The group(s) \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; \\\" \\\\\\n                        \\\"did not exist for user \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt; for Resilient function \u0026lt;b\u0026gt;{3}\u0026lt;/b\u0026gt;.\\\"\\\\\\n                .format(WF_NAME, \\\", \\\".join(str(i) for i in no_such_entity_groups), INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n    else:\\n        note_text += \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: There was no result returned for Resilient function \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, FN_NAME)\\n\\n    incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\\n\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\\ninputs.aws_iam_group_names = rule.properties.aws_iam_group\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_005w2go\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1eky3ca\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_005w2go\" sourceRef=\"StartEvent_155asxm\" targetRef=\"ServiceTask_0l8gfqa\"/\u003e\u003cserviceTask id=\"ServiceTask_1vss89f\" name=\"AWS IAM: List User Groups\" resilient:type=\"function\"\u003e\u003cextensionElements\u003e\u003cresilient:function uuid=\"c8b67eb7-166c-4f5c-8291-1d0e3bd14e68\"\u003e{\"inputs\":{},\"post_processing_script\":\"##  AWS IAM - fn_aws_iam_list_user_groups script ##\\n# Example result:\\n\\\"\\\"\\\"\\nResult: {\u0027version\u0027: \u00271.0\u0027, \u0027success\u0027: True, \u0027reason\u0027: None, \\n         \u0027content\u0027: [{\u0027Path\u0027: \u0027/\u0027, \u0027GroupName\u0027: \u0027null_group\u0027, \u0027GroupId\u0027: \u0027ABCDEFG\u0027, \\n                      \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:group/null_group\u0027, \u0027CreateDate\u0027: \u00272019-12-04 12:31:47\u0027}, \\n                      {\u0027Path\u0027: \u0027/\u0027, \u0027GroupName\u0027: \u0027denyall_group\u0027, \u0027GroupId\u0027: \u0027ABCDEFG\u0027, \\n                       \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:group/denyall_group\u0027, \u0027CreateDate\u0027: \u00272019-11-29 15:49:34\u0027}, \\n                      {\u0027Path\u0027: \u0027/\u0027, \u0027GroupName\u0027: \u0027myS3group\u0027, \u0027GroupId\u0027: \u0027ABCDEFG\u0027, \\n                      \u0027Arn\u0027: \u0027arn:aws:iam::123456789123:group/myS3group\u0027, \u0027CreateDate\u0027: \u00272017-05-29 20:41:50\u0027}], \\n          \u0027raw\u0027: \u0027[{\\\"Path\\\": \\\"/\\\", \\\"GroupName\\\": \\\"null_group\\\", \\\"GroupId\\\": \\\"ABCDEFG\\\", \\n                 \\\"Arn\\\": \\\"arn:aws:iam::123456789123:group/null_group\\\", \\\"CreateDate\\\": \\\"2019-12-04 12:31:47\\\"}, \\n                 \\\"Path\\\": \\\"/\\\", \\\"GroupName\\\": \\\"denyall_group\\\", \\\"GroupId\\\": \\\"ABCDEFG\\\", \\n                 \\\"Arn\\\": \\\"arn:aws:iam::123456789123:group/denyall_group\\\", \\\"CreateDate\\\": \\\"2019-11-29 15:49:34\\\"}, \\n                 {\\\"Path\\\": \\\"/\\\", \\\"GroupName\\\": \\\"myS3group\\\", \\\"GroupId\\\": \\\"ABCDEFG\\\", \\n                 \\\"Arn\\\": \\\"arn:aws:iam::123456789123:group/myS3group\\\", \\\"CreateDate\\\": \\\"2017-05-29 20:41:50\\\"}]\u0027, \\n         \u0027inputs\u0027: {\u0027aws_iam_user_name\u0027: \u0027iam_test_user_1\u0027}, \\n         \u0027metrics\u0027: {\u0027version\u0027: \u00271.0\u0027, \u0027package\u0027: \u0027fn-aws-iam\u0027, \u0027package_version\u0027: \u00271.0.0\u0027, \u0027host\u0027: \u0027myhost.ie.ibm.com\u0027, \\n                     \u0027execution_time_ms\u0027: 944, \u0027timestamp\u0027: \u00272020-03-16 15:43:21\u0027\\n                    }\\n}\\n\\\"\\\"\\\"\\n#  Globals\\n# List of fields in datatable fn_aws_iam_list_user_groups script\\nDATA_TBL_FIELDS = [\\\"Groups\\\"]\\nFN_NAME = \\\"fn_aws_iam_list_user_groups\\\"\\nWF_NAME = \\\"Add User To Group\\\"\\n# Processing\\nCONTENT = results.content\\nINPUTS = results.inputs\\nQUERY_EXECUTION_DATE = results[\\\"metrics\\\"][\\\"timestamp\\\"]\\nnote_text = \u0027\u0027\\n\\ndef main():\\n    note_text = \u0027\u0027\\n    if CONTENT:\\n        groups = []\\n        for grp in CONTENT:\\n            if grp[\\\"GroupName\\\"] is not None:\\n                groups.append(grp[\\\"GroupName\\\"])\\n        row.Groups = \\\",\\\".join(groups)\\n    else:\\n        note_text = \\\"AWS IAM Integration: Workflow \u0026lt;b\u0026gt;{0}\u0026lt;/b\u0026gt;: The user \u0026lt;b\u0026gt;{1}\u0026lt;/b\u0026gt; does not appear to be a member \\\" \\\\\\n                    \\\"of any group for Resilient function \u0026lt;b\u0026gt;{2}\u0026lt;/b\u0026gt;.\\\"\\\\\\n            .format(WF_NAME, INPUTS[\\\"aws_iam_user_name\\\"], FN_NAME)\\n        row.Groups = \\\"\\\"\\n    if note_text:\\n        incident.addNote(helper.createRichText(note_text))\\nif __name__ == \\\"__main__\\\":\\n    main()\",\"post_processing_script_language\":\"python3\",\"pre_processing_script\":\"inputs.aws_iam_user_name = row.UserName\",\"pre_processing_script_language\":\"python3\"}\u003c/resilient:function\u003e\u003c/extensionElements\u003e\u003cincoming\u003eSequenceFlow_1eky3ca\u003c/incoming\u003e\u003coutgoing\u003eSequenceFlow_1ngvzce\u003c/outgoing\u003e\u003c/serviceTask\u003e\u003csequenceFlow id=\"SequenceFlow_1eky3ca\" sourceRef=\"ServiceTask_0l8gfqa\" targetRef=\"ServiceTask_1vss89f\"/\u003e\u003cendEvent id=\"EndEvent_1ksmn2v\"\u003e\u003cincoming\u003eSequenceFlow_1ngvzce\u003c/incoming\u003e\u003c/endEvent\u003e\u003csequenceFlow id=\"SequenceFlow_1ngvzce\" sourceRef=\"ServiceTask_1vss89f\" targetRef=\"EndEvent_1ksmn2v\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1kxxiyt\"\u003e\u003ctext\u003eStart your workflow here\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1seuj48\" sourceRef=\"StartEvent_155asxm\" targetRef=\"TextAnnotation_1kxxiyt\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_0qd9eul\"\u003e\u003ctext\u003eAdd user to a group. Username assigned from data table row. Group name assigned from activity field drop-down.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_09b7isi\" sourceRef=\"ServiceTask_0l8gfqa\" targetRef=\"TextAnnotation_0qd9eul\"/\u003e\u003ctextAnnotation id=\"TextAnnotation_1ritmag\"\u003e\u003ctext\u003eGet updated group list for user\u00a0 and update data table.\n\u00a0Username assigned from data table row.\u003c/text\u003e\u003c/textAnnotation\u003e\u003cassociation id=\"Association_1ko3cb5\" sourceRef=\"ServiceTask_1vss89f\" targetRef=\"TextAnnotation_1ritmag\"/\u003e\u003c/process\u003e\u003cbpmndi:BPMNDiagram id=\"BPMNDiagram_1\"\u003e\u003cbpmndi:BPMNPlane bpmnElement=\"undefined\" id=\"BPMNPlane_1\"\u003e\u003cbpmndi:BPMNShape bpmnElement=\"StartEvent_155asxm\" id=\"StartEvent_155asxm_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"162\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"0\" width=\"90\" x=\"157\" y=\"223\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1kxxiyt\" id=\"TextAnnotation_1kxxiyt_di\"\u003e\u003comgdc:Bounds height=\"30\" width=\"100\" x=\"99\" y=\"254\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1seuj48\" id=\"Association_1seuj48_di\"\u003e\u003comgdi:waypoint x=\"169\" y=\"220\"/\u003e\u003comgdi:waypoint x=\"153\" y=\"254\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_0l8gfqa\" id=\"ServiceTask_0l8gfqa_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"239\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_005w2go\" id=\"SequenceFlow_005w2go_di\"\u003e\u003comgdi:waypoint x=\"198\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"239\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"0\" x=\"218.5\" y=\"184\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"ServiceTask_1vss89f\" id=\"ServiceTask_1vss89f_di\"\u003e\u003comgdc:Bounds height=\"80\" width=\"100\" x=\"479\" y=\"166\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1eky3ca\" id=\"SequenceFlow_1eky3ca_di\"\u003e\u003comgdi:waypoint x=\"339\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"479\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"364\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"EndEvent_1ksmn2v\" id=\"EndEvent_1ksmn2v_di\"\u003e\u003comgdc:Bounds height=\"36\" width=\"36\" x=\"631\" y=\"188\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"604\" y=\"227\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"SequenceFlow_1ngvzce\" id=\"SequenceFlow_1ngvzce_di\"\u003e\u003comgdi:waypoint x=\"579\" y=\"206\"/\u003e\u003comgdi:waypoint x=\"631\" y=\"206\"/\u003e\u003cbpmndi:BPMNLabel\u003e\u003comgdc:Bounds height=\"13\" width=\"90\" x=\"560\" y=\"184.5\"/\u003e\u003c/bpmndi:BPMNLabel\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_0qd9eul\" id=\"TextAnnotation_0qd9eul_di\"\u003e\u003comgdc:Bounds height=\"58\" width=\"217\" x=\"180\" y=\"43\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_09b7isi\" id=\"Association_09b7isi_di\"\u003e\u003comgdi:waypoint x=\"289\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"289\" y=\"101\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003cbpmndi:BPMNShape bpmnElement=\"TextAnnotation_1ritmag\" id=\"TextAnnotation_1ritmag_di\"\u003e\u003comgdc:Bounds height=\"67\" width=\"200\" x=\"429\" y=\"38\"/\u003e\u003c/bpmndi:BPMNShape\u003e\u003cbpmndi:BPMNEdge bpmnElement=\"Association_1ko3cb5\" id=\"Association_1ko3cb5_di\"\u003e\u003comgdi:waypoint x=\"529\" y=\"166\"/\u003e\u003comgdi:waypoint x=\"529\" y=\"105\"/\u003e\u003c/bpmndi:BPMNEdge\u003e\u003c/bpmndi:BPMNPlane\u003e\u003c/bpmndi:BPMNDiagram\u003e\u003c/definitions\u003e"
      },
      "content_version": 4,
      "description": "Add an IAM user to an IAM group. The user is assigned from a field in the selected data table row. A group name is assigned from an activity field drop-down list.  The data table row will be refreshed with updated group values for the selected user.",
      "export_key": "wf_aws_iam_add_user_to_group",
      "last_modified_by": "soar_apps_dev@ibm.com",
      "last_modified_time": 1719371884093,
      "name": "Example: AWS IAM: Add User To Group",
      "object_type": "aws_iam_users",
      "programmatic_name": "wf_aws_iam_add_user_to_group",
      "tags": [],
      "uuid": "7a082ac4-6e47-4aa8-aed9-106541b77807",
      "workflow_id": 4
    }
  ],
  "workspaces": []
}
