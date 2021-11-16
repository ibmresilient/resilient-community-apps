# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_sentinelone"""

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
    Parameters required reload codegen for the fn_sentinelone package
    """
    return {
        "package": u"fn_sentinelone",
        "message_destinations": [u"fn_sentinelone"],
        "functions": [u"sentinelone_connect_to_network", u"sentinelone_get_agent_details", u"sentinelone_get_agents"],
        "workflows": [u"sentinelone_add_agent_to_data_table", u"sentinelone_connect_to_network", u"sentinelone_get_agents", u"sentinelone_write_agent_details_to_note"],
        "actions": [u"SentinelOne: Add Agent to Data Table", u"SentinelOne: Connect to Network", u"SentinelOne: Get Agents", u"SentinelOne: Write Agent Details to Note"],
        "incident_fields": [u"sentinelone_agent_id", u"sentinelone_classification", u"sentinelone_confidence_level", u"sentinelone_incident_status", u"sentinelone_mitigation_status", u"sentinelone_threat_id", u"sentinelone_threat_overview_url"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"sentinelone_agents_dt"],
        "automatic_tasks": [],
        "scripts": [u"Convert JSON to rich text v1.1"],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 40.0.6554

    Contents:
    - Message Destinations:
        - fn_sentinelone
    - Functions:
        - sentinelone_connect_to_network
        - sentinelone_get_agent_details
        - sentinelone_get_agents
    - Workflows:
        - sentinelone_add_agent_to_data_table
        - sentinelone_connect_to_network
        - sentinelone_get_agents
        - sentinelone_write_agent_details_to_note
    - Rules:
        - SentinelOne: Add Agent to Data Table
        - SentinelOne: Connect to Network
        - SentinelOne: Get Agents
        - SentinelOne: Write Agent Details to Note
    - Incident Fields:
        - sentinelone_agent_id
        - sentinelone_classification
        - sentinelone_confidence_level
        - sentinelone_incident_status
        - sentinelone_mitigation_status
        - sentinelone_threat_id
        - sentinelone_threat_overview_url
    - Data Tables:
        - sentinelone_agents_dt
    - Scripts:
        - Convert JSON to rich text v1.1
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)