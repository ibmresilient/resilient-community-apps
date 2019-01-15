# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2019. All Rights Reserved.

from MaaS360APIs import MaaS360APIsHelper
from resilient_lib.components.integration_errors import IntegrationError


class Maas360Utils(MaaS360APIsHelper):
    """
    Helper object Maas360Utils.
    """

    def __init__(self, host, billingId, userName, password, appID, appVersion, platformID, appAccessKey):
        """ Create MaaS360APIsHelper instance for the given customer
        Instance will be created only if valid credentials are provided
        """
        super(Maas360Utils, self).__init__(host, billingId, userName, password, appID, appVersion, platformID, appAccessKey)

