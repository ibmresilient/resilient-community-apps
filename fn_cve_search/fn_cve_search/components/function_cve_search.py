# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult
from resilient_lib import RequestsCommon, readable_datetime

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'function_cve_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cve_search", {})
        self.opts = opts

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cve_search", {})

    @function("function_cve_search")
    def _function_cve_search_function(self, event, *args, **kwargs):
        """Function: A Function to Search Common Vulnerability Exposures Data from https://cve.circl.lu Data Base."""
        try:
            # Getting CVE DataBase URL from app.config file
            CVE_BASE_URL = self.options.get('cve_base_url')
            rc = RequestsCommon(self.opts, self.options)

            # Get the function parameters:
            cve_id = kwargs.get("cve_id", "")  # text
            cve_vendor = kwargs.get("cve_vendor", "")  # text
            cve_product = kwargs.get("cve_product", "")  # text
            cve_published_date_from = kwargs.get("cve_published_date_from", None)  # datepicker

            # Getting Max Result Display Flag from app.config
            MAX_RESULTS_RETURN = int(self.options.get('max_results_display', 50))

            # Variables to Store Parsed CVE API Data
            _result_search_data = dict()

            log = logging.getLogger(__name__)
            log.info("cve_id: %s", cve_id)
            log.info("cve_vendor: %s", cve_vendor)
            log.info("cve_product: %s", cve_product)
            log.info("cve_published_date_from: %s", cve_published_date_from)

            yield StatusMessage(f"Searching the CVE Database. ID: {cve_id}, Vendor: {cve_vendor}, Product: {cve_product}")

            if not cve_id and ((not cve_vendor and cve_product) or (cve_vendor and not cve_product)):
                raise ValueError("Specify both cve_vendor and cve_product or cve-id")
            if cve_id and (cve_product or cve_vendor):
                raise ValueError("Specify both cve_vendor and cve_product or cve-id")

            if cve_id: # Search using the cve_id
                search_data = rc.execute("GET", f"{CVE_BASE_URL}/vulnerability/{cve_id.strip()}").json()
                api_call_type = "cve"
            elif cve_vendor and cve_product: # Search using the vender and product
                search_url = f"{CVE_BASE_URL}/vulnerability/search/{cve_vendor.strip()}/{cve_product.strip()}?per_page={MAX_RESULTS_RETURN}"
                if cve_published_date_from:
                    search_url += f'&since={readable_datetime(cve_published_date_from, rtn_format="%Y-%m-%d")}'
                search_data = rc.execute("GET", search_url).json()
                api_call_type = "search"
            else: # Search the last 30 cves
                search_data = rc.execute("GET", f"{CVE_BASE_URL}/vulnerability/last/{MAX_RESULTS_RETURN}").json()
                api_call_type = "last"

            # Rest Api Response Data
            if search_data:
                _result_search_data['api_call'] = api_call_type
                _result_search_data['content'] = search_data
            log.debug(f"The Data Received from CVE DB : {_result_search_data}")
            yield StatusMessage("Successfully searched the CVE Database.")

            # Produce a FunctionResult with the results
            yield FunctionResult(_result_search_data)
        except Exception as er:
            yield FunctionResult({}, success=False, reason=er)
