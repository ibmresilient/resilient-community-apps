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
    """Component that implements Resilient function 'function_cve"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cve_search", {})
        selftest.selftest_function(opts)
        self.cve_base_url = "https://cve.circl.lu/api/{}"

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cve_search", {})

    def _get_gm_epoch_time_stamp(self,date_string):
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
        log = logging.getLogger(__name__)

        if vendor_name:
            _browse_api = '{}/{}'.format(self.cve_base_url.format('browse'), vendor_name)
        else:
            _browse_api = self.cve_base_url.format('browse')
        return self._make_rest_api_get_call(_browse_api, api_call='browse')

    def _search_cve_api(self, vendor_name=None, product=None):
        """
        :param vendor_name:  Name of the Vendor
        :param product:   Name of the Product
        :return:JSON with all the vulnerabilities per vendor and a specific product
        """
        if vendor_name is not None and product is not None:
            _search_api = '{}/{}/{}'.format(self.cve_base_url.format('search'), vendor_name, product)
        elif vendor_name is not None and product is None:
            _search_api = '{}/{}'.format(self.cve_base_url.format('search'), vendor_name)
        elif vendor_name is None and product is not None:
            _search_api = '{}/{}'.format(self.cve_base_url.format('search'), product)
        return self._make_rest_api_get_call(_search_api, api_call='search')

    def _get_specific_cve_data(self, cve_id=None):
        """
        :param cve_id: Specific CVE ID
        :return:a JSON of a specific CVE ID
        """
        if cve_id:
            _specific_cve_url = '{}/{}'.format(self.cve_base_url.format('cve'), cve_id)
            return self._make_rest_api_get_call(_specific_cve_url, api_call='cve')
        else:
            raise FunctionError("Please Specify the CVE ID to search for Vulnerability")

    def _last_30_cves(self):
        """
        :return:a JSON of the last 30 CVEs including CAPEC, CWE and CPE expansions
        """
        _last_url = '{}'.format(self.cve_base_url.format('last'))
        return self._make_rest_api_get_call(_last_url, api_call='last')

    def _cve_db_information(self):
        """
        :return:more information about the current databases in use and when it was updated
        """
        _db_info_url = '{}'.format(self.cve_base_url.format('dbInfo'))
        return self._make_rest_api_get_call(_db_info_url, api_call='db')

    @function("function_cve")
    def _function_cve_function(self, event, *args, **kwargs):
        """Function: A Function to Search  Common Vulnerability Exposures Data from https://cve.circl.lu Data base."""
        try:
            # Get the function parameters:
            cve_search_data = kwargs.get("cve_search_data")  # text
            cve_search_criteria = kwargs.get("cve_search_criteria")  # text
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

            _MAX_RESULTS_RETURN = int(self.options.get('max_results_display'))

            log = logging.getLogger(__name__)

            log.info("Maximum search result to be returned : {}".format(_MAX_RESULTS_RETURN))
            log.info("cve_search_data: %s type : %s", cve_search_data,type(cve_search_data))
            log.info("cve_search_criteria: %s type : %s", cve_search_criteria,type(cve_search_criteria))
            log.info("cve_id: %s type : %s", cve_id,type(cve_id))
            log.info("cve_vendor: %s type : %s", cve_vendor,type(cve_vendor))
            log.info("cve_product: %s type : %s", cve_product,type(cve_product))
            log.info("cve_published_date_from: %s type : %s", cve_published_date_from,type(cve_published_date_from))
            log.info("cve_published_date_to: %s type : %s", cve_published_date_to,type(cve_published_date_to))

            yield StatusMessage("starting...")
            _browse_data = None   # A variable to store the returned JSON Data
            if cve_search_criteria.lower().find('browse') != -1:
                if cve_vendor is not None and cve_product is not None:
                    _browse_data = self._search_cve_api(vendor_name=cve_vendor, product=cve_product)
                else:
                    _browse_data = self._browse_cve_api(vendor_name=cve_vendor)
            elif cve_search_criteria.lower().find('search') != -1:
                if cve_vendor is None and cve_product is None:
                    _browse_data = self._browse_cve_api(vendor_name=cve_vendor)
                else:
                    _browse_data = self._search_cve_api(vendor_name=cve_vendor, product=cve_product)
            elif cve_search_criteria.lower().find('specific') != -1:
                _browse_data = self._get_specific_cve_data(cve_id=cve_id)
            elif cve_search_criteria.lower().find('last') != -1:
                _browse_data = self._last_30_cves()
            else:
                _browse_data = self._cve_db_information()

            # Filtering the date to send back to resilient
            _result_data_dict = dict()
            _result_data_dict['content'] = []

            # Type Of the rest api call like browse,search,specific cve,last, db info
            _api_call_type = _browse_data['api_call']
            print("API CALL TYPE : {}".format(_api_call_type))
            # Rest Api Response Data
            _browse_data_content = _browse_data['content']
            if _api_call_type == 'browse':
                _result_data_dict['api_call'] = 'browse'
                if isinstance(_browse_data_content, list):
                    raise NotImplementedError()
                elif isinstance(_browse_data_content, dict):
                    for key_data, value_data in _browse_data_content.items():
                        _result_data_dict['content'].append({key_data: value_data})
                else:
                    raise NotImplementedError()
            elif _api_call_type == 'search':
                _result_data_dict['api_call'] = 'search'
                _search_data = None
                if isinstance(_browse_data_content, list):
                    _search_data = _browse_data_content
                elif isinstance(_browse_data_content, dict):
                    _search_data = _browse_data_content.get('data')
                else:
                    raise NotImplementedError()
                if _search_data is not None:
                    for search_data_dict in _search_data:
                        _search_pub_date = search_data_dict.get('Published')
                        _search_pub_date_timestamp = self._get_gm_epoch_time_stamp(date_string=_search_pub_date)

                        # Changing The date format to milli seconds to store in the resilient table
                        search_data_dict['Published'] = _search_pub_date_timestamp

                        if cve_published_date_from is not None and cve_published_date_to is not None:
                            if (_search_pub_date_timestamp >= cve_published_date_from) and (
                                    _search_pub_date_timestamp <= cve_published_date_to):
                                if _MAX_RESULTS_RETURN != 0:
                                    _result_data_dict['content'].append(search_data_dict)
                                    _MAX_RESULTS_RETURN -= 1
                                else:
                                    pass
                            else:
                                pass
                        elif cve_published_date_from is not None and cve_published_date_to is None:
                            if _search_pub_date_timestamp >= cve_published_date_from:
                                if _MAX_RESULTS_RETURN != 0:
                                    _result_data_dict['content'].append(search_data_dict)
                                    _MAX_RESULTS_RETURN -= 1
                                else:
                                    pass
                            else:
                                pass
                        elif cve_published_date_from is None and cve_published_date_to is not None:
                            if _search_pub_date_timestamp <= cve_published_date_to:
                                if _MAX_RESULTS_RETURN != 0:
                                    _result_data_dict['content'].append(search_data_dict)
                                    _MAX_RESULTS_RETURN -= 1
                                else:
                                    pass
                            else:
                                pass
                        else:
                            if _MAX_RESULTS_RETURN != 0:
                                _result_data_dict['content'].append(search_data_dict)
                                _MAX_RESULTS_RETURN -= 1
                            else:
                                pass
            elif _api_call_type == 'last':
                _result_data_dict['api_call'] = 'last'
                if isinstance(_browse_data_content, list):
                    for last_data_dict in _browse_data_content:
                        if _MAX_RESULTS_RETURN != 0:

                            # Changing The date format to milli seconds to store in the resilient table
                            _search_pub_date = last_data_dict.get('Published')
                            _search_pub_date_timestamp = self._get_gm_epoch_time_stamp(date_string=_search_pub_date)
                            last_data_dict['Published'] = _search_pub_date_timestamp

                            _result_data_dict['content'].append(last_data_dict)
                            _MAX_RESULTS_RETURN -= 1
                        else:
                            pass
                elif isinstance(_browse_data_content, dict):
                    raise NotImplementedError()
                else:
                    raise NotImplementedError()
            elif _api_call_type == 'cve':
                _result_data_dict['api_call'] = 'cve'

                # Changing The date format to milli seconds to store in the resilient table
                _search_pub_date = _browse_data_content.get('Published')
                _search_pub_date_timestamp = self._get_gm_epoch_time_stamp(date_string=_search_pub_date)
                _browse_data_content['Published'] = _search_pub_date_timestamp

                _result_data_dict['content'].append(_browse_data_content)
            else:
                _result_data_dict['api_call'] = 'db'
                _result_data_dict['content'].append(_browse_data_content)
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(_result_data_dict)

        except Exception as er:
            yield FunctionError(er)
 