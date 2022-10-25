# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_randori"""

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
    Parameters required reload codegen for the fn_randori package
    """
    return {
        "package": u"fn_randori",
        "message_destinations": [u"fn_randori"],
        "functions": [u"randori_get_target_data"],
        "workflows": [],
        "actions": [],
        "incident_fields": [u"randori_target_affiliation_state", u"randori_target_id", u"randori_target_impact_score", u"randori_target_link", u"randori_target_status", u"randori_target_tags", u"randori_target_tech_category"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [u"Randori: Get Target Data"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

    Contents:
    - Message Destinations:
        - fn_randori
    - Functions:
        - randori_get_target_data
    - Incident Fields:
        - randori_target_affiliation_state
        - randori_target_id
        - randori_target_impact_score
        - randori_target_link
        - randori_target_status
        - randori_target_tags
        - randori_target_tech_category
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)