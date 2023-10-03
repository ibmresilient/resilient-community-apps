# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v50.0.151

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
        "message_destinations": [
            u"mcafee_epo_message_destination"
        ],
        "functions": [
            u"mcafee_epo_add_permission_sets_to_user",
            u"mcafee_epo_add_system",
            u"mcafee_epo_add_user",
            u"mcafee_epo_assign_policy_to_group",
            u"mcafee_epo_assign_policy_to_systems",
            u"mcafee_epo_create_issue",
            u"mcafee_epo_delete_issue",
            u"mcafee_epo_delete_system",
            u"mcafee_epo_execute_query",
            u"mcafee_epo_find_a_system",
            u"mcafee_epo_find_client_tasks",
            u"mcafee_epo_find_groups",
            u"mcafee_epo_find_policies",
            u"mcafee_epo_find_systems_in_group",
            u"mcafee_epo_get_all_permission_sets",
            u"mcafee_epo_get_all_users",
            u"mcafee_epo_list_issues",
            u"mcafee_epo_list_tags",
            u"mcafee_epo_remove_permission_sets_from_user",
            u"mcafee_epo_remove_tag",
            u"mcafee_epo_remove_user",
            u"mcafee_epo_run_client_task",
            u"mcafee_epo_update_issue",
            u"mcafee_epo_update_user",
            u"mcafee_epo_wake_up_agent",
            u"mcafee_tag_an_epo_asset"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"mcafee_epo_client_tasks",
            u"mcafee_epo_groups",
            u"mcafee_epo_issues",
            u"mcafee_epo_permission_sets",
            u"mcafee_epo_policies",
            u"mcafee_epo_systems_dt",
            u"mcafee_epo_tags",
            u"mcafee_epo_users"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

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
    - Data Tables:
        - mcafee_epo_client_tasks
        - mcafee_epo_groups
        - mcafee_epo_issues
        - mcafee_epo_permission_sets
        - mcafee_epo_policies
        - mcafee_epo_systems_dt
        - mcafee_epo_tags
        - mcafee_epo_users
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)