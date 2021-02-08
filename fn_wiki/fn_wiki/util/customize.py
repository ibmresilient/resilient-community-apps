# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_wiki"""

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
        "message_destinations": [u"fn_wiki"],
        "functions": [u"fn_wiki_lookup", u"fn_wiki_get_contents", u"fn_wiki_create_update"],
        "workflows": [u"example_wiki_create_page", u"example_wiki_lookup", u"example_wiki_get_contents"],
        "actions": [u"Example: Wiki Lookup", u"Example: Wiki Get Contents", u"Example: Wiki Create Page"],
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
        - fn_wiki
    - Functions:
        - fn_wiki_lookup
        - fn_wiki_get_contents
        - fn_wiki_create_update
    - Workflows:
        - example_wiki_create_page
        - example_wiki_lookup
        - example_wiki_get_contents
    - Rules:
        - Example: Wiki Lookup
        - Example: Wiki Get Contents
        - Example: Wiki Create Page
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)