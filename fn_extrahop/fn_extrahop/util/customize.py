# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.0.4034

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
        "functions": [u"funct_extrahop_rx_add_detection_note", u"funct_extrahop_rx_assign_tag", u"funct_extrahop_rx_create_tag", u"funct_extrahop_rx_get_activitymaps", u"funct_extrahop_rx_get_detection_note", u"funct_extrahop_rx_get_detections", u"funct_extrahop_rx_get_devices", u"funct_extrahop_rx_get_tags", u"funct_extrahop_rx_get_watchlist", u"funct_extrahop_rx_search_detections", u"funct_extrahop_rx_search_devices", u"funct_extrahop_rx_search_packets", u"funct_extrahop_rx_update_detection", u"funct_extrahop_rx_update_watchlist"],
        "workflows": [u"wf_extrahop_rx_add_artifact", u"wf_extrahop_rx_assign_tag", u"wf_extrahop_rx_create_tag", u"wf_extrahop_rx_get_activitymaps", u"wf_extrahop_rx_get_tags", u"wf_extrahop_rx_get_watchlist", u"wf_extrahop_rx_refresh_incident", u"wf_extrahop_rx_search_detections", u"wf_extrahop_rx_search_devices", u"wf_extrahop_rx_search_packets", u"wf_extrahop_rx_update_detection", u"wf_extrahop_rx_update_incident", u"wf_extrahop_rx_update_watchlist"],
        "actions": [u"Example: Extrahop Reveal(x) add artifact", u"Example: Extrahop Reveal(x) assign tag", u"Example: Extrahop Reveal(x) create tag", u"Example: Extrahop Reveal(x) get activitymaps", u"Example: Extrahop Reveal(x) get tags", u"Example: Extrahop Reveal(x) get watchlist", u"Example: Extrahop Reveal(x) refresh incident", u"Example: Extrahop Reveal(x) search detections", u"Example: Extrahop Reveal(x) search devices", u"Example: Extrahop Reveal(x) search packets", u"Example: Extrahop Reveal(x) update detection", u"Example: Extrahop Reveal(x) update incident", u"Example: Extrahop Reveal(x) update watchlist"],
        "incident_fields": [u"extrahop_assignee", u"extrahop_console_url", u"extrahop_detection_id", u"extrahop_detection_link", u"extrahop_detection_updated", u"extrahop_end_time", u"extrahop_mod_time", u"extrahop_risk_score", u"extrahop_site_name", u"extrahop_site_uuid", u"extrahop_status", u"extrahop_ticket_id", u"extrahop_update_notification", u"extrahop_update_time"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"extrahop_activitymaps", u"extrahop_detections", u"extrahop_devices", u"extrahop_tags", u"extrahop_watchlist"],
        "automatic_tasks": [],
        "scripts": [u"ExtraHop script: add artifact from device", u"ExtraHop script: detection property helper", u"ExtraHop script: device property helper"],
        "playbooks": [u"extrahop_rx_add_artifact", u"extrahop_rx_assign_tag", u"extrahop_rx_create_tag", u"extrahop_rx_get_activity_maps", u"extrahop_rx_get_tags", u"extrahop_rx_get_watchlist", u"extrahop_rx_refresh_case", u"extrahop_rx_search_detections", u"extrahop_rx_search_devices", u"extrahop_rx_update_detection", u"extrahop_rx_update_watchlist"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - fn_extrahop
    - Functions:
        - funct_extrahop_rx_add_detection_note
        - funct_extrahop_rx_assign_tag
        - funct_extrahop_rx_create_tag
        - funct_extrahop_rx_get_activitymaps
        - funct_extrahop_rx_get_detection_note
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
        - wf_extrahop_rx_get_tags
        - wf_extrahop_rx_get_watchlist
        - wf_extrahop_rx_refresh_incident
        - wf_extrahop_rx_search_detections
        - wf_extrahop_rx_search_devices
        - wf_extrahop_rx_search_packets
        - wf_extrahop_rx_update_detection
        - wf_extrahop_rx_update_incident
        - wf_extrahop_rx_update_watchlist
    - Playbooks:
        - extrahop_rx_add_artifact
        - extrahop_rx_assign_tag
        - extrahop_rx_create_tag
        - extrahop_rx_get_activity_maps
        - extrahop_rx_get_tags
        - extrahop_rx_get_watchlist
        - extrahop_rx_refresh_case
        - extrahop_rx_search_detections
        - extrahop_rx_search_devices
        - extrahop_rx_update_detection
        - extrahop_rx_update_watchlist
    - Rules:
        - Example: Extrahop Reveal(x) add artifact
        - Example: Extrahop Reveal(x) assign tag
        - Example: Extrahop Reveal(x) create tag
        - Example: Extrahop Reveal(x) get activitymaps
        - Example: Extrahop Reveal(x) get tags
        - Example: Extrahop Reveal(x) get watchlist
        - Example: Extrahop Reveal(x) refresh incident
        - Example: Extrahop Reveal(x) search detections
        - Example: Extrahop Reveal(x) search devices
        - Example: Extrahop Reveal(x) search packets
        - Example: Extrahop Reveal(x) update detection
        - Example: Extrahop Reveal(x) update incident
        - Example: Extrahop Reveal(x) update watchlist
    - Incident Fields:
        - extrahop_assignee
        - extrahop_console_url
        - extrahop_detection_id
        - extrahop_detection_link
        - extrahop_detection_updated
        - extrahop_end_time
        - extrahop_mod_time
        - extrahop_risk_score
        - extrahop_site_name
        - extrahop_site_uuid
        - extrahop_status
        - extrahop_ticket_id
        - extrahop_update_notification
        - extrahop_update_time
    - Data Tables:
        - extrahop_activitymaps
        - extrahop_detections
        - extrahop_devices
        - extrahop_tags
        - extrahop_watchlist
    - Scripts:
        - ExtraHop script: add artifact from device
        - ExtraHop script: detection property helper
        - ExtraHop script: device property helper
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)