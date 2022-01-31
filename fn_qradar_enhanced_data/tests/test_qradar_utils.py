# encoding: utf-8
#
# Unit tests for fn_qradar_enhanced_data/util/qradar_utils.py
#
from fn_qradar_enhanced_data.util import qradar_utils
from fn_qradar_enhanced_data.util import qradar_constants
from fn_qradar_enhanced_data.util.SearchWaitCommand import SearchWaitCommand, SearchFailure, SearchJobFailure
import base64
import requests
from mock import Mock
from mock import patch
import mock
import urllib
import six
import pytest


# Util function to generate simulated requests response
def _generateResponse(content, status):
    class simResponse:
        def __init__(self, content, status):
            self.status_code = status
            self.content = content

        def json(self):
            return self.content

    return simResponse(content, status)


# Global test data
host = "qradar.instance.com"
username = "admin"
password = "my_password_fake"
token = "FakeSecreteToken"
cafile = True
search_id = "FakeSearch_id"


@pytest.mark.parametrize("val", [ "test", u"test", "ç", u"ç" ])
def test_quote_return(val):
    result = qradar_utils.quote(val)
    assert isinstance(result, six.string_types)


@patch("fn_qradar_enhanced_data.util.qradar_utils.quote_func")
def test_quote_passing_args(mocked_func):
    qradar_utils.quote("test")
    mocked_func.assert_called_with("test".encode("utf-8"))

    qradar_utils.quote("test", "test")
    mocked_func.assert_called_with("test".encode("utf-8"), "test")


def test_auth_info():
    """
    Test singleton AuthInfo
    :return:
    """


    auth_info = qradar_utils.AuthInfo.get_authInfo()
    auth_info.create(host,
                     username=username,
                     password=password,
                     token=None,
                     cafile=cafile)

    assert auth_info.api_url == "https://{}/api/".format(host)
    assert auth_info.cafile == cafile
    assert auth_info.qradar_token == None
    assert auth_info.headers["Authorization"] == b"Basic " + base64.b64encode((username + ':' + password).encode("ascii"))
    assert auth_info.headers["Accept"] == "application/json"

    # use token to auth
    auth_info.create(host,
                     username=None,
                     password=None,
                     token=token,
                     cafile=cafile)
    assert auth_info.headers["SEC"] == token


def test_qradar_client():
    with patch("fn_qradar_enhanced_data.util.qradar_utils.AuthInfo.make_call") as mocked_get_call:
        # 1. Test connection
        qradar_client = qradar_utils.QRadarClient(host,
                                                  username=username,
                                                  password=password,
                                                  token=None,
                                                  cafile=cafile)
        mocked_get_call.return_value = _generateResponse([
            {"id":1,"deprecated":False,"root_resource_ids":[],"removed":True,"version":"0.1"},
            {"id":2,"deprecated":False,"root_resource_ids":[],"removed":True,"version":"0.2"},
            {"id":3,"deprecated":False,"root_resource_ids":[],"removed":True,"version":"1.0"}], 200)

        connected = qradar_client.verify_connect()
        assert connected == True


def test_ariel_graphql_search():
    timeout = 10
    poll = 2
    range_start = 1
    range_end = 100
    query_str = "SELECT * FROM events"

    search_cmd = qradar_utils.ArielSearch(timeout, poll, True)
    assert search_cmd.search_timeout == timeout
    assert search_cmd.polling_period == poll

    timeout = 100
    search_cmd.set_timeout(timeout)
    assert search_cmd.search_timeout == timeout

    # 1. Test get_search_id
    with patch("fn_qradar_enhanced_data.util.qradar_utils.AuthInfo.make_call") as mocked_post_call:
        mocked_post_call.return_value = _generateResponse({"cursor_id": search_id}, 200)

        sid = search_cmd.get_search_id(query_str)
        expected_url = "https://" + host + "/api/" + qradar_constants.ARIEL_SEARCHES
        utf8 = query_str.encode("utf-8")
        data = {"query_expression": utf8}
        headers =  qradar_utils.AuthInfo.get_authInfo().headers.copy()
        mocked_post_call.assert_called_with("POST", expected_url,
                                            data=data, headers=headers)

        assert sid == search_id

        # 2. Test exception
        mocked_post_call.side_effect = Exception("Failed")

        try:
            sid = search_cmd.get_search_id(query_str)
            assert(False)
        except SearchJobFailure as e:
            assert True

    with patch("fn_qradar_enhanced_data.util.qradar_utils.AuthInfo.make_call") as mocked_get_call:
        # 3. Test check_status
        # 3.1 Complete status
        mocked_get_call.return_value = _generateResponse({"status": qradar_constants.SEARCH_STATUS_COMPLETED}, 200)
        status = search_cmd.check_status(search_id)
        assert status == SearchWaitCommand.SEARCH_STATUS_COMPLETED

        # 3.2 WAIT status
        mocked_get_call.return_value = _generateResponse({"status": qradar_constants.SEARCH_STATUS_WAIT}, 200)
        status = search_cmd.check_status(search_id)
        assert status == SearchWaitCommand.SEARCH_STATUS_WAITING

        # 3.3 Exception
        mocked_get_call.side_effect = Exception("Failed")
        try:
            status = search_cmd.check_status(search_id)
            assert False
        except SearchFailure:
            assert True

        # 4. Test get_search_result
        # 4.1 normal return
        mocked_get_call.return_value = _generateResponse({"events": []}, 200)
        mocked_get_call.side_effect = None
        results = search_cmd.get_search_result(search_id)
        assert results["events"] == []

        # 4.2 Exception
        mocked_get_call.side_effect = Exception("Failed")
        try:
            status = search_cmd.get_search_result(search_id)
            assert False
        except SearchFailure:
            assert True


