# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v52.0.0.0.1048

"""Generate the SOAR customizations required for fn_aws_iam"""

import base64
import os
import io
try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_aws_iam package
    """
    return {
        "package": u"fn_aws_iam",
        "message_destinations": [
            u"fn_aws_iam"
        ],
        "functions": [
            u"fn_aws_iam_add_user_to_groups",
            u"fn_aws_iam_attach_user_policies",
            u"fn_aws_iam_deactivate_mfa_devices",
            u"fn_aws_iam_delete_access_keys",
            u"fn_aws_iam_delete_login_profile",
            u"fn_aws_iam_delete_mfa_devices",
            u"fn_aws_iam_delete_signing_certs",
            u"fn_aws_iam_delete_ss_creds",
            u"fn_aws_iam_delete_ssh_keys",
            u"fn_aws_iam_delete_user",
            u"fn_aws_iam_detach_user_policies",
            u"fn_aws_iam_list_mfa_devices",
            u"fn_aws_iam_list_signing_certs",
            u"fn_aws_iam_list_ss_creds",
            u"fn_aws_iam_list_ssh_keys",
            u"fn_aws_iam_list_user_access_key_ids",
            u"fn_aws_iam_list_user_groups",
            u"fn_aws_iam_list_user_policies",
            u"fn_aws_iam_list_users",
            u"fn_aws_iam_remove_user_from_groups",
            u"fn_aws_iam_update_access_key",
            u"fn_aws_iam_update_login_profile"
        ],
        "workflows": [
            u"wf_aws_iam_add_user_to_group",
            u"wf_aws_iam_attach_user_policy",
            u"wf_aws_iam_change_profile_password",
            u"wf_aws_iam_deactivate_access_key",
            u"wf_aws_iam_delete_access_key",
            u"wf_aws_iam_delete_access_key_for_artifact",
            u"wf_aws_iam_delete_access_keys",
            u"wf_aws_iam_delete_login_profile",
            u"wf_aws_iam_delete_user",
            u"wf_aws_iam_delete_user_for_artifact",
            u"wf_aws_iam_detach_all_user_policies",
            u"wf_aws_iam_get_access_key_for_artifact",
            u"wf_aws_iam_get_access_keys",
            u"wf_aws_iam_get_user",
            u"wf_aws_iam_get_user_for_artifact",
            u"wf_aws_iam_list_access_keys",
            u"wf_aws_iam_list_users",
            u"wf_aws_iam_refresh_access_key",
            u"wf_aws_iam_refresh_user",
            u"wf_aws_iam_remove_user_from_all_groups"
        ],
        "actions": [
            u"Example: AWS IAM: Add Access Key As Artifact",
            u"Example: AWS IAM: Add User As Artifact",
            u"Example: AWS IAM: Add User To Group",
            u"Example: AWS IAM: Attach User Policy",
            u"Example: AWS IAM: Change Profile Password",
            u"Example: AWS IAM: Deactivate Access Key",
            u"Example: AWS IAM: Delete Access Key",
            u"Example: AWS IAM: Delete Access Key For Artifact",
            u"Example: AWS IAM: Delete Access Keys",
            u"Example: AWS IAM: Delete Login Profile",
            u"Example: AWS IAM: Delete User",
            u"Example: AWS IAM: Delete User For Artifact",
            u"Example: AWS IAM: Detach All User Policies",
            u"Example: AWS IAM: Get access Key For Artifact",
            u"Example: AWS IAM: Get Access Keys",
            u"Example: AWS IAM: Get User",
            u"Example: AWS IAM: Get User For Artifact",
            u"Example: AWS IAM: List Access Keys",
            u"Example: AWS IAM: List Users",
            u"Example: AWS IAM: Refresh Access Key",
            u"Example: AWS IAM: Refresh User",
            u"Example: AWS IAM: Remove User From All Groups"
        ],
        "incident_fields": [],
        "incident_artifact_types": [
            u"aws_iam_access_key_id",
            u"aws_iam_user_name"
        ],
        "incident_types": [],
        "datatables": [
            u"aws_iam_access_keys",
            u"aws_iam_users"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"scr_aws_iam_add_access_key_as_artifact",
            u"scr_aws_iam_add_user_as_artifact"
        ],
        "playbooks": [],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9340

    Contents:
    - Message Destinations:
        - fn_aws_iam
    - Functions:
        - fn_aws_iam_add_user_to_groups
        - fn_aws_iam_attach_user_policies
        - fn_aws_iam_deactivate_mfa_devices
        - fn_aws_iam_delete_access_keys
        - fn_aws_iam_delete_login_profile
        - fn_aws_iam_delete_mfa_devices
        - fn_aws_iam_delete_signing_certs
        - fn_aws_iam_delete_ss_creds
        - fn_aws_iam_delete_ssh_keys
        - fn_aws_iam_delete_user
        - fn_aws_iam_detach_user_policies
        - fn_aws_iam_list_mfa_devices
        - fn_aws_iam_list_signing_certs
        - fn_aws_iam_list_ss_creds
        - fn_aws_iam_list_ssh_keys
        - fn_aws_iam_list_user_access_key_ids
        - fn_aws_iam_list_user_groups
        - fn_aws_iam_list_user_policies
        - fn_aws_iam_list_users
        - fn_aws_iam_remove_user_from_groups
        - fn_aws_iam_update_access_key
        - fn_aws_iam_update_login_profile
    - Workflows:
        - wf_aws_iam_add_user_to_group
        - wf_aws_iam_attach_user_policy
        - wf_aws_iam_change_profile_password
        - wf_aws_iam_deactivate_access_key
        - wf_aws_iam_delete_access_key
        - wf_aws_iam_delete_access_key_for_artifact
        - wf_aws_iam_delete_access_keys
        - wf_aws_iam_delete_login_profile
        - wf_aws_iam_delete_user
        - wf_aws_iam_delete_user_for_artifact
        - wf_aws_iam_detach_all_user_policies
        - wf_aws_iam_get_access_key_for_artifact
        - wf_aws_iam_get_access_keys
        - wf_aws_iam_get_user
        - wf_aws_iam_get_user_for_artifact
        - wf_aws_iam_list_access_keys
        - wf_aws_iam_list_users
        - wf_aws_iam_refresh_access_key
        - wf_aws_iam_refresh_user
        - wf_aws_iam_remove_user_from_all_groups
    - Rules:
        - Example: AWS IAM: Add Access Key As Artifact
        - Example: AWS IAM: Add User As Artifact
        - Example: AWS IAM: Add User To Group
        - Example: AWS IAM: Attach User Policy
        - Example: AWS IAM: Change Profile Password
        - Example: AWS IAM: Deactivate Access Key
        - Example: AWS IAM: Delete Access Key
        - Example: AWS IAM: Delete Access Key For Artifact
        - Example: AWS IAM: Delete Access Keys
        - Example: AWS IAM: Delete Login Profile
        - Example: AWS IAM: Delete User
        - Example: AWS IAM: Delete User For Artifact
        - Example: AWS IAM: Detach All User Policies
        - Example: AWS IAM: Get access Key For Artifact
        - Example: AWS IAM: Get Access Keys
        - Example: AWS IAM: Get User
        - Example: AWS IAM: Get User For Artifact
        - Example: AWS IAM: List Access Keys
        - Example: AWS IAM: List Users
        - Example: AWS IAM: Refresh Access Key
        - Example: AWS IAM: Refresh User
        - Example: AWS IAM: Remove User From All Groups
    - Custom Artifact Types:
        - aws_iam_access_key_id
        - aws_iam_user_name
    - Data Tables:
        - aws_iam_access_keys
        - aws_iam_users
    - Scripts:
        - scr_aws_iam_add_access_key_as_artifact
        - scr_aws_iam_add_user_as_artifact
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)