# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate the SOAR customizations required for fn_sep"""

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
        "message_destinations": [
            u"fn_sep"
        ],
        "functions": [
            u"fn_sep_add_fingerprint_list",
            u"fn_sep_assign_fingerprint_list_to_group",
            u"fn_sep_delete_fingerprint_list",
            u"fn_sep_get_command_status",
            u"fn_sep_get_computers",
            u"fn_sep_get_domains",
            u"fn_sep_get_file_content_as_base64",
            u"fn_sep_get_fingerprint_list",
            u"fn_sep_get_groups",
            u"fn_sep_move_endpoint",
            u"fn_sep_quarantine_endpoints",
            u"fn_sep_scan_endpoints",
            u"fn_sep_update_fingerprint_list",
            u"fn_sep_upload_file_to_sepm",
            u"sep_cancel_a_command",
            u"sep_get_critical_events_info",
            u"sep_get_exceptions_policy",
            u"sep_get_firewall_policy",
            u"sep_get_policy_summary"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"sep_critical_events",
            u"sep_endpoint_details",
            u"sep_endpoint_status_summary",
            u"sep_endpoints_non_compliant_details",
            u"sep_eoc_scan_results",
            u"sep_fingerprint_lists",
            u"sep_groups"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"scr_sep_add_artifact_from_scan_results",
            u"scr_sep_parse_email_notification"
        ],
        "playbooks": [
            u"sep_add_artifact_from_scan_result",
            u"sep_add_hash_to_blacklist",
            u"sep_assign_blacklist_to_lockdown_group",
            u"sep_cancel_a_command",
            u"sep_delete_blacklist",
            u"sep_delete_hash_from_blacklist",
            u"sep_get_blacklist_information",
            u"sep_get_critical_events",
            u"sep_get_endpoint_details",
            u"sep_get_endpoint_details_for_artifact",
            u"sep_get_endpoints_status_summary",
            u"sep_get_endpoints_status_summary_refresh",
            u"sep_get_exceptions_policy",
            u"sep_get_file_content_as_base64_string",
            u"sep_get_firewall_policy",
            u"sep_get_groups_information",
            u"sep_get_noncompliant_endpoints_status_details",
            u"sep_get_policy_summary",
            u"sep_get_quarantine_status",
            u"sep_get_remediation_status",
            u"sep_get_scan_results",
            u"sep_get_upload_status",
            u"sep_initiate_eoc_scan_for_artifact",
            u"sep_move_endpoint",
            u"sep_quarantine_endpoint",
            u"sep_remediate_artifact_on_endpoint",
            u"sep_unquarantine_endpoint",
            u"sep_upload_file_to_sepm_server"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9340

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
    - Playbooks:
        - sep_add_artifact_from_scan_result
        - sep_add_hash_to_blacklist
        - sep_assign_blacklist_to_lockdown_group
        - sep_cancel_a_command
        - sep_delete_blacklist
        - sep_delete_hash_from_blacklist
        - sep_get_blacklist_information
        - sep_get_critical_events
        - sep_get_endpoint_details
        - sep_get_endpoint_details_for_artifact
        - sep_get_endpoints_status_summary
        - sep_get_endpoints_status_summary_refresh
        - sep_get_exceptions_policy
        - sep_get_file_content_as_base64_string
        - sep_get_firewall_policy
        - sep_get_groups_information
        - sep_get_noncompliant_endpoints_status_details
        - sep_get_policy_summary
        - sep_get_quarantine_status
        - sep_get_remediation_status
        - sep_get_scan_results
        - sep_get_upload_status
        - sep_initiate_eoc_scan_for_artifact
        - sep_move_endpoint
        - sep_quarantine_endpoint
        - sep_remediate_artifact_on_endpoint
        - sep_unquarantine_endpoint
        - sep_upload_file_to_sepm_server
    - Data Tables:
        - sep_critical_events
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