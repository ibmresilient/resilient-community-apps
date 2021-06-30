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
    Parameters to codegen used to generate the fn_rsa_netwitness package
    """
    return {
        "package": u"fn_rsa_netwitness",
        "message_destinations": [u"rsa_netwitness_message_destination"],
        "functions": [u"netwitness_get_meta_id_ranges",
                      u"netwitness_get_meta_values",
                      u"netwitness_query",
                      u"netwitness_retrieve_log_data",
                      u"netwitness_retrieve_pcap_data"],
        "workflows": [u"example_netwitness_get_meta_values",
                      u"example_netwitness_retrieve_log_file",
                      u"example_netwitness_retrieve_pcap_file",
                      u"example_netwitness_retrieve_pcap_file_time"],
        "actions": [u"(Example) NetWitness Get Meta Values",
                    u"(Example) NetWitness Retrieve Log File",
                    u"(Example) NetWitness Retrieve PCAP File",
                    u"(Example) NetWitness Retrieve PCAP File (Time)"],
        "action_fields": [u"netwitness_end_time",
                          u"netwitness_query",
                          u"netwitness_start_time"],
        "function_params": [u"incident_id",
                            u"nw_data_format",
                            u"nw_end_time",
                            u"nw_event_session_ids",
                            u"nw_meta_id1",
                            u"nw_meta_id2",
                            u"nw_query",
                            u"nw_results_size",
                            u"nw_session_id1",
                            u"nw_session_id2",
                            u"nw_start_time"],
        "incident_fields": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "incident_artifact_types": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    Contents:
    - Action fields:
        netwitness_end_time
        netwitness_query
        netwitness_start_time
    - Function inputs:
        incident_id
        nw_data_format
        nw_end_time
        nw_event_session_ids
        nw_meta_id1
        nw_meta_id2
        nw_query
        nw_results_size
        nw_session_id1
        nw_session_id2
        nw_start_time
    - Message Destinations:
        rsa_netwitness_message_destination
    - Functions:
        netwitness_get_meta_id_ranges
        netwitness_get_meta_values
        netwitness_query
        netwitness_retrieve_log_data
        netwitness_retrieve_pcap_data
    - Workflows:
        example_netwitness_get_meta_values
        example_netwitness_retrieve_log_file
        example_netwitness_retrieve_pcap_file
        example_netwitness_retrieve_pcap_file_time
    - Rules:
        (Example) NetWitness Get Meta Values
        (Example) NetWitness Retrieve Log File
        (Example) NetWitness Retrieve PCAP File
        (Example) NetWitness Retrieve PCAP File (Time)
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as file_line:
        b64_data = base64.b64encode(file_line.read().encode('utf-8'))
        yield ImportDefinition(b64_data)
