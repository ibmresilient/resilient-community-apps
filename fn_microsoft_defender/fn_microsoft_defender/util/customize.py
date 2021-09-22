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
        "message_destinations": [u"fn_msdefender"],
        "functions": [u"defender_alert_search", u"defender_app_execution", u"defender_collect_machine_investigation_package", u"defender_delete_indicator", u"defender_find_machines", u"defender_find_machines_by_file", u"defender_find_machines_by_filter", u"defender_get_related_alert_information", u"defender_list_indicators", u"defender_machine_isolation", u"defender_machine_scan", u"defender_machine_vulnerabilities", u"defender_quarantine_file", u"defender_set_indicator", u"defender_update_alert", u"fn_test"],
        "workflows": [u"defender_atp_alerts_by_machine", u"defender_atp_app_execution", u"defender_atp_collect_machine_investigation_package", u"defender_atp_delete_indicator", u"defender_atp_find_machines", u"defender_atp_find_machines_by_file_hash", u"defender_atp_machine_isolation", u"defender_atp_machine_scan", u"defender_atp_machine_unisolate", u"defender_atp_machine_vulnerabilities", u"defender_atp_set_indicator", u"defender_atp_sync_incident_close", u"defender_atp_update_alert", u"defender_atp_update_indicator", u"defender_find_machines_by_filter", u"defender_get_related_alert_information", u"defender_list_indicators", u"defender_quarantine_file", u"example_get_incident_contact_info"],
        "actions": [u"Create Artifact from Indicator", u"Defender ATP Alerts by Machine", u"Defender ATP App Execution Restriction", u"Defender ATP Collect Machine Investigation Package", u"Defender ATP Find machine by DNS name", u"Defender ATP Find Machines", u"Defender ATP Find Machines by File Hash", u"Defender ATP List Indicators", u"Defender ATP Machine Isolate Action", u"Defender ATP Machine Scan", u"Defender ATP Machine Vulnerabilities", u"Defender ATP Quarantine Machine File", u"Defender ATP Set Indicator", u"Defender ATP Sync Incident Close", u"Defender ATP Update Alert", u"Defender Get Related Alert Information", u"Delete Indicator", u"Update Indicator"],
        "incident_fields": [u"defender_alert_id", u"defender_category", u"defender_classification", u"defender_determination", u"defender_incident_id"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"defender_atp_alerts", u"defender_atp_indicators", u"defender_atp_machines"],
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
        - fn_msdefender
    - Functions:
        - defender_alert_search
        - defender_app_execution
        - defender_collect_machine_investigation_package
        - defender_delete_indicator
        - defender_find_machines
        - defender_find_machines_by_file
        - defender_find_machines_by_filter
        - defender_get_related_alert_information
        - defender_list_indicators
        - defender_machine_isolation
        - defender_machine_scan
        - defender_machine_vulnerabilities
        - defender_quarantine_file
        - defender_set_indicator
        - defender_update_alert
        - fn_test
    - Workflows:
        - defender_atp_alerts_by_machine
        - defender_atp_app_execution
        - defender_atp_collect_machine_investigation_package
        - defender_atp_delete_indicator
        - defender_atp_find_machines
        - defender_atp_find_machines_by_file_hash
        - defender_atp_machine_isolation
        - defender_atp_machine_scan
        - defender_atp_machine_unisolate
        - defender_atp_machine_vulnerabilities
        - defender_atp_set_indicator
        - defender_atp_sync_incident_close
        - defender_atp_update_alert
        - defender_atp_update_indicator
        - defender_find_machines_by_filter
        - defender_get_related_alert_information
        - defender_list_indicators
        - defender_quarantine_file
        - example_get_incident_contact_info
    - Rules:
        - Create Artifact from Indicator
        - Defender ATP Alerts by Machine
        - Defender ATP App Execution Restriction
        - Defender ATP Collect Machine Investigation Package
        - Defender ATP Find machine by DNS name
        - Defender ATP Find Machines
        - Defender ATP Find Machines by File Hash
        - Defender ATP List Indicators
        - Defender ATP Machine Isolate Action
        - Defender ATP Machine Scan
        - Defender ATP Machine Vulnerabilities
        - Defender ATP Quarantine Machine File
        - Defender ATP Set Indicator
        - Defender ATP Sync Incident Close
        - Defender ATP Update Alert
        - Defender Get Related Alert Information
        - Delete Indicator
        - Update Indicator
    - Incident Fields:
        - defender_alert_id
        - defender_category
        - defender_classification
        - defender_determination
        - defender_incident_id
    - Data Tables:
        - defender_atp_alerts
        - defender_atp_indicators
        - defender_atp_machines
    - Scripts:
        - Create Artifact from Indicator
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)