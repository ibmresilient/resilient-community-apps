# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_reaqta"""

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
    Parameters required reload codegen for the fn_reaqta package
    """
    return {
        "package": u"fn_reaqta",
        "message_destinations": [],
        "functions": [],
        "workflows": [],
        "actions": [],
        "incident_fields": [u"reaqta_alert_link", u"reaqta_cpu_info", u"reaqta_endpoint_id", u"reaqta_id", u"reaqta_tags"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"reaqta_trigger_events"],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 41.2.41

    Contents:
    - Incident Fields:
        - reaqta_alert_link
        - reaqta_cpu_info
        - reaqta_endpoint_id
        - reaqta_id
        - reaqta_tags
    - Data Tables:
        - reaqta_trigger_events
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)