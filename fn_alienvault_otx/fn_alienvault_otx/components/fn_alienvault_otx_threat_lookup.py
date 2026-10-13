# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_alienvault_otx.util.alienvault_modules import *


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_alienvault_otx_threat_lookup"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_alienvault_otx", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_alienvault_otx", {})

    @function("fn_alienvault_otx_threat_lookup")
    def _fn_alienvault_otx_threat_lookup_function(self, event, *args, **kwargs):
        """Function: A function to lookup threat intelligence information from Alien Vault OTX for given artifact value."""
        try:
            # Get the function parameters:
            alienvault_search_value = kwargs.get("alienvault_search_value")  # text
            alienvault_search_value = alienvault_search_value.strip() if alienvault_search_value else None

            alienvault_search_type = kwargs.get("alienvault_search_type")  # text
            alienvault_search_type = alienvault_search_type.strip() if alienvault_search_type else None

            alienvault_section = kwargs.get("alienvault_section")  # text
            alienvault_section = alienvault_section.strip() if alienvault_section else None

            log = logging.getLogger(__name__)
            log.info("alienvault_search_value: %s", alienvault_search_value)
            log.info("alienvault_search_type: %s", alienvault_search_type)
            log.info("alienvault_section: %s", alienvault_section)

            yield StatusMessage(
                "Getting Threat Intelligence from AlienVault OTX for {}:{}".format(alienvault_search_type,
                                                                                   alienvault_search_value))
            # Getting Alien Vault Base URL from app.config
            AV_BASE_URL = self.options.get('av_base_url')
            if not AV_BASE_URL:
                raise ValueError("alien vault base url should be defined in app.config file.")

            # creating API get call url
            alien_vault_get_url = ApiCallController.create_alienvault_indicators_url(AV_BASE_URL,
                                                                                     alienvault_search_value,
                                                                                     alienvault_search_type,
                                                                                     alienvault_section)
            # Getting Alien Vault API Key From app.config
            AV_API_KEY = self.options.get('av_api_key')

            # Getting Proxy Settings from app.config
            PROXY = self.options.get('proxy')

            # Creating API Call Header
            if AV_API_KEY:
                CALL_HEADER = ApiCallController.create_header(api_key=AV_API_KEY)
            else:
                raise ValueError("alien vault api key should be defined in app.config file.")

            # proxy data to be sent through the api call
            AV_PROXY = ApiCallController.format_proxy_data(proxy_data=PROXY)

            # Api Controller Class Instance
            ApiCallController_instance = ApiCallController()

            # initialising the Session
            _request_session = ApiCallController_instance.session()

            # Connection to Alien Vault OTX to make a GET request call for given URL.
            _api_response = _request_session.get(alien_vault_get_url, headers=CALL_HEADER, proxies=AV_PROXY)

            _api_response.raise_for_status()

            # Just to check received response is json object
            _api_response_json = _api_response.json()

            # Converts a String Timestamp to an int in milliseconds since 1970 epoch
            _api_response_text = _api_response.text
            _api_response_text = ApiCallController.convert_date_string_to_ms_epoch(response_data=_api_response_text)

            # converting string response to json object after changing the time format
            try:
                _api_response_json = json.loads(_api_response_text)
            except Exception as e:
                log.info("Error occurred while converting time stamp to epoch, time stamp is not converted. Error : %s",
                         e)

            results = {
                "content": _api_response_json
            }

            yield StatusMessage("AlienVault OTX Threat Intel received")
            log.info("API CALL URL : %s", alien_vault_get_url)
            log.debug("RESULTS: %s", results)
            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except requests.exceptions.RetryError:
            raise RetryError()
        except Exception as er:
            yield FunctionError(er)
        finally:
            # Closing Connection
            _api_response.close()
