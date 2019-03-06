# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import (
    ResilientComponent,
    function,
    handler,
    StatusMessage,
    FunctionResult,
    FunctionError,
)
import requests
from fn_ip_void.util.ipvoid_helper import *


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_ip_void_request"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ip_void", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ip_void", {})

    @function("fn_ip_void_request")
    def _fn_ip_void_request_function(self, event, *args, **kwargs):
        """Function: IP blacklist check, whois lookup, dns lookup, ping etc."""
        try:
            # Get the function parameters:
            ip_void_request_type = self.get_select_param(
                kwargs.get("ip_void_request_type")
            )  # select, values: "IP Reputation", "Domain Blacklist", "DNS Lookup", 
            # "Email Verify", "Threat Log", "SSL Info"
            ip_void_artifact_type = kwargs.get("ip_void_artifact_type")  # text
            ip_void_artifact_value = kwargs.get("ip_void_artifact_value")  # text

            yield StatusMessage("Getting Intelligence for {} : {}".format(
                    ip_void_artifact_type, ip_void_artifact_value
                )
            )

            base_url = get_config_option("ipvoid_base_url", self.options)
            api_key = get_config_option("ipvoid_api_key", self.options)
            url = get_url(
                base_url, api_key, ip_void_request_type, ip_void_artifact_value
            )

            log = logging.getLogger(__name__)
            log.info("ip_void_request_type: %s", ip_void_request_type)
            log.info("ip_void_artifact_type: %s", ip_void_artifact_type)
            log.info("ip_void_artifact_value: %s", ip_void_artifact_value)

            response = requests.get(url)

            if response.status_code == 200:
                res = response.json()
            else:
                msg = response.json()
                raise ValueError(msg["error"])

            results = res
            yield StatusMessage("IPVOID Intel received.")
            log.debug("RESULTS: %s", results)
            log.info("Complete")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
