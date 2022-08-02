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
        "functions": [u"mcafee_epo_add_permission_sets_to_user", u"mcafee_epo_add_user", u"mcafee_epo_execute_query", u"mcafee_epo_find_a_system", u"mcafee_epo_get_all_permission_sets", u"mcafee_epo_get_all_users", u"mcafee_epo_list_tags", u"mcafee_epo_remove_permission_sets_from_user", u"mcafee_epo_remove_tag", u"mcafee_epo_update_user", u"mcafee_epo_wake_up_agent", u"mcafee_tag_an_epo_asset"],
        "workflows": [u"mcafee_epo_add_permission_sets_to_user", u"mcafee_epo_apply_a_tag", u"mcafee_epo_apply_tags", u"mcafee_epo_get_all_permission_sets", u"mcafee_epo_get_all_systems", u"mcafee_epo_get_all_users", u"mcafee_epo_get_system_info", u"mcafee_epo_get_system_info_from_property", u"mcafee_epo_list_tags", u"mcafee_epo_remove_permission_set_from_user", u"mcafee_epo_remove_tag", u"mcafee_epo_wake_up_agent"],
        "actions": [u"McAfee ePO Add Permission Set to User", u"McAfee ePO apply a tag", u"McAfee ePO apply tags", u"McAfee ePO Get All Permission Sets", u"McAfee ePO Get All Systems", u"McAfee ePO Get All Users", u"McAfee ePO get system info", u"McAfee ePO Get System Info from Property", u"McAfee ePO list tags", u"McAfee ePO Remove Permission Set from User", u"McAfee ePO remove tags", u"McAfee ePO Wake up Agent"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"mcafee_epo_permission_sets", u"mcafee_epo_systems", u"mcafee_epo_tags", u"mcafee_epo_users"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 43.1.49

    Contents:
    - Message Destinations:
        - mcafee_epo_message_destination
    - Functions:
        - mcafee_epo_add_permission_sets_to_user
        - mcafee_epo_add_user
        - mcafee_epo_execute_query
        - mcafee_epo_find_a_system
        - mcafee_epo_get_all_permission_sets
        - mcafee_epo_get_all_users
        - mcafee_epo_list_tags
        - mcafee_epo_remove_permission_sets_from_user
        - mcafee_epo_remove_tag
        - mcafee_epo_update_user
        - mcafee_epo_wake_up_agent
        - mcafee_tag_an_epo_asset
    - Workflows:
        - mcafee_epo_add_permission_sets_to_user
        - mcafee_epo_apply_a_tag
        - mcafee_epo_apply_tags
        - mcafee_epo_get_all_permission_sets
        - mcafee_epo_get_all_systems
        - mcafee_epo_get_all_users
        - mcafee_epo_get_system_info
        - mcafee_epo_get_system_info_from_property
        - mcafee_epo_list_tags
        - mcafee_epo_remove_permission_set_from_user
        - mcafee_epo_remove_tag
        - mcafee_epo_wake_up_agent
    - Rules:
        - McAfee ePO Add Permission Set to User
        - McAfee ePO apply a tag
        - McAfee ePO apply tags
        - McAfee ePO Get All Permission Sets
        - McAfee ePO Get All Systems
        - McAfee ePO Get All Users
        - McAfee ePO get system info
        - McAfee ePO Get System Info from Property
        - McAfee ePO list tags
        - McAfee ePO Remove Permission Set from User
        - McAfee ePO remove tags
        - McAfee ePO Wake up Agent
    - Data Tables:
        - mcafee_epo_permission_sets
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