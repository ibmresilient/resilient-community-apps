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
        "functions": [u"funct_zia_add_to_allowlist", u"funct_zia_add_to_blocklist", u"funct_zia_add_to_url_category", u"funct_zia_add_url_category", u"funct_zia_get_allowlist", u"funct_zia_get_blocklist", u"funct_zia_get_url_categories", u"funct_zia_remove_from_allowlist", u"funct_zia_remove_from_blocklist", u"funct_zia_remove_from_url_category", u"funct_zia_url_lookup"],
        "workflows": [u"wf_zia_add_to_allowlist", u"wf_zia_add_to_blocklist", u"wf_zia_add_to_customlist", u"wf_zia_add_url_category", u"wf_zia_get_allowlist", u"wf_zia_get_blocklist", u"wf_zia_get_customlist", u"wf_zia_get_url_categories", u"wf_zia_remove_from_allowlist", u"wf_zia_remove_from_blocklist", u"wf_zia_remove_from_customlist", u"wf_zia_remove_url_from_allowlist", u"wf_zia_remove_url_from_blocklist", u"wf_zia_remove_url_from_customlist", u"wf_zia_url_lookup"],
        "actions": [u"Example: ZIA: Add To Allowlist", u"Example: ZIA: Add To Blocklist", u"Example: ZIA: Add To Customlist", u"Example: ZIA: Add URL Category", u"Example: ZIA: Get Allowlist", u"Example: ZIA: Get Blocklist", u"Example: ZIA: Get Customlist", u"Example: ZIA: Get URL Categories", u"Example: ZIA: Remove From Allowlist", u"Example: ZIA: Remove From Blocklist", u"Example: ZIA: Remove From Customlist", u"Example: ZIA: Remove URL From Allowlist", u"Example: ZIA: Remove URL From Blocklist", u"Example: ZIA: Remove URL From Customlist", u"Example: ZIA: URL Lookup"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [u"zia_allowlist", u"zia_blocklist", u"zia_customlists", u"zia_url_categories"],
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
        - funct_zia_get_url_categories
        - funct_zia_remove_from_allowlist
        - funct_zia_remove_from_blocklist
        - funct_zia_remove_from_url_category
        - funct_zia_url_lookup
    - Workflows:
        - wf_zia_add_to_allowlist
        - wf_zia_add_to_blocklist
        - wf_zia_add_to_customlist
        - wf_zia_add_url_category
        - wf_zia_get_allowlist
        - wf_zia_get_blocklist
        - wf_zia_get_customlist
        - wf_zia_get_url_categories
        - wf_zia_remove_from_allowlist
        - wf_zia_remove_from_blocklist
        - wf_zia_remove_from_customlist
        - wf_zia_remove_url_from_allowlist
        - wf_zia_remove_url_from_blocklist
        - wf_zia_remove_url_from_customlist
        - wf_zia_url_lookup
    - Rules:
        - Example: ZIA: Add To Allowlist
        - Example: ZIA: Add To Blocklist
        - Example: ZIA: Add To Customlist
        - Example: ZIA: Add URL Category
        - Example: ZIA: Get Allowlist
        - Example: ZIA: Get Blocklist
        - Example: ZIA: Get Customlist
        - Example: ZIA: Get URL Categories
        - Example: ZIA: Remove From Allowlist
        - Example: ZIA: Remove From Blocklist
        - Example: ZIA: Remove From Customlist
        - Example: ZIA: Remove URL From Allowlist
        - Example: ZIA: Remove URL From Blocklist
        - Example: ZIA: Remove URL From Customlist
        - Example: ZIA: URL Lookup
    - Data Tables:
        - zia_allowlist
        - zia_blocklist
        - zia_customlists
        - zia_url_categories
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)