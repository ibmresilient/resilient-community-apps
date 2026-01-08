# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_pulsedive"""

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
    Parameters required reload codegen for the fn_pulsedive package
    """
    return {
        "package": u"fn_pulsedive",
        "message_destinations": [
            u"fn_pulsedive"
        ],
        "functions": [
            u"pulsedive_query_id",
            u"pulsedive_query_value",
            u"pulsedive_search"
        ],
        "workflows": [
            u"example_pulsedive_query_by_id",
            u"example_pulsedive_query_by_value",
            u"example_pulsedive_search"
        ],
        "actions": [
            u"Pulsedive Query by ID",
            u"Pulsedive Query by Value",
            u"Pulsedive Search"
        ],
        "incident_fields": [],
        "incident_artifact_types": [
            u"pulsedive_id"
        ],
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
        - fn_pulsedive
    - Functions:
        - pulsedive_query_id
        - pulsedive_query_value
        - pulsedive_search
    - Workflows:
        - example_pulsedive_query_by_id
        - example_pulsedive_query_by_value
        - example_pulsedive_search
    - Rules:
        - Pulsedive Query by ID
        - Pulsedive Query by Value
        - Pulsedive Search
    - Custom Artifact Types:
        - pulsedive_id
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)