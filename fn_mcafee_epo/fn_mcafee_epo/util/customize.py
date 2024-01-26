# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_mcafee_epo"""

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
    Parameters required reload codegen for the fn_mcafee_epo package
    """
    return {
        "package": u"fn_mcafee_epo",
        "message_destinations": [u"mcafee_epo_message_destination"],
        "functions": [u"mcafee_epo_add_permission_sets_to_user", u"mcafee_epo_add_system", u"mcafee_epo_add_user", u"mcafee_epo_assign_policy_to_group", u"mcafee_epo_assign_policy_to_systems", u"mcafee_epo_create_issue", u"mcafee_epo_delete_issue", u"mcafee_epo_delete_system", u"mcafee_epo_execute_query", u"mcafee_epo_find_a_system", u"mcafee_epo_find_client_tasks", u"mcafee_epo_find_groups", u"mcafee_epo_find_policies", u"mcafee_epo_find_systems_in_group", u"mcafee_epo_get_all_permission_sets", u"mcafee_epo_get_all_users", u"mcafee_epo_list_issues", u"mcafee_epo_list_tags", u"mcafee_epo_remove_permission_sets_from_user", u"mcafee_epo_remove_tag", u"mcafee_epo_remove_user", u"mcafee_epo_run_client_task", u"mcafee_epo_update_issue", u"mcafee_epo_update_user", u"mcafee_epo_wake_up_agent", u"mcafee_tag_an_epo_asset"],
        "workflows": [u"mcafee_epo_add_permission_sets_to_user", u"mcafee_epo_add_system", u"mcafee_epo_add_user", u"mcafee_epo_apply_a_tag", u"mcafee_epo_apply_tags", u"mcafee_epo_assign_policy_to_group_from_group", u"mcafee_epo_assign_policy_to_group_from_policy", u"mcafee_epo_assign_policy_to_system_from_system", u"mcafee_epo_assign_policy_to_systems_from_policy", u"mcafee_epo_create_issue", u"mcafee_epo_delete_issue", u"mcafee_epo_delete_system", u"mcafee_epo_find_all_client_tasks", u"mcafee_epo_find_all_groups", u"mcafee_epo_find_policies", u"mcafee_epo_get_all_permission_sets", u"mcafee_epo_get_all_systems", u"mcafee_epo_get_all_users", u"mcafee_epo_get_system_info", u"mcafee_epo_get_system_info_from_property", u"mcafee_epo_get_system_information", u"mcafee_epo_list_issues", u"mcafee_epo_list_tags", u"mcafee_epo_remove_permission_set_from_user", u"mcafee_epo_remove_tag", u"mcafee_epo_remove_user", u"mcafee_epo_run_client_task", u"mcafee_epo_run_client_task_on_system", u"mcafee_epo_update_issue", u"mcafee_epo_update_user", u"mcafee_epo_wake_up_agent"],
        "actions": [u"McAfee ePO Add Permission Set to User", u"McAfee ePO Add System", u"McAfee ePO Add User", u"McAfee ePO Apply a Tag", u"McAfee ePO Apply Tags", u"McAfee ePO Assign Policy to Group from Group", u"McAfee ePO Assign Policy to Group from Policy", u"McAfee ePO Assign Policy to System from System", u"McAfee ePO Assign Policy to Systems from Policy", u"McAfee ePO Create Issue", u"McAfee ePO Delete Issue", u"McAfee ePO Delete System", u"McAfee ePO Find All Client Tasks", u"McAfee ePO Find All Groups", u"McAfee ePO Find Policies", u"McAfee ePO Get All Permission Sets", u"McAfee ePO Get All Systems", u"McAfee ePO Get All Users", u"McAfee ePO Get System Info", u"McAfee ePO Get System Info from Property", u"McAfee ePO Get System Information", u"McAfee ePO List Issues", u"McAfee ePO List Tags", u"McAfee ePO Remove Permission Set from User", u"McAfee ePO Remove Tags", u"McAfee ePO Remove User", u"McAfee ePO Run Client Task", u"McAfee ePO Run Client Task on System", u"McAfee ePO Update Issue", u"McAfee ePO Update User", u"McAfee ePO Wake up Agent"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"mcafee_epo_client_tasks", u"mcafee_epo_groups", u"mcafee_epo_issues", u"mcafee_epo_permission_sets", u"mcafee_epo_policies", u"mcafee_epo_systems", u"mcafee_epo_tags", u"mcafee_epo_users"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 44.0.7585

    Contents:
    - Message Destinations:
        - mcafee_epo_message_destination
    - Functions:
        - mcafee_epo_add_permission_sets_to_user
        - mcafee_epo_add_system
        - mcafee_epo_add_user
        - mcafee_epo_assign_policy_to_group
        - mcafee_epo_assign_policy_to_systems
        - mcafee_epo_create_issue
        - mcafee_epo_delete_issue
        - mcafee_epo_delete_system
        - mcafee_epo_execute_query
        - mcafee_epo_find_a_system
        - mcafee_epo_find_client_tasks
        - mcafee_epo_find_groups
        - mcafee_epo_find_policies
        - mcafee_epo_find_systems_in_group
        - mcafee_epo_get_all_permission_sets
        - mcafee_epo_get_all_users
        - mcafee_epo_list_issues
        - mcafee_epo_list_tags
        - mcafee_epo_remove_permission_sets_from_user
        - mcafee_epo_remove_tag
        - mcafee_epo_remove_user
        - mcafee_epo_run_client_task
        - mcafee_epo_update_issue
        - mcafee_epo_update_user
        - mcafee_epo_wake_up_agent
        - mcafee_tag_an_epo_asset
    - Workflows:
        - mcafee_epo_add_permission_sets_to_user
        - mcafee_epo_add_system
        - mcafee_epo_add_user
        - mcafee_epo_apply_a_tag
        - mcafee_epo_apply_tags
        - mcafee_epo_assign_policy_to_group_from_group
        - mcafee_epo_assign_policy_to_group_from_policy
        - mcafee_epo_assign_policy_to_system_from_system
        - mcafee_epo_assign_policy_to_systems_from_policy
        - mcafee_epo_create_issue
        - mcafee_epo_delete_issue
        - mcafee_epo_delete_system
        - mcafee_epo_find_all_client_tasks
        - mcafee_epo_find_all_groups
        - mcafee_epo_find_policies
        - mcafee_epo_get_all_permission_sets
        - mcafee_epo_get_all_systems
        - mcafee_epo_get_all_users
        - mcafee_epo_get_system_info
        - mcafee_epo_get_system_info_from_property
        - mcafee_epo_get_system_information
        - mcafee_epo_list_issues
        - mcafee_epo_list_tags
        - mcafee_epo_remove_permission_set_from_user
        - mcafee_epo_remove_tag
        - mcafee_epo_remove_user
        - mcafee_epo_run_client_task
        - mcafee_epo_run_client_task_on_system
        - mcafee_epo_update_issue
        - mcafee_epo_update_user
        - mcafee_epo_wake_up_agent
    - Rules:
        - McAfee ePO Add Permission Set to User
        - McAfee ePO Add System
        - McAfee ePO Add User
        - McAfee ePO Apply a Tag
        - McAfee ePO Apply Tags
        - McAfee ePO Assign Policy to Group from Group
        - McAfee ePO Assign Policy to Group from Policy
        - McAfee ePO Assign Policy to System from System
        - McAfee ePO Assign Policy to Systems from Policy
        - McAfee ePO Create Issue
        - McAfee ePO Delete Issue
        - McAfee ePO Delete System
        - McAfee ePO Find All Client Tasks
        - McAfee ePO Find All Groups
        - McAfee ePO Find Policies
        - McAfee ePO Get All Permission Sets
        - McAfee ePO Get All Systems
        - McAfee ePO Get All Users
        - McAfee ePO Get System Info
        - McAfee ePO Get System Info from Property
        - McAfee ePO Get System Information
        - McAfee ePO List Issues
        - McAfee ePO List Tags
        - McAfee ePO Remove Permission Set from User
        - McAfee ePO Remove Tags
        - McAfee ePO Remove User
        - McAfee ePO Run Client Task
        - McAfee ePO Run Client Task on System
        - McAfee ePO Update Issue
        - McAfee ePO Update User
        - McAfee ePO Wake up Agent
    - Data Tables:
        - mcafee_epo_client_tasks
        - mcafee_epo_groups
        - mcafee_epo_issues
        - mcafee_epo_permission_sets
        - mcafee_epo_policies
        - mcafee_epo_systems
        - mcafee_epo_tags
        - mcafee_epo_users
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)