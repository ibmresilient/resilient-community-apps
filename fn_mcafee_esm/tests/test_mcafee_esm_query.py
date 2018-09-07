# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import get_test_config, generate_response, string_test_config
from fn_mcafee_esm.components.mcafee_esm_query import query_esm, get_results
from fn_mcafee_esm.util.helper import check_config


PACKAGE_NAME = "fn_mcafee_esm"
FUNCTION_NAME = "mcafee_esm_query"

# Read test configuration-data
t_config_data = get_test_config()
config_data = string_test_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_mcafee_esm_query_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("mcafee_esm_query", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("mcafee_esm_query_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestMcafeeEsmQuery:
    """ Tests for the mcafee_esm_query function"""

    @patch("requests.post")
    def test_query_esm(self, mocked_requests_post):
        ops = check_config(t_config_data)
        content1 = {
            "totalRows": 0,
            "resultID": "123456789",
            "totalResultID": "0",
            "groupByString": "",
            "countColumn": 0,
            "labelColumn": 0,
            "attributeColumn": 0,
            "drilldownColumn": 1
        }
        content2 = {
            'totalRecords': 1,
            'complete': True,
            'milliseconds': 5,
            'percentComplete': 100
        }
        mocked_requests_post.side_effect = [generate_response(content1, 200),
                                            generate_response(content2, 200)]
        data = '{"config": {"timeRange": "CUSTOM", "customStart": "2018-08-15T14:49:25.324Z", "customEnd": "2018-08-20T15:49:25.324Z", "order": [{"direction": "ASCENDING", "field": {"name": "FirstTime"}}], "includeTotal": "false", "fields": [{"name": "FirstTime"}, {"name": "LastTime"}, {"name": "DSIDSigID"}, {"name": "EventCount"}, {"name": "SrcIP"}, {"name": "Rule.msg"}, {"name": "AppID"}, {"name": "Filename"}, {"name": "HostID"}, {"name": "Object_Type"}, {"name" : "Threat_Name"}], "filters": [{"type": "EsmFieldFilter", "field": {"name": "DSIDSigID"}, "operator": "IN", "values": [{"type": "EsmBasicValue", "value": "306-50080"}]}]}}'
        r_ID, r = query_esm(ops, {}, data)

        assert 1 == r
        assert '{"resultID": "123456789"}' == r_ID

    @patch("requests.post")
    def test_get_results(self, mocked_requests_post):
        ops = check_config(t_config_data)
        content = {u'rows': [{u'values': [u'08/20/2018 14:58:23', u'08/20/2018 14:58:23', u'306-50080', u'1', u'::', u'A physical network interface connection has been made or removed', u'', u'', u'', u'', u'']}], u'columns': [{u'name': u'Alert.FirstTime'}, {u'name': u'Alert.LastTime'}, {u'name': u'Alert.DSIDSigID'}, {u'name': u'Alert.EventCount'}, {u'name': u'Alert.SrcIP'}, {u'name': u'Rule.msg'}, {u'name': u'Alert.BIN(1)'}, {u'name': u'Alert.4259843'}, {u'name': u'Alert.BIN(4)'}, {u'name': u'Alert.BIN(10)'}, {u'name': u'Alert.65538'}]}

        mocked_requests_post.return_value = generate_response(content, 200)
        response = get_results(ops, {}, "123456789")

        assert content == response

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("mcafee_esm_qry_event_type, mcafee_esm_qry_config, expected_results", [
        ('EVENT', {"type": "text", "content": '{"config": {"timeRange": "CUSTOM", "customStart": "2018-08-15T14:49:25.324Z", "customEnd": "2018-08-20T15:49:25.324Z", "order": [{"direction": "ASCENDING", "field": {"name": "FirstTime"}}], "includeTotal": "false", "fields": [{"name": "FirstTime"}, {"name": "LastTime"}, {"name": "DSIDSigID"}, {"name": "EventCount"}, {"name": "SrcIP"}, {"name": "Rule.msg"}, {"name": "AppID"}, {"name": "Filename"}, {"name": "HostID"}, {"name": "Object_Type"}, {"name" : "Threat_Name"}], "filters": [{"type": "EsmFieldFilter", "field": {"name": "DSIDSigID"}, "operator": "IN", "values": [{"type": "EsmBasicValue", "value": "306-50080"}]}]}}'}, {'inputs': {'mcafee_esm_qry_config': '{"config": {"timeRange": "CUSTOM", "customStart": "2018-08-15T14:49:25.324Z", "customEnd": "2018-08-20T15:49:25.324Z", "order": [{"direction": "ASCENDING", "field": {"name": "FirstTime"}}], "includeTotal": "false", "fields": [{"name": "FirstTime"}, {"name": "LastTime"}, {"name": "DSIDSigID"}, {"name": "EventCount"}, {"name": "SrcIP"}, {"name": "Rule.msg"}, {"name": "AppID"}, {"name": "Filename"}, {"name": "HostID"}, {"name": "Object_Type"}, {"name" : "Threat_Name"}], "filters": [{"type": "EsmFieldFilter", "field": {"name": "DSIDSigID"}, "operator": "IN", "values": [{"type": "EsmBasicValue", "value": "306-50080"}]}]}}', 'mcafee_esm_qry_event_type': 'EVENT'}, 'result': {u'rows': [{u'values': [u'08/20/2018 14:58:23', u'08/20/2018 14:58:23', u'306-50080', u'1', u'::', u'A physical network interface connection has been made or removed', u'', u'', u'', u'', u'']}], u'columns': [{u'name': u'Alert.FirstTime'}, {u'name': u'Alert.LastTime'}, {u'name': u'Alert.DSIDSigID'}, {u'name': u'Alert.EventCount'}, {u'name': u'Alert.SrcIP'}, {u'name': u'Rule.msg'}, {u'name': u'Alert.BIN(1)'}, {u'name': u'Alert.4259843'}, {u'name': u'Alert.BIN(4)'}, {u'name': u'Alert.BIN(10)'}, {u'name': u'Alert.65538'}]}})
    ])
    @patch("requests.post")
    def test_success(self, mocked_requests_post, circuits_app, mcafee_esm_qry_event_type, mcafee_esm_qry_config, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "mcafee_esm_qry_event_type": mcafee_esm_qry_event_type,
            "mcafee_esm_qry_config": mcafee_esm_qry_config
        }
        content1 = {
            "status": "success"
        }
        content2 = {
            "totalRows": 0,
            "resultID": "123456789",
            "totalResultID": "0",
            "groupByString": "",
            "countColumn": 0,
            "labelColumn": 0,
            "attributeColumn": 0,
            "drilldownColumn": 1
        }
        content3 = {
            'totalRecords': 1,
            'complete': True,
            'milliseconds': 5,
            'percentComplete': 100
        }
        content4 = {u'rows': [{u'values': [u'08/20/2018 14:58:23', u'08/20/2018 14:58:23', u'306-50080', u'1', u'::', u'A physical network interface connection has been made or removed', u'', u'', u'', u'', u'']}], u'columns': [{u'name': u'Alert.FirstTime'}, {u'name': u'Alert.LastTime'}, {u'name': u'Alert.DSIDSigID'}, {u'name': u'Alert.EventCount'}, {u'name': u'Alert.SrcIP'}, {u'name': u'Rule.msg'}, {u'name': u'Alert.BIN(1)'}, {u'name': u'Alert.4259843'}, {u'name': u'Alert.BIN(4)'}, {u'name': u'Alert.BIN(10)'}, {u'name': u'Alert.65538'}]}
        mocked_requests_post.side_effect = [generate_response(content1, 200),
                                            generate_response(content2, 200),
                                            generate_response(content3, 200),
                                            generate_response(content4, 200)]

        results = call_mcafee_esm_query_function(circuits_app, function_params)
        del results["metrics"]
        assert(expected_results == results)
