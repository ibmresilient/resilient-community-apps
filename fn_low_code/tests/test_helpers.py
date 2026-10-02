import pytest
import re
from resilient_lib import IntegrationError, RequestsCommon

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

# edit tenant_id, client_id and client_secret before using
oauth_security = {
    "scheme": "BEARER",
    "generate_bearer_token": True,
    "auth_token_auth_url": "https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
    "auth_token_payload": "grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&scope=https://graph.microsoft.com/.default",
    "auth_token_property_name": "access_token",
    "auth_token_payload_content_type": "application/x-www-form-urlencoded"
}

authorization_pattern = re.compile(r"Bearer .{512,2048}$")

@pytest.mark.parametrize("mock_inputs, expected_headers, expected_query_params", [
    (basic_security, {"Authorization": "Basic YXBpLWtleTAxMjM6YXBpLXNlY3JldDAxMjM="}, {}),
    (apikey_header_security, {"Authorization": f"{apikey_header_security['api_key']}"}, {}),
    (apikey_query_security, {}, {apikey_query_security["api_key_param_name"]: apikey_query_security["api_key"]}),
    (bearer_security, {"Authorization": f"Bearer {bearer_security['auth_token']}"}, {})
])
def test_set_security_data(mock_inputs, expected_headers, expected_query_params):
    headers, query_params = set_security_data(mock_inputs, None)
    assert headers == expected_headers
    assert query_params == expected_query_params

def test_set_security_data_fail():
    scheme = "unknown"
    bad_security = {
        "auth_token" : "abcdefg123456",
        "scheme" : scheme
    }
    with pytest.raises(IntegrationError) as interror:
        headers, query_params = set_security_data(bad_security, None)
        
        # make sure headers and query inputs stayed the same
        assert not headers
        assert not query_params
        assert f"Scheme {scheme} not supported" in interror.value.value

@pytest.mark.livetest
def test_oauth_security_data():
    rc = RequestsCommon({}, {})
    headers, _query_params = set_security_data(oauth_security, rc)
    assert authorization_pattern.findall(headers.get("Authorization"))
