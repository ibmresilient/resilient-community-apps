# encoding: utf-8
#
# Unit tests for fn_qradar_integration/util/qradar_utils.py
#
from fn_qradar_integration.util import qradar_utils
from fn_qradar_integration.util import qradar_constants
from fn_qradar_integration.util.SearchWaitCommand import SearchWaitCommand, SearchFailure, SearchJobFailure
from base64 import b64encode
from mock import patch
from six import string_types
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
    assert isinstance(result, string_types)

@patch("fn_qradar_integration.util.qradar_utils.quote_func")
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
    assert auth_info.headers["Authorization"] == b"Basic " + b64encode((username + ':' + password).encode("ascii"))
    assert auth_info.headers["Accept"] == "application/json"

    # use token to auth
    auth_info.create(host,
                     username=None,
                     password=None,
                     token=token,
                     cafile=cafile)
    assert auth_info.headers["SEC"] == token

def test_qradar_client():
    with patch("fn_qradar_integration.util.qradar_utils.AuthInfo.make_call") as mocked_get_call:
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

        # 2. Test search_ref_set
        ref_set_name = "Sample Suspect IPs"
        mocked_get_call.return_value = _generateResponse({"creation_time":1523020929069,
                                                             "timeout_type":"FIRST_SEEN",
                                                             "number_of_elements":2,
                                                             "data":[
                                                                 {"last_seen":1523020984874,
                                                                  "first_seen":1523020984874,
                                                                  "source":"admin",
                                                                  "value":"8.8.8.8"}],
                                                             "name":"Sample Suspect IPs",
                                                             "element_type":"IP"},
                                                            200)
        ret = qradar_client.search_ref_set(ref_set_name, "8.8.8.8")
        assert ret["found"] == "True"

        # 3. Exception in search_ref_set
        mocked_get_call.side_effect = Exception("Failed")
        try:
            ret = qradar_client.search_ref_set(ref_set_name, "1.1.1.1")
            assert False
        except qradar_utils.IntegrationError:
            assert True

    # 4. normal add_ref_element
    with patch("fn_qradar_integration.util.qradar_utils.AuthInfo.make_call") as mocked_post_call:
        mocked_post_call.return_value = _generateResponse({"creation_time": 1523020929069,
                                                            "timeout_type": "FIRST_SEEN",
                                                             "number_of_elements": 2,
                                                             "data": [
                                                                 {"last_seen": 1523020984874,
                                                                  "first_seen": 1523020984874,
                                                                  "source": "admin",
                                                                  "value": "8.8.8.8"}],
                                                             "name": "Sample Suspect IPs",
                                                             "element_type": "IP"},
                                                            200)
        ret = qradar_client.add_ref_element(ref_set_name, "8.8.8.8")
        assert ret["status_code"] == 200

        # 5. add_ref_element exception
        mocked_post_call.side_effect = Exception("Failed")
        try:
            qradar_client.add_ref_element(ref_set_name, "8.8.8.8")
        except qradar_utils.IntegrationError:
            assert True

    # 6. normal delete_ref_element
    with patch("fn_qradar_integration.util.qradar_utils.AuthInfo.make_call") as mocked_delete_call:
        mocked_delete_call.return_value = _generateResponse({"creation_time": 1523020929069,
                                                             "timeout_type": "FIRST_SEEN",
                                                             "number_of_elements": 2,
                                                             "data": [
                                                                 {"last_seen": 1523020984874,
                                                                  "first_seen": 1523020984874,
                                                                  "source": "admin",
                                                                  "value": "8.8.8.8"}],
                                                             "name": "Sample Suspect IPs",
                                                             "element_type": "IP"},
                                                            200)
        ret = qradar_client.delete_ref_element(ref_set_name, "8.8.8.8")
        assert ret["status_code"] == 200

        # 7. exception in delete_ref_element
        mocked_delete_call.side_effect = Exception("Failed")
        try:
            qradar_client.delete_ref_element(ref_set_name, "8.8.8.8")
        except qradar_utils.IntegrationError:
            assert True

