# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import pytest, unittest, logging

from unittest.mock import patch, MagicMock
from fn_rest_api.lib.authentication_handler import *

AUTH_TYPE = "auth_type"
CODE_OR_REFRESH_TOKEN = "code_or_refresh_token"

def mock_update_tokens(obj):
    assert obj._oauth_properties.get(TOKEN_URL)
    assert obj._oauth_properties.get(REFRESH_TOKEN)
    assert obj._oauth_properties.get(CLIENT_ID)
    assert obj._oauth_properties.get(CLIENT_SECRET)
    if obj._oauth_properties.get(TOKEN_URL) == "https://www.validurl.com":
        return True
    else:
        return False

@pytest.fixture
def fx_create_oauth_auth_client():
    yield OAuth2Authorization(None, {}, {})


def test_constants():
    assert DEFAULT_AUTH_CONTENT_TYPE == "application/x-www-form-urlencoded"
    assert REFRESH_GRANT_TYPE == "refresh_token"
    assert ACCESS_GRANT_TYPE == "authorization_code"
    assert AUTH_URL == "auth_url"
    assert TOKEN_URL == "token_url"
    assert CODE == "code"
    assert STATE == "state"
    assert SCOPE == "scope"
    assert CLIENT_ID == "client_id"
    assert GRANT_TYPE == "grant_type"
    assert TOKEN_TYPE == "token_type"
    assert EXPIRES_IN == "expires_in"
    assert ACCESS_TOKEN == "access_token"
    assert CLIENT_SECRET == "client_secret"
    assert REFRESH_TOKEN == "refresh_token"
    assert RESPONSE_MODE == "response_mode"
    assert RESPONSE_TYPE == "response_type"
    assert REDIRECT_URI == "redirect_uri"
    assert CONTENT_TYPE == "content_type"
    assert ADDITIONAL_HEADERS == "additional_headers"
    assert ADDITIONAL_ATTRIBUTES == "additional_attributes"




def test_check_oauth_not_ready(fx_create_oauth_auth_client):
    _status = fx_create_oauth_auth_client.check_oauth_ready()
    assert _status == {
        'oauth_supported'         : False,
        'access_token_flow'       : False,
        'authorization_flow'      : False,
        'client_credentials_flow' : False,
        'refresh_token_flow'      : False}

