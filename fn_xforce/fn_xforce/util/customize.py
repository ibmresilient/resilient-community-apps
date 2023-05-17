# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4368

"""Generate the Resilient customizations required for fn_xforce"""

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
    Parameters required reload codegen for the fn_xforce package
    """
    return {
        "package": u"fn_xforce",
        "message_destinations": [u"fn_xforce"],
        "functions": [u"xforce_get_collection_by_id", u"xforce_query_collection"],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [u"query collections output"],
        "playbooks": [u"example_xforce_query_collection_by_id", u"example_xforce_query_from_artifact_pb", u"example_xforce_return_top_3_from_collections_pb"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

    Contents:
    - Message Destinations:
        - fn_xforce
    - Functions:
        - xforce_get_collection_by_id
        - xforce_query_collection
    - Playbooks:
        - example_xforce_query_collection_by_id
        - example_xforce_query_from_artifact_pb
        - example_xforce_return_top_3_from_collections_pb
    - Scripts:
        - query collections output
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)