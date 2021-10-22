# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_sentinelone"""

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
    Parameters required reload codegen for the fn_sentinelone package
    """
    return {
        "package": u"fn_sentinelone",
        "message_destinations": [u"fn_sentinelone"],
        "functions": [u"senitinelone_get_agents"],
        "workflows": [u"sentinelone_get_agents"],
        "actions": [u"SentinelOne: Get Agents"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 40.0.6554

    Contents:
    - Message Destinations:
        - fn_sentinelone
    - Functions:
        - senitinelone_get_agents
    - Workflows:
        - sentinelone_get_agents
    - Rules:
        - SentinelOne: Get Agents
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)