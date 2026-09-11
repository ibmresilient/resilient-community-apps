# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon
from fn_cisco_asa.lib.functions_common import CiscoASAFirewalls
from fn_cisco_asa.lib.cisco_asa_client import CiscoASAClient

PACKAGE_NAME = "fn_cisco_asa"
FN_NAME = "cisco_asa_get_network_objects"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'cisco_asa_get_network_objects''"""
    def _convert_csv_to_list(self, csv):
        return [item.strip() for item in csv.split(",")]

    def _load_opts(self, opts):
        """ Load the options """
        self.fn_options = opts.get(PACKAGE_NAME, {})

        # Load the firewall options from the app.config
        self.firewalls = CiscoASAFirewalls(opts, self.fn_options)

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self._load_opts(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._load_opts(opts)

    @function(FN_NAME)
    def _cisco_asa_get_network_objects_function(self, event, *args, **kwargs):
        """Function: Query the Cisco ASA firewall and return the network objects contained in the specified network object group."""
        try:
            LOG = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.fn_options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            yield StatusMessage("Starting '{0}'".format(FN_NAME))

            # Get the function parameters
            firewall_name = kwargs.get("cisco_asa_firewall")  # text
            network_object_group = kwargs.get("cisco_asa_network_object_group")  # text

            LOG.info(u"cisco_asa_firewall: %s", firewall_name)
            LOG.info(u"cisco_asa_network_object_group: %s", network_object_group)

            # Get the the options for this firewall.
            firewall_options = self.firewalls.get_firewall(firewall_name)

            # Initialize the Cisco ASA object.
            asa = CiscoASAClient(firewall_name, self.fn_options, firewall_options, rc)

            yield StatusMessage("Validations complete. Get the network objects.")

            # Call the ASA API to get the network objects in this network object group.
            members = asa.get_network_object_group_detailed(network_object_group)

            member_results = {"member_list": members}
            results = rp.done(True, member_results)

            LOG.info("'%s' complete", FN_NAME)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
