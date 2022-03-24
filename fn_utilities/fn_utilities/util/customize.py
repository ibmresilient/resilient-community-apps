# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_utilities"""

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
    Parameters required reload codegen for the fn_utilities package
    """
    return {
        "package": u"fn_utilities",
        "message_destinations": [u"fn_utilities"],
        "functions": [u"utilities_attachment_hash", u"utilities_attachment_to_base64", u"utilities_attachment_zip_extract", u"utilities_attachment_zip_list", u"utilities_base64_to_artifact", u"utilities_base64_to_attachment", u"utilities_call_rest_api", u"utilities_domain_distance", u"utilities_email_parse", u"utilities_excel_query", u"utilities_expand_url", u"utilities_extract_ssl_cert_from_url", u"utilities_get_contact_info", u"utilities_json2html", u"utilities_parse_ssl_certificate", u"utilities_pdfid", u"utilities_resilient_search", u"utilities_shell_command", u"utilities_string_to_attachment", u"utilities_timer", u"utilities_xml_transformation"],
        "workflows": [u"example_artifact_attachment_to_base64", u"example_attachment_hash", u"example_attachment_to_base64", u"example_call_rest_api", u"example_create_artifacts_from_excel_data", u"example_domain_distance", u"example_email_parsing_artifact", u"example_email_parsing_attachment", u"example_extract_ssl_cert_from_url", u"example_get_incident_contact_info", u"example_get_task_contact_info", u"example_json2html", u"example_parse_ssl_certificate", u"example_pdfid", u"example_resilient_search", u"example_shell_command", u"example_string_to_attachment", u"example_timer", u"example_timer_parallel", u"example_xml_transformation", u"example_zip_list", u"example_zip_to_artifact", u"utilities_expand_url"],
        "actions": [u"Example: (Artifact) Attachment to Base64", u"Example: Attachment Hash", u"Example: Attachment to Base64", u"Example: Call REST API", u"Example: Domain Distance", u"Example: Email Parsing (Artifact)", u"Example: Email Parsing (Attachment)", u"Example: Expand URL", u"Example: Extract SSL Certificate", u"Example: Get Incident Contact Info", u"Example: Get Task Contact Info", u"Example: JSON2HTML", u"Example: Parse SSL Certificate", u"Example: PDFiD", u"Example: Resilient Search", u"Example: Shell Command", u"Example: String to Attachment", u"Example: Timer Epoch", u"Example: Timers in Parallel", u"Example: Use Excel Data", u"Example: XML Transformation", u"Example: Zip Extract", u"Example: Zip List"],
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

    IBM SOAR Platform Version: 42.0.7058

    Contents:
    - Message Destinations:
        - fn_utilities
    - Functions:
        - utilities_artifact_hash
        - utilities_attachment_hash
        - utilities_attachment_to_base64
        - utilities_attachment_zip_extract
        - utilities_attachment_zip_list
        - utilities_base64_to_artifact
        - utilities_base64_to_attachment
        - utilities_call_rest_api
        - utilities_domain_distance
        - utilities_email_parse
        - utilities_excel_query
        - utilities_expand_url
        - utilities_extract_ssl_cert_from_url
        - utilities_get_contact_info
        - utilities_json2html
        - utilities_parse_ssl_certificate
        - utilities_pdfid
        - utilities_resilient_search
        - utilities_shell_command
        - utilities_string_to_attachment
        - utilities_timer
        - utilities_xml_transformation
    - Workflows:
        - example_artifact_attachment_to_base64
        - example_artifact_hash
        - example_attachment_hash
        - example_attachment_to_base64
        - example_call_rest_api
        - example_create_artifacts_from_excel_data
        - example_domain_distance
        - example_email_parsing_artifact
        - example_email_parsing_attachment
        - example_extract_ssl_cert_from_url
        - example_get_incident_contact_info
        - example_get_task_contact_info
        - example_json2html
        - example_parse_ssl_certificate
        - example_pdfid
        - example_resilient_search
        - example_shell_command
        - example_string_to_attachment
        - example_timer
        - example_timer_parallel
        - example_xml_transformation
        - example_zip_list
        - example_zip_to_artifact
        - utilities_expand_url
    - Rules:
        - Example: (Artifact) Attachment to Base64
        - Example: Artifact Hash
        - Example: Attachment Hash
        - Example: Attachment to Base64
        - Example: Call REST API
        - Example: Domain Distance
        - Example: Email Parsing (Artifact)
        - Example: Email Parsing (Attachment)
        - Example: Expand URL
        - Example: Extract SSL Certificate
        - Example: Get Incident Contact Info
        - Example: Get Task Contact Info
        - Example: JSON2HTML
        - Example: Parse SSL Certificate
        - Example: PDFiD
        - Example: Resilient Search
        - Example: Shell Command
        - Example: String to Attachment
        - Example: Timer Epoch
        - Example: Timers in Parallel
        - Example: Use Excel Data
        - Example: XML Transformation
        - Example: Zip Extract
        - Example: Zip List
    - Scripts:
        - Convert JSON to rich text v1.0
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)