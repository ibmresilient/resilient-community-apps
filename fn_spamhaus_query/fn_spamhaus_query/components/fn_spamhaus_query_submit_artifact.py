# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import requests
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_spamhaus_query.util.selftest as selftest
from resilient_lib import RequestsCommon, ResultPayload
from fn_spamhaus_query.util.info_response import STATIC_INFO_RESPONSE
from fn_spamhaus_query.util.spamhause_helper import *
import json

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
            spamhause_search_resource = kwargs.get("spamhause_search_resource")  # text

            # Get the app.config parameters:
            spamhaus_wqs_url = self.options.get("spamhaus_wqs_url")
            spamhaus_dqs_key = self.options.get("spamhaus_dqs_key")

            # Get proxy Configuration
            proxies = {"http": self.options.get('http_proxy'), "https": self.options.get('https_proxy')}

            log = logging.getLogger(__name__)
            log.info("spamhaus_query_string: %s", spamhaus_query_string)
            log.info("spamhause_search_resource: %s", spamhause_search_resource)
            log.info("spamhaus_wqs_url: %s", spamhaus_wqs_url)
            log.info("spamhaus_dqs_key: %s", spamhaus_dqs_key)

            yield StatusMessage(
                "Checking Artifact: {} against Spamhaus block list resource {} database.".format(spamhaus_query_string,
                                                                                                 spamhause_search_resource))

            # Checking API Key
            if not spamhaus_dqs_key:
                raise ApikeyError("API key must be defined in App.config file Spamhaus section.")

            # Initialising the Result payload object
            result_object = ResultPayload("fn_spamhaus_query", **kwargs)

            # Construct call header with api key
            header_data = {'Authorization': 'Bearer {}'.format(spamhaus_dqs_key)}

            # Make Get Call to Spamhause website

            response_object = requests.get(spamhaus_wqs_url.format(spamhause_search_resource, spamhaus_query_string),
                                           headers=header_data, proxies=proxies)

            # Get Received data in JSON format.
            response_json = response_object.json()
            if not response_json:
                raise SpamhauseRequestCallError("No Response Returned from Api call")

            # Checking for returned status code error messages.
            spamhause_call_error(response_object)

            if response_object.status_code == 404:
                response_json['is_in_blocklist'] = False          # a bool flag to for block list status
            elif response_object.status_code == 200:
                response_json['is_in_blocklist'] = True
                resp_code_list = response_json.get('resp')
                # Checking STATIC_INFO_RESPONSE for more information on returned info code.
                for code in resp_code_list:
                    code_information = STATIC_INFO_RESPONSE.get(code)
                    # If information not found in `STATIC_INFO_RESPONSE`, Then trying with Spamhaus info API Call
                    if not code_information:
                        code_reponse_obj = requests.get(spamhaus_wqs_url.format('info', code), headers=header_data, proxies=proxies)
                        # Checking for returned status code error messages.
                        spamhause_call_error(code_reponse_obj)

                        if code_reponse_obj.status_code == 404:
                            response_json[code] = None
                        elif code_reponse_obj.status_code == 200:
                            response_json[code] = code_reponse_obj.json()
                    else:
                        response_json[code] = code_information
            yield StatusMessage("Completed Checking artifact against Spamhaus block list.")

            # populating the result output set
            results = result_object.done(success=True, content=response_json)
            with open('a.txt', 'w+') as fh:
                json.dump(results, fh)
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err_msg:
            yield FunctionError(err_msg)
