# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_zia"""

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
    Parameters required reload codegen for the fn_zia package
    """
    return {
        "package": u"fn_zia",
        "message_destinations": [u"zia"],
        "functions": [u"funct_zia_add_to_allowlist", u"funct_zia_add_to_blocklist", u"funct_zia_add_to_url_category", u"funct_zia_add_url_category", u"funct_zia_get_allowlist", u"funct_zia_get_blocklist", u"funct_zia_get_sandbox_report", u"funct_zia_get_url_categories", u"funct_zia_remove_from_allowlist", u"funct_zia_remove_from_blocklist", u"funct_zia_remove_from_url_category", u"funct_zia_url_lookup"],
        "workflows": [u"wf_zia_add_artifact_to_allowlist", u"wf_zia_add_artifact_to_blocklist", u"wf_zia_add_artifact_to_customlist", u"wf_zia_add_custom_category", u"wf_zia_add_urls_to_allowlist", u"wf_zia_add_urls_to_blocklist", u"wf_zia_add_urls_to_customlist", u"wf_zia_get_allowlist", u"wf_zia_get_blocklist", u"wf_zia_get_customlist", u"wf_zia_get_sandbox_report", u"wf_zia_get_url_categories", u"wf_zia_remove_artifact_from_allowlist", u"wf_zia_remove_artifact_from_blocklist", u"wf_zia_remove_artifact_from_customlist", u"wf_zia_remove_from_allowlist", u"wf_zia_remove_from_blocklist", u"wf_zia_remove_from_customlist", u"wf_zia_url_lookup"],
        "actions": [u"ZIA: Add Artifact To Allowlist", u"ZIA: Add Artifact To Blocklist", u"ZIA: Add Artifact To Customlist", u"ZIA: Add Custom Category", u"ZIA: Add URLs To AllowList", u"ZIA: Add URLs To BlockList", u"ZIA: Add URLs To CustomList", u"ZIA: Get Allowlist", u"ZIA: Get Blocklist", u"ZIA: Get Customlist", u"ZIA: Get Sandbox Report", u"ZIA: Get URL Categories", u"ZIA: Remove Artifact From Allowlist", u"ZIA: Remove Artifact From Blocklist", u"ZIA: Remove Artifact From Customlist", u"ZIA: Remove From Allowlist", u"ZIA: Remove From Blocklist", u"ZIA: Remove From Customlist", u"ZIA: URL Lookup"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [u"zia_allowlist", u"zia_blocklist", u"zia_customlists", u"zia_sandbox_report_summary", u"zia_url_categories"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 39.0.6328

    Contents:
    - Message Destinations:
        - zia
    - Functions:
        - funct_zia_add_to_allowlist
        - funct_zia_add_to_blocklist
        - funct_zia_add_to_url_category
        - funct_zia_add_url_category
        - funct_zia_get_allowlist
        - funct_zia_get_blocklist
        - funct_zia_get_sandbox_report
        - funct_zia_get_url_categories
        - funct_zia_remove_from_allowlist
        - funct_zia_remove_from_blocklist
        - funct_zia_remove_from_url_category
        - funct_zia_url_lookup
    - Workflows:
        - wf_zia_add_artifact_to_allowlist
        - wf_zia_add_artifact_to_blocklist
        - wf_zia_add_artifact_to_customlist
        - wf_zia_add_custom_category
        - wf_zia_add_urls_to_allowlist
        - wf_zia_add_urls_to_blocklist
        - wf_zia_add_urls_to_customlist
        - wf_zia_get_allowlist
        - wf_zia_get_blocklist
        - wf_zia_get_customlist
        - wf_zia_get_sandbox_report
        - wf_zia_get_url_categories
        - wf_zia_remove_artifact_from_allowlist
        - wf_zia_remove_artifact_from_blocklist
        - wf_zia_remove_artifact_from_customlist
        - wf_zia_remove_from_allowlist
        - wf_zia_remove_from_blocklist
        - wf_zia_remove_from_customlist
        - wf_zia_url_lookup
    - Rules:
        - ZIA: Add Artifact To Allowlist
        - ZIA: Add Artifact To Blocklist
        - ZIA: Add Artifact To Customlist
        - ZIA: Add Custom Category
        - ZIA: Add URLs To AllowList
        - ZIA: Add URLs To BlockList
        - ZIA: Add URLs To CustomList
        - ZIA: Get Allowlist
        - ZIA: Get Blocklist
        - ZIA: Get Customlist
        - ZIA: Get Sandbox Report
        - ZIA: Get URL Categories
        - ZIA: Remove Artifact From Allowlist
        - ZIA: Remove Artifact From Blocklist
        - ZIA: Remove Artifact From Customlist
        - ZIA: Remove From Allowlist
        - ZIA: Remove From Blocklist
        - ZIA: Remove From Customlist
        - ZIA: URL Lookup
    - Data Tables:
        - zia_allowlist
        - zia_blocklist
        - zia_customlists
        - zia_sandbox_report_summary
        - zia_url_categories
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)