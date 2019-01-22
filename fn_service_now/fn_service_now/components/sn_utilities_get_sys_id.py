# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_service_now.util.resilient_helper import ResilientHelper


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
    """Component that implements Resilient function 'sn_utilities_get_sys_id"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_service_now", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_service_now", {})

    @function("sn_utilities_get_sys_id")
    def _sn_utilities_get_sys_id_function(self, event, *args, **kwargs):
        """Function: Function that gets the 'sys_id' of a ServiceNow record"""

        log = logging.getLogger(__name__)

        try:
            # Instansiate helper (which gets appconfigs from file)
            res_helper = ResilientHelper(self.options)

            # Get the function inputs:
            inputs = {
                "sn_query_field": res_helper.get_function_input(kwargs, "sn_query_field"),  # text (required)
                "sn_table_name": res_helper.get_function_input(kwargs, "sn_table_name"),  # text (required)
                "sn_query_value": res_helper.get_function_input(kwargs, "sn_query_value")  # text (required)
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Call custom endpoint '/get_sys_id' with 3 params
            get_sys_id_response = res_helper.sn_GET("/get_sys_id", params=payload.inputs)

            # Get response text
            response_result = get_sys_id_response.text

            # Check if result is there
            if response_result is not None and "result" in response_result:
                response_result = json.loads(response_result)

                # Check if sys_id is defined
                if response_result["result"]["sys_id"]:
                    payload.success = True
                    payload.sys_id = response_result["result"]["sys_id"]
                    yield StatusMessage('"{0}" FOUND in Field: "{1}", Table: "{2}"'.format(
                        payload.inputs["sn_query_value"],
                        payload.inputs["sn_query_field"],
                        payload.inputs["sn_table_name"]))
                else:
                    yield StatusMessage('"{0}" NOT FOUND in Field: "{1}", Table: "{2}"'.format(
                        payload.inputs["sn_query_value"],
                        payload.inputs["sn_query_field"],
                        payload.inputs["sn_table_name"]))

            # Handle error messages
            elif response_result is not None and "error" in response_result:
                response_result = json.loads(response_result)
                err_msg = response_result["error"]["message"]
                if "invalid table name" in err_msg:
                    err_msg = '"{0}" is an invalid ServiceNow table name'.format(payload.inputs["sn_table_name"])
                raise ValueError(err_msg)

            # Set results to the payload
            results = payload.as_dict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
