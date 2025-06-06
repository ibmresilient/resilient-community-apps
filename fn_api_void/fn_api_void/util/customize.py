# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_api_void"""

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
    Parameters required reload codegen for the fn_api_void package
    """
    return {
        "package": u"fn_api_void",
        "message_destinations": [
            u"fn_api_void"
        ],
        "functions": [
            u"fn_api_void_request"
        ],
        "workflows": [
            u"example_apivoid_dns_lookup",
            u"example_apivoid_domain_reputation",
            u"example_apivoid_email_verify",
            u"example_apivoid_ip_reputation",
            u"example_apivoid_ssl_info",
            u"example_apivoid_threatlog",
            u"example_apivoid_url_reputation"
        ],
        "actions": [
            u"Example: APIVoid DNS Lookup",
            u"Example: APIVoid Domain Reputation",
            u"Example: APIVoid Email Verify",
            u"Example: APIVoid IP Reputation",
            u"Example: APIVoid SSL Info",
            u"Example: APIVoid ThreatLog",
            u"Example: APIVoid URL Reputation"
        ],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [
            u"Convert JSON to rich text v1.3"
        ],
        "playbooks": [],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9339

    Contents:
    - Message Destinations:
        - fn_api_void
    - Functions:
        - fn_api_void_request
    - Workflows:
        - example_apivoid_dns_lookup
        - example_apivoid_domain_reputation
        - example_apivoid_email_verify
        - example_apivoid_ip_reputation
        - example_apivoid_ssl_info
        - example_apivoid_threatlog
        - example_apivoid_url_reputation
    - Rules:
        - Example: APIVoid DNS Lookup
        - Example: APIVoid Domain Reputation
        - Example: APIVoid Email Verify
        - Example: APIVoid IP Reputation
        - Example: APIVoid SSL Info
        - Example: APIVoid ThreatLog
        - Example: APIVoid URL Reputation
    - Scripts:
        - Convert JSON to rich text v1.3
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)