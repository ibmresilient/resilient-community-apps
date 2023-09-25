# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import pytest
from unittest.mock import patch, MagicMock
from fn_rest_api.lib.authentication_handler import *

AUTH_TYPE = "auth_type"
CODE_OR_REFRESH_TOKEN = "code_or_refresh_token"


def test_check_oauth_ready():

    client = OAuth2Authorization(None, {})
    assert client.check_oauth_ready() == False

    client._oauth_properties = {}
    client._oauth_properties = {
        ACCESS_TOKEN : "access123"}
    assert client.check_oauth_ready()

    client._oauth_properties = {}
    client._oauth_properties = {
        REFRESH_TOKEN : "refresh123",
        CODE : "code123"}
    assert client.check_oauth_ready() == False

    client._oauth_properties = {
        TOKEN_URL : "https://www.example.com/tokens",
        CLIENT_ID : "client123",
        CODE : "code123"}
    assert client.check_oauth_ready()

    client._oauth_properties = {}
    client._oauth_properties = {
        TOKEN_URL : "https://www.example.com/tokens",
        CLIENT_ID : "client123",
        ACCESS_TOKEN : "access123"}
    assert client.check_oauth_ready()

    client._oauth_properties = {}
    client._oauth_properties = {
        TOKEN_URL : "https://www.example.com/tokens",
        CLIENT_ID : "client123",
        REFRESH_TOKEN : "refresh123"}
    assert client.check_oauth_ready()


def test_compile_headers():

    client = OAuth2Authorization(None, {})
    header = client._compile_headers()
    assert len(header) == 1
    assert "Authorization" in header.keys()
    assert len(list(header.values())) == 1
    assert "bearer" in list(header.values())[0]
    assert "None" in list(header.values())[0]

    client._oauth_properties[TOKEN_TYPE] = "keychain"
    header = client._compile_headers()
    assert "keychain" in list(header.values())[0]
    assert "keychain None" == list(header.values())[0]

    client._oauth_properties[TOKEN_TYPE] = "Vault Code"
    client._oauth_properties[ACCESS_TOKEN] = "112233"
    header = client._compile_headers()
    assert "Vault Code 112233" == header["Authorization"]


def mock_fetch_renew_tokens(*args, **kwargs):
    assert TOKEN_URL in kwargs
    assert AUTH_TYPE in kwargs
    assert CODE_OR_REFRESH_TOKEN in kwargs
    assert CLIENT_ID in kwargs
    assert CLIENT_SECRET in kwargs
    assert GRANT_TYPE in kwargs
    assert REDIRECT_URI in kwargs
    assert SCOPE in kwargs
    assert ADDITIONAL_ATTRIBUTES in kwargs

    assert kwargs.get(TOKEN_URL)
    assert kwargs.get(CODE_OR_REFRESH_TOKEN)
    assert kwargs.get(AUTH_TYPE) in [CODE, REFRESH_TOKEN]
    assert kwargs.get(CLIENT_ID)
    
    ret = {
        REFRESH_TOKEN : "refresh1234",
        ACCESS_TOKEN  : "access1234",
        TOKEN_TYPE    : "bearer"}
    mock_response = MagicMock()
    mock_response.json = MagicMock(return_value = ret)
    mock_response.status_code = 200
    return mock_response


@patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization.fetch_renew_tokens", mock_fetch_renew_tokens)
def test_update_tokens_access():
    client = OAuth2Authorization(None, {
        CLIENT_ID : "client_id 1234",
        TOKEN_URL : "https://www.tokenurl.com",
        REFRESH_TOKEN : "refreshmeup"})
    assert client._update_tokens()

    with pytest.raises(ValueError) as err:
        client = OAuth2Authorization(None, {
            CLIENT_ID : "client_id 1234",
            TOKEN_URL : "https://www.tokenurl.com",
            CODE : "refreshmeup"})
        assert client._update_tokens()


@patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization.fetch_renew_tokens", mock_fetch_renew_tokens)
def test_update_tokens_refresh():
    client = OAuth2Authorization(None, {
        CLIENT_ID : "client_id 1234",
        TOKEN_URL : "https://www.tokenurl.com",
        REFRESH_TOKEN : "refreshmeup"})
    assert client._update_tokens()

    with pytest.raises(ValueError) as err:
        client = OAuth2Authorization(None, {
            CLIENT_ID : "client_id 1234",
            TOKEN_URL : "https://www.tokenurl.com",
            CODE : "refreshmeup"})
        assert client._update_tokens()


@patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization.fetch_renew_tokens", mock_fetch_renew_tokens)
def test_refresh_tokens():
    client = OAuth2Authorization(None, {
        CLIENT_ID : "client_id 1234",
        TOKEN_URL : "https://www.tokenurl.com",
        CODE : "refreshmeup"})
    assert client._get_tokens()

    with pytest.raises(ValueError) as err:
        client = OAuth2Authorization(None, {
            CLIENT_ID : "client_id 1234",
            TOKEN_URL : "https://www.tokenurl.com",
            REFRESH_TOKEN : "refreshmeup"})
        assert client._get_tokens()


def test_process_endpoint_response():
    client = OAuth2Authorization(None, {})
    with pytest.raises(IntegrationError):
        mock_value = MagicMock(status_code=300)
        client._process_endpoint_response(mock_value)

    with pytest.raises(ValueError):
        mock_value = MagicMock(status_code=200)
        mock_value.json = MagicMock(return_value = {})
        mock_value.text = MagicMock(return_value = "invalid response")
        client._process_endpoint_response(mock_value)

    client._oauth_properties = {}
    response_data = {
        REFRESH_TOKEN : "refresh1234",
        ACCESS_TOKEN  : "access1234",
        TOKEN_TYPE    : "bearer"}
    mock_response = MagicMock(status_code=200)
    mock_response.json = MagicMock(return_value = response_data)
    assert client._process_endpoint_response(mock_response)
    assert client._oauth_properties == response_data


def mock_update_tokens(self):
    assert self._oauth_properties.get(TOKEN_URL)
    assert self._oauth_properties.get(REFRESH_TOKEN)
    assert self._oauth_properties.get(CLIENT_ID)
    assert self._oauth_properties.get(CLIENT_SECRET)
    if self._oauth_properties.get(TOKEN_URL) == "https://www.validurl.com":
        return True    
    else:
        return False
    

@patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization._update_tokens", mock_update_tokens)
def test_force_refresh_tokens():
    oauth_config = {
        TOKEN_URL     : "https://www.validurl.com",
        REFRESH_TOKEN : "refresh_token_!23",
        CLIENT_ID     : "clientid123",
        CLIENT_SECRET : "secret123"}

    client = OAuth2Authorization(None, oauth_config)
    assert client.force_refresh_tokens()

    with pytest.raises(IntegrationError):
        oauth_config[TOKEN_URL] = "https://www.invalidurl.com"
        client = OAuth2Authorization(None, oauth_config)
        assert client.force_refresh_tokens()

    with pytest.raises(IntegrationError):
        oauth_config[TOKEN_URL] = "https://www.validurl.com"
        oauth_config[REFRESH_TOKEN] = None
        client = OAuth2Authorization(None, oauth_config)
        assert client.force_refresh_tokens()

    with pytest.raises(IntegrationError):
        client = OAuth2Authorization(None, {})
        assert client.force_refresh_tokens()

def test_show_tokens():
    prop_oauth = {
        ACCESS_TOKEN  : "token123",
        REFRESH_TOKEN : "token123",
        TOKEN_TYPE    : "bearer",
        EXPIRES_IN    : 100000000}
    client = OAuth2Authorization(None, prop_oauth)
    assert client.show_tokens() == prop_oauth

