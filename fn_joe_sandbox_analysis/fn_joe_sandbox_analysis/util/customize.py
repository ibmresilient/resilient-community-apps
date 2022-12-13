# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_joe_sandbox_analysis"""

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
    Parameters required reload codegen for the fn_joe_sandbox_analysis package
    """
    return {
        "package": u"fn_joe_sandbox_analysis",
        "message_destinations": [u"joe_sandbox_message_destination"],
        "functions": [u"fn_joe_sandbox_analysis"],
        "workflows": [u"example_joe_sandbox_analysis_attachment", u"example_joe_sandbox_artifact"],
        "actions": [u"Example: Joe Sandbox Analysis [Artifact]", u"Example: Joe Sandbox Analysis [Attachment]"],
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

    IBM SOAR Platform Version: 44.0.7585

    Contents:
    - Message Destinations:
        - joe_sandbox_message_destination
    - Functions:
        - fn_joe_sandbox_analysis
    - Workflows:
        - example_joe_sandbox_analysis_attachment
        - example_joe_sandbox_artifact
    - Rules:
        - Example: Joe Sandbox Analysis [Artifact]
        - Example: Joe Sandbox Analysis [Attachment]
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)