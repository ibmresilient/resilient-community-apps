# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.6.0.1543

"""Generate the SOAR customizations required for fn_microsoft_defender"""

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
    Parameters required reload codegen for the fn_microsoft_defender package
    """
    return {
        "package": u"fn_microsoft_defender",
        "message_destinations": [
            u"fn_microsoft_defender"
        ],
        "functions": [
            u"defender_alert_search",
            u"defender_app_execution",
            u"defender_collect_machine_investigation_package",
            u"defender_delete_indicator",
            u"defender_find_machines",
            u"defender_find_machines_by_file",
            u"defender_find_machines_by_filter",
            u"defender_get_file_information",
            u"defender_get_incident",
            u"defender_get_related_alert_information",
            u"defender_list_indicators",
            u"defender_machine_isolation",
            u"defender_machine_scan",
            u"defender_machine_vulnerabilities",
            u"defender_quarantine_file",
            u"defender_set_indicator",
            u"defender_update_alert",
            u"defender_update_incident"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"defender_classification",
            u"defender_determination",
            u"defender_incident_createtime",
            u"defender_incident_id",
            u"defender_incident_lastupdatetime",
            u"defender_incident_url",
            u"defender_tags"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"defender_alerts",
            u"defender_indicators",
            u"defender_machines"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"Create Artifact from Indicator"
        ],
        "playbooks": [
            u"create_artifact_from_indicator_pb",
            u"defender_close_incident_pb",
            u"defender_find_machine_by_dns_name_pb",
            u"defender_find_machines_by_file_hash_pb",
            u"defender_find_machines_by_internal_ip_address_pb",
            u"defender_get_file_information_pb",
            u"defender_get_incident_pb",
            u"defender_list_indicators_pb",
            u"defender_machine_app_execution_restriction_pb",
            u"defender_machine_collect_investigation_package_pb",
            u"defender_machine_isolate_action_pb",
            u"defender_machine_quarantine_file_pb",
            u"defender_machine_refresh_information_pb",
            u"defender_machine_scan_pb",
            u"defender_machine_update_information_pb",
            u"defender_machine_vulnerabilities_pb",
            u"defender_refresh_incident_pb",
            u"defender_set_indicator_pb",
            u"defender_sync_comment_pb",
            u"defender_sync_incident_pb",
            u"defender_update_alert_pb",
            u"delete_indicator_pb",
            u"update_indicator_pb"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_microsoft_defender
    - Functions:
        - defender_alert_search
        - defender_app_execution
        - defender_collect_machine_investigation_package
        - defender_delete_indicator
        - defender_find_machines
        - defender_find_machines_by_file
        - defender_find_machines_by_filter
        - defender_get_file_information
        - defender_get_incident
        - defender_get_related_alert_information
        - defender_list_indicators
        - defender_machine_isolation
        - defender_machine_scan
        - defender_machine_vulnerabilities
        - defender_quarantine_file
        - defender_set_indicator
        - defender_update_alert
        - defender_update_incident
    - Playbooks:
        - create_artifact_from_indicator_pb
        - defender_close_incident_pb
        - defender_find_machine_by_dns_name_pb
        - defender_find_machines_by_file_hash_pb
        - defender_find_machines_by_internal_ip_address_pb
        - defender_get_file_information_pb
        - defender_get_incident_pb
        - defender_list_indicators_pb
        - defender_machine_app_execution_restriction_pb
        - defender_machine_collect_investigation_package_pb
        - defender_machine_isolate_action_pb
        - defender_machine_quarantine_file_pb
        - defender_machine_refresh_information_pb
        - defender_machine_scan_pb
        - defender_machine_update_information_pb
        - defender_machine_vulnerabilities_pb
        - defender_refresh_incident_pb
        - defender_set_indicator_pb
        - defender_sync_comment_pb
        - defender_sync_incident_pb
        - defender_update_alert_pb
        - delete_indicator_pb
        - update_indicator_pb
    - Incident Fields:
        - defender_classification
        - defender_determination
        - defender_incident_createtime
        - defender_incident_id
        - defender_incident_lastupdatetime
        - defender_incident_url
        - defender_tags
    - Data Tables:
        - defender_alerts
        - defender_indicators
        - defender_machines
    - Scripts:
        - Create Artifact from Indicator
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)