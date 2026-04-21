# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
from fn_guardium_insights_integration.lib.insights_rest_handler import GuardiumInsightsAPI
from fn_guardium_insights_integration.util.constants import *


class InsightsServices(GuardiumInsightsAPI):
    def __init__(self, options, log=None):
        super(InsightsServices, self).__init__(options, log)
        self.guardium_host = options.get("insights_host")
        self.port = options.get("rest_service_port")

    def retrieve_anamolies(self, start_time, end_time):
        """
        A method to retrieve anamolies data based on given start and stop time stamps
        """
        _url = ANAMOLIES.format(host=self.guardium_host, port=self.port)
        _param_dict = {"isResolved": "ALL", "isTicketAssigned": "ALL", "asset.asset_type": "ALL_ASSET_TYPE",
                       "asset.user_type": "ALL_USER_TYPE", "filter.start_time": start_time, "filter.end_time": end_time}
        _response = self.grd_get(_url, params=_param_dict)
        return _response

    def get_anamolies_details_by_event_id(self, event_id):
        """
        A method to retrieve anamolies details based on passed event id.
        """
        _url = ANAMOLIES_DETAILS.format(host=self.guardium_host, port=self.port, event_id=event_id)
        _response = self.grd_get(_url)
        return _response

    def get_assets_information(self, anomaly_details):
        """
        A method to get Assets Information
        asset_type: user, system, all_asset_types, public_network etc. for more info refer refer insights api guide.
        """
        asset_affected = anomaly_details.get("record").get("asset_affected").lower()
        _event_details = anomaly_details.get("record").get("event_details")[0]
        _database_id = _event_details.get("what").get("asset").get("database_id")

        # Defining the asset type based on GI
        if asset_affected == "user":
            _type = _event_details.get("who").get("type")
            _actor = _event_details.get("who").get("actor")
            if _type == "ACCESS_ID":
                _tmp_url = "&asset_type=user&access_id={}".format(_actor)
            else:
                _tmp_url = "&asset_type=user&database_id={}&asset_name={}".format(_database_id, _actor)
        elif asset_affected == "object":
            _table_name = _event_details.get("what").get("asset").get("table")
            _tmp_url = "&asset_type=database_table&database_id={}&asset_name={}".format(_database_id, _table_name)
        elif asset_affected == "datasource":
            _tmp_url = "&asset_type=database&database_id={}".format(_database_id)
        else:
            _tmp_url = "&asset_type=all_asset_types"
        _url = ASSETS.format(host=self.guardium_host, port=self.port)
        _final_url = "{}{}".format(_url, _tmp_url)
        try:
            _response = self.grd_get(_final_url)
        except Exception as er:
            self.log.info("Error while getting the assets information of anomalies.- {}".format(er))
            _response = dict()
        return _response

    def block_user(self, body_payload):
        """
        Method to block the user.
        """
        _url = BLOCK_USER.format(host=self.guardium_host, port=self.port)
        _response = self.grd_post(_url, json=body_payload)
        return _response

    def list_all_reports(self):
        """
        Method to List all available GI reports.
        """
        _url = LIST_REPORTS.format(host=self.guardium_host, port=self.port)
        _response = self.grd_get(_url)
        return _response

    @staticmethod
    def generate_report_payload(from_date, to_date, fetch_size, data_source_ip, port):
        """
        Method to generate the Classification report payload.
        """
        _pay_body = CLASSIFICATION_REPORT_BODY.copy()
        _tmp_ip_dict = {
            "brackets": {
                "brackets_id": 3,
                "sequence": 3,
                "option_type": "OR",
                "filters_array": [
                    {
                        "condition": {
                            "filter_id": 1,
                            "sequence": 1,
                            "header_id": "916",
                            "header_name": "DataSourceIP",
                            "field_nls_translation_key": "CLASSIFICATION_DATASOURCEIP",
                            "table_name": "CLASSIFICATION",
                            "parameter_type": "FREE_TEXT",
                            "values": [data_source_ip],
                            "operator_type": "EQUAL"
                        }
                    }
                ]
            }
        }

        _tmp_port_dict = {
            "brackets": {
                "brackets_id": 3,
                "sequence": 3,
                "option_type": "OR",
                "filters_array": [
                    {
                        "condition": {
                            "filter_id": 1,
                            "sequence": 1,
                            "header_id": "919",
                            "header_name": "Port",
                            "field_nls_translation_key": "CLASSIFICATION_PORT",
                            "table_name": "CLASSIFICATION",
                            "parameter_type": "FREE_TEXT",
                            "values": [port],
                            "operator_type": "EQUAL"
                        }
                    }
                ]
            }
        }

        _tmp_port_dict_2 = {
            "brackets": {
                "brackets_id": 4,
                "sequence": 4,
                "option_type": "OR",
                "filters_array": [
                    {
                        "condition": {
                            "filter_id": 2,
                            "sequence": 2,
                            "header_id": "919",
                            "header_name": "Port",
                            "field_nls_translation_key": "CLASSIFICATION_PORT",
                            "table_name": "CLASSIFICATION",
                            "parameter_type": "FREE_TEXT",
                            "values": [port],
                            "operator_type": "EQUAL"
                        }
                    }
                ]
            }
        }
        if data_source_ip and not port:
            _pay_body["report_definition"]["report_filters"]["filters_array"].insert(0, _tmp_ip_dict)
        elif port and not data_source_ip:
            _pay_body["report_definition"]["report_filters"]["filters_array"].insert(0, _tmp_port_dict)
        elif data_source_ip and port:
            _pay_body["report_definition"]["report_filters"]["filters_array"].insert(0, _tmp_ip_dict)
            _pay_body["report_definition"]["report_filters"]["filters_array"].insert(1, _tmp_port_dict_2)

        _pay_body["fetch_size"] = fetch_size
        _pay_body["runtime_parameter_list"][0]["value"] = from_date
        _pay_body["runtime_parameter_list"][1]["value"] = to_date
        return _pay_body

    def run_report(self, body_payload):
        """
        Method to run the report against given payload data.
        """
        _url = RUN_REPORT.format(host=self.guardium_host, port=self.port)
        _response = self.grd_post(_url, json=body_payload)
        return _response

    @staticmethod
    def get_report_id(report_list, report_name):
        for each_report in report_list.get("reports_list"):
            name = each_report.get("report_name")
            if name == report_name:
                return each_report.get("report_id")

    @staticmethod
    def get_report_data(report_list, report_name):
        for each_report in report_list.get("reports_list"):
            name = each_report.get("report_name")
            if name == report_name:
                return each_report
