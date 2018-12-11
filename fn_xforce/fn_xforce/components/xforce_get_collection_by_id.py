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
            HTTPS_PROXY, HTTP_PROXY, XFORCE_APIKEY, XFORCE_BASEURL, XFORCE_PASSWORD = helper.setup_config()

            # Get the function parameters:
            xforce_collection_id = kwargs.get("xforce_collection_id")  # text

            log = logging.getLogger(__name__)
            log.info("xforce_collection_id: %s", xforce_collection_id)

            if xforce_collection_id is None:
                raise ValueError("No Query provided for XForce search.")

            if isinstance(str(xforce_collection_id),str) == False:
                raise ValueError("Input must be a string.")

            # Setup proxies parameter if exist in appconfig file
            proxies = {}

            proxies = helper.setup_proxies(proxies, HTTP_PROXY, HTTPS_PROXY)

            try:
                case_files = {}
                # Create the session and set the proxies.
                with requests.Session() as session:
                    session.proxies = proxies

                    # Prepare request string
                    request_string = '{}/casefiles/{}'.format(XFORCE_BASEURL, str(xforce_collection_id))

                    # Make the HTTP request through the session.
                    res = session.get(request_string, auth=(XFORCE_APIKEY, XFORCE_PASSWORD))

                    # Is the status code in the 2XX family?
                    if int(res.status_code / 100) == 2:
                        case_files = res.json()
                    elif res.status_code == 401:
                        raise FunctionError("401 Status code returned. Retry function with updated credentials")
                    elif res.status_code == 403:
                        raise FunctionError("403 Forbidden response received by API")

                    else:
                        yield StatusMessage("Got no results or unexpected result from request.")
            except Exception:
                raise ValueError("Encountered issue when contacting XForce API")
            # Prepare results object
            if 'contents' in case_files:
                results = {
                    "success": True,
                    # We json.dump for python 2&3 compat
                    "plaintext": json.dumps(case_files["contents"]["plainText"],default=lambda o: o.__dict__,
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





