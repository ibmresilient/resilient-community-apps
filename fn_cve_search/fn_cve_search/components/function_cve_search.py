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
    """Component that implements Resilient function 'function_cve_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cve_search", {})
        selftest.selftest_function(opts)

        # Getting CVE DataBase URL from app.config file
        self.CVE_BASE_URL = self.options.get('cve_base_url') + '/{}'

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
                print("JSON DATA RETURNED : {}".format(_response_json_object))
                return _response_json_object
            else:
                raise FunctionError("CVE Api Call Failed with status code : {}".format(_response_code))

        except Exception as call_err:
            raise FunctionError("CVE Api Call Failed : {}".format(call_err))

    def _search_cve_api(self, vendor_name=None, product=None):
        """
        :param vendor_name:  Name of the Vendor
        :param product:   Name of the Product
        :return:JSON with all the vulnerabilities per vendor and a specific product
        """
        if vendor_name is not None and product is not None:
            _search_api = '{}/{}/{}'.format(self.CVE_BASE_URL.format('search'), vendor_name, product)
        elif vendor_name is not None and product is None:
            _search_api = '{}/{}'.format(self.CVE_BASE_URL.format('search'), vendor_name)
        elif vendor_name is None and product is not None:
            _search_api = '{}/{}'.format(self.CVE_BASE_URL.format('search'), product)
        print("SSSSSSSSSSSSSSSSSSSSSS{}".format(_search_api))
        return self._make_rest_api_get_call(_search_api, api_call='search')

    def _get_specific_cve_data(self, cve_id=None):
        """
        :param cve_id: Specific CVE ID
        :return:a JSON of a specific CVE ID
        """
        if cve_id:
            _specific_cve_url = '{}/{}'.format(self.CVE_BASE_URL.format('cve'), cve_id)
            return self._make_rest_api_get_call(_specific_cve_url, api_call='cve')
        else:
            raise FunctionError("Please Specify the CVE ID to search for Vulnerability")

    def _last_30_cves(self):
        """
        :return:a JSON of the last 30 CVEs including CAPEC, CWE and CPE expansions
        """
        _last_url = '{}'.format(self.CVE_BASE_URL.format('last'))
        return self._make_rest_api_get_call(_last_url, api_call='last')

    def _parse_search_results(self, api_data, cve_pub_date_from, cve_pub_date_to):
        """
        :param api_data:CVE Search Rest API Call Result Data to Parsed
        :param cve_pub_date_from: User Given from Published date
        :param cve_pub_date_to: User Given up to Published date
        :return:assigning parsed data to class attribute  - _result_data_dict which is a dictionary
        """
        _search_data = None
        if isinstance(api_data, list):
            _search_data = api_data
        elif isinstance(api_data, dict):
            _search_data = api_data.get('data')
        else:
            raise NotImplementedError()
        print("SSSSSSSEEEEEERRRRRRRRRRRCCCCCCCCCCCCCCCHHHHHHHH:{}".format(_search_data))
        print("MAX_RESULTS_RETURN : {}".format(self.MAX_RESULTS_RETURN))
        if _search_data is not None:
            for search_data_dict in _search_data:
                _search_pub_date = search_data_dict.get('Published')
                _search_pub_date_timestamp = self._get_gm_epoch_time_stamp(date_string=_search_pub_date)

                # Changing The date format to milli seconds to store in the resilient table
                search_data_dict['Published'] = _search_pub_date_timestamp

                if cve_pub_date_from is not None and cve_pub_date_to is not None:
                    if (_search_pub_date_timestamp >= cve_pub_date_from) and (
                            _search_pub_date_timestamp <= cve_pub_date_to):
                        if self.MAX_RESULTS_RETURN != 0:
                            self._result_data_dict['content'].append(search_data_dict)
                            self.MAX_RESULTS_RETURN -= 1
                        else:
                            pass
                    else:
                        pass
                elif cve_pub_date_from is not None and cve_pub_date_to is None:
                    if _search_pub_date_timestamp >= cve_pub_date_from:
                        if self.MAX_RESULTS_RETURN != 0:
                            self._result_data_dict['content'].append(search_data_dict)
                            self.MAX_RESULTS_RETURN -= 1
                        else:
                            pass
                    else:
                        pass
                elif cve_pub_date_from is None and cve_pub_date_to is not None:
                    if _search_pub_date_timestamp <= cve_pub_date_to:
                        if self.MAX_RESULTS_RETURN != 0:
                            self._result_data_dict['content'].append(search_data_dict)
                            self.MAX_RESULTS_RETURN -= 1
                        else:
                            pass
                    else:
                        pass
                else:
                    if self.MAX_RESULTS_RETURN != 0:
                        self._result_data_dict['content'].append(search_data_dict)
                        self.MAX_RESULTS_RETURN -= 1
                    else:
                        pass

    def _parse_last_cve_results(self, api_data):
        """
        :param api_data:CVE Last 30 CVE's Rest API Call Result Data to Parsed
        :return:assigning parsed data to class attribute  - _result_data_dict which is a dictionary
        """
        if isinstance(api_data, list):
            for last_data_dict in api_data:
                if self.MAX_RESULTS_RETURN != 0:

                    # Changing The date format to milli seconds to store in the resilient table
                    _search_pub_date = last_data_dict.get('Published')
                    _search_pub_date_timestamp = self._get_gm_epoch_time_stamp(date_string=_search_pub_date)
                    last_data_dict['Published'] = _search_pub_date_timestamp

                    self._result_data_dict['content'].append(last_data_dict)
                    self.MAX_RESULTS_RETURN -= 1
                else:
                    pass
        elif isinstance(api_data, dict):
            raise NotImplementedError()
        else:
            raise NotImplementedError()

    def _parse_cve_results(self, api_data):
        """

        :param api_data: Specific CVE Rest API Call Result Data to Parsed
        :return:assigning parsed data to class attribute  - _result_data_dict which is a dictionary
        """
        # Changing The date format to milli seconds to store in the resilient table
        _search_pub_date = api_data.get('Published')
        _search_pub_date_timestamp = self._get_gm_epoch_time_stamp(date_string=_search_pub_date)
        api_data['Published'] = _search_pub_date_timestamp
        self._result_data_dict['content'].append(api_data)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cve_search", {})

    @function("function_cve_search")
    def _function_cve_search_function(self, event, *args, **kwargs):
        """Function: A Function to Search  Common Vulnerability Exposures Data from https://cve.circl.lu Data Base."""
        try:
            # Get the function parameters:
            cve_search_data = kwargs.get("cve_search_data")  # text
            if cve_search_data:
                cve_search_data = cve_search_data.strip()

            cve_search_criteria = kwargs.get("cve_search_criteria")  # text
            if cve_search_criteria:
                cve_search_criteria = cve_search_criteria.strip()

            cve_id = kwargs.get("cve_id")  # text
            if cve_id:
                cve_id = cve_id.strip()

            cve_vendor = kwargs.get("cve_vendor")  # text
            if cve_vendor:
                cve_vendor = cve_vendor.strip()

            cve_product = kwargs.get("cve_product")  # text
            if cve_product:
                cve_product = cve_product.strip()

            cve_published_date_from = kwargs.get("cve_published_date_from")  # datepicker
            cve_published_date_to = kwargs.get("cve_published_date_to")  # datepicker

            # Getting Max Result Display Flag from app.config
            self.MAX_RESULTS_RETURN = int(self.options.get('max_results_display'))

            # Variables to Store Parsed CVE API Data
            self._result_data_dict = dict()

            log = logging.getLogger(__name__)
            log.info("cve_search_data: %s", cve_search_data)
            log.info("cve_search_criteria: %s", cve_search_criteria)
            log.info("cve_id: %s", cve_id)
            log.info("cve_vendor: %s", cve_vendor)
            log.info("cve_product: %s", cve_product)
            log.info("cve_published_date_from: %s", cve_published_date_from)
            log.info("cve_published_date_to: %s", cve_published_date_to)

            yield StatusMessage("starting...")

            if cve_search_criteria.lower().find('search') != -1:
                if cve_vendor is None and cve_product is None:
                    raise FunctionError('Please Provide Vendor or Product Name')
                else:
                    _browse_data = self._search_cve_api(vendor_name=cve_vendor, product=cve_product)
            elif cve_search_criteria.lower().find('specific') != -1:
                _browse_data = self._get_specific_cve_data(cve_id=cve_id)
            else:
                _browse_data = self._last_30_cves()

            # Defining a key in result dictionary to store parsed data
            self._result_data_dict['content'] = []

            # Type Of the rest api call like browse,search,specific cve,last, db info
            _api_call_type = _browse_data['api_call']

            # Rest Api Response Data
            _browse_data_content = _browse_data['content']

            if _api_call_type == 'search':
                self._result_data_dict['api_call'] = 'search'
                self._parse_search_results(_browse_data_content, cve_published_date_from, cve_published_date_to)
            elif _api_call_type == 'cve':
                self._result_data_dict['api_call'] = 'cve'
                self._parse_cve_results(_browse_data_content)
            else:
                self._result_data_dict['api_call'] = 'last'
                self._parse_last_cve_results(_browse_data_content)

            log.info("The Data Received from CVE DB : {}".format(self._result_data_dict))
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(self._result_data_dict)
        except Exception as er:
            yield FunctionError(er)