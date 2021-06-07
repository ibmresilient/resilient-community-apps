# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_greynoise"""

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
    Parameters required reload codegen for the fn_greynoise package
    """
    return {
        "package": u"fn_greynoise",
        "message_destinations": [u"fn_greynoise"],
        "functions": [u"greynoise_ip_query"],
        "workflows": [u"example_greynoise_ip_query"],
        "actions": [u"Example: GreyNoise IP Query"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 36.0.5634

    Contents:
    - Message Destinations:
        - fn_greynoise
    - Functions:
        - greynoise_ip_query
    - Workflows:
        - example_greynoise_ip_query
    - Rules:
        - Example: GreyNoise IP Query
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)