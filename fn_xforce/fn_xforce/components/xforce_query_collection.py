# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, \
                                StatusMessage, FunctionResult, FunctionError
from fn_xforce.util.helper import XForceHelper
from resilient_lib import RequestsCommon, ResultPayload, validate_fields
try:
    from urllib import quote as url_encode  # Python 2.X
except ImportError:
    from urllib.parse import quote as url_encode  # Python 3+


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
            inputs = validate_fields(["xforce_query"], kwargs)
            xforce_collection_type = inputs.get("xforce_collection_type")
            xforce_query = inputs.get("xforce_query")

            log = logging.getLogger(__name__)
            log.info("xforce_collection_type: %s", xforce_collection_type)
            log.info("xforce_query: %s", xforce_query)
            log.info("X-Force Proxies: HTTP %s and HTTPS %s", HTTP_PROXY, HTTPS_PROXY)

            # Setup proxies parameter if exists in app.config file
            proxies = {}
            # returns None if len(proxies) == 0
            proxies = helper.setup_proxies(proxies, HTTP_PROXY, HTTPS_PROXY)

            try:
                case_files = {}
                # Initialize RequestsCommon with configs
                rc = RequestsCommon(self.opts, self.options)

                # Prepare request string
                collection_type = url_encode(str(xforce_collection_type))
                query = url_encode(xforce_query)

                request_string = '{}/casefiles/{}/fulltext?q={}'.format(XFORCE_BASEURL, collection_type, query)
                log.info("Making GET request to the url: %s", request_string)

                # Make the HTTP request through resilient_lib.
                res = rc.execute_call_v2(
                    "get", request_string, proxies=proxies, auth=(XFORCE_APIKEY, XFORCE_PASSWORD), callback=helper.handle_case_response)
                # Is the status code in the 2XX family?
                # Save returned case files
                if int(res.status_code / 100) == 2:
                    case_files = res.json()
            except Exception as error:
                log.info(error)
                raise ValueError("Encountered issue when querying X-Force API")

            # initialize result object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # assign keys and values from the response
            if len(case_files["casefiles"]):
                result = rp.done(True, res.json())
                # backwards compatibility
                result["case_files"] = case_files["casefiles"]
                result["num_of_casefiles"] = len(case_files["casefiles"])
            else:
                content = "Search query returned no results."
                result = rp.done(True, content)

            yield StatusMessage("Finished function; Success:"+str(result['success']))

            # Produce a FunctionResult with the results
            yield FunctionResult(result)
        except Exception:
            yield FunctionError()
