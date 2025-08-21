# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.6.0.1543

"""Generate the SOAR customizations required for fn_qradar_enhanced_data"""

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
    Parameters required reload codegen for the fn_qradar_enhanced_data package
    """
    return {
        "package": u"fn_qradar_enhanced_data",
        "message_destinations": [
            u"fn_qradar_enhanced_data"
        ],
        "functions": [
            u"qradar_create_note",
            u"qradar_get_offense_mitre_reference",
            u"qradar_offense_summary",
            u"qradar_top_events"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"qr_assigned",
            u"qr_credibility",
            u"qr_destination_ip_count",
            u"qr_event_count",
            u"qr_flow_count",
            u"qr_last_updated_time",
            u"qr_magnitude",
            u"qr_offense_domain",
            u"qr_offense_index_type",
            u"qr_offense_index_value",
            u"qr_offense_last_updated_time",
            u"qr_offense_source",
            u"qr_offense_start_time",
            u"qr_offense_status",
            u"qr_relevance",
            u"qr_severity",
            u"qr_source_ip_count",
            u"qradar_destination",
            u"qradar_id"
        ],
        "incident_artifact_types": [
            u"ec_file_hash",
            u"ec_file_path",
            u"ec_filename",
            u"ec_imp_hash",
            u"ec_md5_hash",
            u"ec_parentcommandline",
            u"ec_process_commandline",
            u"ec_sha1_hash",
            u"ec_sha256_hash",
            u"filehash",
            u"md5_hash",
            u"sha1_hash",
            u"sha256_hash"
        ],
        "incident_types": [],
        "datatables": [
            u"qr_assets",
            u"qr_categories",
            u"qr_flows",
            u"qr_offense_top_events",
            u"qr_top_destination_ips",
            u"qr_top_source_ips",
            u"qr_triggered_rules",
            u"qradar_rules_and_mitre_tactics_and_techniques"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"Set Incident Last Updated Time"
        ],
        "playbooks": [
            u"create_artifact_from_assets_info_pb",
            u"create_artifact_from_destination_ip_info_pb",
            u"create_artifact_from_events_info_pb",
            u"create_artifact_from_source_ip_info_pb",
            u"create_artifacts_from_flows_info_pb",
            u"qradar_create_note",
            u"qradar_enhanced_data_pb",
            u"qradar_enhanced_data_poller_pb",
            u"qradar_enhanced_data_refresh_pb",
            u"qradar_get_qradar_rule_mitre_reference",
            u"subplaybook_example_of_fetching_contributing_rules_for_offense",
            u"subplaybook_example_of_searching_and_returning_assets_information",
            u"subplaybook_example_of_searching_and_returning_categories",
            u"subplaybook_example_of_searching_and_returning_destination_ips_information",
            u"subplaybook_example_of_searching_and_returning_source_ips_information",
            u"subplaybook_example_of_searching_qradar_flows_using_offense_id",
            u"subplaybook_example_of_searching_qradar_top_events_using_offense_id",
            u"subplaybook_qradar_offense_summary"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.4.0.10288

    Contents:
    - Message Destinations:
        - fn_qradar_enhanced_data
    - Functions:
        - qradar_create_note
        - qradar_get_offense_mitre_reference
        - qradar_offense_summary
        - qradar_top_events
    - Playbooks:
        - create_artifact_from_assets_info_pb
        - create_artifact_from_destination_ip_info_pb
        - create_artifact_from_events_info_pb
        - create_artifact_from_source_ip_info_pb
        - create_artifacts_from_flows_info_pb
        - qradar_create_note
        - qradar_enhanced_data_pb
        - qradar_enhanced_data_poller_pb
        - qradar_enhanced_data_refresh_pb
        - qradar_get_qradar_rule_mitre_reference
        - subplaybook_example_of_fetching_contributing_rules_for_offense
        - subplaybook_example_of_searching_and_returning_assets_information
        - subplaybook_example_of_searching_and_returning_categories
        - subplaybook_example_of_searching_and_returning_destination_ips_information
        - subplaybook_example_of_searching_and_returning_source_ips_information
        - subplaybook_example_of_searching_qradar_flows_using_offense_id
        - subplaybook_example_of_searching_qradar_top_events_using_offense_id
        - subplaybook_qradar_offense_summary
    - Incident Fields:
        - qr_assigned
        - qr_credibility
        - qr_destination_ip_count
        - qr_event_count
        - qr_flow_count
        - qr_last_updated_time
        - qr_magnitude
        - qr_offense_domain
        - qr_offense_index_type
        - qr_offense_index_value
        - qr_offense_last_updated_time
        - qr_offense_source
        - qr_offense_start_time
        - qr_offense_status
        - qr_relevance
        - qr_severity
        - qr_source_ip_count
        - qradar_destination
        - qradar_id
    - Custom Artifact Types:
        - ec_file_hash
        - ec_file_path
        - ec_filename
        - ec_imp_hash
        - ec_md5_hash
        - ec_parentcommandline
        - ec_process_commandline
        - ec_sha1_hash
        - ec_sha256_hash
        - filehash
        - md5_hash
        - sha1_hash
        - sha256_hash
    - Data Tables:
        - qr_assets
        - qr_categories
        - qr_flows
        - qr_offense_top_events
        - qr_top_destination_ips
        - qr_top_source_ips
        - qr_triggered_rules
        - qradar_rules_and_mitre_tactics_and_techniques
    - Scripts:
        - Set Incident Last Updated Time
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)