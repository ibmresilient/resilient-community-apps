# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.5.0.1475

"""AppFunction implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload
from fn_greynoise.lib.common import call_greynoise

SECTION_HEADER = "fn_greynoise"
HTTP_HEADERS = {
    "Accept": "application/json",
    "key": None
}

class FunctionComponent(ResilientComponent):
    """Component that implements function 'greynoise_ip_query_community'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(SECTION_HEADER, {})
    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(SECTION_HEADER, {})

    @function("greynoise_ip_query_community")
    def _greynoise_ip_query_function(self, event, *args, **kwargs):
        """Function: Perform IP Address analysis"""
        try:
            # Get the function parameters:
            greynoise_value = kwargs.get("greynoise_value")  # text
            greynoise_type = self.get_select_param(kwargs.get("greynoise_type"))  # select

            log = logging.getLogger(__name__)
            log.info("greynoise_value: %s", greynoise_value)
            log.info("greynoise_type: %s", greynoise_type)

            # validate input
            validate_fields(("greynoise_type", "greynoise_value"), kwargs)
            validate_fields(("api_key"), self.options)

            yield StatusMessage("starting...")

            # build result
            result_payload = ResultPayload(SECTION_HEADER, **kwargs)

            greynoise_result, error_msg = call_greynoise(self.opts, self.options, greynoise_type, greynoise_value)

            results = result_payload.done(True if not error_msg else False, greynoise_result, reason=error_msg)

            yield StatusMessage("done...")

            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