@patch("fn_qradar_integration.util.SearchWaitCommand.SearchWaitCommand.perform_search")
def test_ariel_search_more(mocked_perform_search):
    qradar_client = qradar_utils.QRadarClient(host,
                                              username=username,
                                              password=password,
                                              token=None,
                                              cafile=cafile)
    query_string = "SELECT * FROM events"
    query_all_results = False
    range_start = 1
    range_end = 10
    time_out = 1000
    ret_events = {
                   "events":[
                            {"starttime":"12345","category":"cat1"},
                            {"starttime":"23456","category":"cat2"}
                            ]
                  }
    mocked_perform_search.return_value = ret_events
    ret = qradar_client.ariel_search(query_string, query_all_results, range_start, range_end, time_out)

    assert ret == ret_events

def test_ariel_search():
    timeout = 10
    poll = 2
    range_start = 1
    range_end = 100
    query_str = "SELECT * FROM events"

    search_cmd = qradar_utils.ArielSearch(timeout, poll)
    assert search_cmd.search_timeout == timeout
    assert search_cmd.polling_period == poll

    timeout = 100
    search_cmd.set_timeout(timeout)
    assert search_cmd.search_timeout == timeout

    search_cmd.set_range_start(range_start)
    search_cmd.set_range_end(range_end)

    # 1. Test get_search_id
    with patch("fn_qradar_integration.util.qradar_utils.AuthInfo.make_call") as mocked_post_call:
        mocked_post_call.return_value = _generateResponse({"search_id": search_id}, 200)

        sid = search_cmd.get_search_id(query_str)
        expected_url = "https://" + host + "/api/" + qradar_constants.ARIEL_SEARCHES

        mocked_post_call.assert_called_with("POST", expected_url,
                                            data={"query_expression": query_str.encode("utf-8")})

        assert sid == search_id

        # 2. Test exception
        mocked_post_call.side_effect = Exception("Failed")

        try:
            sid = search_cmd.get_search_id(query_str)
            assert(False)
        except SearchJobFailure as e:
            assert True

    with patch("fn_qradar_integration.util.qradar_utils.AuthInfo.make_call") as mocked_get_call:
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

@patch("fn_qradar_integration.util.qradar_utils.QRadarClient.get_all_ref_set")
@patch("fn_qradar_integration.util.qradar_utils.QRadarClient.search_ref_set")
def test_find_all_ref_set_contains(mocked_search_ref_set, mocked_get_all_ref_set):

    qradar_client = qradar_utils.QRadarClient(host,
                                              username=username,
                                              password=password,
                                              token=None,
                                              cafile=cafile)

    all_sets = [
        {
            "timeout_type": "FIRST_SEEN",
            "name": "Reference Set 1",
            "element_type": "IP"
        },
        {
            "timeout_type": "FIRST_SEEN",
            "name": "Reference Set 2",
            "element_type": "Hash-512"
        }
    ]

    mocked_get_all_ref_set.return_value = all_sets

    ret1 = {
        "found": "False",
        "content": None
    }
    content = {
        "item_name": "Item1"
    }
    ret2 = {
        "found": "True",
        "content": content
    }

    mocked_search_ref_set.side_effect=[ret1, ret2]

    ret = qradar_client.find_all_ref_set_contains("Item1")

    assert len(ret) == 1
    assert ret[0] == content

@patch("fn_qradar_integration.util.qradar_utils.AuthInfo.make_call")
def test_get_ref_set(mocked_make_call):
    qradar_client = qradar_utils.QRadarClient(host,
                                              username=username,
                                              password=password,
                                              token=None,
                                              cafile=cafile)

    all_sets = [
        {
            "timeout_type": "FIRST_SEEN",
            "name": "Reference Set 1",
            "element_type": "IP"
        },
        {
            "timeout_type": "FIRST_SEEN",
            "name": "Reference Set 2",
            "element_type": "Hash-512"
        }
    ]
    mocked_make_call.return_value = _generateResponse(all_sets, 200)

    ret = qradar_client.get_all_ref_set()

    assert len(ret) == 2

    mocked_make_call.side_effect = Exception("Error!")

    try:
        ret = qradar_client.get_all_ref_set()
        assert False
    except qradar_utils.IntegrationError:
        assert True

def test_quote():
    """
    Adding test for INT-3117 - working with URLs and reference sets causes an error.
    The issue is that forward slash doesn't get replaced by urllib.quote, and it causes issue with URL routing.
    """
    from six.moves.urllib_parse import quote as urlquote
    assert (qradar_utils.quote("/") == urlquote(qradar_utils.FORWARD_SLASH))

    test_val = "å∫ç∂´ƒ:_%^.abcdef1234"
    assert qradar_utils.quote(test_val) == urlquote(test_val)
