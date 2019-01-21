# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

from MaaS360APIs import MaaS360APIsHelper
from resilient_lib.components.integration_errors import IntegrationError


class Maas360Utils(MaaS360APIsHelper):
    """
    Helper object Maas360Utils.
    """

    def __init__(self, host, billingId, userName, password, appID, appVersion, platformID, appAccessKey, requests_common):
        """ Create MaaS360APIsHelper instance for the given customer
        Instance will be created only if valid credentials are provided
        """
        super(Maas360Utils, self).__init__(host, billingId, userName, password, appID, appVersion, platformID, appAccessKey)

        self.rc = requests_common

    def get_devices(self, basic_search_url, query_string, log):
        """
        Search for devices by Device Name, Username, Phone Number, Platform, Device Status and other Device Identifiers.
        Support for partial match for Device Name, Username, Phone Number.
        :param basic_search_url:
        :param query_string:
        :param log:
        :return: count, device or list of devices or None if there aren't any found
        """

        url_endpoint = self.host + basic_search_url + self.billingId

        headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
                   'Authorization': 'MaaS token="' + self.authToken + '"'}
        try:
            results_basic_search = self.rc.execute_call("get", url_endpoint, query_string, log=log, headers=headers)
        except IntegrationError as err:
            return err

        devices = results_basic_search.get("devices")
        if not devices:
            return None, None

        count = devices.get("count")
        if not count:
            return None, None

        return count, devices
