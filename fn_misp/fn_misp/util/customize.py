# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.0.2.575

"""Generate the SOAR customizations required for fn_misp"""

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
    Parameters required reload codegen for the fn_misp package
    """
    return {
        "package": u"fn_misp",
        "message_destinations": [
            u"fn_misp"
        ],
        "functions": [
            u"misp_create_attribute",
            u"misp_create_event",
            u"misp_create_sighting",
            u"misp_create_tag",
            u"misp_search_attribute",
            u"misp_sighting_list"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"misp_event_id"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"misp_create_attribute",
            u"misp_create_event",
            u"misp_create_sighting",
            u"misp_create_tag_on_attribute",
            u"misp_create_tag_on_event",
            u"misp_search_attribute",
            u"misp_sighting_list"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 49.0.8803

    Contents:
    - Message Destinations:
        - fn_misp
    - Functions:
        - misp_create_attribute
        - misp_create_event
        - misp_create_sighting
        - misp_create_tag
        - misp_search_attribute
        - misp_sighting_list
    - Playbooks:
        - misp_create_attribute
        - misp_create_event
        - misp_create_sighting
        - misp_create_tag_on_attribute
        - misp_create_tag_on_event
        - misp_search_attribute
        - misp_sighting_list
    - Incident Fields:
        - misp_event_id
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)