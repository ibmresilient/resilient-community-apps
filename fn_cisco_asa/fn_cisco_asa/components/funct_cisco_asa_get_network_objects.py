# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon, validate_fields, IntegrationError
from fn_cisco_asa.lib.functions_common import CiscoASAFirewalls
from fn_cisco_asa.lib.cisco_asa_client import CiscoASAClient

PACKAGE_NAME = "fn_cisco_asa"
FN_NAME = "cisco_asa_get_network_objects"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'cisco_asa_get_network_objects''"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.fn_options = opts.get(PACKAGE_NAME, {})
        
        required_fields = ["firewalls"]
        validate_fields(required_fields, self.fn_options)

        # Put the comma separated list of firewalls into python list format.
        cisco_asa_firewalls = self.fn_options.get("firewalls")
        firewall_list = [item.strip() for item in cisco_asa_firewalls.split(",")]

        self._init_firewall_choices("cisco_asa_firewall", firewall_list)
        self.firewalls = CiscoASAFirewalls(opts, self.fn_options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.fn_options = opts.get(PACKAGE_NAME, {})
        self.firewalls = CiscoASAFirewalls(opts, self.fn_options)
        self._init_firewall_choices("cisco_asa_firewall", self.firewalls)

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
            LOG.info(u"cisco_asa_network_object_group: %s", network_object_group)

            yield StatusMessage("Validations complete. Starting business logic")
            firewall_options = self.firewalls.get_firewall(firewall_name)
            asa = CiscoASAClient(firewall_options, rc)
            response = asa.get_network_object_group(network_object_group)

            results = rp.done(True, response)

            LOG.info("'%s' complete", FN_NAME)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)


    def _init_firewall_choices(self, field_name, field_value=None):
        """
        Update the rule activity select field choices.  
        We do not know the firewall list til run time as they are defined by
        the user n the app.config.
        """
        try: 
            # Get the current firewall rule activity select list.
            uri = "/types/actioninvocation/fields/{0}".format(field_name)
            get_response = self.rest_client().get(uri)

            values = []

            # Add each firewall as a select list entry.
            for firewall in field_value:
                entry = {'label': firewall,
                         'enabled': True,
                         'hidden': False}
                values.append(entry)

            # Put the new values into the select list to replace the current values there.
            get_response['values'] = values
            put_response = self.rest_client().put(uri, payload=get_response)

            return put_response

        except Exception as err:
            raise IntegrationError(err)