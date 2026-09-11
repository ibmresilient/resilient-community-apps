from unittest.mock import ANY, Mock
from fn_service_now.util.resilient_helper import ResilientHelper


def test_get_table_name_non_secops():
    config_data = {
        "sn_host": "https://test.service-now.com",
        "sn_api_uri": "/api/x_ibmrt_resilient/api",
        "sn_table_name": "incident",
        "sn_username": "ibmresilient",
        "sn_password": "$testpassword"
    }

    res_helper = ResilientHelper({}, config_data)

    assert res_helper.get_table_name() == "incident"

def test_get_table_name_secops():
    config_data = {
        "sn_host": "https://test.service-now.com",
        "sn_api_uri": "/api/x_ibmrt_resilient/api",
        "sn_table_name": "sn_si_incident",
        "sn_username": "ibmresilient",
        "sn_password": "$testpassword"
    }

    res_helper = ResilientHelper({}, config_data)

    assert res_helper.get_table_name() == "sn_si_incident"

def test_get_table_with_function_inputs():
    config_data = {
        "sn_host": "https://test.service-now.com",
        "sn_api_uri": "/api/x_ibmrt_resilient/api",
        "sn_table_name": "sn_si_incident",
        "sn_username": "ibmresilient",
        "sn_password": "$testpassword"
    }

    res_helper = ResilientHelper({}, config_data)

    # note the difference here from the config data
    assert res_helper.get_table_name(fn_table_name_input="incident") == "incident"

def test_get_table_with_function_inputs_secops():
    config_data = {
        "sn_host": "https://test.service-now.com",
        "sn_api_uri": "/api/x_ibmrt_resilient/api",
        "sn_table_name": "incident",
        "sn_username": "ibmresilient",
        "sn_password": "$testpassword"
    }

    res_helper = ResilientHelper({}, config_data)

    # note the difference here from the config data
    assert res_helper.get_table_name(fn_table_name_input="sn_si_incident") == "sn_si_incident"

def test_api_key_auth_init_without_username_password():
    config_data = {
        "sn_host": "https://test.service-now.com",
        "sn_api_uri": "/api/x_ibmrt_resilient/api",
        "sn_table_name": "incident",
        "sn_api_key": "test_api_key"
    }

    res_helper = ResilientHelper({}, config_data)

    assert res_helper._auth_mode == "api_key"
    assert res_helper.username is None

def test_sn_api_request_uses_api_key_header():
    config_data = {
        "sn_host": "https://test.service-now.com",
        "sn_api_uri": "/api/x_ibmrt_resilient/api",
        "sn_table_name": "incident",
        "sn_api_key": "test_api_key"
    }

    res_helper = ResilientHelper({}, config_data)
    response = Mock(request=Mock(method="GET", url="https://test.service-now.com", body=None), status_code=200)

    res_helper.rc = Mock()
    res_helper.rc.execute.return_value = response
    result = res_helper.sn_api_request("GET", "/test_connection", return_whole_response_obj=True, callback=lambda x: x)

    assert result == response
    res_helper.rc.execute.assert_called_once_with(
        method="GET",
        url="https://test.service-now.com/api/x_ibmrt_resilient/api/test_connection",
        headers={"Content-Type": "application/json", "Accept": "application/json", "x-sn-apikey": "test_api_key"},
        params=None,
        data="null",
        callback=ANY
    )

def test_sn_api_request_uses_basic_auth_when_api_key_missing():
    config_data = {
        "sn_host": "https://test.service-now.com",
        "sn_api_uri": "/api/x_ibmrt_resilient/api",
        "sn_table_name": "incident",
        "sn_username": "ibmresilient",
        "sn_password": "$testpassword"
    }

    res_helper = ResilientHelper({}, config_data)
    response = Mock(request=Mock(method="GET", url="https://test.service-now.com", body=None), status_code=200)

    res_helper.rc = Mock()
    res_helper.rc.execute.return_value = response
    result = res_helper.sn_api_request("GET", "/test_connection", return_whole_response_obj=True, callback=lambda x: x)

    assert result == response
    res_helper.rc.execute.assert_called_once_with(
        method="GET",
        url="https://test.service-now.com/api/x_ibmrt_resilient/api/test_connection",
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        params=None,
        data="null",
        callback=ANY,
        auth=("ibmresilient", "$testpassword")
    )
