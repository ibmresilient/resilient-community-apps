#
# Unit tests for fn_qradar_integration/util/qradar_utils.py
#
from fn_qradar_integration.util import qradar_utils
from fn_qradar_integration.util import qradar_constants
from fn_qradar_integration.util.SearchWaitCommand import SearchWaitCommand, SearchFailure, SearchJobFailure
import base64
import requests
from mock import Mock
from mock import patch
import mock
import urllib

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



@patch("requests.Session.delete")
@patch("requests.Session.get")
@patch("requests.Session.post")
def test_qradar_client(mocked_session_post,
                       mocked_session_get,
                       mocked_session_delete):
    # 1. Test connection
    qradar_client = qradar_utils.QRadarClient(host,
                                              username=username,
                                              password=password,
                                              token=None,
                                              cafile=cafile)
    mocked_session_get.return_value = _generateResponse([
        {"id":1,"deprecated":False,"root_resource_ids":[],"removed":True,"version":"0.1"},
        {"id":2,"deprecated":False,"root_resource_ids":[],"removed":True,"version":"0.2"},
        {"id":3,"deprecated":False,"root_resource_ids":[],"removed":True,"version":"1.0"}], 200)

    connected = qradar_client.verify_connect()
    assert connected == True

    # 2. Test search_ref_set
    ref_set_name = "Sample Suspect IPs"
    mocked_session_get.return_value = _generateResponse({"creation_time":1523020929069,
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
    mocked_session_get.side_effect = Exception("Failed")
    try:
        ret = qradar_client.search_ref_set(ref_set_name, "1.1.1.1")
        assert False
    except qradar_utils.RequestError:
        assert True

    # 4. normal add_ref_element
    mocked_session_post.return_value = _generateResponse({"creation_time": 1523020929069,
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
    mocked_session_post.side_effect = Exception("Failed")
    try:
        qradar_client.add_ref_element(ref_set_name, "8.8.8.8")
    except qradar_utils.RequestError:
        assert True

    # 6. normal delete_ref_element
    mocked_session_delete.return_value = _generateResponse({"creation_time": 1523020929069,
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
    mocked_session_delete.side_effect = Exception("Failed")
    try:
        qradar_client.delete_ref_element(ref_set_name, "8.8.8.8")
    except qradar_utils.DeleteError:
        assert True


@patch("fn_qradar_integration.util.SearchWaitCommand.SearchWaitCommand.perform_search")
def test_ariel_search(mocked_perform_search):
    qradar_client = qradar_utils.QRadarClient(host,
                                              username=username,
                                              password=password,
                                              token=None,
                                              cafile=cafile)
    query_string = "SELECT * FROM events"
    range_start = 1
    range_end = 10
    ret_events = {
                   "events":[
                            {"starttime":"12345","category":"cat1"},
                            {"starttime":"23456","category":"cat2"}
                            ]
                  }
    mocked_perform_search.return_value = ret_events
    ret = qradar_client.ariel_search(query_string, range_start, range_end)


    assert ret == ret_events


@patch("requests.Session.get")
@patch("requests.Session.post")
def test_ariel_search(mocked_session_post,
                      mocked_session_get):
    timeout = 10
    poll = 2
    range_start = 1
    range_end = 100
    query_str = "SELECT * FROM events"

    search_cmd = qradar_utils.ArielSearch(timeout, poll)
    assert search_cmd.search_timeout == timeout
    assert search_cmd.polling_period == poll

    search_cmd.set_range_start(range_start)
    search_cmd.set_range_end(range_end)

    # 1. Test get_search_id

    mocked_session_post.return_value = _generateResponse({"search_id": search_id}, 200)

    sid = search_cmd.get_search_id(query_str)
    expected_url = "https://" + host + "/api/" + qradar_constants.ARIEL_SEARCHES

    mocked_session_post.assert_called_with(url=expected_url,
                                           headers=qradar_utils.AuthInfo.get_authInfo().headers,
                                           data={"query_expression": query_str.encode("utf-8")},
                                           verify=qradar_utils.AuthInfo.get_authInfo().cafile)
    assert sid == search_id

    # 2. Test exception
    mocked_session_post.side_effect = Exception("Failed")

    try:
        sid = search_cmd.get_search_id(query_str)
        assert(False)
    except SearchJobFailure as e:
        assert True

    # 3. Test check_status
    # 3.1 Complete status
    mocked_session_get.return_value = _generateResponse({"status": qradar_constants.SEARCH_STATUS_COMPLETED}, 200)
    status = search_cmd.check_status(search_id)
    assert status == SearchWaitCommand.SEARCH_STATUS_COMPLETED

    # 3.2 WAIT status
    mocked_session_get.return_value = _generateResponse({"status": qradar_constants.SEARCH_STATUS_WAIT}, 200)
    status = search_cmd.check_status(search_id)
    assert status == SearchWaitCommand.SEARCH_STATUS_WAITING

    # 3.3 Exception
    mocked_session_get.side_effect = Exception("Failed")
    try:
        status = search_cmd.check_status(search_id)
        assert False
    except SearchFailure:
        assert True

    # 4. Test get_search_result
    # 4.1 normal return
    mocked_session_get.return_value = _generateResponse({"events": []}, 200)
    mocked_session_get.side_effect = None
    results = search_cmd.get_search_result(search_id)
    assert results["events"] == []

    # 4.2 Exception
    mocked_session_get.side_effect = Exception("Failed")
    try:
        status = search_cmd.get_search_result(search_id)
        assert False
    except SearchFailure:
        assert True


