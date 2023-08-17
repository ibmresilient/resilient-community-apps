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
        "functions": [u"azure_add_or_update_automation_account", u"azure_delete_automation_account", u"azure_delete_runbook", u"azure_execute_runbook", u"azure_get_automation_account", u"azure_get_automation_job", u"azure_get_automation_job_output", u"azure_get_automation_module_activity", u"azure_get_runbook", u"azure_list_automation_accounts", u"azure_list_automation_accounts_by_resource_group", u"azure_list_automation_jobs_by_automation_account", u"azure_list_automation_module_activities", u"azure_list_runbooks_by_automation_account", u"azure_resume_automation_job", u"azure_stop_automation_job", u"azure_suspend_automation_job"],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"azure_automation_utilities_create_or_update_automation_account", u"azure_automation_utilities_delete_automation_account", u"azure_automation_utilities_delete_runbook", u"azure_automation_utilities_execute_runbook", u"azure_automation_utilities_get_automation_account", u"azure_automation_utilities_get_automation_job", u"azure_automation_utilities_get_automation_job_output", u"azure_automation_utilities_get_automation_module_activity", u"azure_automation_utilities_get_runbook", u"azure_automation_utilities_list_automation_accounts", u"azure_automation_utilities_list_automation_accounts_by_resource_group", u"azure_automation_utilities_list_automation_jobs_by_automation_account", u"azure_automation_utilities_list_automation_module_activities", u"azure_automation_utilities_list_runbooks_by_automation_account", u"azure_automation_utilities_resume_automation_job", u"azure_automation_utilities_stop_automation_job", u"azure_automation_utilities_suspend_automation_job"]
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
        - azure_delete_runbook
        - azure_execute_runbook
        - azure_get_automation_account
        - azure_get_automation_job
        - azure_get_automation_job_output
        - azure_get_automation_module_activity
        - azure_get_runbook
        - azure_list_automation_accounts
        - azure_list_automation_accounts_by_resource_group
        - azure_list_automation_jobs_by_automation_account
        - azure_list_automation_module_activities
        - azure_list_runbooks_by_automation_account
        - azure_resume_automation_job
        - azure_stop_automation_job
        - azure_suspend_automation_job
    - Playbooks:
        - azure_automation_utilities_create_or_update_automation_account
        - azure_automation_utilities_delete_automation_account
        - azure_automation_utilities_delete_runbook
        - azure_automation_utilities_execute_runbook
        - azure_automation_utilities_get_automation_account
        - azure_automation_utilities_get_automation_job
        - azure_automation_utilities_get_automation_job_output
        - azure_automation_utilities_get_automation_module_activity
        - azure_automation_utilities_get_runbook
        - azure_automation_utilities_list_automation_accounts
        - azure_automation_utilities_list_automation_accounts_by_resource_group
        - azure_automation_utilities_list_automation_jobs_by_automation_account
        - azure_automation_utilities_list_automation_module_activities
        - azure_automation_utilities_list_runbooks_by_automation_account
        - azure_automation_utilities_resume_automation_job
        - azure_automation_utilities_stop_automation_job
        - azure_automation_utilities_suspend_automation_job
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)