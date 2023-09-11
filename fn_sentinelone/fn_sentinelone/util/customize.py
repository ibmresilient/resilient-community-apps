# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# Generated with resilient-sdk v50.0.151

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
        "message_destinations": [
            u"fn_sentinelone"
        ],
        "functions": [
            u"sentinelone_abort_disk_scan",
            u"sentinelone_connect_to_network",
            u"sentinelone_disconnect_from_network",
            u"sentinelone_get_agent_details",
            u"sentinelone_get_hash_reputation",
            u"sentinelone_get_threat_details",
            u"sentinelone_initiate_disk_scan",
            u"sentinelone_resolve_threat_in_sentinelone",
            u"sentinelone_restart_agent",
            u"sentinelone_send_soar_note_to_sentinelone",
            u"sentinelone_shutdown_agent",
            u"sentinelone_update_notes_from_sentinelone",
            u"sentinelone_update_threat_status"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"sentinelone_agent_id",
            u"sentinelone_classification",
            u"sentinelone_confidence_level",
            u"sentinelone_incident_status",
            u"sentinelone_mitigation_status",
            u"sentinelone_mitigation_status_description",
            u"sentinelone_threat_analyst_verdict",
            u"sentinelone_threat_id",
            u"sentinelone_threat_name",
            u"sentinelone_threat_overview_url"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"sentinelone_agents_dt"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"Convert JSON to rich text v1.3"
        ],
        "playbooks": [
            u"sentinelone_abort_disk_scan_pb",
            u"sentinelone_add_agent_to_data_table_pb",
            u"sentinelone_connect_agent_to_network_pb",
            u"sentinelone_disconnect_agent_from_network_pb",
            u"sentinelone_get_hash_reputation_pb",
            u"sentinelone_initiate_disk_scan_pb",
            u"sentinelone_resolve_threat_in_sentinelone_pb",
            u"sentinelone_restart_agent_pb",
            u"sentinelone_send_soar_note_to_sentinelone_pb",
            u"sentinelone_shutdown_agent_pb",
            u"sentinelone_update_agent_in_data_table_pb",
            u"sentinelone_update_analyst_verdict_and_threat_status",
            u"sentinelone_update_notes_from_sentinelone_pb",
            u"sentinelone_write_agent_details_to_note_pb",
            u"sentinelone_write_threat_details_to_note_pb"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

    Contents:
    - Message Destinations:
        - fn_sentinelone
    - Functions:
        - sentinelone_abort_disk_scan
        - sentinelone_connect_to_network
        - sentinelone_disconnect_from_network
        - sentinelone_get_agent_details
        - sentinelone_get_hash_reputation
        - sentinelone_get_threat_details
        - sentinelone_initiate_disk_scan
        - sentinelone_resolve_threat_in_sentinelone
        - sentinelone_restart_agent
        - sentinelone_send_soar_note_to_sentinelone
        - sentinelone_shutdown_agent
        - sentinelone_update_notes_from_sentinelone
        - sentinelone_update_threat_status
    - Playbooks:
        - sentinelone_abort_disk_scan_pb
        - sentinelone_add_agent_to_data_table_pb
        - sentinelone_connect_agent_to_network_pb
        - sentinelone_disconnect_agent_from_network_pb
        - sentinelone_get_hash_reputation_pb
        - sentinelone_initiate_disk_scan_pb
        - sentinelone_resolve_threat_in_sentinelone_pb
        - sentinelone_restart_agent_pb
        - sentinelone_send_soar_note_to_sentinelone_pb
        - sentinelone_shutdown_agent_pb
        - sentinelone_update_agent_in_data_table_pb
        - sentinelone_update_analyst_verdict_and_threat_status
        - sentinelone_update_notes_from_sentinelone_pb
        - sentinelone_write_agent_details_to_note_pb
        - sentinelone_write_threat_details_to_note_pb
    - Incident Fields:
        - sentinelone_agent_id
        - sentinelone_classification
        - sentinelone_confidence_level
        - sentinelone_incident_status
        - sentinelone_mitigation_status
        - sentinelone_mitigation_status_description
        - sentinelone_threat_analyst_verdict
        - sentinelone_threat_id
        - sentinelone_threat_name
        - sentinelone_threat_overview_url
    - Data Tables:
        - sentinelone_agents_dt
    - Scripts:
        - Convert JSON to rich text v1.3
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)