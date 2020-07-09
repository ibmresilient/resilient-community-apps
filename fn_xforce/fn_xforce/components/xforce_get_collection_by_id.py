# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, \
    StatusMessage, FunctionResult, FunctionError
from fn_xforce.util.helper import XForceHelper
from resilient_lib import RequestsCommon


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function
         'xforce_get_collection_by_id"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get("fn_xforce", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get("fn_xforce", {})

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
            if not isinstance(str(xforce_collection_id), str):
                raise ValueError("Input must be a string.")

            # Setup proxies parameter if exists in app.config file
            proxies = {}
            # returns None if len(proxies) == 0
            proxies = helper.setup_proxies(proxies, HTTP_PROXY, HTTPS_PROXY)

            try:
                # Initialize RequestsCommon with configs
                rc = RequestsCommon(self.opts, self.options)

                # Prepare request string
                request_string = '{}/casefiles/{}'.format(XFORCE_BASEURL, str(xforce_collection_id))
                log.info("Making GET request to the url: %s", request_string)
                # Make the HTTP request through resilient_lib.
                res = rc.execute_call_v2(
                    "get", request_string, proxies=proxies, auth=(XFORCE_APIKEY, XFORCE_PASSWORD))
                # Is the status code in the 2XX family?
                # Save returned case files
                case_files = helper.handle_case_response(res)
            except Exception:
                raise ValueError("Encountered issue when contacting XForce API")

            # Prepare results object
            if 'contents' in case_files:
                results = {
                    "success": True,
                    # We json.dump for python 2&3 compat
                    "plaintext": json.dumps(case_files["contents"]["plainText"], default=lambda o: o.__dict__,
                                            sort_keys=True, indent=4),
                    "wiki": case_files["contents"]["wiki"],
                    "created": case_files["created"],
                    "title": case_files["title"],
                    "tags": case_files["tags"]
                }
            # If no 'contents' set success to false for other functions
            else:
                results = {
                    "success": False
                }
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
