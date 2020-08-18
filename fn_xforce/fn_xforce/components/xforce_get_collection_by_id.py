# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, \
    StatusMessage, FunctionResult, FunctionError
from fn_xforce.util.helper import XForceHelper
from resilient_lib import RequestsCommon, ResultPayload


CONFIG_DATA_SECTION = 'fn_xforce'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function
         'xforce_get_collection_by_id"""

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

    @function("xforce_get_collection_by_id")
    def _xforce_get_collection_by_id_function(self, event, *args, **kwargs):
        """Function: Takes in a parameter of a casefileID 
        and then submits this to the X-Force API to gather data for the provided case."""
        try:

            yield StatusMessage("Starting")
            helper = XForceHelper(self.opts, self.options)
            # Get Xforce params
            HTTPS_PROXY, HTTP_PROXY, XFORCE_APIKEY, XFORCE_BASEURL, XFORCE_PASSWORD = helper.setup_config()

            # Get the function parameters:
            xforce_collection_id = kwargs.get("xforce_collection_id")  # text

            log = logging.getLogger(__name__)
            log.info("xforce_collection_id: %s", xforce_collection_id)
            log.info("X-Force Proxies: HTTP %s and HTTPS %s", HTTP_PROXY, HTTPS_PROXY)

            if xforce_collection_id is None:
                raise ValueError("No Query provided for XForce search.")
            # ensure query is a string
            try:
                xforce_collection_id = str(xforce_collection_id)
            except Exception as e:
                log.error(e)
                raise ValueError("Input must be a string.")

            # Setup proxies parameter if exists in app.config file
            proxies = {}
            # returns None if len(proxies) == 0
            proxies = helper.setup_proxies(proxies, HTTP_PROXY, HTTPS_PROXY)

            try:
                case_files = {}
                # Initialize RequestsCommon with configs
                rc = RequestsCommon(self.opts, self.options)

                # Prepare request string
                request_string = '{}/casefiles/{}'.format(XFORCE_BASEURL, str(xforce_collection_id))
                log.info("Making GET request to the url: %s", request_string)
                # Make the HTTP request through resilient_lib.
                res = rc.execute_call_v2(
                    "get", request_string, proxies=proxies, auth=(XFORCE_APIKEY, XFORCE_PASSWORD), callback=helper.handle_case_response)
                # Is the status code in the 2XX family?
                # Save returned case files
                if res.status_code / 100 == 2:
                    case_files = res.json()
            except Exception:
                raise ValueError("Encountered issue when contacting XForce API")

            # initialize ResultPayload object
            result = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            # set keys and values from response
            if 'contents' in case_files:
                result.done(True, res.json())
                # backwards compatibility with original results keys
                result["plaintext"] = json.dumps(case_files["contents"]["plainText"], default=lambda o: o.__dict__,
                                                sort_keys=True, indent=4)
                result["wiki"] = case_files["contents"]["wiki"]
                result["created"] = case_files["created"]
                result["title"] = case_files["title"]
                result["tags"] = case_files["tags"]

            # If no 'contents' set success to true and notify that no results match the queried ID
            else:
                content = "No case files match ID: {}".format(xforce_collection_id)
                result.done(True, content)

            # Produce a FunctionResult with the results
            yield FunctionResult(result)
        except Exception:
            yield FunctionError()
