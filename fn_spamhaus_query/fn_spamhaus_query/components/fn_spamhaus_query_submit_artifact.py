# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_spamhaus_query.util.selftest as selftest
from resilient_lib import RequestsCommon, ResultPayload
from fn_spamhaus_query.util.info_response import STATIC_INFO_RESPONSE


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
            ipaddress = kwargs.get("ipaddress")  # text
            domain_name = kwargs.get("domain_name")  # text

            # Getting Configuration parameters from app.config
            spamhaus_wqs_url = self.options.get("spamhaus_wqs_url")
            spamhaus_dqs_key = self.options.get("spamhaus_dqs_key")
            ip_resource_list = self.options.get("ip_resource_list")
            domain_resource_list = self.options.get("domain_resource_list")

            proxies = {'http': self.options.get('http_proxy'), 'https': self.options.get('https_proxy')}

            log = logging.getLogger(__name__)
            log.info("ipaddress: %s", ipaddress)
            log.info("domain_name: %s", domain_name)
            log.info("spamhaus_wqs_url: %s", spamhaus_wqs_url)
            log.info("spamhaus_dqs_key: %s", spamhaus_dqs_key)
            log.info("ip_resource_list: %s", ip_resource_list)
            log.info("domain_resource_list: %s", domain_resource_list)

            # Checking API Key
            if not spamhaus_dqs_key:
                raise ValueError("API key must be defined in App.config file Spamhaus section.")

            # Initialising the Result Object
            result_object = ResultPayload("fn_spamhaus_query", kwargs)

            # Initialising the RequestCommon to make REST API Calls
            requestcommon_obj = RequestsCommon()

            # Constructing call header with api key
            header_data = {'Authorization': 'Bearer {}'.format(spamhaus_dqs_key)}

            if ipaddress:
                """
                Wrapper is called IP Address Artifact
                """
                _resource_list = ip_resource_list
                _query_string = ipaddress.strip()
            else:
                """
                Wrapper is called on Domain Name Artifacts
                """
                _resource_list = domain_resource_list
                _query_string = domain_name.strip()

            response_dict = dict()
            for resource in _resource_list:
                try:
                    response_json = requestcommon_obj.execute_call('GET',
                                                                   spamhaus_wqs_url.format(resource, _query_string),
                                                                   headers=header_data, proxies=proxies)
                    response_dict[resource] = response_json
                except Exception as err_msg:
                    if response_json.get('status') == 404:
                        response_dict[resource] = None
                    else:
                        raise FunctionError(err_msg)
            for resource_name, data in response_dict:
                if data:
                    resp_code_list = data.get("resp")

                    # Checking Existing static data for response code more information
                    for code in resp_code_list:
                        info = STATIC_INFO_RESPONSE.get(code)

                        # not found locally hence getting from Spamhaus Database
                        if not info:
                            info = requestcommon_obj.execute_call('GET',
                                                                   spamhaus_wqs_url.format('info', code),
                                                                   headers=header_data, proxies=proxies)

                        response_dict[resource_name][code] = info

            # Producing the result object
            result = result_object.done(success= True, content=response_dict)

            # Produce a FunctionResult with the results
            yield FunctionResult(result)
        except Exception as err_msg:
            yield FunctionError(err_msg)
