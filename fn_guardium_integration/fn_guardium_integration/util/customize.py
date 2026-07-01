# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.0.974

"""Generate the SOAR customizations required for fn_guardium_integration"""

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
    Parameters required reload codegen for the fn_guardium_integration package
    """
    return {
        "package": u"fn_guardium_integration",
        "message_destinations": [
            u"fn_guardium"
        ],
        "functions": [
            u"function_guardium_block_user",
            u"function_guardium_generate_client_secret",
            u"function_guardium_list_parameter_names_by_report_name",
            u"function_guardium_search_outlier_details",
            u"function_guardium_search_report",
            u"function_guardium_search_sensitive_object"
        ],
        "workflows": [
            u"example_generate_guardium_client_secret",
            u"example_guardium_block_user_acces_to_db",
            u"example_guardium_list_parameter_names_by_report_name",
            u"example_guardium_run_active_risk_spotter",
            u"example_guardium_search_outlier_details",
            u"example_guardium_search_report",
            u"example_guardium_search_sensitive_objects"
        ],
        "actions": [
            u"Guardium: 1. Run Active Risk Spotter - Risky Users Scores",
            u"Guardium: 2. Search for Entitlements to Sensitive Objects",
            u"Guardium: 3. Search for User Outlier Details",
            u"Guardium: 4A. List Parameter Names By Report Name",
            u"Guardium: 4B. Search All Guardium Reports",
            u"Guardium: 5. Block User from Data Source",
            u"Guardium: Generate Client Secret"
        ],
        "incident_fields": [
            u"grd_inc_field_client_hostname",
            u"grd_inc_field_client_ip",
            u"grd_inc_field_confidence_score",
            u"grd_inc_field_database",
            u"grd_inc_field_database_type",
            u"grd_inc_field_db_user",
            u"grd_inc_field_diverse_behavior",
            u"grd_inc_field_error_outlier",
            u"grd_inc_field_high_volume_outlier",
            u"grd_inc_field_ongoing_outlier",
            u"grd_inc_field_os_user",
            u"grd_inc_field_privileged_user",
            u"grd_inc_field_rare_or_new_behavior",
            u"grd_inc_field_server",
            u"grd_inc_field_source_program",
            u"grd_inc_field_unusual_working_hours",
            u"grd_inc_field_vulnerable_obj_outlier"
        ],
        "incident_artifact_types": [],
        "incident_types": [
            u"Guardium Outliers",
            u"Guardium Policy Violations"
        ],
        "datatables": [
            u"grd_outlier_details",
            u"grd_sensitive_objects",
            u"guardium_search_report_data"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"Check Guardium Client Secret"
        ],
        "playbooks": [],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9340

    Contents:
    - Message Destinations:
        - fn_guardium
    - Functions:
        - function_guardium_block_user
        - function_guardium_generate_client_secret
        - function_guardium_list_parameter_names_by_report_name
        - function_guardium_search_outlier_details
        - function_guardium_search_report
        - function_guardium_search_sensitive_object
    - Workflows:
        - example_generate_guardium_client_secret
        - example_guardium_block_user_acces_to_db
        - example_guardium_list_parameter_names_by_report_name
        - example_guardium_run_active_risk_spotter
        - example_guardium_search_outlier_details
        - example_guardium_search_report
        - example_guardium_search_sensitive_objects
    - Rules:
        - Guardium: 1. Run Active Risk Spotter - Risky Users Scores
        - Guardium: 2. Search for Entitlements to Sensitive Objects
        - Guardium: 3. Search for User Outlier Details
        - Guardium: 4A. List Parameter Names By Report Name
        - Guardium: 4B. Search All Guardium Reports
        - Guardium: 5. Block User from Data Source
        - Guardium: Generate Client Secret
    - Incident Fields:
        - grd_inc_field_client_hostname
        - grd_inc_field_client_ip
        - grd_inc_field_confidence_score
        - grd_inc_field_database
        - grd_inc_field_database_type
        - grd_inc_field_db_user
        - grd_inc_field_diverse_behavior
        - grd_inc_field_error_outlier
        - grd_inc_field_high_volume_outlier
        - grd_inc_field_ongoing_outlier
        - grd_inc_field_os_user
        - grd_inc_field_privileged_user
        - grd_inc_field_rare_or_new_behavior
        - grd_inc_field_server
        - grd_inc_field_source_program
        - grd_inc_field_unusual_working_hours
        - grd_inc_field_vulnerable_obj_outlier
    - Data Tables:
        - grd_outlier_details
        - grd_sensitive_objects
        - guardium_search_report_data
    - Scripts:
        - Check Guardium Client Secret
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)