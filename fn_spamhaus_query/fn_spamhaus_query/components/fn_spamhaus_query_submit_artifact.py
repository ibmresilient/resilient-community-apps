# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon, validate_fields

from fn_spamhaus_query.util.info_response import STATIC_INFO_RESPONSE
from fn_spamhaus_query.util.spamhaus_helper import CONFIG_DATA_SECTION, make_api_call, SpamhausRequestCallError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_spamhaus_query_submit_artifact"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("fn_spamhaus_query_submit_artifact")
    def _fn_spamhaus_query_submit_artifact_function(self, event, *args, **kwargs):
        """Function: Function to check IP Address & Domain Names against Spamhaus Database to see whether IP Address or Domain Names appears in Spamhaus block list records or not."""
        try:

            log = logging.getLogger(__name__)
            rc = RequestsCommon(self.opts, self.options)
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get + validate the app.config parameters:
            app_configs = validate_fields(["spamhaus_wqs_url", "spamhaus_dqs_key"], self.options)
            log.info("Validated app configs")

            # Get + validate the function parameters:
            fn_inputs = validate_fields(["spamhaus_query_string", "spamhaus_search_resource"], kwargs)
            log.info("Validated function inputs: %s", fn_inputs)

            yield StatusMessage(u"Checking Artifact: {} against Spamhaus dataset {}".format(
                fn_inputs.get("spamhaus_query_string"), fn_inputs.get("spamhaus_search_resource")))

            # Make Get Call to Spamhaus website
            res = make_api_call(
                base_url=app_configs.get("spamhaus_wqs_url"),
                api_key=app_configs.get("spamhaus_dqs_key"),
                search_resource=fn_inputs.get("spamhaus_search_resource"),
                qry=fn_inputs.get("spamhaus_query_string"),
                rc=rc
            )

            # Get Received data in JSON format.
            response_json = res.json()
            if not response_json:
                raise SpamhausRequestCallError("No Response Returned from Api call")

            response_json['is_in_blocklist'] = False  # a bool flag to for block list status

            if res.status_code == 200:
                response_json['is_in_blocklist'] = True
                resp_code_list = response_json.get('resp')

                # Checking STATIC_INFO_RESPONSE for more information on returned info code.
                for code in resp_code_list:

                    code_information = STATIC_INFO_RESPONSE.get(code)

                    # If the response is not found in STATIC_INFO_RESPONSE,
                    # then use an API call again to get the response info
                    if not code_information:
                        code_response_obj = make_api_call(
                            base_url=app_configs.get("spamhaus_wqs_url"),
                            api_key=app_configs.get("spamhaus_dqs_key"),
                            search_resource="info",
                            qry=code,
                            rc=rc
                        )

                        if code_response_obj.status_code == 200:
                            response_json[code] = code_response_obj.json()

                        else:
                            response_json[code] = None

                    else:
                        response_json[code] = code_information

            else:
                raise SpamhausRequestCallError("Unhandled API status code returned: {0}".format(res.status_code))

            # populating the result output set
            results = rp.done(success=True, content=response_json)

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err_msg:
            yield FunctionError(err_msg)
