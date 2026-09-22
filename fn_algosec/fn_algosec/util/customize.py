# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""Generate the SOAR customizations required for fn_algosec"""

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
    Parameters required reload codegen for the fn_algosec package
    """
    return {
        "package": u"fn_algosec",
        "message_destinations": [
            u"fn_algosec"
        ],
        "functions": [
            u"algosec_traffic_change_request",
            u"algosec_traffic_change_request_details",
            u"algosec_traffic_simulation_query"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"algosec_internet_connectivity_queries",
            u"algosec_isolation_requests"
        ],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": [
            u"algosec_check_host_internet_connectivity",
            u"algosec_isolate_from_network"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 51.0.0.0.9340

    Contents:
    - Message Destinations:
        - fn_algosec
    - Functions:
        - algosec_traffic_change_request
        - algosec_traffic_change_request_details
        - algosec_traffic_simulation_query
    - Playbooks:
        - algosec_check_host_internet_connectivity
        - algosec_isolate_from_network
    - Data Tables:
        - algosec_internet_connectivity_queries
        - algosec_isolation_requests
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)