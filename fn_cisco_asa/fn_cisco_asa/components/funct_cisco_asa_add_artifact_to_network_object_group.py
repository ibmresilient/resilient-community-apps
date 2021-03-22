# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon, validate_fields, IntegrationError
from fn_cisco_asa.lib.functions_common import CiscoASAFirewalls
from fn_cisco_asa.lib.cisco_asa_client import CiscoASAClient
from fn_cisco_asa.lib.resilient_helper import artifact_type_to_network_object_kind

PACKAGE_NAME = "fn_cisco_asa"
FN_NAME = "cisco_asa_add_artifact_to_network_object_group"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'cisco_asa_add_artifact_to_network_object_group''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.fn_options = opts.get(PACKAGE_NAME, {})
        # Load the firewall options from the app.config
        self.firewalls = CiscoASAFirewalls(opts, self.fn_options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.fn_options = opts.get(PACKAGE_NAME, {})
        self.firewalls = CiscoASAFirewalls(opts, self.fn_options)

    @function(FN_NAME)
    def _cisco_asa_add_artifact_to_network_object_group_function(self, event, *args, **kwargs):
        """Function: Add a network object to the network object group."""
        try:
            LOG = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.fn_options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            yield StatusMessage("Starting '{0}'".format(FN_NAME))

            # Get the function parameters
            firewall_name = kwargs.get("cisco_asa_firewall")  # text
            network_object_group = kwargs.get("cisco_asa_network_object_group")  # text
            network_object_name = kwargs.get("cisco_asa_network_object_name")  # text
            network_object_value = kwargs.get("cisco_asa_network_object_value")  # text
            artifact_type = kwargs.get("cisco_asa_artifact_type")  # text
            ipv4_netmask = kwargs.get("cisco_asa_ipv4_netmask")  # text
            ipv4_end_range = kwargs.get("cisco_asa_ipv4_end_range")  # text

            LOG.info(u"cisco_asa_firewall: %s", firewall_name)
            LOG.info(u"cisco_asa_network_object_group: %s", network_object_group)
            LOG.info(u"cisco_asa_network_object_name: %s", network_object_name)
            LOG.info(u"cisco_asa_network_object_value: %s", network_object_value)
            LOG.info(u"cisco_asa_artifact_type: %s", artifact_type)
            LOG.info(u"cisco_asa_ipv4_netmask: %s", ipv4_netmask)
            LOG.info(u"cisco_asa_ipv4_end_range: %s", ipv4_end_range)

            # Get the the options for this firewall.
            firewall_options = self.firewalls.get_firewall(firewall_name)

            # Initialize the Cisco ASA object.
            asa = CiscoASAClient(firewall_name, self.fn_options, firewall_options, rc)

            yield StatusMessage("Validations complete. Add the network object.")

            # Translate Resilient artifact type to Cisco ASA network object kind.
            network_object_kind = artifact_type_to_network_object_kind(artifact_type,
                                            network_object_value, ipv4_netmask, ipv4_end_range)
 
            if ipv4_netmask:
                netmask = ipv4_netmask.split(" /")[1]
                if netmask == '32':
                    network_object_value = u"{0}/{1}".format(network_object_value, "255.255.255.255")
                    network_object_kind = "IPv4Address"
                else:
                    network_object_value = u"{0}/{1}".format(network_object_value, netmask)
            elif ipv4_end_range:
                network_object_value = u"{0}-{1}".format(network_object_value, ipv4_end_range)

            # Call the ASA API to add the network object to the network object group.
            response = asa.add_to_network_object_group(network_object_group, network_object_name, 
                                                       network_object_kind, network_object_value)

            content = {"firewall": firewall_name,
                       "network_object_group": network_object_group,
                       "network_object_name": network_object_name,
                       "network_object_kind": network_object_kind,
                       "network_object_value": network_object_value}
            results = rp.done(response, content)

            LOG.info("'%s' complete", FN_NAME)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)

