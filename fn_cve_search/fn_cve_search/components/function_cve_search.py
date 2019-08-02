# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cve_search.util.cve import make_rest_api_get_call, get_gm_epoch_time_stamp


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_cve_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cve_search", {})

        # Getting CVE DataBase URL from app.config file
        self.CVE_BASE_URL = self.options.get('cve_base_url') + '/{}'

    def _search_cve_api(self, vendor_name=None, product=None):
        """
        :param vendor_name:  Name of the Vendor
        :param product:   Name of the Product
        :return:JSON with all the vulnerabilities as per vendor and product
        """
        if vendor_name is not None and product is not None:
            search_api = '{}/{}/{}'.format(self.CVE_BASE_URL.format('search'), vendor_name, product)
        elif vendor_name is not None and product is None:
            search_api = '{}/{}'.format(self.CVE_BASE_URL.format('search'), vendor_name)
        elif vendor_name is None and product is not None:
            search_api = '{}/{}'.format(self.CVE_BASE_URL.format('search'), product)
        return make_rest_api_get_call(search_api, api_call='search')

    def _get_specific_cve_data(self, cve_id=None):
        """
        :param cve_id: Specific CVE ID
        :return:a JSON of a specific CVE ID
        """
        if cve_id:
            specific_cve_url = '{}/{}'.format(self.CVE_BASE_URL.format('cve'), cve_id)
            return make_rest_api_get_call(specific_cve_url, api_call='cve')
        else:
            raise FunctionError("Please Specify the CVE ID to search for Vulnerability")

    def _last_30_cves(self):
        """
        :return:a JSON of the last 30 CVEs including CAPEC, CWE and CPE expansions
        """
        last_url = '{}'.format(self.CVE_BASE_URL.format('last'))
        return make_rest_api_get_call(last_url, api_call='last')

    def _parse_search_results(self, api_data, cve_pub_date_from, cve_pub_date_to, max_res_counter):
        """
        :param api_data:CVE Search Rest API Call Result Data to be Parsed
        :param cve_pub_date_from: User Given from Published date
        :param cve_pub_date_to: User Given up to Published date
        :param max_res_counter : maximum no of vulnerabilities to return
        :return: Array of search data dictionaries
        """
        search_data = None
        tmp_search_data = []
        if isinstance(api_data, list):
            search_data = api_data
        elif isinstance(api_data, dict):
            search_data = api_data.get('data')
        else:
            raise NotImplementedError("Search Data type is not recognized")
        if search_data is not None:
            for search_data_dict in search_data:
                search_pub_date = search_data_dict.get('Published')
                search_pub_date_timestamp = get_gm_epoch_time_stamp(date_string=search_pub_date)

                # Changing The date format to milli seconds to store in the resilient table
                search_data_dict['Published'] = search_pub_date_timestamp

                if cve_pub_date_from is not None and cve_pub_date_to is not None:
                    if (search_pub_date_timestamp >= cve_pub_date_from) and (
                            search_pub_date_timestamp <= cve_pub_date_to):
                        if max_res_counter != 0:
                            tmp_search_data.append(search_data_dict)
                            max_res_counter -= 1
                elif cve_pub_date_from is not None and cve_pub_date_to is None:
                    if search_pub_date_timestamp >= cve_pub_date_from:
                        if max_res_counter != 0:
                            tmp_search_data.append(search_data_dict)
                            max_res_counter -= 1
                elif cve_pub_date_from is None and cve_pub_date_to is not None:
                    if search_pub_date_timestamp <= cve_pub_date_to:
                        if max_res_counter != 0:
                            tmp_search_data.append(search_data_dict)
                            max_res_counter -= 1
                else:
                    if max_res_counter != 0:
                        tmp_search_data.append(search_data_dict)
                        max_res_counter -= 1
            return tmp_search_data

    def _parse_last_cve_results(self, api_data, max_res_counter):
        """
        :param api_data:CVE Last 30 CVE's Rest API Call Result Data to Parsed
        :param max_res_counter : maximum no of vulnerabilities to return
        :return:an array of latest CVE's
        """
        tmp_last_cve_data = []
        if isinstance(api_data, list):
            for last_data_dict in api_data:
                if max_res_counter != 0:
                    # Changing The date format to milli seconds to store in the resilient table
                    search_pub_date = last_data_dict.get('Published')
                    search_pub_date_timestamp = get_gm_epoch_time_stamp(date_string=search_pub_date)
                    last_data_dict['Published'] = search_pub_date_timestamp
                    tmp_last_cve_data.append(last_data_dict)
                    max_res_counter -= 1
                else:
                    break
            return tmp_last_cve_data
        elif isinstance(api_data, dict):
            raise NotImplementedError("dictionary datatypes are not supported")
        else:
            raise NotImplementedError("result last cve call datatypes is not recognized")

    def _parse_cve_results(self, api_data):
        """

        :param api_data: Specific CVE Rest API Call Result Data to Parsed
        :return:an array of specific cve data
        """
        tmp_cve_list = []
        # Changing The date format to milli seconds to store in the resilient table
        search_pub_date = api_data.get('Published')
        search_pub_date_timestamp = get_gm_epoch_time_stamp(date_string=search_pub_date)
        api_data['Published'] = search_pub_date_timestamp
        tmp_cve_list.append(api_data)
        return tmp_cve_list

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cve_search", {})

    @function("function_cve_search")
    def _function_cve_search_function(self, event, *args, **kwargs):
        """Function: A Function to Search  Common Vulnerability Exposures Data from https://cve.circl.lu Data Base."""
        try:
            # Get the function parameters:
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
            MAX_RESULTS_RETURN = int(self.options.get('max_results_display'))

            # Variables to Store Parsed CVE API Data
            _result_search_data = dict()

            log = logging.getLogger(__name__)
            log.info("cve_id: %s", cve_id)
            log.info("cve_vendor: %s", cve_vendor)
            log.info("cve_product: %s", cve_product)
            log.info("cve_published_date_from: %s", cve_published_date_from)
            log.info("cve_published_date_to: %s", cve_published_date_to)

            yield StatusMessage(
                "Searching the CVE Database. ID:{}, Vendor:{}, Product:{}".format(cve_id, cve_vendor, cve_product))

            if cve_id is None and ((cve_vendor is None and cve_product) or (cve_vendor and cve_product is None)):
                raise ValueError("Specify both cve_vendor and cve_product or cve-id")
            if cve_id and (cve_product or cve_vendor):
                raise ValueError("Specify both cve_vendor and cve_product or cve-id")

            if cve_id:
                _browse_data = self._get_specific_cve_data(cve_id=cve_id)

            elif cve_vendor and cve_product:
                _browse_data = self._search_cve_api(vendor_name=cve_vendor, product=cve_product)
            else:
                _browse_data = self._last_30_cves()

            # Defining a key in result dictionary to store parsed data
            _result_search_data['content'] = []

            # Type Of the rest api call like browse,search,specific cve,last, db info
            api_call_type = _browse_data['api_call']

            # Rest Api Response Data
            _browse_data_content = _browse_data['content']
            if _browse_data_content:
                if api_call_type == 'search':
                    _result_search_data['api_call'] = 'search'
                    search_data_list = self._parse_search_results(_browse_data_content, cve_published_date_from,
                                                                  cve_published_date_to, MAX_RESULTS_RETURN)
                    _result_search_data['content'].extend(search_data_list)
                elif api_call_type == 'cve':
                    _result_search_data['api_call'] = 'cve'
                    cve_data_list = self._parse_cve_results(_browse_data_content)
                    _result_search_data['content'].extend(cve_data_list)
                elif api_call_type == 'last':
                    _result_search_data['api_call'] = 'last'
                    last_data_list = self._parse_last_cve_results(_browse_data_content, MAX_RESULTS_RETURN)
                    _result_search_data['content'].extend(last_data_list)
            log.debug("The Data Received from CVE DB : {}".format(_result_search_data))
            yield StatusMessage("Successfully searched the CVE Database.")

            # Produce a FunctionResult with the results
            yield FunctionResult(_result_search_data)
        except Exception as er:
            yield FunctionError(er)
