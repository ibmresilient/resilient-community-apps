# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.0.1.486

"""Generate the SOAR customizations required for fn_pa_panorama"""

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
        "message_destinations": [
            u"palo_alto_panorama"
        ],
        "functions": [
            u"panorama_create_address",
            u"panorama_edit_address_group",
            u"panorama_edit_users_in_a_group",
            u"panorama_get_address_groups",
            u"panorama_get_addresses",
            u"panorama_get_users_in_a_group"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"example_panorama_block_dns_name",
            u"example_panorama_block_ip_address",
            u"example_panorama_block_user",
            u"example_panorama_get_address_groups",
            u"example_panorama_unblock_dns_name",
            u"example_panorama_unblock_ip_address",
            u"example_panorama_unblock_user"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 48.2.16

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
    - Playbooks:
        - example_panorama_block_dns_name
        - example_panorama_block_ip_address
        - example_panorama_block_user
        - example_panorama_get_address_groups
        - example_panorama_unblock_dns_name
        - example_panorama_unblock_ip_address
        - example_panorama_unblock_user
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)