def test_check_oauth_with_access_token_not_ready(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs = {}
    fx_create_oauth_auth_client._oauth_inputs = {
        ACCESS_TOKEN : "access123"}
    _status = fx_create_oauth_auth_client.check_oauth_ready()
    assert _status == {
        'oauth_supported'         : True,
        'access_token_flow'       : True,
        'authorization_flow'      : False,
        'client_credentials_flow' : False,
        'refresh_token_flow'      : False}

def test_check_oauth_with_refresh_token_not_ready(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs = {}
    fx_create_oauth_auth_client._oauth_inputs = {
        REFRESH_TOKEN : "refresh123",
        CODE : "code123"}
    _status = fx_create_oauth_auth_client.check_oauth_ready()
    assert _status == {
        'oauth_supported'         : False,
        'access_token_flow'       : False,
        'authorization_flow'      : False,
        'client_credentials_flow' : False,
        'refresh_token_flow'      : False}

def test_check_oauth_with_client_id_and_code(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs = {
        TOKEN_URL : "https://www.example.com/tokens",
        CLIENT_ID : "client123",
        CODE : "code123"}
    _status = fx_create_oauth_auth_client.check_oauth_ready()
    assert _status == {
        'oauth_supported'         : True,
        'access_token_flow'       : False,
        'authorization_flow'      : True,
        'client_credentials_flow' : False,
        'refresh_token_flow'      : False}

def test_check_oauth_with_client_id_and_access_token(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs = {}
    fx_create_oauth_auth_client._oauth_inputs = {
        TOKEN_URL : "https://www.example.com/tokens",
        CLIENT_ID : "client123",
        ACCESS_TOKEN : "access123"}
    _status = fx_create_oauth_auth_client.check_oauth_ready()
    assert _status == {
        'oauth_supported'         : True,
        'access_token_flow'       : True,
        'authorization_flow'      : False,
        'client_credentials_flow' : False,
        'refresh_token_flow'      : False}

def test_check_oauth_with_client_id_and_refresh_token(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs = {}
    fx_create_oauth_auth_client._oauth_inputs = {
        TOKEN_URL : "https://www.example.com/tokens",
        CLIENT_ID : "client123",
        REFRESH_TOKEN : "refresh123"}
    _status = fx_create_oauth_auth_client.check_oauth_ready()
    assert _status == {
        'oauth_supported'         : True,
        'access_token_flow'       : False,
        'authorization_flow'      : False,
        'client_credentials_flow' : False,
        'refresh_token_flow'      : True}

def test_check_oauth_with_client_credentials_flow(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs = {}
    fx_create_oauth_auth_client._oauth_inputs = {
        TOKEN_URL : "https://www.example.com/tokens",
        CLIENT_ID : "client123",
        CLIENT_SECRET : "secret123",
        GRANT_TYPE : "client_credentials"}
    _status = fx_create_oauth_auth_client.check_oauth_ready()
    assert _status == {
        'oauth_supported'         : True,
        'access_token_flow'       : False,
        'authorization_flow'      : False,
        'client_credentials_flow' : True,
        'refresh_token_flow'      : False}

def test_check_oauth_with_client_credentials_flow_title(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs = {}
    fx_create_oauth_auth_client._oauth_inputs = {
        TOKEN_URL : "https://www.example.com/tokens",
        CLIENT_ID : "client123",
        CLIENT_SECRET : "secret123",
        GRANT_TYPE : "Client_Credentials"}
    _status = fx_create_oauth_auth_client.check_oauth_ready()
    assert _status == {
        'oauth_supported'         : True,
        'access_token_flow'       : False,
        'authorization_flow'      : False,
        'client_credentials_flow' : True,
        'refresh_token_flow'      : False}

def test_check_oauth_with_client_credentials_flow_allcaps(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs = {}
    fx_create_oauth_auth_client._oauth_inputs = {
        TOKEN_URL : "https://www.example.com/tokens",
        CLIENT_ID : "client123",
        CLIENT_SECRET : "secret123",
        GRANT_TYPE : "CLIENT_CREDENTIALS"}
    _status = fx_create_oauth_auth_client.check_oauth_ready()
    assert _status == {
        'oauth_supported'         : True,
        'access_token_flow'       : False,
        'authorization_flow'      : False,
        'client_credentials_flow' : True,
        'refresh_token_flow'      : False}

def test_check_oauth_all_true(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs = {}
    fx_create_oauth_auth_client._oauth_inputs = {
        TOKEN_URL : "https://www.example.com/tokens",
        CLIENT_ID : "client123",
        CLIENT_SECRET : "secret123",
        GRANT_TYPE : "CLIENT_CREDENTIALS",
        REFRESH_TOKEN : "refreshmeup112233",
        ACCESS_TOKEN : "access112233",
        CODE : "access_code"}
    _status = fx_create_oauth_auth_client.check_oauth_ready()
    assert _status == {
        'oauth_supported'         : True,
        'access_token_flow'       : True,
        'authorization_flow'      : True,
        'client_credentials_flow' : True,
        'refresh_token_flow'      : True}




def test_compile_empty_headers(fx_create_oauth_auth_client):
    header = fx_create_oauth_auth_client._compile_headers()
    assert len(header) == 1
    assert "Authorization" in header.keys()
    assert len(list(header.values())) == 1
    assert "None None" == header["Authorization"]

def test_token_type_in_header(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs[TOKEN_TYPE] = "keychain"
    header = fx_create_oauth_auth_client._compile_headers()
    assert "keychain" in list(header.values())[0]
    # assert "keychain 112233" == list(header.values())[0]

def test_compiled_header(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs[TOKEN_TYPE] = "Vault Code"
    fx_create_oauth_auth_client._oauth_inputs[ACCESS_TOKEN] = "112233"
    header = fx_create_oauth_auth_client._compile_headers()
    assert "Vault Code 112233" == header["Authorization"]



def test_response_handling_status_code300(fx_create_oauth_auth_client):
    with pytest.raises(IntegrationError):
        mock_value = MagicMock(status_code=300)
        fx_create_oauth_auth_client._process_endpoint_response(mock_value)

def test_response_handling_status_code200(fx_create_oauth_auth_client):
    with pytest.raises(ValueError):
        mock_value = MagicMock(status_code=200)
        mock_value.json = MagicMock(return_value = {})
        mock_value.text = MagicMock(return_value = "invalid response")
        fx_create_oauth_auth_client._process_endpoint_response(mock_value)

def test_response_handling(fx_create_oauth_auth_client):
    fx_create_oauth_auth_client._oauth_inputs = {}
    response_data = {
        REFRESH_TOKEN : "refresh1234",
        ACCESS_TOKEN  : "access1234",
        TOKEN_TYPE    : "bearer"}
    additional_params = {
        GRANT_TYPE : "refresh_token"}
    mock_response = MagicMock(status_code=200)
    mock_response.json = MagicMock(return_value = response_data)
    assert fx_create_oauth_auth_client._process_endpoint_response(mock_response)
    response_data.update(additional_params)
    assert fx_create_oauth_auth_client._oauth_inputs == response_data

def _mock_fetch_renew_tokens(_, token_url, client_id, **kwargs):
    kwargs.update({
        "token_url" : token_url,
        "client_id" : client_id})
    return kwargs


def test_unsupported_flow(caplog):
    caplog.set_level(logging.INFO)
    client = OAuth2Authorization(None, {
        CLIENT_ID : "",
        REFRESH_TOKEN : "",
        CODE : ""}, {})
    with pytest.raises(IntegrationError):
        client.authenticate()
    assert caplog.records[0].levelname == "ERROR"
    assert caplog.records[0].message == 'Application does not support OAuth authentication.'

@patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization.fetch_renew_tokens", _mock_fetch_renew_tokens)
def test_refresh_flow(caplog):
    def compare_response(_, response):
        assert response == {
            'auth_type': 'refresh_token',
            'token_value': 'refreshmeup112233',
            'grant_type': 'refresh_token',
            'client_secret': None,
            'redirect_uri': None,
            'scope': None,
            'token_url': 'www.token_url.com',
            'client_id': 'clientid112233'}
        assert caplog.records[0].levelname == "INFO"
        assert caplog.records[0].message == f"Application OAuth compliant. Detected: Refresh Token Flow"
        assert caplog.records[1].levelname == "INFO"
        assert caplog.records[1].message == f"REFRESH_TOKEN detected. Fetching new ACCESS_TOKEN and possibly a REFRESH_TOKEN"

    caplog.set_level(logging.INFO)
    client = OAuth2Authorization(None, {
        TOKEN_URL : "www.token_url.com",
        REFRESH_TOKEN : "refreshmeup112233",
        CLIENT_ID : "clientid112233"}, {})

    with patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization._process_endpoint_response", compare_response):
        client.authenticate()

@patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization.fetch_renew_tokens", _mock_fetch_renew_tokens)
def test_client_credentials_flow(caplog):
    def compare_response(_, response):
        assert response == {
            'grant_type': 'client_credentials',
            'client_secret': 'clientsecret112233',
            'redirect_uri': None,
            'scope': None,
            'token_url': 'www.token_url.com',
            'client_id': 'clientid112233'}
        assert caplog.records[0].levelname == "INFO"
        assert caplog.records[0].message == f"Application OAuth compliant. Detected: Client-Credentials Flow"
        assert caplog.records[1].levelname == "INFO"
        assert caplog.records[1].message == f"Client-Credentials detected. Fetching new ACCESS_TOKEN and possibly a REFRESH_TOKEN"

    caplog.set_level(logging.INFO)
    client = OAuth2Authorization(None, {
        TOKEN_URL : "www.token_url.com",
        CLIENT_SECRET : "clientsecret112233",
        CLIENT_ID  : "clientid112233",
        GRANT_TYPE : "client_credentials"}, {})

    with patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization._process_endpoint_response", compare_response):
        client.authenticate()

@patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization.fetch_renew_tokens", _mock_fetch_renew_tokens)
def test_authorization_flow(caplog):
    def compare_response(_, response):
        assert response == {
            'auth_type': 'code',
            'token_value': 'code112233',
            'grant_type': 'authorization_code',
            'client_secret': None,
            'redirect_uri': None,
            'scope': None,
            'token_url': 'www.token_url.com',
            'client_id': 'clientid112233'}
        assert caplog.records[0].levelname == "INFO"
        assert caplog.records[0].message == f"Application OAuth compliant. Detected: Authorization Flow"
        assert caplog.records[1].levelname == "INFO"
        assert caplog.records[1].message == f"CODE detected. Fetching new ACCESS_TOKEN and possibly a REFRESH_TOKEN"

    caplog.set_level(logging.INFO)
    client = OAuth2Authorization(None, {
        TOKEN_URL : "www.token_url.com",
        CODE : "code112233",
        CLIENT_ID : "clientid112233"}, {})

    with patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization._process_endpoint_response", compare_response):
        client.authenticate()

@patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization.fetch_renew_tokens", _mock_fetch_renew_tokens)
def test_grant_type_override(caplog):
    def compare_response(_, response):
        assert response == {
            'auth_type': 'code',
            'token_value': 'code112233',
            'grant_type': 'overridden_grant',
            'client_secret': None,
            'redirect_uri': None,
            'scope': None,
            'token_url': 'www.token_url.com',
            'client_id': 'clientid112233'}
        assert caplog.records[0].levelname == "INFO"
        assert caplog.records[0].message == f"Application OAuth compliant. Detected: Authorization Flow"
        assert caplog.records[1].levelname == "INFO"
        assert caplog.records[1].message == f"CODE detected. Fetching new ACCESS_TOKEN and possibly a REFRESH_TOKEN"

    caplog.set_level(logging.INFO)
    client = OAuth2Authorization(None, {
        TOKEN_URL : "www.token_url.com",
        CODE : "code112233",
        CLIENT_ID : "clientid112233",
        GRANT_TYPE : "overridden_grant"}, {})

    with patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization._process_endpoint_response", compare_response):
        client.authenticate()


def test_renew_tokens():
    def compare_response(method, url, headers, data, **retry_options):
        assert method == "post"
        assert url == "www.token_url.com"
        assert headers == {
            'content_type': 'application/ibm',
            'header_key1': 'header_value1',
            'header_key2': 'header_value2'}
        assert data == {
            'add_key1': 'add_value1',
                'add_key2': 'add_value2',
                'client_id': 'clientid112233',
                'client_secret': 'secret123',
                'code': 'code112233',
                'redirect_uri': 'www.redirect.com',
                'scope': 'bass treble mids'}
        assert retry_options == {}

    mock_rc = MagicMock()
    mock_rc.execute = compare_response
    client = OAuth2Authorization(mock_rc, {}, {})
    client.fetch_renew_tokens(**{
        TOKEN_URL : "www.token_url.com",
        TOKEN_VALUE : "code112233",
        CLIENT_ID : "clientid112233",
        AUTH_TYPE : "code",
        CLIENT_SECRET : "secret123",
        GRANT_TYPE : "",
        REDIRECT_URI : "www.redirect.com",
        SCOPE : "bass treble mids",
        CONTENT_TYPE : "application/ibm",
        "additional_attributes" : {
            "add_key1" : "add_value1",
            "add_key2" : "add_value2"},
        "additional_headers" : {
            "header_key1" : "header_value1",
            "header_key2" : "header_value2"}})

def test_defaults():
    def compare_response(method, url, headers, data, **retry_options):
        assert method == "post"
        assert url == "www.token_url.com"
        assert headers == {'content_type': 'application/x-www-form-urlencoded'}
        assert data == {'client_id': 'clientid112233'}
        assert retry_options == {}

    mock_rc = MagicMock()
    mock_rc.execute = compare_response
    client = OAuth2Authorization(mock_rc, {}, {})
    client.fetch_renew_tokens(**{
        TOKEN_URL : "www.token_url.com",
        CLIENT_ID : "clientid112233"})

def test_additional_attributes():
    def compare_response(method, url, headers, data, **retry_options):
        assert method == "post"
        assert url == "www.token_url.com"
        assert headers == {
            'content_type': 'application/x-www-form-urlencoded',
            "header_key1" : "header_value1",
            "header_key2" : "header_value2"}
        assert data == {
            'client_id': 'clientid112233',
            "add_key1" : "add_value1",
            "add_key2" : "add_value2"}
        assert retry_options == {}

    mock_rc = MagicMock()
    mock_rc.execute = compare_response
    client = OAuth2Authorization(mock_rc, {}, {})
    client.fetch_renew_tokens(**{
        TOKEN_URL : "www.token_url.com",
        CLIENT_ID : "clientid112233",
        "additional_attributes" : {
            "add_key1" : "add_value1",
            "add_key2" : "add_value2"},
        "additional_headers" : {
            "header_key1" : "header_value1",
            "header_key2" : "header_value2"}})

def test_retry():
    def compare_response(method, url, headers, data, **retry_options):
        assert method == "post"
        assert url == "www.token_url.com"
        assert headers == {'content_type': 'application/x-www-form-urlencoded'}
        assert data == {'client_id': 'clientid112233'}
        assert retry_options == {"retry_tries" : 10, "retry_delay" : 9, "retry_backoff" : 7}

    mock_rc = MagicMock()
    mock_rc.execute = compare_response
    client = OAuth2Authorization(mock_rc, {}, {
        "retry_tries" : 10,
        "retry_delay" : 9,
        "retry_backoff" : 7})
    client.fetch_renew_tokens(**{
        TOKEN_URL : "www.token_url.com",
        CLIENT_ID : "clientid112233"})
