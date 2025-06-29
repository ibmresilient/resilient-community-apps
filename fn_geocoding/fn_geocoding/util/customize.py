# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_geocoding"""

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
    Parameters required reload codegen for the fn_geocoding package
    """
    return {
        "package": u"fn_geocoding",
        "message_destinations": [
            u"fn_geocoding"
        ],
        "functions": [
            u"geocoding"
        ],
        "workflows": [
            u"example_geocoding_get_address",
            u"example_geocoding_get_coordinates"
        ],
        "actions": [
            u"Example: Geocoding Get Address",
            u"Example: Geocoding Get Coordinates"
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
        - fn_geocoding
    - Functions:
        - geocoding
    - Workflows:
        - example_geocoding_get_address
        - example_geocoding_get_coordinates
    - Rules:
        - Example: Geocoding Get Address
        - Example: Geocoding Get Coordinates
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)