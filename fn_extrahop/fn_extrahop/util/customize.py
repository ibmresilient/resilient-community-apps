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
        "message_destinations": [u"extrahop"],
        "functions": [u"funct_extrahop_rx_assign_tag", u"funct_extrahop_rx_create_tag", u"funct_extrahop_rx_get_activitymaps", u"funct_extrahop_rx_get_detections", u"funct_extrahop_rx_get_devices", u"funct_extrahop_rx_get_tags", u"funct_extrahop_rx_get_watchlist", u"funct_extrahop_rx_search_detections", u"funct_extrahop_rx_search_devices", u"funct_extrahop_rx_search_packets", u"funct_extrahop_rx_update_detection", u"funct_extrahop_rx_update_watchlist"],
        "workflows": [u"wf_extrahop_rx_assign_tag", u"wf_extrahop_rx_create_tag", u"wf_extrahop_rx_get_activitymaps", u"wf_extrahop_rx_get_detections", u"wf_extrahop_rx_get_devices", u"wf_extrahop_rx_get_tags", u"wf_extrahop_rx_get_watchlist", u"wf_extrahop_rx_search_detections", u"wf_extrahop_rx_search_devices", u"wf_extrahop_rx_search_packets", u"wf_extrahop_rx_update_detection", u"wf_extrahop_rx_update_watchlist"],
        "actions": [u"Example: Extrahop revealx assign tag", u"Example: Extrahop revealx get activitymaps", u"Example: Extrahop revealx get detections", u"Example: Extrahop revealx get devices", u"Example: Extrahop revealx get watchlist", u"Example: Extrahop revealx search detections", u"Example: Extrahop revealx search devices", u"Example: Extrahop revealx search packets", u"Example: Extrahop revealx update detection", u"Example: Extrahop revealx update watchlist"],
        "incident_fields": [u"extrahop_detection_id"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM Resilient Platform Version: 41.0.6783

    Contents:
    - Message Destinations:
        - extrahop
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
        - wf_extrahop_rx_assign_tag
        - wf_extrahop_rx_create_tag
        - wf_extrahop_rx_get_activitymaps
        - wf_extrahop_rx_get_detections
        - wf_extrahop_rx_get_devices
        - wf_extrahop_rx_get_tags
        - wf_extrahop_rx_get_watchlist
        - wf_extrahop_rx_search_detections
        - wf_extrahop_rx_search_devices
        - wf_extrahop_rx_search_packets
        - wf_extrahop_rx_update_detection
        - wf_extrahop_rx_update_watchlist
    - Rules:
        - Example: Extrahop revealx assign tag
        - Example: Extrahop revealx get activitymaps
        - Example: Extrahop revealx get detections
        - Example: Extrahop revealx get devices
        - Example: Extrahop revealx get watchlist
        - Example: Extrahop revealx search detections
        - Example: Extrahop revealx search devices
        - Example: Extrahop revealx search packets
        - Example: Extrahop revealx update detection
        - Example: Extrahop revealx update watchlist
    - Incident Fields:
        - extrahop_detection_id
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)