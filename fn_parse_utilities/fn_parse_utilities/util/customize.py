# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_parse_utilities"""

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
        "message_destinations": [u"fn_parse_utilities"],
        "functions": [u"parse_utilities_email_parse", u"parse_utilities_parse_ssl_certificate", u"parse_utilities_pdfid", u"parse_utilities_xml_transformation"],
        "workflows": [u"example_parse_utilities_email_parsing_artifact", u"example_parse_utilities_email_parsing_attachment", u"example_parse_utilities_parse_ssl_certificate", u"example_parse_utilities_pdfid", u"example_parse_utilities_pdfid_attachment", u"example_parse_utilities_xml_attachment", u"example_parse_utilities_xml_transformation"],
        "actions": [u"Example: Parse Utilities Email Parsing (Artifact)", u"Example: Parse Utilities Email Parsing (Attachment)", u"Example: Parse Utilities Parse SSL Certificate", u"Example: Parse Utilities PDFID (Artifact)", u"Example: Parse Utilities PDFID (Attachment)", u"Example: Parse Utilities XML Transformation", u"Example: Parse Utilities XML Transformation (Attachment)"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [u"Convert JSON to rich text v1.0"],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

    Contents:
    - Message Destinations:
        - fn_parse_utilities
    - Functions:
        - parse_utilities_email_parse
        - parse_utilities_parse_ssl_certificate
        - parse_utilities_pdfid
        - parse_utilities_xml_transformation
    - Workflows:
        - example_parse_utilities_email_parsing_artifact
        - example_parse_utilities_email_parsing_attachment
        - example_parse_utilities_parse_ssl_certificate
        - example_parse_utilities_pdfid
        - example_parse_utilities_pdfid_attachment
        - example_parse_utilities_xml_attachment
        - example_parse_utilities_xml_transformation
    - Rules:
        - Example: Parse Utilities Email Parsing (Artifact)
        - Example: Parse Utilities Email Parsing (Attachment)
        - Example: Parse Utilities Parse SSL Certificate
        - Example: Parse Utilities PDFID (Artifact)
        - Example: Parse Utilities PDFID (Attachment)
        - Example: Parse Utilities XML Transformation
        - Example: Parse Utilities XML Transformation (Attachment)
    - Scripts:
        - Convert JSON to rich text v1.0
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)