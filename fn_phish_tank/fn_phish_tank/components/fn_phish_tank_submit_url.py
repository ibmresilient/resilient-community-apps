# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon, validate_fields
from fn_phish_tank.util.phish_tank_helper import phish_tank_helper


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_phish_tank_submit_url"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_phish_tank", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_phish_tank", {})

    @function("fn_phish_tank_submit_url")
    def _fn_phish_tank_submit_url_function(self, event, *args, **kwargs):
        """This function checks URLs against PhishTank(https://www.phishtank.com/) database to see if the URL is flagged as Phishing or not Phishing"""
        try:
            validate_fields(["phish_tank_check_url"], kwargs)
            validate_fields(["phish_tank_api_url",  "phish_tank_api_key"], self.options)

            # Get the function parameters:
            phish_tank_check_url = kwargs.get("phish_tank_check_url")  # text

            # Get function parameters from config file.
            phish_tank_api_url = self.options.get('phish_tank_api_url')
            phish_tank_api_key = self.options.get('phish_tank_api_key')

            # PhishTank Proxy Data
            if self.options.get("proxy"):
                pt_proxy = phish_tank_helper.format_proxy_data(proxy_data=self.options.get("proxy"))
            else:
                rc = RequestsCommon(self.opts, self.options)
                pt_proxy = rc.get_proxies()

            log = logging.getLogger(__name__)
            log.info("PhishTank Check URL: %s", phish_tank_check_url)
            log.info("PhishTank API Access URL: %s", phish_tank_api_url)
            log.info("PhishTank API Access KEY: %s", f"{phish_tank_api_key[:4]}***")
            log.info("Proxy Server Address: %s", pt_proxy)

            yield StatusMessage(f"Checking Phishing Status Against URL: {phish_tank_check_url}")

            # Initialing the resilient result object
            _result_obj = ResultPayload('fn_phish_tank', **kwargs)

            # Validating the Phish Tank Check URL
            if (not phish_tank_check_url.lower().startswith('http')) and (not phish_tank_check_url.lower().startswith('https')):
                phish_tank_check_url = f"http://{phish_tank_check_url}"

            # PhishTank POST Call Data
            pt_post_call_data = phish_tank_helper.create_post_data(phish_tank_check_url, api_key=phish_tank_api_key)

            # Initialising the Request Session
            pt_helper_class_instance = phish_tank_helper()
            _request_session = pt_helper_class_instance.session()

            headers = { "User-Agent": "phishtank/IBMSOAR" }

            # Making Post request to PhishTank Database for check Phishing status against given URL
            _api_response = _request_session.post(phish_tank_api_url,
                                                  data=pt_post_call_data,
                                                  headers=headers,
                                                  proxies=pt_proxy)

            _api_response.raise_for_status()

            # Converting received response to json format
            _api_response_json = _api_response.json()

            # Converting string time to epoch format
            _epoch_time = phish_tank_helper.timestamp_to_ms_epoch(_api_response_json.get('meta').get('timestamp'))

            # Converting verified string time to epoch format if verified is true from api_response
            _verified_status = _api_response_json.get('results').get('verified')
            if _verified_status:
                _epoch_verified_time = phish_tank_helper.timestamp_to_ms_epoch(
                    _api_response_json.get('results').get('verified_at'))
                _api_response_json['results']['verified_at_modified'] = _epoch_verified_time

            # Replacing string time with epoch converted time
            _api_response_json['meta']['timestamp_modified'] = _epoch_time

            results = _result_obj.done(True, _api_response_json)

            # Produce a FunctionResult with the results
            yield StatusMessage("Checking Phishing Status Completed.")
            yield FunctionResult(results)
        except Exception as err_msg:
            yield FunctionError(err_msg)
        finally:
            # Closing Connection
            _api_response.close()
