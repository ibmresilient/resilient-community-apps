# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_pa_panorama"""

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
    Parameters required reload codegen for the fn_pa_panorama package
    """
    return {
        "package": u"fn_pa_panorama",
        "message_destinations": [u"palo_alto_panorama"],
        "functions": [u"panorama_create_address", u"panorama_edit_address_group", u"panorama_edit_users_in_a_group", u"panorama_get_address_groups", u"panorama_get_addresses", u"panorama_get_users_in_a_group"],
        "workflows": [u"example_panorama_block_dns_name", u"example_panorama_block_ip_address", u"example_panorama_block_user", u"example_panorama_unblock_dns_name", u"example_panorama_unblock_ip_address", u"example_panorama_unblock_user"],
        "actions": [u"Example: Panorama Block DNS Name", u"Example: Panorama Block IP Address", u"Example: Panorama Block User", u"Example: Panorama Unblock DNS Name", u"Example: Panorama Unblock IP Address", u"Example: Panorama Unblock User"],
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
        - palo_alto_panorama
    - Functions:
        - panorama_create_address
        - panorama_edit_address_group
        - panorama_edit_users_in_a_group
        - panorama_get_address_groups
        - panorama_get_addresses
        - panorama_get_users_in_a_group
    - Workflows:
        - example_panorama_block_dns_name
        - example_panorama_block_ip_address
        - example_panorama_block_user
        - example_panorama_unblock_dns_name
        - example_panorama_unblock_ip_address
        - example_panorama_unblock_user
    - Rules:
        - Example: Panorama Block DNS Name
        - Example: Panorama Block IP Address
        - Example: Panorama Block User
        - Example: Panorama Unblock DNS Name
        - Example: Panorama Unblock IP Address
        - Example: Panorama Unblock User
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)