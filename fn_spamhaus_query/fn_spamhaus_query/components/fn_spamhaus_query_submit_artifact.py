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

            # Get the app.config parameters:
            spamhaus_wqs_url = self.options.get("spamhaus_wqs_url")
            spamhaus_dqs_key = self.options.get("spamhaus_dqs_key")
            ip_resource_list = self.options.get("ip_resource_list")
            domain_resource_list = self.options.get("domain_resource_list")

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

            # Initialising the Result payload object
            result_object = ResultPayload("fn_spamhaus_query", **kwargs)

            # Initialising the RequestCommon to make REST API Calls to spamhaus
            requestcommon_obj = RequestsCommon(function_opts=self.options)

            # Get proxy Configuration
            proxies = requestcommon_obj.get_proxies()

            # Construct call header with api key
            header_data = {'Authorization': 'Bearer {}'.format(spamhaus_dqs_key)}

            if ipaddress:
                """
                Function is called on IP Address
                """
                _resource_list = ip_resource_list
                _query_string = ipaddress.strip()
            else:
                """
                Function is called on Domain Names
                """
                _resource_list = domain_resource_list
                _query_string = domain_name.strip()

            response_dict = dict()   # dictionary to hold the result data
            for resource in _resource_list:
                try:
                    # Make Get Call to Spamhause website
                    response_json = requestcommon_obj.execute_call('GET',
                                                                   spamhaus_wqs_url.format(resource, _query_string),
                                                                   headers=header_data, proxies=proxies)
                    response_dict[resource] = response_json
                except Exception as err_msg:
                    """If Artifact is not found in spamhaus block list then returned error message will be status:404, 
                    for 404 error message assign the particular resource with 'None' Object. 
                    for any other errors raise an Function Error. 
                    """
                    if response_json.get('status') == 404:
                        response_dict[resource] = None
                    else:
                        raise FunctionError(err_msg)

            # check to see if spamhaus block list database has given artifact
            status = None
            for resource_name, data in response_dict.items():
                if data:
                    status = True   # Flag to make sure we found data
                    resp_code_list = data.get("resp")
                    # Checking Existing static data for response code more information
                    for code in resp_code_list:
                        info = STATIC_INFO_RESPONSE.get(code)

                        # If information not found in `STATIC_INFO_RESPONSE`, Then trying with info API Call
                        if not info:
                            try:
                                info = requestcommon_obj.execute_call('GET', spamhaus_wqs_url.format('info', code), headers=header_data, proxies=proxies)
                            except Exception as err_msg:
                                if info.get('status') == 404:
                                    info = None
                                else:
                                    raise FunctionError(err_msg)
                        response_dict[resource_name][code] = info
            if status:
                sucess_bol = True
                msg = "Success"
            else:
                sucess_bol = False
                msg = "Artifact is : {} is Not listed on Spamhaus Database.".format(_query_string)


            # Producing the result object
            result = result_object.done(success=sucess_bol, content=response_dict, reason=msg)

            # Produce a FunctionResult with the results
            yield FunctionResult(result)
        except Exception as err_msg:
            yield FunctionError(err_msg)
