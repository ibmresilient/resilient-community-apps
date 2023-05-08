# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from fn_xforce.util.helper import XForceHelper, PACKAGE_NAME
from resilient_lib import validate_fields
from urllib.parse import quote as url_encode

FN_NAME = "xforce_query_collection"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'xforce_query_collection"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Allows user to submit a query to the X-Force Collections API.
        Supports searching either public or private collections.
        Inputs:
            -   fn_inputs.xforce_query
            -   fn_inputs.xforce_collection_type
        """
        try:

            yield self.status_message("Starting")
            helper = XForceHelper(self.options)
            # Get Xforce params
            XFORCE_APIKEY, XFORCE_BASEURL, XFORCE_PASSWORD = helper.setup_config()
            # Get the function parameters:
            validate_fields(["xforce_query"], fn_inputs)
            xforce_collection_type = getattr(fn_inputs, "xforce_collection_type")
            xforce_query = fn_inputs.xforce_query

            self.LOG.info(f"xforce_collection_type: {xforce_collection_type}")
            self.LOG.info(f"xforce_query: {xforce_query}")

            # Returns {} if len(proxies) == 0
            proxies = helper.setup_proxies()

            try:
                case_files = {}

                # Prepare request string
                collection_type = url_encode(str(xforce_collection_type))
                query = url_encode(xforce_query)

                request_string = f'{XFORCE_BASEURL}/casefiles/{collection_type}/fulltext?q={query}'
                self.LOG.info(f"Making GET request to the url: {request_string}")

                # Make the HTTP request through resilient_lib.
                res = self.rc.execute("get", request_string, proxies=proxies, auth=(XFORCE_APIKEY, XFORCE_PASSWORD), callback=helper.handle_case_response)
                # Is the status code in the 2XX family?
                if int(res.status_code / 100) == 2:
                    case_files = res.json() # Save returned case files
            except Exception as error:
                self.LOG.info(error)
                raise ValueError("Encountered issue when querying X-Force API")

            casefiles_len = len(case_files.get("casefiles", []))

            # Assign keys and values from the response
            if casefiles_len > 0:
                case_files["num_of_casefiles"] = casefiles_len
                result = FunctionResult(case_files)
                # Backwards compatibility
                setattr(result, "case_files", case_files.get("casefiles"))
                setattr(result, "num_of_casefiles", casefiles_len)
            else:
                result = FunctionResult(f"Search query returned no results matching '{xforce_query}'")
                # Backwards compatibility
                setattr(result, "num_of_casefiles", 0)

            # Produce a FunctionResult with the results
            yield result
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
