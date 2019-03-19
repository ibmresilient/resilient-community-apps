# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cve_search.util.cve import make_rest_api_get_call


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_cve_browse"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cve_search", {})

        # Getting CVE DataBase URL from app.config file
        self.CVE_BASE_URL = self.options.get('cve_base_url')+'/{}'

    def _browse_cve_api(self, vendor_name=None):
        """
        :param vendor_name: Vendor Name to search for Vulnerabilities from CVE DB
        :return: if vendor_name=None  then returns JSON with all the vendors, otherwise JSON with all the products
        associated to a vendor
        """

        if vendor_name:
            browse_api = '{}/{}'.format(self.CVE_BASE_URL.format('browse'), vendor_name)
        else:
            browse_api = self.CVE_BASE_URL.format('browse')
        return make_rest_api_get_call(browse_api, api_call='browse')

    def _cve_db_information(self):
        """
        :return:more information about the current databases in use and when it was updated
        """
        db_info_url = '{}'.format(self.CVE_BASE_URL.format('dbInfo'))
        return make_rest_api_get_call(db_info_url, api_call='db')

    def _parse_browse_results(self, api_data):
        """
        :param api_data: Rest API Call Result Data to Parsed.
        :return: returning an array  of product and vendor data
        """
        tmp_browse_list = []
        if isinstance(api_data, list):
            raise NotImplementedError()
        elif isinstance(api_data, dict):
            for key_data, value_data in api_data.items():
                tmp_browse_list.append({key_data: value_data})
            return tmp_browse_list
        else:
            raise NotImplementedError()

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cve_search", {})

    @function("function_cve_browse")
    def _function_cve_browse_function(self, event, *args, **kwargs):
        """Function: A Function to Browse Common Vulnerability Exposures  Vendors and Product & Database information from https://cve.circl.lu Data Base."""
        try:
            # Get the function parameters:
            cve_browse_data = kwargs.get("cve_browse_data")  # text
            if cve_browse_data:
                cve_browse_data = cve_browse_data.strip()

            cve_browse_criteria = kwargs.get("cve_browse_criteria")  # text
            if cve_browse_criteria:
                cve_browse_criteria = cve_browse_criteria.strip()

            cve_vendor = kwargs.get("cve_vendor")  # text
            if cve_vendor:
                cve_vendor = cve_vendor.strip()

            # Variables to Store Parsed CVE API Data
            result_data_dict = dict()

            log = logging.getLogger(__name__)
            log.info("cve_browse_data: %s", cve_browse_data)
            log.info("cve_browse_criteria: %s", cve_browse_criteria)
            log.info("cve_vendor: %s", cve_vendor)

            yield StatusMessage("starting...")

            if cve_browse_criteria.lower().find('browse') != -1:
                browse_data = self._browse_cve_api(vendor_name=cve_vendor)
            elif cve_browse_criteria.lower().find('db') != -1:
                browse_data = self._cve_db_information()
            else:
                raise ValueError("CVE Browse Criteria is not recognized..!")

            # Defining a key in result dictionary to store parsed data
            result_data_dict['content'] = []

            # Type Of the rest api call like browse,search,specific cve,last, db info
            api_call_type = browse_data['api_call']

            # Rest Api Response Data
            browse_data_content = browse_data['content']

            if api_call_type == 'browse':
                result_data_dict['api_call'] = 'browse'
                _browse_dict_list = self._parse_browse_results(api_data=browse_data_content)
                result_data_dict['content'].extend(_browse_dict_list)
            elif api_call_type == 'db':
                result_data_dict['api_call'] = 'db'
                result_data_dict['content'].append(browse_data_content)

            log.debug("The Data Received from CVE: {}".format(result_data_dict))
            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(result_data_dict)
        except Exception as er:
            yield FunctionError(er)
