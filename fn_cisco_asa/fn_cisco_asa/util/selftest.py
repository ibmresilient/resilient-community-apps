# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn_cisco_asa
    resilient-circuits selftest --print-env -l fn_cisco_asa

Return examples:
    return {
        "state": "success",
        "reason": "Successful connection to third party endpoint"
    }

    return {
        "state": "failure",
        "reason": "Failed to connect to third party endpoint"
    }
"""

import logging
from resilient_lib import RequestsCommon, validate_fields
from fn_cisco_asa.lib.functions_common import CiscoASAFirewalls
from fn_cisco_asa.lib.cisco_asa_client import CiscoASAClient

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_cisco_asa"

def selftest_function(opts):
    """
    Test connectivity to at least one Cisco ASA device defined in the app.config.
    """
    fn_options = opts.get("fn_cisco_asa", {})

    rc = RequestsCommon(opts, fn_options)

    # Load the firewall options from the app.config
    firewalls = CiscoASAFirewalls(opts, fn_options)
    firewall_list = firewalls.get_firewall_name_list()

    # Loop through the firewalls to find at least one that is up and connectable.
    for firewall_name in firewall_list:
        # Get the the options for this firewall.
        firewall_options = firewalls.get_firewall(firewall_name)

        # Initialize the Cisco ASA object.
        asa = CiscoASAClient(firewall_name, fn_options, firewall_options, rc)

        try:
            # Check if we can access this Cisco ASA device.
            # See if we can get just one object.
            status_code, response = asa.get_network_objects(limit=1)
            if status_code == 200:
                reason = "Successfull connection to firewall {0}.".format(firewall_name)
                return {
                    "state": "success",
                    "reason": reason
                }
        except Exception as err:
            LOG.info(err)
            continue

    return {
        "state": "failure",
        "reason": "Unable to connect to any Cisco ASA firewall."
    }