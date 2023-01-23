# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_sep"""

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
    Parameters required reload codegen for the fn_sep package
    """
    return {
        "package": u"fn_sep",
        "message_destinations": [u"fn_sep"],
        "functions": [u"fn_sep_add_fingerprint_list", u"fn_sep_assign_fingerprint_list_to_group", u"fn_sep_delete_fingerprint_list", u"fn_sep_get_command_status", u"fn_sep_get_computers", u"fn_sep_get_domains", u"fn_sep_get_file_content_as_base64", u"fn_sep_get_fingerprint_list", u"fn_sep_get_groups", u"fn_sep_move_endpoint", u"fn_sep_quarantine_endpoints", u"fn_sep_scan_endpoints", u"fn_sep_update_fingerprint_list", u"fn_sep_upload_file_to_sepm", u"sep_cancel_a_command", u"sep_get_critical_events_info", u"sep_get_exceptions_policy", u"sep_get_firewall_policy", u"sep_get_policy_summary"],
        "workflows": [u"wf_sep_add_fingerprint_list", u"wf_sep_assign_fingerprint_list_to_lockdown_group", u"wf_sep_delete_fingerprint_list", u"wf_sep_delete_hash_from_fingerprint_list", u"wf_sep_get_blacklist_information", u"wf_sep_get_endpoint_details", u"wf_sep_get_endpoint_details_for_artifact", u"wf_sep_get_endpoints_status", u"wf_sep_get_endpoints_status_details", u"wf_sep_get_endpoints_status_refresh", u"wf_sep_get_file_content_as_base64_string", u"wf_sep_get_groups_information", u"wf_sep_get_quarantine_status", u"wf_sep_get_remediation_status", u"wf_sep_get_scan_results", u"wf_sep_get_upload_status", u"wf_sep_initiate_eoc_scan_for_artifact", u"wf_sep_move_endpoint", u"wf_sep_quarantine_endpoint", u"wf_sep_remediate_artifact_on_endpoint", u"wf_sep_upload_file_to_sepm"],
        "actions": [u"Example: SEP - Add Artifact from Scan Result", u"Example: SEP - Add Hash to Blacklist", u"Example: SEP - Assign Blacklist to lockdown group", u"Example: SEP - Delete Blacklist", u"Example: SEP - Delete Hash from Blacklist", u"Example: SEP - Get Blacklist information", u"Example: SEP - Get Endpoint Details", u"Example: SEP - Get Endpoint Details for artifact", u"Example: SEP - Get Endpoints status summary", u"Example: SEP - Get Endpoints status summary (refresh)", u"Example: SEP - Get File Content as Base64 string", u"Example: SEP - Get Groups information", u"Example: SEP - Get Non-Compliant Endpoints status details", u"Example: SEP - Get Quarantine status", u"Example: SEP - Get Remediation status", u"Example: SEP - Get Scan results", u"Example: SEP - Get Upload status", u"Example: SEP - Initiate EOC Scan for Artifact", u"Example: SEP - Move Endpoint", u"Example: SEP - Parse notification", u"Example: SEP - Quarantine Endpoint", u"Example: SEP - Remediate Artifact on Endpoint", u"Example: SEP - Un-Quarantine Endpoint", u"Example: SEP - Upload file to SEPM server"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"sep_endpoint_details", u"sep_endpoint_status_summary", u"sep_endpoints_non_compliant_details", u"sep_eoc_scan_results", u"sep_fingerprint_lists", u"sep_groups"],
        "automatic_tasks": [],
        "scripts": [u"scr_sep_add_artifact_from_scan_results", u"scr_sep_parse_email_notification"],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - fn_sep
    - Functions:
        - fn_sep_add_fingerprint_list
        - fn_sep_assign_fingerprint_list_to_group
        - fn_sep_delete_fingerprint_list
        - fn_sep_get_command_status
        - fn_sep_get_computers
        - fn_sep_get_domains
        - fn_sep_get_file_content_as_base64
        - fn_sep_get_fingerprint_list
        - fn_sep_get_groups
        - fn_sep_move_endpoint
        - fn_sep_quarantine_endpoints
        - fn_sep_scan_endpoints
        - fn_sep_update_fingerprint_list
        - fn_sep_upload_file_to_sepm
        - sep_cancel_a_command
        - sep_get_critical_events_info
        - sep_get_exceptions_policy
        - sep_get_firewall_policy
        - sep_get_policy_summary
    - Workflows:
        - wf_sep_add_fingerprint_list
        - wf_sep_assign_fingerprint_list_to_lockdown_group
        - wf_sep_delete_fingerprint_list
        - wf_sep_delete_hash_from_fingerprint_list
        - wf_sep_get_blacklist_information
        - wf_sep_get_endpoint_details
        - wf_sep_get_endpoint_details_for_artifact
        - wf_sep_get_endpoints_status
        - wf_sep_get_endpoints_status_details
        - wf_sep_get_endpoints_status_refresh
        - wf_sep_get_file_content_as_base64_string
        - wf_sep_get_groups_information
        - wf_sep_get_quarantine_status
        - wf_sep_get_remediation_status
        - wf_sep_get_scan_results
        - wf_sep_get_upload_status
        - wf_sep_initiate_eoc_scan_for_artifact
        - wf_sep_move_endpoint
        - wf_sep_quarantine_endpoint
        - wf_sep_remediate_artifact_on_endpoint
        - wf_sep_upload_file_to_sepm
    - Rules:
        - Example: SEP - Add Artifact from Scan Result
        - Example: SEP - Add Hash to Blacklist
        - Example: SEP - Assign Blacklist to lockdown group
        - Example: SEP - Delete Blacklist
        - Example: SEP - Delete Hash from Blacklist
        - Example: SEP - Get Blacklist information
        - Example: SEP - Get Endpoint Details
        - Example: SEP - Get Endpoint Details for artifact
        - Example: SEP - Get Endpoints status summary
        - Example: SEP - Get Endpoints status summary (refresh)
        - Example: SEP - Get File Content as Base64 string
        - Example: SEP - Get Groups information
        - Example: SEP - Get Non-Compliant Endpoints status details
        - Example: SEP - Get Quarantine status
        - Example: SEP - Get Remediation status
        - Example: SEP - Get Scan results
        - Example: SEP - Get Upload status
        - Example: SEP - Initiate EOC Scan for Artifact
        - Example: SEP - Move Endpoint
        - Example: SEP - Parse notification
        - Example: SEP - Quarantine Endpoint
        - Example: SEP - Remediate Artifact on Endpoint
        - Example: SEP - Un-Quarantine Endpoint
        - Example: SEP - Upload file to SEPM server
    - Data Tables:
        - sep_endpoint_details
        - sep_endpoint_status_summary
        - sep_endpoints_non_compliant_details
        - sep_eoc_scan_results
        - sep_fingerprint_lists
        - sep_groups
    - Scripts:
        - scr_sep_add_artifact_from_scan_results
        - scr_sep_parse_email_notification
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)