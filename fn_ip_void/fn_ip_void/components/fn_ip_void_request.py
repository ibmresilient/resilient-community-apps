# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
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
from resilient_lib import ResultPayload, RequestsCommon, validate_fields
from fn_ip_void.util.ipvoid_helper import CONFIG_DATA_SECTION, make_api_call


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_ip_void_request"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("fn_ip_void_request")
    def _fn_ip_void_request_function(self, event, *args, **kwargs):
        """Function: IP Void Lookup"""
        try:

            log = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get and validate app configs
            app_configs = validate_fields([{"name": "ipvoid_api_key", "placeholder": "<your-api-key>"}, "ipvoid_base_url"], self.options)

            # Get the function parameters:
            fn_inputs = validate_fields(["ip_void_request_type", "ip_void_artifact_value", "ip_void_request_type"], kwargs)

            yield StatusMessage("Getting Intelligence for {}: {}".format(
                fn_inputs.get("ip_void_artifact_type"), fn_inputs.get("ip_void_artifact_value")))

            # Execute api call
            res = make_api_call(
                base_url=app_configs.get("ipvoid_base_url"),
                sub_url=app_configs.get("ipvoid_sub_url"),
                query_type=fn_inputs.get("ip_void_request_type"),
                value=fn_inputs.get("ip_void_artifact_value"),
                api_key=app_configs.get("ipvoid_api_key"),
                rc=rc
            )

            results = rp.done(True, res.json())

            # Backwards compatibility
            results["data"] = results.get("content", {}).get("data")

            log.debug("RESULTS: %s", results)
            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
