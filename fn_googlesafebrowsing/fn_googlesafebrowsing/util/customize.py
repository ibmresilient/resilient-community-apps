# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_googlesafebrowsing"""

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
    Parameters required reload codegen for the fn_googlesafebrowsing package
    """
    return {
        "package": u"fn_googlesafebrowsing",
        "message_destinations": [u"googlesafebrowsing"],
        "functions": [u"fn_googlesafebrowsing"],
        "workflows": [u"google_safe_browsing_url_lookup"],
        "actions": [u"GoogleSafeBrowsing URL Lookup"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
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
        - googlesafebrowsing
    - Functions:
        - fn_googlesafebrowsing
    - Workflows:
        - google_safe_browsing_url_lookup
    - Rules:
        - GoogleSafeBrowsing URL Lookup
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)