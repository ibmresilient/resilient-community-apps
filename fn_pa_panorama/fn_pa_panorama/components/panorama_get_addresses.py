# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_pa_panorama.util.panorama_util import PanoramaClient


log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'panorama_edit_address_group"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_pa_panorama", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_pa_panorama", {})

    @function("panorama_get_addresses")
    def _panorama_get_addresses_function(self, event, *args, **kwargs):
        """Function: Panorama get addresses returns a list of the address objects"""
        try:
            yield StatusMessage("Getting list of addresses")
            rp = ResultPayload("fn_pa_panorama", **kwargs)

            # Get the function parameters:
            location = self.get_select_param(kwargs.get("panorama_location"))  # select
            vsys = kwargs.get("panorama_vsys")  # text

            # Log inputs
            if location is None:
                raise ValueError("panorama_location needs to be set.")
            log.info("panorama_location: {}".format(location))
            log.info("panorama_vsys: {}".format(vsys))

            panorama_util = PanoramaClient(self.opts, location, vsys)
            response = panorama_util.get_addresses()

            yield StatusMessage("{} addresses returned.".format(response["result"]["@count"]))
            results = rp.done(True, response)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
