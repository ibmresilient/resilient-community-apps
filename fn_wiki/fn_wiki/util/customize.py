# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_wiki"""

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
    Parameters required reload codegen for the fn_wiki package
    """
    return {
        "package": u"fn_wiki",
        "message_destinations": [
            u"fn_wiki"
        ],
        "functions": [
            u"fn_wiki_create_update",
            u"fn_wiki_get_contents",
            u"fn_wiki_lookup"
        ],
        "workflows": [
            u"example_wiki_create_page",
            u"example_wiki_get_contents",
            u"example_wiki_lookup"
        ],
        "actions": [
            u"Example: Wiki Create Page",
            u"Example: Wiki Get Contents",
            u"Example: Wiki Lookup"
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
        - fn_wiki
    - Functions:
        - fn_wiki_create_update
        - fn_wiki_get_contents
        - fn_wiki_lookup
    - Workflows:
        - example_wiki_create_page
        - example_wiki_get_contents
        - example_wiki_lookup
    - Rules:
        - Example: Wiki Create Page
        - Example: Wiki Get Contents
        - Example: Wiki Lookup
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)