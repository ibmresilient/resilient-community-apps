# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_ioc_parser_v2"""

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
    Parameters required reload codegen for the fn_ioc_parser_v2 package
    """
    return {
        "package": u"fn_ioc_parser_v2",
        "message_destinations": [
            u"fn_ioc_parser_v2"
        ],
        "functions": [
            u"func_ioc_parser_v2"
        ],
        "workflows": [
            u"example_parse_iocs_artifact",
            u"example_parse_iocs_attachment"
        ],
        "actions": [
            u"Parse IOCs (Artifact)",
            u"Parse IOCs (Attachment)"
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
        - fn_ioc_parser_v2
    - Functions:
        - func_ioc_parser_v2
    - Workflows:
        - example_parse_iocs_artifact
        - example_parse_iocs_attachment
    - Rules:
        - Parse IOCs (Artifact)
        - Parse IOCs (Attachment)
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)