# -*- coding: utf-8 -*-

"""Generate the Resilient customizations required for fn_network_utilities"""

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
    Parameters required reload codegen for the fn_network_utilities package
    """
    return {
        "package": u"fn_network_utilities",
        "message_destinations": [u"fn_network_utilities"],
        "functions": [u"network_utilities_domain_distance", u"network_utilities_expand_url", u"network_utilities_extract_ssl_cert_from_url", u"network_utilities_linux_shell_command", u"network_utilities_local_shell_command", u"network_utilities_windows_shell_command"],
        "workflows": [u"example_network_utilities_domain_distance", u"example_network_utilities_expand_url", u"example_network_utilities_extract_ssl_cert_from_url", u"example_network_utilities_linux_shell_command", u"example_network_utilities_local_command", u"example_network_utilities_windows_shell_command"],
        "actions": [u"Example: Network Utilities Domain Distance", u"Example: Network Utilities Expand URL", u"Example: Network Utilities Extract SSL Certificate from URL", u"Example: Network Utilities Linux Shell Command", u"Example: Network Utilities Local Shell Command", u"Example: Network Utilities Windows Shell Command"],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [],
        "playbooks": []
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 45.0.7899

    Contents:
    - Message Destinations:
        - fn_network_utilities
    - Functions:
        - network_utilities_domain_distance
        - network_utilities_expand_url
        - network_utilities_extract_ssl_cert_from_url
        - network_utilities_linux_shell_command
        - network_utilities_local_shell_command
        - network_utilities_windows_shell_command
    - Workflows:
        - example_network_utilities_domain_distance
        - example_network_utilities_expand_url
        - example_network_utilities_extract_ssl_cert_from_url
        - example_network_utilities_linux_shell_command
        - example_network_utilities_local_command
        - example_network_utilities_windows_shell_command
    - Rules:
        - Example: Network Utilities Domain Distance
        - Example: Network Utilities Expand URL
        - Example: Network Utilities Extract SSL Certificate from URL
        - Example: Network Utilities Linux Shell Command
        - Example: Network Utilities Local Shell Command
        - Example: Network Utilities Windows Shell Command
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)