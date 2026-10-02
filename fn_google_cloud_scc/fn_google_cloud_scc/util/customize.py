# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_google_cloud_scc"""

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
    Parameters required reload codegen for the fn_google_cloud_scc package
    """
    return {
        "package": u"fn_google_cloud_scc",
        "message_destinations": [u"fn_google_cloud_scc"],
        "functions": [u"google_cloud_scc_list_assets", u"google_cloud_scc_update_finding", u"google_cloud_scc_update_security_mark", u"google_scc_get_findings"],
        "workflows": [u"google_scc_add_finding_source_property_in_scc", u"google_scc_auto_update_severity_in_scc", u"google_scc_close_finding_in_scc", u"google_scc_delete_security_mark", u"google_scc_list_assets", u"google_scc_refresh_finding", u"google_scc_update_finding_source_property_in_scc_from_dt", u"google_scc_update_next_steps_in_scc", u"google_scc_update_security_mark", u"google_scc_update_severity_in_scc", u"google_scc_update_state_in_scc"],
        "actions": [u"SCC: Add Source Property", u"SCC: Close Finding", u"SCC: Delete Security Mark", u"SCC: List Assets", u"SCC: Refresh Finding", u"SCC: Update Next Steps", u"SCC: Update Security Marks", u"SCC: Update Severity", u"SCC: Update Severity on Change", u"SCC: Update Source Property", u"SCC: Update State"],
        "incident_fields": [u"google_scc_category", u"google_scc_class", u"google_scc_compliance_standards", u"google_scc_id", u"google_scc_name", u"google_scc_next_steps", u"google_scc_project_display_name", u"google_scc_project_name", u"google_scc_recommendation", u"google_scc_remediation_link", u"google_scc_resource_display_name", u"google_scc_resource_name", u"google_scc_security_marks", u"google_scc_state", u"google_scc_type", u"google_scc_url", u"google_scc_vulnerability"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"google_scc_finding_source_properties_dt"],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 43.1.49

    Contents:
    - Message Destinations:
        - fn_google_cloud_scc
    - Functions:
        - google_cloud_scc_list_assets
        - google_cloud_scc_update_finding
        - google_cloud_scc_update_security_mark
        - google_scc_get_findings
    - Workflows:
        - google_scc_add_finding_source_property_in_scc
        - google_scc_auto_update_severity_in_scc
        - google_scc_close_finding_in_scc
        - google_scc_delete_security_mark
        - google_scc_list_assets
        - google_scc_refresh_finding
        - google_scc_update_finding_source_property_in_scc_from_dt
        - google_scc_update_next_steps_in_scc
        - google_scc_update_security_mark
        - google_scc_update_severity_in_scc
        - google_scc_update_state_in_scc
    - Rules:
        - SCC: Add Source Property
        - SCC: Close Finding
        - SCC: Delete Security Mark
        - SCC: List Assets
        - SCC: Refresh Finding
        - SCC: Update Next Steps
        - SCC: Update Security Marks
        - SCC: Update Severity
        - SCC: Update Severity on Change
        - SCC: Update Source Property
        - SCC: Update State
    - Incident Fields:
        - google_scc_category
        - google_scc_class
        - google_scc_compliance_standards
        - google_scc_id
        - google_scc_name
        - google_scc_next_steps
        - google_scc_project_display_name
        - google_scc_project_name
        - google_scc_recommendation
        - google_scc_remediation_link
        - google_scc_resource_display_name
        - google_scc_resource_name
        - google_scc_security_marks
        - google_scc_state
        - google_scc_type
        - google_scc_url
        - google_scc_vulnerability
    - Data Tables:
        - google_scc_finding_source_properties_dt
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)