# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_parse_utilities"""

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
    Parameters required reload codegen for the fn_parse_utilities package
    """
    return {
        "package": u"fn_parse_utilities",
        "message_destinations": [
            u"fn_parse_utilities"
        ],
        "functions": [
            u"parse_utilities_email_parse",
            u"parse_utilities_parse_ssl_certificate",
            u"parse_utilities_pdfid",
            u"parse_utilities_xml_transformation"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [
            u"Convert JSON to rich text v1.3"
        ],
        "playbooks": [
            u"parse_utilities_email_parsing_artifact_pb",
            u"parse_utilities_email_parsing_attachment_pb",
            u"parse_utilities_parse_ssl_certificate",
            u"parse_utilities_pdfid_artifact",
            u"parse_utilities_pdfid_attachment",
            u"parse_utilities_xml_transformation_artifact",
            u"parse_utilities_xml_transformation_attachment_pb"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_parse_utilities
    - Functions:
        - parse_utilities_email_parse
        - parse_utilities_parse_ssl_certificate
        - parse_utilities_pdfid
        - parse_utilities_xml_transformation
    - Playbooks:
        - parse_utilities_email_parsing_artifact_pb
        - parse_utilities_email_parsing_attachment_pb
        - parse_utilities_parse_ssl_certificate
        - parse_utilities_pdfid_artifact
        - parse_utilities_pdfid_attachment
        - parse_utilities_xml_transformation_artifact
        - parse_utilities_xml_transformation_attachment_pb
    - Scripts:
        - Convert JSON to rich text v1.3
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)