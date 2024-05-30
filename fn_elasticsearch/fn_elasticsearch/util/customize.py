# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_elasticsearch"""

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
    Parameters required reload codegen for the fn_elasticsearch package
    """
    return {
        "package": u"fn_elasticsearch",
        "message_destinations": [u"fn_elasticsearch"],
        "functions": [u"fn_elasticsearch_query"],
        "workflows": [u"example_elasticsearch_query_from_artifact", u"example_elasticsearch_query_from_incident"],
        "actions": [u"Example: ElasticSearch Query from Artifact", u"Example: ElasticSearch Query from Incident"],
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

    IBM SOAR Platform Version: 43.0.0

    Contents:
    - Message Destinations:
        - fn_elasticsearch
    - Functions:
        - fn_elasticsearch_query
    - Workflows:
        - example_elasticsearch_query_from_artifact
        - example_elasticsearch_query_from_incident
    - Rules:
        - Example: ElasticSearch Query from Artifact
        - Example: ElasticSearch Query from Incident
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)