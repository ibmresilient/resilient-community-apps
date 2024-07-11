# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from json import loads
from logging import getLogger

from resilient_circuits import (FunctionResult, ResilientComponent,
                                StatusMessage, function, handler)
from resilient_lib import ResultPayload, validate_fields

from fn_service_now.util.resilient_helper import (CONFIG_DATA_SECTION,
                                                  ResilientHelper)


class FunctionPayload(object):
    """Class that contains the payload sent back to UI and available in the post-processing script"""

    def __init__(self, inputs):
        self.success = False
        self.inputs = inputs
        self.sys_id = None

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_snow_lookup_sysid"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("fn_snow_lookup_sysid")
    def _fn_snow_lookup_sysid_function(self, event, *args, **kwargs):
        """Function: Function that gets the 'sys_id' of a ServiceNow Record."""

        log = getLogger(__name__)

        # Instantiate helper (which gets app configs from file)
        res_helper = ResilientHelper(self.opts, self.options)
        rp = ResultPayload(CONFIG_DATA_SECTION)
        validate_fields(["sn_query_field", "sn_table_name", "sn_query_value"], kwargs)

        # Get the function inputs:
        inputs = {
            # text (required)
            "sn_query_field": kwargs.get("sn_query_field"),
            # text (required)
            "sn_table_name": kwargs.get("sn_table_name"),
            # text (required)
            "sn_query_value": kwargs.get("sn_query_value")
        }

        # Create payload dict with inputs
        payload = FunctionPayload(inputs)

        yield StatusMessage("Function Inputs OK")

        yield StatusMessage("Querying ServiceNow for a sys_id. table: {0} field: {1} value: {2}".format(
            payload.inputs.get("sn_table_name"), payload.inputs.get("sn_query_field"), payload.inputs.get("sn_query_value")))

        # Call custom endpoint '/get_sys_id' with 3 params
        get_sys_id_response = res_helper.sn_api_request("GET", "/get_sys_id", params=payload.inputs)

        # Get response text
        response_result = get_sys_id_response.text

        # Check if result is there
        if response_result and "result" in response_result:
            response_result = loads(response_result)

            # Check if sys_id is defined
            if response_result["result"]["sys_id"]:
                payload.success = True
                payload.sys_id = response_result["result"]["sys_id"]
                yield StatusMessage(f"sys_id found: {payload.sys_id}")
            else:
                yield StatusMessage("No sys_id found")

        # Handle error messages
        elif response_result and "error" in response_result:
            response_result = loads(response_result)
            err_msg = response_result["error"]["message"]
            if "invalid table name" in err_msg:
                err_msg = f'"{payload.inputs["sn_table_name"]}" is an invalid ServiceNow table name'
            raise ValueError(err_msg)

        # Set results to the payload
        results = payload.as_dict()
        rp_results = rp.done(results.get("success"), results)
        # add in all results for backward-compatibility
        rp_results.update(results)

        log.debug("RESULTS: %s", rp_results)
        log.info("Complete")

        # Produce a FunctionResult with the rp_results
        yield FunctionResult(rp_results)
