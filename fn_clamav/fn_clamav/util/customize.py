# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_clamav"""

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
    Parameters required reload codegen for the fn_clamav package
    """
    return {
        "package": u"fn_clamav",
        "message_destinations": [u"fn_clamav"],
        "functions": [u"clamav_scan_stream"],
        "workflows": [u"example_clamav_scan_artifact_attachment", u"example_clamav_scan_attachment"],
        "actions": [u"Example: ClamAV scan artifact attachment", u"Example: ClamAV scan attachment"],
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

    IBM Resilient Platform Version: 41.0.6783

    Contents:
    - Message Destinations:
        - fn_clamav
    - Functions:
        - clamav_scan_stream
    - Workflows:
        - example_clamav_scan_artifact_attachment
        - example_clamav_scan_attachment
    - Rules:
        - Example: ClamAV scan artifact attachment
        - Example: ClamAV scan attachment
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)