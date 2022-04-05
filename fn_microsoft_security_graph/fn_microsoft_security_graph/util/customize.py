# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_microsoft_security_graph"""

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
    Parameters required reload codegen for the fn_microsoft_security_graph package
    """
    return {
        "package": u"fn_microsoft_security_graph",
        "message_destinations": [u"microsoft_security_graph_message_destination"],
        "functions": [u"microsoft_security_graph_alert_search", u"microsoft_security_graph_get_alert_details", u"microsoft_security_graph_update_alert"],
        "workflows": [u"example_microsoft_security_graph_alert_search", u"example_microsoft_security_graph_get_alert_details", u"example_microsoft_security_graph_resolve_alert", u"example_microsoft_security_graph_update_alert"],
        "actions": [u"Example: Microsoft Security Graph Alert Search", u"Example: Microsoft Security Graph Get Details", u"Example: Microsoft Security Graph Resolve Alert", u"Example: Microsoft Security Graph Update Alert"],
        "incident_fields": [u"microsoft_security_graph_alert_id"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [u"Convert json to rich text"],
        "playbooks": []
    }

def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 41.0.6783

    Contents:
    - Message Destinations:
        - microsoft_security_graph_message_destination
    - Functions:
        - microsoft_security_graph_alert_search
        - microsoft_security_graph_get_alert_details
        - microsoft_security_graph_update_alert
    - Workflows:
        - example_microsoft_security_graph_alert_search
        - example_microsoft_security_graph_get_alert_details
        - example_microsoft_security_graph_resolve_alert
        - example_microsoft_security_graph_update_alert
    - Rules:
        - Example: Microsoft Security Graph Alert Search
        - Example: Microsoft Security Graph Get Details
        - Example: Microsoft Security Graph Resolve Alert
        - Example: Microsoft Security Graph Update Alert
    - Incident Fields:
        - microsoft_security_graph_alert_id
    - Scripts:
        - Convert json to rich text
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)