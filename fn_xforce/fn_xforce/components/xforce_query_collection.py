# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, \
                                StatusMessage, FunctionResult, FunctionError
from fn_xforce.util.helper import XForceHelper
from resilient_lib import RequestsCommon


CONFIG_DATA_SECTION = "fn_xforce"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'xforce_query_collection"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("xforce_query_collection")
    def _xforce_query_collection_function(self, event, *args, **kwargs):
        """Function: Allows user to submit a query to the X-Force Collections API.
         Supports searching either public or private collections."""
        try:

            yield StatusMessage("Starting")
            helper = XForceHelper(self.opts, self.options)
            # Get Xforce params
            HTTPS_PROXY, HTTP_PROXY, XFORCE_APIKEY, XFORCE_BASEURL, XFORCE_PASSWORD = helper.setup_config()
            # Get the function parameters:
            xforce_collection_type = self.get_select_param(
                kwargs.get("xforce_collection_type"))
            xforce_query = kwargs.get("xforce_query")  # text

            log = logging.getLogger(__name__)
            log.info("xforce_collection_type: %s", xforce_collection_type)
            log.info("xforce_query: %s", xforce_query)
            log.info("X-Force Proxies: HTTP %s and HTTPS %s", HTTP_PROXY, HTTPS_PROXY)

            if xforce_query is None:
                raise ValueError("No Query provided for XForce search.")
            if not isinstance(str(xforce_query), str):
                raise ValueError("Input must be a string.")

            # Setup proxies parameter if exists in app.config file
            proxies = {}
            # returns None if len(proxies) == 0
            proxies = helper.setup_proxies(proxies, HTTP_PROXY, HTTPS_PROXY)

            try:
                # Initialize RequestsCommon with configs
                rc = RequestsCommon(self.opts, self.options)

                # Prepare request string
                request_string = '{}/casefiles/{}/fulltext?q={}'.format(XFORCE_BASEURL, str(xforce_collection_type), str(xforce_query))
                log.info("Making GET request to the url: %s", request_string)
                # Make the HTTP request through resilient_lib.
                res = rc.execute_call_v2(
                    "get", request_string, proxies=proxies, auth=(XFORCE_APIKEY, XFORCE_PASSWORD))
                # Is the status code in the 2XX family?
                # Save returned case files
                case_files = helper.handle_case_response(res)
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
