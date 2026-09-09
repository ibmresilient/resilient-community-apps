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
