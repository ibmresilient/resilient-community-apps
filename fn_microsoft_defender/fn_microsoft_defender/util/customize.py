# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_microsoft_defender"""

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
        "message_destinations": [u"fn_microsoft_defender"],
        "functions": [u"defender_alert_search", u"defender_app_execution", u"defender_collect_machine_investigation_package", u"defender_delete_indicator", u"defender_find_machines", u"defender_find_machines_by_file", u"defender_find_machines_by_filter", u"defender_get_file_information", u"defender_get_incident", u"defender_get_related_alert_information", u"defender_list_indicators", u"defender_machine_isolation", u"defender_machine_scan", u"defender_machine_vulnerabilities", u"defender_quarantine_file", u"defender_set_indicator", u"defender_update_alert", u"defender_update_incident"],
        "workflows": [u"defender_atp_app_execution", u"defender_atp_collect_machine_investigation_package", u"defender_atp_delete_indicator", u"defender_atp_find_machines", u"defender_atp_find_machines_by_file_hash", u"defender_atp_get_file_information", u"defender_atp_machine_isolation", u"defender_atp_machine_scan", u"defender_atp_machine_vulnerabilities", u"defender_atp_set_indicator", u"defender_atp_update_alert", u"defender_atp_update_indicator", u"defender_close_incident", u"defender_find_machines_by_filter", u"defender_get_incident", u"defender_get_updated_machine_information", u"defender_list_indicators", u"defender_quarantine_file", u"defender_sync_comment", u"defender_sync_incident"],
        "actions": [u"Create Artifact from Indicator", u"Defender Close Incident", u"Defender Find Machine by DNS name", u"Defender Find Machines by File Hash", u"Defender Find Machines by Internal IP Address", u"Defender Get File Information", u"Defender Get Incident", u"Defender List Indicators", u"Defender Machine App Execution Restriction", u"Defender Machine Collect Investigation Package", u"Defender Machine Isolate Action", u"Defender Machine Quarantine File", u"Defender Machine Refresh Information", u"Defender Machine Scan", u"Defender Machine Update Information", u"Defender Machine Vulnerabilities", u"Defender Set Indicator", u"Defender Sync Comment", u"Defender Sync Incident", u"Defender Update Alert", u"Delete Indicator", u"Update Indicator"],
        "incident_fields": [u"defender_classification", u"defender_determination", u"defender_incident_createtime", u"defender_incident_id", u"defender_incident_lastupdatetime", u"defender_incident_url", u"defender_tags"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"defender_alerts", u"defender_indicators", u"defender_machines"],
        "automatic_tasks": [],
        "scripts": [u"Create Artifact from Indicator"],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 39.0.6328

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
    - Workflows:
        - defender_atp_app_execution
        - defender_atp_collect_machine_investigation_package
        - defender_atp_delete_indicator
        - defender_atp_find_machines
        - defender_atp_find_machines_by_file_hash
        - defender_atp_get_file_information
        - defender_atp_machine_isolation
        - defender_atp_machine_scan
        - defender_atp_machine_vulnerabilities
        - defender_atp_set_indicator
        - defender_atp_update_alert
        - defender_atp_update_indicator
        - defender_close_incident
        - defender_find_machines_by_filter
        - defender_get_incident
        - defender_get_updated_machine_information
        - defender_list_indicators
        - defender_quarantine_file
        - defender_sync_comment
        - defender_sync_incident
    - Rules:
        - Create Artifact from Indicator
        - Defender Close Incident
        - Defender Find Machine by DNS name
        - Defender Find Machines by File Hash
        - Defender Find Machines by Internal IP Address
        - Defender Get File Information
        - Defender Get Incident
        - Defender List Indicators
        - Defender Machine App Execution Restriction
        - Defender Machine Collect Investigation Package
        - Defender Machine Isolate Action
        - Defender Machine Quarantine File
        - Defender Machine Refresh Information
        - Defender Machine Scan
        - Defender Machine Update Information
        - Defender Machine Vulnerabilities
        - Defender Set Indicator
        - Defender Sync Comment
        - Defender Sync Incident
        - Defender Update Alert
        - Delete Indicator
        - Update Indicator
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