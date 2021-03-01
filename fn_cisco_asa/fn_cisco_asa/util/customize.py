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
        "functions": [u"cisco_asa_get_network_objects"],
        "workflows": [u"example_cisco_asa_get_blacklist_inbound", u"example_cisco_asa_get_blacklist_outbound"],
        "actions": [u"Example: Cisco ASA Get Blacklist Inbound", u"Example: Cisco ASA Get Blacklist Outbound"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [u"cisco_asa_inbound_dt", u"cisco_asa_outbound_dt"],
        "automatic_tasks": [],
        "scripts": []
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
        - cisco_asa_get_network_objects
    - Workflows:
        - example_cisco_asa_get_blacklist_inbound
        - example_cisco_asa_get_blacklist_outbound
    - Rules:
        - Example: Cisco ASA Get Blacklist Inbound
        - Example: Cisco ASA Get Blacklist Outbound
    - Data Tables:
        - cisco_asa_inbound_dt
        - cisco_asa_outbound_dt
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)