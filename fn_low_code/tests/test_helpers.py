import pytest
from resilient_lib import IntegrationError

from fn_low_code.lib.helpers import set_security_data

basic_security = {
    "api_key" : "api-key0123",
    "api_key_secret" : "api-secret0123", # YXBpLWtleTAxMjM6YXBpLXNlY3JldDAxMjM=
    "generate_bearer_token" : False,
    "scheme" : "BASIC"
}

apikey_header_security = {
    "api_key" : "api-key0123:api-secret0123",
    "api_key_in": "header",
    "generate_bearer_token" : False,
    "scheme" : "ApiKey"
}

apikey_query_security = {
    "api_key" : "api-key0123:api-secret0123",
    "api_key_in": "query",
    "api_key_param_name": "put_api_key_here",
    "generate_bearer_token": False,
    "scheme" : "ApiKey"
}

bearer_security = {
    "auth_token" : "abcdefg123456",
    "scheme" : "Bearer"
}

@pytest.mark.parametrize("mock_inputs, expected_headers, expected_query_params", [
    (basic_security, {"Authorization": "Basic YXBpLWtleTAxMjM6YXBpLXNlY3JldDAxMjM="}, {}),
    (apikey_header_security, {"Authorization": f"{apikey_header_security['api_key']}"}, {}),
    (apikey_query_security, {}, {apikey_query_security["api_key_param_name"]: apikey_query_security["api_key"]}),
    (bearer_security, {"Authorization": f"Bearer {bearer_security['auth_token']}"}, {})
])
def test_set_security_data(mock_inputs, expected_headers, expected_query_params):
    headers, query_params = set_security_data(mock_inputs)
    assert headers == expected_headers
    assert query_params == expected_query_params

def test_set_security_data_fail():
    scheme = "unknown"
    bad_security = {
        "auth_token" : "abcdefg123456",
        "scheme" : scheme
    }
    with pytest.raises(IntegrationError) as interror:
        headers, query_params = set_security_data(bad_security)
        
        # make sure headers and query inputs stayed the same
        assert not headers
        assert not query_params
        assert f"Scheme {scheme} not supported" in interror.value.value
