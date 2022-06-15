# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_netdevice"""

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
    Parameters required reload codegen for the fn_netdevice package
    """
    return {
        "package": u"fn_netdevice",
        "message_destinations": [u"fn_netdevice"],
        "functions": [u"fn_netdevice_config", u"fn_netdevice_query"],
        "workflows": [u"example_execute_netdevice_command", u"example_execute_netdevice_configuration_commands"],
        "actions": [u"Example: Execute Netdevice Configuration Changes", u"Example: Execute Netdevice Queries"],
        "incident_fields": [],
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

    IBM Resilient Platform Version: 40.0.6554

    Contents:
    - Message Destinations:
        - fn_netdevice
    - Functions:
        - fn_netdevice_config
        - fn_netdevice_query
    - Workflows:
        - example_execute_netdevice_command
        - example_execute_netdevice_configuration_commands
    - Rules:
        - Example: Execute Netdevice Configuration Changes
        - Example: Execute Netdevice Queries
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)