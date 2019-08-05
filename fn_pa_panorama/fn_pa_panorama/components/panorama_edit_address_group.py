# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from resilient_lib.components.resilient_common import validate_fields
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

    @function("panorama_edit_address_group")
    def _panorama_edit_address_group_function(self, event, *args, **kwargs):
        """Function: Panorama edit address group edits an address group,
        ie: add or remove ip addresses from the group"""
        try:
            yield StatusMessage("Editing address group...")
            rp = ResultPayload("fn_pa_panorama", **kwargs)

            validate_fields(["panorama_name_parameter", "panorama_request_body"], kwargs)

            # Get the function parameters:
            location = self.get_select_param(kwargs.get("panorama_location"))  # select
            vsys = kwargs.get("panorama_vsys")  # text
            name = kwargs.get("panorama_name_parameter")  # text
            body = self.get_textarea_param(kwargs.get("panorama_request_body"))  # textarea

            # Log inputs
            if location is None:
                raise ValueError("panorama_location needs to be set.")
            log.info("panorama_location: {}".format(location))
            log.info("panorama_vsys: {}".format(vsys))
            log.info("panorama_name_parameter: {}".format(name))
            log.info("panorama_request_body: {}".format(body))

            panorama_util = PanoramaClient(self.opts, location, vsys)
            response = panorama_util.edit_address_groups(name, body)

            yield StatusMessage("Address Group Updated")
            results = rp.done(True, response)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
