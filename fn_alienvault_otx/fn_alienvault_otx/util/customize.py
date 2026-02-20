# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""Generate the SOAR customizations required for fn_alienvault_otx"""

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
    Parameters required reload codegen for the fn_alienvault_otx package
    """
    return {
        "package": u"fn_alienvault_otx",
        "message_destinations": [
            u"fn_alienvault_otx"
        ],
        "functions": [
            u"fn_alienvault_otx_threat_lookup"
        ],
        "workflows": [
            u"example_alien_vault_otx_cve",
            u"example_alien_vault_otx_dns_name",
            u"example_alien_vault_otx_hash",
            u"example_alien_vault_otx_host_name",
            u"example_alien_vault_otx_ip",
            u"example_alien_vault_otx_url"
        ],
        "actions": [
            u"Example: Alien Vault - CVE Lookup",
            u"Example: Alien Vault - DNS Name Lookup",
            u"Example: Alien Vault - File Hash Lookup",
            u"Example: Alien Vault - Host Name Lookup",
            u"Example: Alien Vault - IP Address Lookup",
            u"Example: Alien Vault - URL Lookup"
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
        - fn_alienvault_otx
    - Functions:
        - fn_alienvault_otx_threat_lookup
    - Workflows:
        - example_alien_vault_otx_cve
        - example_alien_vault_otx_dns_name
        - example_alien_vault_otx_hash
        - example_alien_vault_otx_host_name
        - example_alien_vault_otx_ip
        - example_alien_vault_otx_url
    - Rules:
        - Example: Alien Vault - CVE Lookup
        - Example: Alien Vault - DNS Name Lookup
        - Example: Alien Vault - File Hash Lookup
        - Example: Alien Vault - Host Name Lookup
        - Example: Alien Vault - IP Address Lookup
        - Example: Alien Vault - URL Lookup
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)