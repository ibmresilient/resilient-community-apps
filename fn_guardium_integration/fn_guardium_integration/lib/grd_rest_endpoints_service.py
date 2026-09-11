# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
import json
from collections import OrderedDict
from fn_guardium_integration.lib.grd_api_service import GuardiumAPI
from fn_guardium_integration.lib.custom_exceptions import check_for_invalid_response
from fn_guardium_integration.util.static_data import DEFAULT_DELTA_SCAN_RANGE, GRD_BASE_URL, GRD_SEARCH, GRD_FIELD, \
    GRD_LIST_PARAM, GRD_ONLINE_REPORT, GRD_GRP_MEMBER_BY_DESC, GRD_CREATE_GRP_MEM_BY_DESC, RE_INSTALL_POLICY_URL, \
    LIST_INSTALLED_POLICY, GRD_FIELDS_JSON, SEARCH_COUNT


class GrdRestEndpoint(GuardiumAPI):

    def __init__(self, options, client_secret, unique_id, log):
        super(GrdRestEndpoint, self).__init__(options, client_secret, unique_id, log)
        self.utc_offset = int(options.get("utc_offset")) if options.get("utc_offset") else DEFAULT_DELTA_SCAN_RANGE
        self.log = log
        self.last_proc_violation_data = []  # to store last processed violation data
        self.last_proc_outliers_data = []  # to store last processed outliers data

    def get_fields_titles(self):
        """
        Gets the Guardium fields data.
        """
        _result = self.grd_get(GRD_FIELD.format(host=self.guardium_host, port=self.port))
        _result_json = _result.json()
        if "ErrorCode" in _result_json:
            if _result_json.get("ErrorCode") == "1004":
                if _result_json.get("ErrorMessage").find("getFieldsTitles: Unknown error") != -1:
                    self.log.warning("""Error occurred while getting Guardium fields data.
                    using default fields data to manipulate search data.""")
                    return GRD_FIELDS_JSON
        else:
            check_for_invalid_response(_result)
            if isinstance(_result_json, dict):
                if "Message" in _result_json:
                    titles_dict = json.loads(_result_json.get("Message"))
                else:
                    raise ValueError(u"Guardium fieldsTitle data format is not recognized!")
            elif isinstance(_result_json, list):
                titles_dict = _result_json[0]
            else:
                raise ValueError(u"Guardium fieldsTitle data format is not recognized!")
            return titles_dict

    def grd_search(self, query=None, count=SEARCH_COUNT, start=None, with_facets=None, category=None, summary_by=None,
                   start_time=None, end_time=None, api_taret_host=None):
        """
        Calls Guardium Search function.
        """
        _titles_dict = self.get_fields_titles()
        payload_params = {"QUERY": query, "COUNT": count, "START": start, "WITH_FACETS": with_facets,
                          "CATEGORY": category, "SUMMARY_BY": summary_by, "api_target_host": api_taret_host}
        __search_url = GRD_SEARCH.format(base_url=GRD_BASE_URL.format(host=self.guardium_host, port=self.port),
                                         start_time=start_time, end_time=end_time)
        _response = self.grd_get(__search_url, params=payload_params)
        check_for_invalid_response(_response)
        _response = _response.json()[0]
        order_of_fields = []
        if "maxLengthMapByOrder" in _response:
            for x in _response.get("maxLengthMapByOrder"):
                for k, v in x.items():
                    order_of_fields.append(k)
            _response.pop("maxLengthMapByOrder")
        else:
            order_of_fields = []
        for index, record in enumerate(_response["items"]):
            new_record = OrderedDict()
            new_record['id'] = record.get('id')
            for field_number in order_of_fields:
                if field_number in record:
                    new_record[_titles_dict.get(field_number)] = record.get(field_number)
            _response["items"][index] = new_record
        return [_response]

    def list_parameter_names_by_report_name(self, report_name):
        """
        Function get run time parameters to run guardium reports.
        :param report_name: Select Report Name
        :return: Guardium api return data
        """
        result = self.grd_get(GRD_LIST_PARAM.format(host=self.guardium_host, port=self.port),
                              params={"reportName": report_name})
        check_for_invalid_response(result)
        return result.json()

    def create_online_report(self, report, fetchsize, period_from="", period_to="", show_aliases="TRUE",
                             remote_data_source="", param_label="", param_value="", sortcolumn="", sorttype=""):
        """
        Function to run guardium reports from resilient.
        :param report: Guardium Report Name
        :param fetchsize: No of events to be fetched
        :param period_from: From Date
        :param period_to: To Date
        :param show_aliases:
        :param remote_data_source: Remote host Names
        :param param_label: Additional Parameter Names
        :param param_value: Additional Parameter Value
        :param sortcolumn: Name of the columns to be shorted
        :param sorttype: Type `ASC`/`DESC`
        :return:
        """

        report_parameters = {"QUERY_FROM_DATE": period_from,
                             "QUERY_TO_DATE": period_to,
                             "SHOW_ALIASES": show_aliases,
                             "DBUserName": "%",
                             "REMOTE_SOURCE": remote_data_source,
                             "HostnameLike": "%",
                             "hostLike": "%"}
        if param_label:
            param_label_list = param_label.split(',')
            param_value_list = param_value.split(',')
            __additional_param = dict()
            for index, value in enumerate(param_label_list):
                __additional_param[value] = param_value_list[index]
            report_parameters.update(__additional_param)

        task = {"reportName": report, "reportParameter": report_parameters, "fetchSize": fetchsize,
                "sortColumn": sortcolumn, "sortType": sorttype}
        response = self.grd_post(GRD_ONLINE_REPORT.format(host=self.guardium_host, port=self.port), json=task)
        check_for_invalid_response(response)
        return json.loads(response.text, object_pairs_hook=OrderedDict)

    def group_members_by_group_desc(self, group_desc):
        """
        group members by using group description
        :param group_desc: Group Description
        :return:
        """
        result = self.grd_get(GRD_GRP_MEMBER_BY_DESC.format(host=self.guardium_host, port=self.port),
                              params={"desc": group_desc})
        check_for_invalid_response(result)
        return result.json()

    def create_member_to_group_by_desc(self, group_desc, member):
        """
        Add Member to group
        :param group_desc: Group Description
        :param member: Name of the member
        :return:
        """
        result = self.grd_post(GRD_CREATE_GRP_MEM_BY_DESC.format(host=self.guardium_host, port=self.port),
                               json={"desc": group_desc, "member": "++{}++++".format(member)})
        check_for_invalid_response(result)
        return result.json()

    def reinstall_policy(self, policy, api_target_host=""):
        """
        Function to re-install the policy in Guardium.
        :param policy: Name of the policy
        :param api_target_host: Guardium Host IP/DNS
        :return:
        """
        result = self.grd_post(RE_INSTALL_POLICY_URL.format(host=self.guardium_host, port=self.port),
                               json={"policy": policy, "api_target_host": api_target_host})
        return result.json()

    def list_policy_installed(self):
        """
        Function to get installed policy list from guardium
        """
        result = self.grd_get(LIST_INSTALLED_POLICY.format(host=self.guardium_host, port=self.port))
        check_for_invalid_response(result)
        return result.json()
