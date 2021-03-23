# -*- coding: utf-8 -*-

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
        "functions": [u"cisco_asa_add_artifact_to_network_object_group", u"cisco_asa_add_network_object_to_network_object_group", u"cisco_asa_get_network_object_details", u"cisco_asa_get_network_objects", u"cisco_asa_remove_network_object_from_network_object_group"],
        "workflows": [u"cisco_asa_add_artifact_to_network_object_group", u"cisco_asa_add_network_object_to_network_object_group", u"cisco_asa_get_network_object_details", u"cisco_asa_get_network_object_group", u"cisco_asa_remove_network_object_from_network_object_group"],
        "actions": [u"Cisco ASA: Add IPv4Address to Network Object Group", u"Cisco ASA: Add IPv4FQDN to Network Object Group", u"Cisco ASA: Add IPv4Network to Network Object Group", u"Cisco ASA: Add IPv4Range to Network Object Group", u"Cisco ASA: Add Network Object to Network Object Group", u"Cisco ASA: Get Network Object Details", u"Cisco ASA: Get Network Object Group", u"Cisco ASA: Remove Network Object from Network Object Group"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [u"cisco_asa_network_object_dt"],
        "automatic_tasks": [],
        "scripts": [u"Convert JSON to rich text v1.1"],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 37.0.5832

    Contents:
    - Message Destinations:
        - fn_cisco_asa
    - Functions:
        - cisco_asa_add_artifact_to_network_object_group
        - cisco_asa_add_network_object_to_network_object_group
        - cisco_asa_get_network_object_details
        - cisco_asa_get_network_objects
        - cisco_asa_remove_network_object_from_network_object_group
    - Workflows:
        - cisco_asa_add_artifact_to_network_object_group
        - cisco_asa_add_network_object_to_network_object_group
        - cisco_asa_get_network_object_details
        - cisco_asa_get_network_object_group
        - cisco_asa_remove_network_object_from_network_object_group
    - Rules:
        - Cisco ASA: Add IPv4Address to Network Object Group
        - Cisco ASA: Add IPv4FQDN to Network Object Group
        - Cisco ASA: Add IPv4Network to Network Object Group
        - Cisco ASA: Add IPv4Range to Network Object Group
        - Cisco ASA: Add Network Object to Network Object Group
        - Cisco ASA: Get Network Object Details
        - Cisco ASA: Get Network Object Group
        - Cisco ASA: Remove Network Object from Network Object Group
    - Data Tables:
        - cisco_asa_network_object_dt
    - Scripts:
        - Convert JSON to rich text v1.1
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)