# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_harfanglab_edr"""

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
    Parameters required reload codegen for the fn_harfanglab_edr package
    """
    return {
        "package": u"fn_harfanglab_edr",
        "message_destinations": [u"fn_harfanglab_edr"],
        "functions": [u"harfanglab_add_ioc_to_source", u"harfanglab_get_endpoint_details", u"harfanglab_isolate_endpoint", u"harfanglab_run_job", u"harfanglab_telemetry_get_binary", u"harfanglab_telemetry_search_destination_ip", u"harfanglab_telemetry_search_driver_by_filename", u"harfanglab_telemetry_search_driver_by_hash", u"harfanglab_telemetry_search_hash", u"harfanglab_telemetry_search_source_ip", u"harfanglab_unisolate_endpoint"],
        "workflows": [],
        "actions": [],
        "incident_fields": [u"harfanglab_agent_id", u"harfanglab_agent_name", u"harfanglab_alert_id", u"harfanglab_alert_type", u"harfanglab_os_product_type", u"harfanglab_os_type", u"harfanglab_rule_name", u"harfanglab_security_event_url", u"harfanglab_status"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"harfanglab_agents_dt"],
        "automatic_tasks": [],
        "scripts": [u"fn_harfanglab_edr_post_process_agent_details_results", u"fn_harfanglab_edr_post_process_job_result"],
        "playbooks": [u"harfanglab_add_ioc_to_source", u"harfanglab_get_binary", u"harfanglab_get_endpoint_details", u"harfanglab_isolate_endpoint", u"harfanglab_run_job", u"harfanglab_telemetry_search_destination_ip", u"harfanglab_telemetry_search_driver_by_filename", u"harfanglab_telemetry_search_driver_by_hash", u"harfanglab_telemetry_search_hash", u"harfanglab_telemetry_search_source_ip", u"harfanglab_unisolate_endpoint"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.2.43

    Contents:
    - Message Destinations:
        - fn_harfanglab_edr
    - Functions:
        - harfanglab_add_ioc_to_source
        - harfanglab_get_endpoint_details
        - harfanglab_isolate_endpoint
        - harfanglab_run_job
        - harfanglab_telemetry_get_binary
        - harfanglab_telemetry_search_destination_ip
        - harfanglab_telemetry_search_driver_by_filename
        - harfanglab_telemetry_search_driver_by_hash
        - harfanglab_telemetry_search_hash
        - harfanglab_telemetry_search_source_ip
        - harfanglab_unisolate_endpoint
    - Playbooks:
        - harfanglab_add_ioc_to_source
        - harfanglab_get_binary
        - harfanglab_get_endpoint_details
        - harfanglab_isolate_endpoint
        - harfanglab_run_job
        - harfanglab_telemetry_search_destination_ip
        - harfanglab_telemetry_search_driver_by_filename
        - harfanglab_telemetry_search_driver_by_hash
        - harfanglab_telemetry_search_hash
        - harfanglab_telemetry_search_source_ip
        - harfanglab_unisolate_endpoint
    - Incident Fields:
        - harfanglab_agent_id
        - harfanglab_agent_name
        - harfanglab_alert_id
        - harfanglab_alert_type
        - harfanglab_os_product_type
        - harfanglab_os_type
        - harfanglab_rule_name
        - harfanglab_security_event_url
        - harfanglab_status
    - Data Tables:
        - harfanglab_agents_dt
    - Scripts:
        - fn_harfanglab_edr_post_process_agent_details_results
        - fn_harfanglab_edr_post_process_job_result
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)
