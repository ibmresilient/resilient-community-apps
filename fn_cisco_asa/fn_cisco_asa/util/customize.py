# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.0.4034

"""Generate the Resilient customizations required for fn_cisco_asa"""

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
    Parameters required reload codegen for the fn_cisco_asa package
    """
    return {
        "package": u"fn_cisco_asa",
        "message_destinations": [u"fn_cisco_asa"],
        "functions": [u"cisco_asa_add_artifact_to_network_object_group", u"cisco_asa_get_network_object_details", u"cisco_asa_get_network_objects", u"cisco_asa_remove_network_object_from_network_object_group"],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"cisco_asa_network_object_dt"],
        "automatic_tasks": [],
        "scripts": [u"Convert JSON to rich text v1.3"],
        "playbooks": [u"cisco_asa_add_fqdn_to_network_object_group", u"cisco_asa_add_ip_address_to_network_object_group", u"cisco_asa_add_ip_range_to_network_object_group", u"cisco_asa_add_ipv4network_to_network_object_group", u"cisco_asa_add_ipv6network_to_network_object_group", u"cisco_asa_get_network_object_details", u"cisco_asa_get_network_object_group", u"cisco_asa_remove_network_object_from_network_object_group"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - fn_cisco_asa
    - Functions:
        - cisco_asa_add_artifact_to_network_object_group
        - cisco_asa_get_network_object_details
        - cisco_asa_get_network_objects
        - cisco_asa_remove_network_object_from_network_object_group
    - Playbooks:
        - cisco_asa_add_fqdn_to_network_object_group
        - cisco_asa_add_ip_address_to_network_object_group
        - cisco_asa_add_ip_range_to_network_object_group
        - cisco_asa_add_ipv4network_to_network_object_group
        - cisco_asa_add_ipv6network_to_network_object_group
        - cisco_asa_get_network_object_details
        - cisco_asa_get_network_object_group
        - cisco_asa_remove_network_object_from_network_object_group
    - Data Tables:
        - cisco_asa_network_object_dt
    - Scripts:
        - Convert JSON to rich text v1.3
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)