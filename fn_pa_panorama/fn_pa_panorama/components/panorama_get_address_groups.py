# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_pa_panorama.util.panorama_util import PanoramaClient


log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'panorama_get_address_groups"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_pa_panorama", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_pa_panorama", {})

    @function("panorama_get_address_groups")
    def _panorama_get_address_groups_function(self, event, *args, **kwargs):
        """Function: Panorama get address groups returns the list of address groups """
        try:
            yield StatusMessage("Getting list of Address Groups")
            rp = ResultPayload("fn_pa_panorama", **kwargs)

            # Get the function parameters:
            location = self.get_select_param(kwargs.get("panorama_location"))  # select
            vsys = kwargs.get("panorama_vsys")  # text
            name = kwargs.get("panorama_name_parameter")  # text (optional parameter)

            # Log inputs
            if location is None:
                raise ValueError("panorama_location needs to be set.")
            log.info("panorama_location: {}".format(location))
            log.info("panorama_vsys: {}".format(vsys))
            log.info("panorama_name_parameter: {}".format(name))

            panorama_util = PanoramaClient(self.opts, location, vsys)
            response = panorama_util.get_address_groups(name)

            yield StatusMessage("{} groups returned.".format(response["result"]["@count"]))
            results = rp.done(True, response)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
