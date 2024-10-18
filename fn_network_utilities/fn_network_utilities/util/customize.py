# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2023. All Rights Reserved.
# pragma pylint: disable=pointless-string-statement, line-too-long, wrong-import-order
# Generated with resilient-sdk v50.0.151

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
        "message_destinations": [
            u"fn_network_utilities"
        ],
        "functions": [
            u"network_utilities_domain_distance",
            u"network_utilities_expand_url",
            u"network_utilities_extract_ssl_cert_from_url",
            u"network_utilities_linux_shell_command",
            u"network_utilities_local_shell_command",
            u"network_utilities_windows_shell_command"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [],
        "automatic_tasks": [],
        "scripts": [
            u"network_utilities_shell_results"
        ],
        "playbooks": [
            u"network_utilities_domain_distance_pb_example",
            u"network_utilities_expand_url_pb_example",
            u"network_utilities_extract_ssl_certificate_from_url_pb_example",
            u"network_utilities_linux_shell_command_pb_example",
            u"network_utilities_local_shell_command",
            u"network_utilities_windows_shell_command_pb_example"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 46.0.8131

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
    - Playbooks:
        - network_utilities_domain_distance_pb_example
        - network_utilities_expand_url_pb_example
        - network_utilities_extract_ssl_certificate_from_url_pb_example
        - network_utilities_linux_shell_command_pb_example
        - network_utilities_local_shell_command
        - network_utilities_windows_shell_command_pb_example
    - Scripts:
        - network_utilities_shell_results
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)