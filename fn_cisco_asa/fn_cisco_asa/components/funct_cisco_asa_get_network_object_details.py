# -*- coding: utf-8 -*-
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon
from fn_cisco_asa.lib.functions_common import CiscoASAFirewalls
from fn_cisco_asa.lib.cisco_asa_client import CiscoASAClient

PACKAGE_NAME = "fn_cisco_asa"
FN_NAME = "cisco_asa_get_network_object_details"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'cisco_asa_get_network_object_details''"""

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
        # Load the firewall options from the app.config
        self.firewalls = CiscoASAFirewalls(opts, self.fn_options)


    @function(FN_NAME)
    def _cisco_asa_get_network_object_details_function(self, event, *args, **kwargs):
        """Function: Get the details of the Cisco ASA network object."""
        try:
            LOG = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.fn_options)
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            yield StatusMessage("Starting '{0}'".format(FN_NAME))

            # Get the function parameters
            firewall_name = kwargs.get("cisco_asa_firewall")  # text
            network_object_id = kwargs.get("cisco_asa_network_object_id")  # text

            LOG.info(u"cisco_asa_firewall: %s", firewall_name)
            LOG.info(u"cisco_asa_network_object_id: %s", network_object_id)

            # Get the the options for this firewall.
            firewall_options = self.firewalls.get_firewall(firewall_name)

            # Initialize the Cisco ASA object.
            asa = CiscoASAClient(firewall_name, self.fn_options, firewall_options, rc)

            yield StatusMessage("Validations complete. Get the network objects.")

            # Call the ASA API to get the network objects in this network object group.
            response = asa.get_network_object(network_object_id)

            results = rp.done(True, response)

            LOG.info("'%s' complete", FN_NAME)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)