# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon, ResultPayload, validate_fields
from fn_api_void.lib.apivoid_helper import make_apivoid_api_call

PACKAGE_NAME = "fn_api_void"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_api_void_urlrep''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("fn_api_void_request")
    def _fn_api_void_request_function(self, event, *args, **kwargs):
        """Function: Use the APIVoid API to make an APIVoid API request.  Results are written to an incident note."""
        try:
            yield StatusMessage("APIVoid API request function started...")
            log = logging.getLogger(__name__)
            rp = ResultPayload("fn_api_void", **kwargs)

            # Add support for Requests Common
            rc = RequestsCommon(self.opts, self.options)

            apivoid_base_url = self.options.get("apivoid_base_url")
            apivoid_sub_url = self.options.get("apivoid_sub_url")
            apivoid_api_key = self.options.get("apivoid_api_key")

            # Get the function parameters:
            validate_fields(["api_void_request_type", "api_void_artifact_value", "api_void_artifact_value"], kwargs)
            api_void_artifact_type = kwargs.get("api_void_artifact_type")  # text
            api_void_artifact_value = kwargs.get("api_void_artifact_value")  # text
            api_void_request_type = kwargs.get("api_void_request_type")  # select


            log.info("api_void_artifact_value: %s", api_void_artifact_value)

            yield StatusMessage("Getting Intelligence for {}: {}".format(api_void_artifact_type,
                                                                         api_void_artifact_value))

            # Execute APIVoid API call
            response = make_apivoid_api_call(
                base_url=apivoid_base_url,
                sub_url=apivoid_sub_url,
                query_type=api_void_request_type,
                value=api_void_artifact_value,
                api_key=apivoid_api_key,
                rc=rc
            )

            response_json = response.json()

            yield StatusMessage("APIVoid request function completed successfully...")
            results = rp.done(True, response_json)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)