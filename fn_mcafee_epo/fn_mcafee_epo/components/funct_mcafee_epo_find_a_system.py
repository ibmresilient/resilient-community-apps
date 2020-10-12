# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
from fn_mcafee_epo.lib.epo_helper import init_client
from resilient_lib import ResultPayload, validate_fields
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_mcafee_epo"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'mcafee_epo_find_a_system''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @function("mcafee_epo_find_a_system")
    def _mcafee_epo_find_a_system_function(self, event, *args, **kwargs):
        """Function: Find an ePO system based on property such as system name, tag, IP address, MAC address, etc."""
        try:
            # Get the function parameters:
            validate_fields(["mcafee_epo_systems"], kwargs)
            mcafee_epo_systems = kwargs.get("mcafee_epo_systems")  # text
            client = init_client(self.opts, self.options)

            log = logging.getLogger(__name__)
            log.info("mcafee_epo_systems: %s", mcafee_epo_systems)

            yield StatusMessage("Starting")

            rc = ResultPayload(PACKAGE_NAME, **kwargs)

            params = {"searchText": mcafee_epo_systems.strip()}
            response = client.request("system.find", params)

            yield StatusMessage("Finished")

            results = rc.done(True, response)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