@patch("fn_qradar_enhanced_data.util.qradar_utils.QRadarClient.get_qr_sessionid")
@patch("fn_qradar_enhanced_data.util.qradar_utils.AuthInfo.make_call")
def test_get_offense_summary_data(mocked_make_call, mocked_qr_call):

    mocked_qr_call.return_value = ""

    qradar_client = qradar_utils.QRadarClient(host,
                                              username=username,
                                              password=password,
                                              token=None,
                                              cafile=cafile)

    offense_summary = {
        "data":{
            "getOffense":{
                "id": 1,
                "offenseType":{
                    "name": "Source IP"
                }
             }
            }
        }

    mocked_make_call.return_value = _generateResponse(offense_summary, 200)

    ret = qradar_client.get_offense_summary_data(1)

    assert ret["content"]["id"] == offense_summary["data"]["getOffense"]["id"]
    assert ret["content"]["offenseType"]["name"] == offense_summary["data"]["getOffense"]["offenseType"]["name"]

    mocked_make_call.side_effect = Exception("Error!")


@patch("fn_qradar_enhanced_data.util.qradar_utils.QRadarClient.get_qr_sessionid")
@patch("fn_qradar_enhanced_data.util.qradar_utils.AuthInfo.make_call")
def test_get_rules_data(mocked_make_call, mocked_qr_call):
    mocked_qr_call.return_value = ""
    qradar_client = qradar_utils.QRadarClient(host,
                                              username=username,
                                              password=password,
                                              token=None,
                                              cafile=cafile)

    rules_data = {
        "data":{
            "getOffense": {
                "rules": [
                    {
                        "id":1,
                        "name":"test rule"
                    }
                ]
            }
        }

    }

    mocked_make_call.return_value = _generateResponse(rules_data, 200)

    ret = qradar_client.get_rules_data(1)

    assert ret["content"]["rules"][0]["id"] == rules_data["data"]["getOffense"]["rules"][0]["id"]
    assert ret["content"]["rules"][0]["name"] == rules_data["data"]["getOffense"]["rules"][0]["name"]

    mocked_make_call.side_effect = Exception("Error!")


@patch("fn_qradar_enhanced_data.util.qradar_utils.QRadarClient.get_qr_sessionid")
@patch("fn_qradar_enhanced_data.util.qradar_utils.AuthInfo.make_call")
def test_get_sourceip_data(mocked_make_call, mocked_qr_call):
    mocked_qr_call.return_value = ""
    qradar_client = qradar_utils.QRadarClient(host,
                                              username=username,
                                              password=password,
                                              token=None,
                                              cafile=cafile)

    sourceip_data = {
        "data":{
            "getAsset":{
                "id": 1,
                "interfaces":[
                    {
                      "macAddress": "00:00:00:a1:2b:bb"
                    }],
                    "riskScoreSum":5,
                    "vulnerabilityCount":2
            }
        }

    }

    mocked_make_call.return_value = _generateResponse(sourceip_data, 200)

    test_source = {
        "sourceip": "127.0.0.1",
        "domainid": 0
    }

    ret = qradar_client.get_sourceip_data(test_source)

    assert ret["content"]["id"] == sourceip_data["data"]["getAsset"]["id"]
    assert ret["content"]["interfaces"][0]["macAddress"] == sourceip_data["data"]["getAsset"]["interfaces"][0]["macAddress"]

    mocked_make_call.side_effect = Exception("Error!")


@patch("fn_qradar_enhanced_data.util.qradar_utils.QRadarClient.get_qr_sessionid")
@patch("fn_qradar_enhanced_data.util.qradar_utils.AuthInfo.make_call")
def test_get_offense_source(mocked_make_call, mocked_qr_call):
    mocked_qr_call.return_value = ""
    qradar_client = qradar_utils.QRadarClient(host,
                                              username=username,
                                              password=password,
                                              token=None,
                                              cafile=cafile)

    offense_source_data = {
        "data":{
            "getOffense":{
              "sourceAddresses": [
                {
                    "id": 1,
                    "domainId":0,
                    "sourceIp":"127.0.0.1"
                 }
                ]
         }
        }
    }

    mocked_make_call.return_value = _generateResponse(offense_source_data, 200)

    ret = qradar_client.get_offense_source(1)

    assert ret["content"][0]["id"] == offense_source_data["data"]["getOffense"]["sourceAddresses"][0]["id"]
    assert ret["content"][0]["sourceIp"] == offense_source_data["data"]["getOffense"]["sourceAddresses"][0]["sourceIp"]

    mocked_make_call.side_effect = Exception("Error!")


@patch("fn_qradar_enhanced_data.util.qradar_utils.QRadarClient.get_qr_sessionid")
@patch("fn_qradar_enhanced_data.util.qradar_utils.AuthInfo.make_call")
def get_offense_asset_data(mocked_make_call, mocked_qr_call):
    mocked_qr_call.return_value = ""
    qradar_client = qradar_utils.QRadarClient(host,
                                              username=username,
                                              password=password,
                                              token=None,
                                              cafile=cafile)

    asset_data = {
        "data": {
            "getAsset": {
                "id": 1,
                "users":[
                    {
                      "id": 1,
                      "username":"test"
                    }
                ]
            }
        }

    }

    mocked_make_call.return_value = _generateResponse(asset_data, 200)

    test_source = {
        "sourceip": "127.0.0.1",
        "domainid": 0
    }

    ret = qradar_client.offense_asset_data(test_source)

    assert ret["content"]["users"][0]["id"] == asset_data["data"]["getAsset"]["users"][0]["id"]
    assert ret["content"]["users"][0]["username"] == asset_data["data"]["getAsset"]["users"][0]["username"]

    mocked_make_call.side_effect = Exception("Error!")