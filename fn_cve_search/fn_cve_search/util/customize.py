# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_cve_search"""

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
    Parameters required reload codegen for the fn_cve_search package
    """
    return {
        "package": u"fn_cve_search",
        "message_destinations": [
            u"fn_cve"
        ],
        "functions": [
            u"function_cve_browse",
            u"function_cve_search"
        ],
        "workflows": [
            u"example_cve_browse",
            u"example_cve_search"
        ],
        "actions": [
            u"Example: CVE Browse",
            u"Example: CVE Search"
        ],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"cve_data"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_cve
    - Functions:
        - function_cve_browse
        - function_cve_search
    - Workflows:
        - example_cve_browse
        - example_cve_search
    - Rules:
        - Example: CVE Browse
        - Example: CVE Search
    - Data Tables:
        - cve_data
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)