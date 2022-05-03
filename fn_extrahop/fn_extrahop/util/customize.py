# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_extrahop"""

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
    Parameters required reload codegen for the fn_extrahop package
    """
    return {
        "package": u"fn_extrahop",
        "message_destinations": [u"fn_extrahop"],
        "functions": [u"funct_extrahop_rx_assign_tag", u"funct_extrahop_rx_create_tag", u"funct_extrahop_rx_get_activitymaps", u"funct_extrahop_rx_get_detections", u"funct_extrahop_rx_get_devices", u"funct_extrahop_rx_get_tags", u"funct_extrahop_rx_get_watchlist", u"funct_extrahop_rx_search_detections", u"funct_extrahop_rx_search_devices", u"funct_extrahop_rx_search_packets", u"funct_extrahop_rx_update_detection", u"funct_extrahop_rx_update_watchlist"],
        "workflows": [u"wf_extrahop_rx_add_artifact", u"wf_extrahop_rx_assign_tag", u"wf_extrahop_rx_create_tag", u"wf_extrahop_rx_get_activitymaps", u"wf_extrahop_rx_get_devices", u"wf_extrahop_rx_get_tags", u"wf_extrahop_rx_get_watchlist", u"wf_extrahop_rx_search_detections", u"wf_extrahop_rx_search_devices", u"wf_extrahop_rx_search_packets", u"wf_extrahop_rx_update_detection", u"wf_extrahop_rx_update_incident", u"wf_extrahop_rx_update_watchlist"],
        "actions": [u"Example: Extrahop Reveal(x) add artifact", u"Example: Extrahop Reveal(x) assign tag", u"Example: Extrahop Reveal(x) create tag", u"Example: Extrahop Reveal(x) get activitymaps", u"Example: Extrahop Reveal(x) get devices", u"Example: Extrahop Reveal(x) get tags", u"Example: Extrahop Reveal(x) get watchlist", u"Example: Extrahop Reveal(x) search detections", u"Example: Extrahop Reveal(x) search devices", u"Example: Extrahop Reveal(x) search packets", u"Example: Extrahop Reveal(x) update detection", u"Example: Extrahop Reveal(x) update incident", u"Example: Extrahop Reveal(x) update watchlist"],
        "incident_fields": [u"extrahop_assignee", u"extrahop_detection_id", u"extrahop_detection_link", u"extrahop_detection_updated", u"extrahop_end_time", u"extrahop_risk_score", u"extrahop_status", u"extrahop_ticket_id", u"extrahop_update_time"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"extrahop_activitymaps", u"extrahop_detections", u"extrahop_devices", u"extrahop_tags", u"extrahop_watchlist"],
        "automatic_tasks": [],
        "scripts": [u"scr_extrahop_rx_add_artifact_from_device"],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 41.2.41

    Contents:
    - Message Destinations:
        - fn_extrahop
    - Functions:
        - funct_extrahop_rx_assign_tag
        - funct_extrahop_rx_create_tag
        - funct_extrahop_rx_get_activitymaps
        - funct_extrahop_rx_get_detections
        - funct_extrahop_rx_get_devices
        - funct_extrahop_rx_get_tags
        - funct_extrahop_rx_get_watchlist
        - funct_extrahop_rx_search_detections
        - funct_extrahop_rx_search_devices
        - funct_extrahop_rx_search_packets
        - funct_extrahop_rx_update_detection
        - funct_extrahop_rx_update_watchlist
    - Workflows:
        - wf_extrahop_rx_add_artifact
        - wf_extrahop_rx_assign_tag
        - wf_extrahop_rx_create_tag
        - wf_extrahop_rx_get_activitymaps
        - wf_extrahop_rx_get_devices
        - wf_extrahop_rx_get_tags
        - wf_extrahop_rx_get_watchlist
        - wf_extrahop_rx_search_detections
        - wf_extrahop_rx_search_devices
        - wf_extrahop_rx_search_packets
        - wf_extrahop_rx_update_detection
        - wf_extrahop_rx_update_incident
        - wf_extrahop_rx_update_watchlist
    - Rules:
        - Example: Extrahop Reveal(x) add artifact
        - Example: Extrahop Reveal(x) assign tag
        - Example: Extrahop Reveal(x) create tag
        - Example: Extrahop Reveal(x) get activitymaps
        - Example: Extrahop Reveal(x) get devices
        - Example: Extrahop Reveal(x) get tags
        - Example: Extrahop Reveal(x) get watchlist
        - Example: Extrahop Reveal(x) search detections
        - Example: Extrahop Reveal(x) search devices
        - Example: Extrahop Reveal(x) search packets
        - Example: Extrahop Reveal(x) update detection
        - Example: Extrahop Reveal(x) update incident
        - Example: Extrahop Reveal(x) update watchlist
    - Incident Fields:
        - extrahop_assignee
        - extrahop_detection_id
        - extrahop_detection_link
        - extrahop_detection_updated
        - extrahop_end_time
        - extrahop_risk_score
        - extrahop_status
        - extrahop_ticket_id
        - extrahop_update_time
    - Data Tables:
        - extrahop_activitymaps
        - extrahop_detections
        - extrahop_devices
        - extrahop_tags
        - extrahop_watchlist
    - Scripts:
        - scr_extrahop_rx_add_artifact_from_device
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)