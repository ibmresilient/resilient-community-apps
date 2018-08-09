# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
import requests
from resilient_circuits import ResilientComponent, function, handler, \
    StatusMessage, FunctionResult, FunctionError
from fn_xforce.util.helper import XForceHelper

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function
         'xforce_get_collection_by_id"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_xforce", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_xforce", {})

    @function("xforce_get_collection_by_id")
    def _xforce_get_collection_by_id_function(self, event, *args, **kwargs):
        """Function: Takes in a parameter of a casefileID 
        and then submits this to the X-Force API to gather data for the provided case."""
        try:
            yield StatusMessage("Starting")
            helper = XForceHelper(self.options)
            # Get Xforce params
            XFORCE_API_KEY = helper.get_config_option("xforce_apikey")
            XFORCE_API_PASSWORD = helper.get_config_option("xforce_password")
            XFORCE_BASEURL = helper.get_config_option("xforce_baseurl")
            HTTP_PROXY = helper.get_config_option("xforce_http_proxy", True)
            HTTPS_PROXY = helper.get_config_option("xforce_https_proxy", True)
            # Get the function parameters:
            xforce_collection_id = kwargs.get("xforce_collection_id")  # text

            log = logging.getLogger(__name__)
            log.info("xforce_collection_id: %s", xforce_collection_id)

            if xforce_collection_id is None:
                raise ValueError("No Query provided for XForce search.")

            # Setup proxies parameter if exist in appconfig file
            proxies = {}

            if HTTP_PROXY:
                proxies["http"] = HTTP_PROXY

            if HTTPS_PROXY:
                proxies["https"] = HTTPS_PROXY

            if len(proxies) == 0:
                proxies = None

            try:
                # Create the session and set the proxies.
                with requests.Session() as session:
                    session.proxies = proxies


                    # Prepare request string
                    request_string = '{}/casefiles/{}'.format(XFORCE_BASEURL, str(xforce_collection_id))
                    # Make the HTTP request through the session.
                    res = session.get(request_string, auth=(XFORCE_API_KEY, XFORCE_API_PASSWORD))
                    case_files = res.json()
            except Exception as e:
                log.info(e)
                raise ValueError("Encountered issue when querying X-Force API")
            #Prepare results object
            print(case_files["contents"]["plainText"])
            if 'contents' in case_files:
                results = {
                    "success": True,
                    "plaintext": case_files["contents"]["plainText"].replace(u'\xa0', u' ').encode('utf-8'),
                    "created": case_files["created"],
                    "title": case_files["title"],
                    "tags": json.dumps(case_files["tags"])
                }
                print results
            # If no 'contents' set success to false for other functions
            else:
                results = {
                    "success": False
                }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()