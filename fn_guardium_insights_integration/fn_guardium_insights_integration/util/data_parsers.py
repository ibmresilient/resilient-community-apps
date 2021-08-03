# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
import re


def map_details_assets(event_data, asset_data):
    """
    Based on asset_type needs to map other detail will take some time.
    """
    _data_map = {"user_data": [], "consumed": event_data.get("record").get("consumed")}
    asset_affected = event_data.get("record").get("asset_affected").lower()
    _data_map["asset_affected"] = asset_affected
    _event_details = event_data.get("record").get("event_details")

    # iterating through each anomalies event data to get details and asset information.
    for each_details in _event_details:
        _sub_map = dict()
        _assets = asset_data.get("assets", [])
        for each_asset in _assets:
            _as_name = each_asset.get("name")
            if asset_affected == "user":
                _sub_map["who"] = _as_name
                _sub_map["what"] = {"database_name": each_asset.get("built_in_attributes").get("database_name"),
                                    "server_port": each_asset.get("built_in_attributes").get("server_port"),
                                    "service_name": each_asset.get("built_in_attributes").get("service_name"),
                                    "sever_hostname": each_asset.get("built_in_attributes").get("server_hostname"),
                                    "server_ip": each_asset.get("ip")}
            elif asset_affected == "object":
                _sub_map["what"] = {"database_name": each_asset.get("built_in_attributes").get("database_name"),
                                    "table_name": _as_name,
                                    "server_port": each_asset.get("built_in_attributes").get("server_port"),
                                    "service_name": each_asset.get("built_in_attributes").get("service_name"),
                                    "sever_hostname": each_asset.get("built_in_attributes").get(
                                        "server_hostname"),
                                    "server_ip": each_asset.get("ip")}
            elif asset_affected == "datasource":
                _sub_map["what"] = {"database_name": each_asset.get("built_in_attributes").get("database_name"),
                                    "server_port": each_asset.get("built_in_attributes").get("server_port"),
                                    "service_name": each_asset.get("built_in_attributes").get("service_name"),
                                    "sever_hostname": each_asset.get("built_in_attributes").get("server_hostname"),
                                    "server_ip": each_asset.get("ip")}
            _sub_map["when"] = each_details.get("when")
            _sub_map["where"] = each_details.get("where")
            _sub_map["why"] = each_details.get("why")
            if "logical_operation" in each_details.get("what"):
                _sub_map["sequence_anomaly"] = each_details.get("what").get("logical_operation").split()
            _data_map["user_data"].append(_sub_map)

    # populating html data
    desc_html = ""
    desc_html += "<p><div><strong>Consumed &emsp;&emsp;&emsp;&emsp;: </strong>{}</div></p>".format(
        _data_map.get("consumed"))
    desc_html += "<p><div><strong>Asset Affected &emsp;&emsp;: </strong>{}</div></p>".format(
        _data_map.get("asset_affected"))
    for u_data in _data_map.get("user_data"):
        desc_html += "<p><div><strong>Who &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;: </strong>{}</div></p>".format(
            u_data.get("who", ""))

        # Adding what data
        what_data = u_data.get("what", {})
        _what_html = ""
        for what_key, what_value in what_data.items():
            _what_html += "{} : {}<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;".format(
                re.sub("_", " ", what_key).title(), what_value)
        desc_html += "<p><div><strong>What &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;: </strong>{}</div></p>".format(
            _what_html)

        # Adding when data
        when_data = u_data.get("when", {})
        for when_key, when_value in when_data.items():
            desc_html += "<p><div><strong>When &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;: </strong>{} : {}</div></p>".format(
                re.sub("_", " ", when_key).title(), when_value)

        # adding where data
        where_data = u_data.get("where")
        if not where_data:
            desc_html += "<p><div><strong>Where &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;: </strong></div></p>"
        else:
            for where_key, where_value in where_data.items():
                desc_html += "<p><div><strong>Where &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;: </strong>{} : {}</div></p>".format(
                    re.sub("_", " ", where_key).title(), where_value)

        # adding why data
        why_data = u_data.get("why").get("details", {})
        _why_html = ""
        for why_key, why_value in why_data.items():
            _why_html += "{} : {}<br>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;".format(
                re.sub("_", " ", why_key).title(), why_value)
        desc_html += "<p><div><strong>Why &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;: </strong>{}</div></p>".format(
            _why_html)

        # Sequence anamoly
        if "sequence_anomaly" in _data_map.get("user_data")[0]:
            seq_data = ""
            for seq in _data_map.get("user_data")[0].get("sequence_anomaly", []):
                seq_data += "<p>{};</p>".format(seq)
            desc_html += "<p><div><strong>Sequence anomaly : </strong>{}</div></p>".format(seq_data)
    return _data_map, desc_html
