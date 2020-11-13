# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_isitphishing"""

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
    Parameters required reload codegen for the fn_isitphishing package
    """
    return {
        "package": u"fn_isitphishing",
        "message_destinations": [u"fn_isitphishing"],
        "functions": [u"isitphishing_html_document", u"isitphishing_url"],
        "workflows": [u"example_isitphishing_analyze_html_document_artifact", u"example_isitphishing_analyze_html_document", u"example_isitphishing_analyze_url"],
        "actions": [u"Example: IsItPhishing Analyze HTML Document: Artifact", u"Example: IsItPhishing Analyze URL", u"Example: IsItPhishing Analyze HTML Document: Attachment"],
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
        - fn_isitphishing
    - Functions:
        - isitphishing_html_document
        - isitphishing_url
    - Workflows:
        - example_isitphishing_analyze_html_document_artifact
        - example_isitphishing_analyze_html_document
        - example_isitphishing_analyze_url
    - Rules:
        - Example: IsItPhishing Analyze HTML Document: Artifact
        - Example: IsItPhishing Analyze URL
        - Example: IsItPhishing Analyze HTML Document: Attachment
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)