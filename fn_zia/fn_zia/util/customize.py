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
        "functions": [u"funct_zia_add_to_blocklist", u"funct_zia_get_blocklist", u"funct_zia_remove_from_blocklist"],
        "workflows": [u"wf_zia_add_to_blocklist", u"wf_zia_get_blocklist", u"wf_zia_remove_from_blocklist", u"wf_zia_remove_url_from_blocklist"],
        "actions": [u"Example: ZIA: Add To Blocklist", u"Example: ZIA: Get Blocklist", u"Example: ZIA: Remove From Blocklist", u"Example: ZIA: Remove URL From Blocklist"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [u"zia_blocklist"],
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
        - funct_zia_add_to_blocklist
        - funct_zia_get_blocklist
        - funct_zia_remove_from_blocklist
    - Workflows:
        - wf_zia_add_to_blocklist
        - wf_zia_get_blocklist
        - wf_zia_remove_from_blocklist
        - wf_zia_remove_url_from_blocklist
    - Rules:
        - Example: ZIA: Add To Blocklist
        - Example: ZIA: Get Blocklist
        - Example: ZIA: Remove From Blocklist
        - Example: ZIA: Remove URL From Blocklist
    - Data Tables:
        - zia_blocklist
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)