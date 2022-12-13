# -*- coding: utf-8 -*-

"""Generate the SOAR customizations required for fn_bigfix"""

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
    Parameters required reload codegen for the fn_bigfix package
    """
    return {
        "package": u"fn_bigfix",
        "message_destinations": [u"fn_bigfix"],
        "functions": [u"fn_bigfix_action_status", u"fn_bigfix_artifact", u"fn_bigfix_assets", u"fn_bigfix_remediation"],
        "workflows": [u"bigfix_query_for_artifact", u"bigfix_remediate", u"bigfix_retrieve_resource_details", u"bigfix_update_action_status"],
        "actions": [u"Example: BigFix Query for Artifact", u"Example: BigFix Remediate", u"Example: BigFix Retrieve Resource Details", u"Example: BigFix Update Action status"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"res_bigfix_query_results"],
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
        - fn_bigfix
    - Functions:
        - fn_bigfix_action_status
        - fn_bigfix_artifact
        - fn_bigfix_assets
        - fn_bigfix_remediation
    - Workflows:
        - bigfix_query_for_artifact
        - bigfix_remediate
        - bigfix_retrieve_resource_details
        - bigfix_update_action_status
    - Rules:
        - Example: BigFix Query for Artifact
        - Example: BigFix Remediate
        - Example: BigFix Retrieve Resource Details
        - Example: BigFix Update Action status
    - Data Tables:
        - res_bigfix_query_results
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)