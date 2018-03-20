# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from threading import Thread
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from ..util.dxl_ePOConnector import tagSystemsOnEPO

from dxlclient.client import DxlClient
from dxlclient.client_config import DxlClientConfig
from dxleposervice import EpoService

LOG = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_tag_an_epo_asset"""

    config_file = "dxlclient_config"

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        try:
            self.options = opts.get("mcafee", {})
            config = self.options.get(self.config_file)
            if config is None:
                LOG.error(self.config_file + " is not set. You must set this path to run this threat service")
                raise ValueError(self.config_file + " is not set. You must set this path to run this threat service")

            # Create configuration from file for DxlClient
            self.config = DxlClientConfig.create_dxl_config_from_file(config)
        except AttributeError:
            LOG.error("There is no [mcafee] section in the config file, "
                      "please set that by running resilient-circuits config -u")
            raise AttributeError("[mcafee] section is not set in the config file")

        # Create client
        self.client = DxlClient(self.config)
        self._connect_client()

    def _connect_client(self):
        # Connect client
        if not self.client.connected:
            self.client.connect()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("mcafee", {})

    @function("mcafee_tag_an_epo_asset")
    def _mcafee_tag_an_epo_asset_function(self, event, *args, **kwargs):
        """Function: A function which takes two inputs:

mcafee_epo_system: Comma separated list of Hostnames/IpAddress. These systems must be managed on ePO.
mcafee_epo_tag: A Tag managed on ePO.

Applies tag to the systems in ePO."""
        try:
            yield StatusMessage("starting...")

            # Get the function parameters:
            mcafee_epo_systems = kwargs.get("mcafee_epo_systems")  # text
            mcafee_epo_tag = kwargs.get("mcafee_epo_tag")  # text

            log = logging.getLogger(__name__)
            log.info("mcafee_epo_systems: %s", mcafee_epo_systems)
            log.info("mcafee_epo_tag: %s", mcafee_epo_tag)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            tagSystemsOnEPO("something", mcafee_epo_systems, mcafee_epo_tag)

            yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
