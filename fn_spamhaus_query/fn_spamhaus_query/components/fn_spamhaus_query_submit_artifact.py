# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_spamhaus_query.util.selftest as selftest
from resilient_lib import ResultPayload, RequestsCommon
from fn_spamhaus_query.util.info_response import STATIC_INFO_RESPONSE
from fn_spamhaus_query.util.spamhaus_helper import *


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_spamhaus_query_submit_artifact"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_spamhaus_query", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_spamhaus_query", {})

    @function("fn_spamhaus_query_submit_artifact")
    def _fn_spamhaus_query_submit_artifact_function(self, event, *args, **kwargs):
        """Function: Function to check IP Address & Domain Names against Spamhaus Database to see whether IP Address or Domain Names appears in Spamhaus block list records or not."""
        try:
            # Get the function parameters:
            spamhaus_query_string = kwargs.get("spamhaus_query_string")  # text
            spamhaus_search_resource = kwargs.get("spamhaus_search_resource")  # text

            # Get the app.config parameters:
            spamhaus_wqs_url = self.options.get("spamhaus_wqs_url")
            spamhaus_dqs_key = self.options.get("spamhaus_dqs_key")

            log = logging.getLogger(__name__)
            log.info("spamhaus_query_string: %s", spamhaus_query_string)
            log.info("spamhaus_search_resource: %s", spamhaus_search_resource)
            log.info("spamhaus_wqs_url: %s", spamhaus_wqs_url)
            log.info("spamhaus_dqs_key: %s", spamhaus_dqs_key)

            yield StatusMessage(
                u"Checking Artifact: {} against Spamhaus block list resource {} database.".format(spamhaus_query_string,
                                                                                                  spamhaus_search_resource))

            # Checking API Key
            if not spamhaus_dqs_key:
                raise ApikeyError("API key must be defined in App.config file Spamhaus section.")

            # Initialising the Result payload object
            result_object = ResultPayload("fn_spamhaus_query", **kwargs)

            # Initialising Request Common for REST Api Call
            request_common_obj = RequestsCommon(opts=self.options)

            # Get proxy Configuration
            proxies = request_common_obj.get_proxies()

            # Construct call header with api key
            header_data = {'Authorization': 'Bearer {}'.format(spamhaus_dqs_key)}

            # Make Get Call to Spamhaus website
            response_object = request_common_obj.execute_call(verb='GET',
                                                              url=spamhaus_wqs_url.format(spamhaus_search_resource,
                                                                                          spamhaus_query_string),
                                                              headers=header_data, proxies=proxies,
                                                              callback=spamhaus_call_error)
            # Get Received data in JSON format.
            response_json = response_object.json()
            if not response_json:
                raise SpamhausRequestCallError("No Response Returned from Api call")

            if response_object.status_code == 404:
                response_json['is_in_blocklist'] = False  # a bool flag to for block list status
            elif response_object.status_code == 200:
                response_json['is_in_blocklist'] = True
                resp_code_list = response_json.get('resp')
                # Checking STATIC_INFO_RESPONSE for more information on returned info code.
                for code in resp_code_list:
                    code_information = STATIC_INFO_RESPONSE.get(code)
                    # If information not found in `STATIC_INFO_RESPONSE`, Then trying with Spamhaus info API Call
                    if not code_information:
                        code_reponse_obj = request_common_obj.execute_call(verb='GET',
                                                                           url=spamhaus_wqs_url.format('info', code),
                                                                           headers=header_data, proxies=proxies,
                                                                           callback=spamhaus_call_error)
                        if code_reponse_obj.status_code == 404:
                            response_json[code] = None
                        elif code_reponse_obj.status_code == 200:
                            response_json[code] = code_reponse_obj.json()
                    else:
                        response_json[code] = code_information
            yield StatusMessage(u"Completed Checking artifact against Spamhaus block list.")

            # populating the result output set
            results = result_object.done(success=True, content=response_json)
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err_msg:
            yield FunctionError(err_msg)
