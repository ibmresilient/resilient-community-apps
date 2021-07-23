# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_rsa_netwitness"""

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
    Parameters required reload codegen for the fn_rsa_netwitness package
    """
    return {
        "package": u"fn_rsa_netwitness",
        "message_destinations": [u"rsa_netwitness_message_destination"],
        "functions": [u"netwitness_get_meta_id_ranges", u"netwitness_get_meta_values", u"netwitness_query", u"netwitness_retrieve_log_data", u"netwitness_retrieve_pcap_data"],
        "workflows": [u"example_netwitness_get_meta_values", u"example_netwitness_retrieve_log_file", u"example_netwitness_retrieve_pcap_file", u"example_netwitness_retrieve_pcap_file_time"],
        "actions": [u"(Example) NetWitness Get Meta Values", u"(Example) NetWitness Retrieve Log File", u"(Example) NetWitness Retrieve PCAP File", u"(Example) NetWitness Retrieve PCAP File (Time)"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 39.0.0

    Contents:
    - Message Destinations:
        - rsa_netwitness_message_destination
    - Functions:
        - netwitness_get_meta_id_ranges
        - netwitness_get_meta_values
        - netwitness_query
        - netwitness_retrieve_log_data
        - netwitness_retrieve_pcap_data
    - Workflows:
        - example_netwitness_get_meta_values
        - example_netwitness_retrieve_log_file
        - example_netwitness_retrieve_pcap_file
        - example_netwitness_retrieve_pcap_file_time
    - Rules:
        - (Example) NetWitness Get Meta Values
        - (Example) NetWitness Retrieve Log File
        - (Example) NetWitness Retrieve PCAP File
        - (Example) NetWitness Retrieve PCAP File (Time)
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)
        