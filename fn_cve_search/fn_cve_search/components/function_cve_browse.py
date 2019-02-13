# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_cve_search.util.selftest as selftest
import requests
import time
import calendar

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_cve_browse"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cve_search", {})
        selftest.selftest_function(opts)

        # Getting CVE DataBase URL from app.config file
        self.CVE_BASE_URL = self.options.get('cve_base_url')+'/{}'

    def _get_gm_epoch_time_stamp(self, date_string):
        """
        :param date_string:  date string like 2018-09-11
        :return: time stamp in milli seconds

        """
        string_format_date = date_string.split('T')[0]
        time_tuple = time.strptime(string_format_date, "%Y-%m-%d")
        time_miliseconds = calendar.timegm(time_tuple) * 1000
        return time_miliseconds

    def _make_rest_api_get_call(self, rest_url, api_call=None):
        """
        :param rest_url: Rest Api URL
        :param api_call: Just reference
        :return: JSON Object Returned from the Call
        """
        _response_json_object = dict()
        try:
            _response_object = requests.get(url=rest_url)
            _response_code = _response_object.status_code
            if _response_code == 200:
                _response_json_object['content'] = _response_object.json()
                _response_json_object['api_call'] = api_call
                return _response_json_object
            else:
                raise FunctionError("CVE Api Call Failed with status code : {}".format(_response_code))

        except Exception as call_err:
            raise FunctionError("CVE Api Call Failed : {}".format(call_err))

    def _browse_cve_api(self, vendor_name=None):
        """
        :param vendor_name: Vendor Name to search for Vulnerabilities from CVE DB
        :return: if vendor_name=None  then returns JSON with all the vendors, otherwise JSON with all the products
        associated to a vendor
        """

        if vendor_name:
            _browse_api = '{}/{}'.format(self.CVE_BASE_URL.format('browse'), vendor_name)
        else:
            _browse_api = self.CVE_BASE_URL.format('browse')
        return self._make_rest_api_get_call(_browse_api, api_call='browse')

    def _cve_db_information(self):
        """
        :return:more information about the current databases in use and when it was updated
        """
        _db_info_url = '{}'.format(self.CVE_BASE_URL.format('dbInfo'))
        return self._make_rest_api_get_call(_db_info_url, api_call='db')

    def _parse_browse_results(self, api_data):
        """
        :param api_data: Rest API Call Result Data to Parsed.
        :return: assigning parsed data to class attribute  - _result_data_dict which is a dictionary
        """

        if isinstance(api_data, list):
            raise NotImplementedError()
        elif isinstance(api_data, dict):
            for key_data, value_data in api_data.items():
                self._result_data_dict['content'].append({key_data: value_data})
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
            self._result_data_dict = dict()

            log = logging.getLogger(__name__)
            log.info("cve_browse_data: %s", cve_browse_data)
            log.info("cve_browse_criteria: %s", cve_browse_criteria)
            log.info("cve_vendor: %s", cve_vendor)

            yield StatusMessage("starting...")

            _browse_data = None  # A variable to store the returned JSON Data
            if cve_browse_criteria.lower().find('browse') != -1:
                _browse_data = self._browse_cve_api(vendor_name=cve_vendor)
            else:
                _browse_data = self._cve_db_information()

            # Defining a key in result dictionary to store parsed data
            self._result_data_dict['content'] = []

            # Type Of the rest api call like browse,search,specific cve,last, db info
            _api_call_type = _browse_data['api_call']

            # Rest Api Response Data
            _browse_data_content = _browse_data['content']

            if _api_call_type == 'browse':
                self._result_data_dict['api_call'] = 'browse'

                self._parse_browse_results(api_data=_browse_data_content)
            else:
                self._result_data_dict['api_call'] = 'db'
                self._result_data_dict['content'].append(_browse_data_content)

            log.debug("The Data Received from CVE: {}".format(self._result_data_dict))
            yield StatusMessage("done...")
            # Produce a FunctionResult with the results
            yield FunctionResult(self._result_data_dict)
        except Exception as er:
            yield FunctionError(er)