# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from fn_xforce.util.helper import XForceHelper, PACKAGE_NAME
from resilient_lib import validate_fields
from urllib.parse import quote as url_encode
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)

FN_NAME = "xforce_get_collection_by_id"

class FunctionComponent(AppFunctionComponent):
    """Component that implements Resilient function 'xforce_get_collection_by_id"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Takes in a parameter of a casefileID and then submits this to the X-Force API to
        gather data for the provided case.
        Inputs:
            -   fn_inputs.xforce_collection_id
        """
        try:
            yield self.status_message("Starting")
            helper = XForceHelper(self.options)
            # Get Xforce baseurl
            XFORCE_BASEURL = helper.get_baseurl()

            # Get the function parameters:
            validate_fields(["xforce_collection_id"], fn_inputs)
            xforce_collection_id = fn_inputs.xforce_collection_id  # text

            self.LOG.info(f"xforce_collection_id: {xforce_collection_id}")

            case_files = {}

            # Prepare request string
            id = url_encode(str(xforce_collection_id))
            request_string = f'{XFORCE_BASEURL}/casefiles/{id}'
            self.LOG.info(f"Making GET request to the url: {request_string}")

            try:
                # Make the HTTP request through resilient_lib.
                res = helper.make_xforce_api_request(request_string)
                # Is the status code in the 2XX family?
                if (res.status_code / 100) == 2:
                    case_files = res.json() # Save returned case files
            except Exception:
                raise ValueError("Encountered issue when contacting XForce API")

            # Set keys and values from response
            if case_files.get("contents"):
                result = FunctionResult(case_files)

            # If no 'contents' set success to true and notify that no results match the queried ID
            else:
                result = FunctionResult(f"No case files match ID: {xforce_collection_id}")

            # Produce a FunctionResult with the results
            yield result
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
