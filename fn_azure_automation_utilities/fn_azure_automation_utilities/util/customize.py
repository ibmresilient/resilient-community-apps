# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""Generate the Resilient customizations required for fn_azure_automation_utilities"""

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
    Parameters required reload codegen for the fn_azure_automation_utilities package
    """
    return {
        "package": u"fn_azure_automation_utilities",
        "message_destinations": [u"fn_azure_automation_utilities"],
        "functions": [u"azure_add_or_update_automation_account", u"azure_delete_automation_account", u"azure_get_automation_account", u"azure_get_automation_module_activity", u"azure_list_automation_accounts", u"azure_list_automation_accounts_by_resource_group", u"azure_list_automation_module_activities"],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"azure_automation_utilities_create_or_update_automation_account", u"azure_automation_utilities_delete_automation_account", u"azure_automation_utilities_get_automation_account", u"azure_automation_utilities_get_automation_module_activity", u"azure_automation_utilities_list_automation_accounts", u"azure_automation_utilities_list_automation_accounts_by_resource_group", u"azure_automation_utilities_list_automation_module_activities"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - fn_azure_automation_utilities
    - Functions:
        - azure_add_or_update_automation_account
        - azure_delete_automation_account
        - azure_get_automation_account
        - azure_get_automation_module_activity
        - azure_list_automation_accounts
        - azure_list_automation_accounts_by_resource_group
        - azure_list_automation_module_activities
    - Playbooks:
        - azure_automation_utilities_create_or_update_automation_account
        - azure_automation_utilities_delete_automation_account
        - azure_automation_utilities_get_automation_account
        - azure_automation_utilities_get_automation_module_activity
        - azure_automation_utilities_list_automation_accounts
        - azure_automation_utilities_list_automation_accounts_by_resource_group
        - azure_automation_utilities_list_automation_module_activities
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)