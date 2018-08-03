# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, \
                                StatusMessage, FunctionResult, FunctionError
import requests
from fn_xforce.util.helper import XForceHelper


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'xforce_query_collection"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_xforce", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_xforce", {})

    @function("xforce_query_collection")
    def _xforce_query_collection_function(self, event, *args, **kwargs):
        """Function: Allows user to submit a query to the X-Force Collections API.
         Supports searching either public or private collections."""
        try:

            yield StatusMessage("Starting")
            helper = XForceHelper(self.options)
            # Get Xforce params
            XFORCE_APIKEY = helper.get_config_option("xforce_apikey")
            XFORCE_PASSWORD = helper.get_config_option("xforce_password")
            HTTP_PROXY = helper.get_config_option("xforce_http_proxy", True)
            HTTPS_PROXY = helper.get_config_option("xforce_https_proxy", True)
            # Get the function parameters:
            xforce_collection_type = self.get_select_param(
                kwargs.get("xforce_collection_type"))
            xforce_query = kwargs.get("xforce_query")  # text

            log = logging.getLogger(__name__)
            log.info("xforce_collection_type: %s", xforce_collection_type)
            log.info("xforce_query: %s", xforce_query)
            log.info("Proxies :HTTP %s and HTTPS %s", HTTP_PROXY, HTTPS_PROXY)
            if xforce_query is None:
                raise ValueError("No Query provided for XForce search.")

            # Setup proxies parameter if exist in appconfig file
            proxies = {}

            if HTTP_PROXY:
                proxies["http"] = HTTP_PROXY
            if HTTPS_PROXY:
                proxies["https"] = HTTPS_PROXY
            if len(proxies) == 0:
                proxies = None

            case_files = None
            try:
                # Create the session and set the proxies.
                with requests.Session() as session:
                    session.proxies = proxies

                    # Make the HTTP request through the session.
                    request_string = 'https://api.xforce.ibmcloud.com/casefiles/'+str(xforce_collection_type)+'/fulltext?q='+str(xforce_query)
                    res = session.get(
                        request_string, auth=(XFORCE_APIKEY, XFORCE_PASSWORD))
                    case_files = json.loads(res.content)
            except Exception as error:
                log.info(error)
                raise ValueError("Encountered issue when querying X-Force API")

            results = {
                "success": (True if len(case_files["casefiles"]) else False),
                "case_files": case_files["casefiles"],
                "num_of_casefiles": len(case_files["casefiles"])
            }
            yield StatusMessage("Finished function; Success:"+str(results['success']))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()