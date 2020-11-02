# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_isitPhishing"""

try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition
import base64
import os
from resilient_circuits import FunctionError

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_isitPhishing package
    """
    return {
        "package": u"fn_isitPhishing",
        "message_destinations": [u"fn_isitphishing"],
        "functions": [u"isitphishing_url", u"isitphishing_html_document"],
        "workflows": [u"example_isitphishing_analyze_html_document", u"example_isitphishing_analyze_url", u"example_isitphishing_analyze_html_document_artifact"],
        "actions": [u"Example: IsItPhishing Analyze HTML Document: Attachment", u"Example: IsItPhishing Analyze URL", u"Example: IsItPhishing Analyze HTML Document: Artifact"],
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
        - isitphishing_url
        - isitphishing_html_document
    - Workflows:
        - example_isitphishing_analyze_html_document
        - example_isitphishing_analyze_url
        - example_isitphishing_analyze_html_document_artifact
    - Rules:
        - Example: IsItPhishing Analyze HTML Document: Attachment
        - Example: IsItPhishing Analyze URL
        - Example: IsItPhishing Analyze HTML Document: Artifact
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FunctionError("{} not found".format(RES_FILE))

    with open(res_file, 'rb') as f:
        b64_data = base64.b64encode(f.read())
        yield ImportDefinition(b64_data)
