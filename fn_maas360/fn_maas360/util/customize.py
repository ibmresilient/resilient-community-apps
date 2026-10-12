# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v50.1.262

"""Generate the Resilient customizations required for fn_maas360"""

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
    Parameters required reload codegen for the fn_maas360 package
    """
    return {
        "package": u"fn_maas360",
        "message_destinations": [
            u"fn_maas360"
        ],
        "functions": [
            u"maas360_action",
            u"maas360_basic_search",
            u"maas360_delete_app",
            u"maas360_stop_app_distribution"
        ],
        "workflows": [
            u"example_maas360_basic_search",
            u"example_maas360_cancel_pending_wipe",
            u"example_maas360_delete_app",
            u"example_maas360_get_software_installed",
            u"example_maas360_locate_device",
            u"example_maas360_lock_device",
            u"example_maas360_stop_app_distribution",
            u"example_maas360_wipe_device"
        ],
        "actions": [
            u"Example: Create Artifact for App ID",
            u"Example: Create Artifact for Device ID",
            u"Example: MaaS360 Basic Search",
            u"Example: MaaS360 Cancel Pending Wipe",
            u"Example: MaaS360 Delete App",
            u"Example: MaaS360 Get Software Installed",
            u"Example: MaaS360 Locate Device",
            u"Example: MaaS360 Lock Device",
            u"Example: MaaS360 Stop App Distribution",
            u"Example: MaaS360 Wipe Device"
        ],
        "incident_fields": [],
        "incident_artifact_types": [
            u"maas360_app_id",
            u"maas360_device_id"
        ],
        "incident_types": [],
        "datatables": [
            u"maas360_device_dt",
            u"maas360_installed_software_datatable"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"Example: Create Artifact for App ID",
            u"Example: Create Artifact for Device ID"
        ],
        "playbooks": [],
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

    Contents:
    - Message Destinations:
        - fn_maas360
    - Functions:
        - maas360_action
        - maas360_basic_search
        - maas360_delete_app
        - maas360_stop_app_distribution
    - Workflows:
        - example_maas360_basic_search
        - example_maas360_cancel_pending_wipe
        - example_maas360_delete_app
        - example_maas360_get_software_installed
        - example_maas360_locate_device
        - example_maas360_lock_device
        - example_maas360_stop_app_distribution
        - example_maas360_wipe_device
    - Rules:
        - Example: Create Artifact for App ID
        - Example: Create Artifact for Device ID
        - Example: MaaS360 Basic Search
        - Example: MaaS360 Cancel Pending Wipe
        - Example: MaaS360 Delete App
        - Example: MaaS360 Get Software Installed
        - Example: MaaS360 Locate Device
        - Example: MaaS360 Lock Device
        - Example: MaaS360 Stop App Distribution
        - Example: MaaS360 Wipe Device
    - Custom Artifact Types:
        - maas360_app_id
        - maas360_device_id
    - Data Tables:
        - maas360_device_dt
        - maas360_installed_software_datatable
    - Scripts:
        - Example: Create Artifact for App ID
        - Example: Create Artifact for Device ID
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)