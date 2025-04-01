# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_whois_rdap"""

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
    Parameters required reload codegen for the fn_whois_rdap package
    """
    return {
        "package": u"fn_whois_rdap",
        "message_destinations": [
            u"fn_whois_rdap"
        ],
        "functions": [
            u"rdap_query",
            u"whois_rdap_query"
        ],
        "workflows": [
            u"example_rdap_query",
            u"example_whois_query"
        ],
        "actions": [
            u"Run rdap query against Artifact",
            u"Run whois query against Artifact (RDAP)"
        ],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
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
        - fn_whois_rdap
    - Functions:
        - rdap_query
        - whois_rdap_query
    - Workflows:
        - example_rdap_query
        - example_whois_query
    - Rules:
        - Run rdap query against Artifact
        - Run whois query against Artifact (RDAP)
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)