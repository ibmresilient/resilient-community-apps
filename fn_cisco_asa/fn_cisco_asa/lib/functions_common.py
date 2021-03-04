# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
from resilient_lib import validate_fields

REQUIRED_FIREWALL_FIELDS = ["host"]

PACKAGE_NAME = "fn_cisco_asa"

class CiscoASAFirewalls():
    def __init__(self, opts, options):
        self.firewalls = self._load_firewalls(opts, options)

    def _load_firewalls(self, opts, options):
        """load the app.config firewalls for fn_cisco_asa. 
        Raises:
            KeyError: [error when a named firewall is not found in app.config]
        """
        cisco_asa_firewalls = options["firewalls"]

        # confirm all firewalls are valid
        firewalls = {}
        firewall_list = [item.strip() for item in cisco_asa_firewalls.split(",")]
        for firewall in firewall_list:
            firewall_name = u"{}:{}".format(PACKAGE_NAME, firewall)
            firewall_data = opts.get(firewall_name)
            if not firewall_data:
                raise KeyError(u"Unable to find Cisco ASA firewall: {}".format(firewall_name))

            # check each firewall for the correct settings
            validate_fields(REQUIRED_FIREWALL_FIELDS, firewall_data)

            firewalls[firewall] = firewall_data

        return firewalls

    def get_firewall(self, firewall_name):
        """collect the settings for a Cisco ASA firewall: host, username, password
        Args:
            firewall_name ([str]): [name of firewall in app.config]
        Raises:
            KeyError: [firewall not found]
        Returns:
            [dict]: [settings for a Cisco ASA firewall]
        """
        if not firewall_name in self.firewalls:
            raise KeyError(u"Unable to find firewall: {}".format(firewall_name))

        return self.firewalls[firewall_name]

    def get_firewalls(self):
        """
        Return all firewalls
        """
        return self.firewalls