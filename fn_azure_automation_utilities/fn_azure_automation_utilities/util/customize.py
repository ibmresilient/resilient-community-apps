# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v50.1.262

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
        "message_destinations": [
            u"fn_azure_automation_utilities"
        ],
        "functions": [
            u"azure_create_account",
            u"azure_create_credential",
            u"azure_create_schedule",
            u"azure_delete_account",
            u"azure_delete_credential",
            u"azure_delete_runbook",
            u"azure_delete_schedule",
            u"azure_execute_runbook",
            u"azure_get_account",
            u"azure_get_agent_registration_information",
            u"azure_get_credential",
            u"azure_get_job",
            u"azure_get_module_activity",
            u"azure_get_node_report",
            u"azure_get_runbook",
            u"azure_get_schedule",
            u"azure_list_jobs_by_automation_account",
            u"azure_list_runbooks_by_automation_account",
            u"azure_list_schedule_by_automation_account",
            u"azure_list_statistics_by_automation_account",
            u"azure_list_usage_by_automation_account",
            u"azure_regenerate_agent_registration_key"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"azure_automation_accounts"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"azure_automation_account_delete",
            u"azure_automation_account_update",
            u"azure_automation_utilities_create_account",
            u"azure_automation_utilities_create_credential",
            u"azure_automation_utilities_create_schedule",
            u"azure_automation_utilities_delete_credential",
            u"azure_automation_utilities_delete_runbook",
            u"azure_automation_utilities_delete_schedule",
            u"azure_automation_utilities_execute_runbook",
            u"azure_automation_utilities_get_account",
            u"azure_automation_utilities_get_agent_registration_information",
            u"azure_automation_utilities_get_credential",
            u"azure_automation_utilities_get_job",
            u"azure_automation_utilities_get_job_output",
            u"azure_automation_utilities_get_module_activity",
            u"azure_automation_utilities_get_node_report",
            u"azure_automation_utilities_get_runbook",
            u"azure_automation_utilities_get_schedule",
            u"azure_automation_utilities_list_jobs_by_automation_account",
            u"azure_automation_utilities_list_runbooks_by_automation_account",
            u"azure_automation_utilities_list_schedule_by_automation_account",
            u"azure_automation_utilities_list_statistics_by_automation_account",
            u"azure_automation_utilities_list_usage_by_automation_account",
            u"azure_automation_utilities_regenerate_agent_registration_key",
            u"azure_automation_utilities_update_credential",
            u"azure_automation_utilities_update_schedule"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

    Contents:
    - Message Destinations:
        - fn_azure_automation_utilities
    - Functions:
        - azure_create_account
        - azure_create_credential
        - azure_create_schedule
        - azure_delete_account
        - azure_delete_credential
        - azure_delete_runbook
        - azure_delete_schedule
        - azure_execute_runbook
        - azure_get_account
        - azure_get_agent_registration_information
        - azure_get_credential
        - azure_get_job
        - azure_get_module_activity
        - azure_get_node_report
        - azure_get_runbook
        - azure_get_schedule
        - azure_list_jobs_by_automation_account
        - azure_list_runbooks_by_automation_account
        - azure_list_schedule_by_automation_account
        - azure_list_statistics_by_automation_account
        - azure_list_usage_by_automation_account
        - azure_regenerate_agent_registration_key
    - Playbooks:
        - azure_automation_account_delete
        - azure_automation_account_update
        - azure_automation_utilities_create_account
        - azure_automation_utilities_create_credential
        - azure_automation_utilities_create_schedule
        - azure_automation_utilities_delete_credential
        - azure_automation_utilities_delete_runbook
        - azure_automation_utilities_delete_schedule
        - azure_automation_utilities_execute_runbook
        - azure_automation_utilities_get_account
        - azure_automation_utilities_get_agent_registration_information
        - azure_automation_utilities_get_credential
        - azure_automation_utilities_get_job
        - azure_automation_utilities_get_job_output
        - azure_automation_utilities_get_module_activity
        - azure_automation_utilities_get_node_report
        - azure_automation_utilities_get_runbook
        - azure_automation_utilities_get_schedule
        - azure_automation_utilities_list_jobs_by_automation_account
        - azure_automation_utilities_list_runbooks_by_automation_account
        - azure_automation_utilities_list_schedule_by_automation_account
        - azure_automation_utilities_list_statistics_by_automation_account
        - azure_automation_utilities_list_usage_by_automation_account
        - azure_automation_utilities_regenerate_agent_registration_key
        - azure_automation_utilities_update_credential
        - azure_automation_utilities_update_schedule
    - Data Tables:
        - azure_automation_accounts
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)