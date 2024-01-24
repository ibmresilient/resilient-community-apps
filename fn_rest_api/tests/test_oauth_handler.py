# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import pytest, unittest

from unittest.mock import patch, MagicMock
from fn_rest_api.lib.authentication_handler import *

AUTH_TYPE = "auth_type"
CODE_OR_REFRESH_TOKEN = "code_or_refresh_token"

def mock_update_tokens(self):
    assert self._oauth_properties.get(TOKEN_URL)
    assert self._oauth_properties.get(REFRESH_TOKEN)
    assert self._oauth_properties.get(CLIENT_ID)
    assert self._oauth_properties.get(CLIENT_SECRET)
    if self._oauth_properties.get(TOKEN_URL) == "https://www.validurl.com":
        return True
    else:
        return False


class TestOauthConstants(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(DEFAULT_AUTH_CONTENT_TYPE, "application/x-www-form-urlencoded")
        self.assertEqual(REFRESH_GRANT_TYPE, "refresh_token")
        self.assertEqual(ACCESS_GRANT_TYPE , "authorization_code")
        self.assertEqual(AUTH_URL, "auth_url")
        self.assertEqual(TOKEN_URL, "token_url")
        self.assertEqual(CODE , "code")
        self.assertEqual(STATE, "state")
        self.assertEqual(SCOPE, "scope")
        self.assertEqual(CLIENT_ID , "client_id")
        self.assertEqual(GRANT_TYPE, "grant_type")
        self.assertEqual(TOKEN_TYPE, "token_type")
        self.assertEqual(EXPIRES_IN, "expires_in")
        self.assertEqual(ACCESS_TOKEN, "access_token")
        self.assertEqual(CLIENT_SECRET, "client_secret")
        self.assertEqual(REFRESH_TOKEN, "refresh_token")
        self.assertEqual(RESPONSE_MODE, "response_mode")
        self.assertEqual(RESPONSE_TYPE, "response_type")
        self.assertEqual(REDIRECT_URI , "redirect_uri")
        self.assertEqual(CONTENT_TYPE , "content_type")
        self.assertEqual(ADDITIONAL_HEADERS, "additional_headers")
        self.assertEqual(ADDITIONAL_ATTRIBUTES, "additional_attributes")


class TestCheckOauthReady(unittest.TestCase):

    client = OAuth2Authorization(None, {}, {})

    def test_check_oauth_not_ready(self):
        client = OAuth2Authorization(None, {}, {})
        _status = client.check_oauth_ready()
        self.assertDictEqual(_status, {
            'oauth_supported'         : False,
            'access_token_flow'       : False,
            'authorization_flow'      : False,
            'client_credentials_flow' : False,
            'refresh_token_flow'      : False})

    def test_check_oauth_with_access_token_not_ready(self):
        client = OAuth2Authorization(None, {}, {})
        client._oauth_inputs = {}
        client._oauth_inputs = {
            ACCESS_TOKEN : "access123"}
        _status = client.check_oauth_ready()
        self.assertDictEqual(_status, {
            'oauth_supported'         : True,
            'access_token_flow'       : True,
            'authorization_flow'      : False,
            'client_credentials_flow' : False,
            'refresh_token_flow'      : False})

    def test_check_oauth_with_refresh_token_not_ready(self):
        self.client._oauth_inputs = {}
        self.client._oauth_inputs = {
            REFRESH_TOKEN : "refresh123",
            CODE : "code123"}
        _status = self.client.check_oauth_ready()
        self.assertDictEqual(_status, {
            'oauth_supported'         : False,
            'access_token_flow'       : False,
            'authorization_flow'      : False,
            'client_credentials_flow' : False,
            'refresh_token_flow'      : False})

    def test_check_oauth_with_client_id_and_code(self):
        self.client._oauth_inputs = {
            TOKEN_URL : "https://www.example.com/tokens",
            CLIENT_ID : "client123",
            CODE : "code123"}
        _status = self.client.check_oauth_ready()
        self.assertDictEqual(_status, {
            'oauth_supported'         : True,
            'access_token_flow'       : False,
            'authorization_flow'      : True,
            'client_credentials_flow' : False,
            'refresh_token_flow'      : False})

    def test_check_oauth_with_client_id_and_access_token(self):
        self.client._oauth_inputs = {}
        self.client._oauth_inputs = {
            TOKEN_URL : "https://www.example.com/tokens",
            CLIENT_ID : "client123",
            ACCESS_TOKEN : "access123"}
        _status = self.client.check_oauth_ready()
        self.assertDictEqual(_status, {
            'oauth_supported'         : True,
            'access_token_flow'       : True,
            'authorization_flow'      : False,
            'client_credentials_flow' : False,
            'refresh_token_flow'      : False})

    def test_check_oauth_with_client_id_and_refresh_token(self):
        self.client._oauth_inputs = {}
        self.client._oauth_inputs = {
            TOKEN_URL : "https://www.example.com/tokens",
            CLIENT_ID : "client123",
            REFRESH_TOKEN : "refresh123"}
        _status = self.client.check_oauth_ready()
        self.assertDictEqual(_status, {
            'oauth_supported'         : True,
            'access_token_flow'       : False,
            'authorization_flow'      : False,
            'client_credentials_flow' : False,
            'refresh_token_flow'      : True})

    def test_check_oauth_with_client_credentials_flow(self):
        self.client._oauth_inputs = {}
        self.client._oauth_inputs = {
            TOKEN_URL : "https://www.example.com/tokens",
            CLIENT_ID : "client123",
            CLIENT_SECRET : "secret123",
            GRANT_TYPE : "client_credentials"}
        _status = self.client.check_oauth_ready()
        self.assertDictEqual(_status, {
            'oauth_supported'         : True,
            'access_token_flow'       : False,
            'authorization_flow'      : False,
            'client_credentials_flow' : True,
            'refresh_token_flow'      : False})

    def test_check_oauth_with_client_credentials_flow_title(self):
        self.client._oauth_inputs = {}
        self.client._oauth_inputs = {
            TOKEN_URL : "https://www.example.com/tokens",
            CLIENT_ID : "client123",
            CLIENT_SECRET : "secret123",
            GRANT_TYPE : "Client_Credentials"}
        _status = self.client.check_oauth_ready()
        self.assertDictEqual(_status, {
            'oauth_supported'         : True,
            'access_token_flow'       : False,
            'authorization_flow'      : False,
            'client_credentials_flow' : True,
            'refresh_token_flow'      : False})

    def test_check_oauth_with_client_credentials_flow_allcaps(self):
        self.client._oauth_inputs = {}
        self.client._oauth_inputs = {
            TOKEN_URL : "https://www.example.com/tokens",
            CLIENT_ID : "client123",
            CLIENT_SECRET : "secret123",
            GRANT_TYPE : "CLIENT_CREDENTIALS"}
        _status = self.client.check_oauth_ready()
        self.assertDictEqual(_status, {
            'oauth_supported'         : True,
            'access_token_flow'       : False,
            'authorization_flow'      : False,
            'client_credentials_flow' : True,
            'refresh_token_flow'      : False})

    def test_check_oauth_all_true(self):
        self.client._oauth_inputs = {}
        self.client._oauth_inputs = {
            TOKEN_URL : "https://www.example.com/tokens",
            CLIENT_ID : "client123",
            CLIENT_SECRET : "secret123",
            GRANT_TYPE : "CLIENT_CREDENTIALS",
            REFRESH_TOKEN : "refreshmeup112233",
            ACCESS_TOKEN : "access112233",
            CODE : "access_code"}
        _status = self.client.check_oauth_ready()
        self.assertDictEqual(_status, {
            'oauth_supported'         : True,
            'access_token_flow'       : True,
            'authorization_flow'      : True,
            'client_credentials_flow' : True,
            'refresh_token_flow'      : True})


class TestHeaderCompilation(unittest.TestCase):

    client = OAuth2Authorization(None, {}, {})

    def test_compile_empty_headers(self):
        header = self.client._compile_headers()
        assert len(header) == 1
        assert "Authorization" in header.keys()
        assert len(list(header.values())) == 1
        assert "None None" == header["Authorization"]

    def test_token_type_in_header(self):
        self.client._oauth_inputs[TOKEN_TYPE] = "keychain"
        header = self.client._compile_headers()
        assert "keychain" in list(header.values())[0]
        # assert "keychain 112233" == list(header.values())[0]

    def test_compiled_header(self):
        self.client._oauth_inputs[TOKEN_TYPE] = "Vault Code"
        self.client._oauth_inputs[ACCESS_TOKEN] = "112233"
        header = self.client._compile_headers()
        assert "Vault Code 112233" == header["Authorization"]


class TestEndpointResponse(unittest.TestCase):

    client = OAuth2Authorization(None, {}, {})
    def test_response_handling_status_code300(self):
        with pytest.raises(IntegrationError):
            mock_value = MagicMock(status_code=300)
            self.client._process_endpoint_response(mock_value)

    def test_response_handling_status_code200(self):
        with pytest.raises(ValueError):
            mock_value = MagicMock(status_code=200)
            mock_value.json = MagicMock(return_value = {})
            mock_value.text = MagicMock(return_value = "invalid response")
            self.client._process_endpoint_response(mock_value)

    def test_response_handling(self):
        self.client._oauth_inputs = {}
        response_data = {
            REFRESH_TOKEN : "refresh1234",
            ACCESS_TOKEN  : "access1234",
            TOKEN_TYPE    : "bearer"}
        additional_params = {
            GRANT_TYPE : "refresh_token"}
        mock_response = MagicMock(status_code=200)
        mock_response.json = MagicMock(return_value = response_data)
        assert self.client._process_endpoint_response(mock_response)
        response_data.update(additional_params)
        assert self.client._oauth_inputs == response_data

def mock_fetch_renew_tokens(_, token_url, client_id, **kwargs):
    kwargs.update({
        "token_url" : token_url,
        "client_id" : client_id})
    return kwargs

class TestOAuthAuthenticate(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def init_caplog_fixture(self, caplog):
        self.caplog = caplog
        self.caplog.set_level(logging.INFO)

    def test_unsupported_flow(self):
        self.caplog.clear()
        client = OAuth2Authorization(None, {
            CLIENT_ID : "",
            REFRESH_TOKEN : "",
            CODE : ""}, {})
        with pytest.raises(IntegrationError):
            client.authenticate()
        assert self.caplog.records[0].levelname == "ERROR"
        assert self.caplog.records[0].message == 'Application does not support OAuth authentication.'

    @patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization.fetch_renew_tokens", mock_fetch_renew_tokens)
    def test_refresh_flow(self):
        def compare_response(_, response):
            self.assertDictEqual(response, {
                'auth_type': 'refresh_token',
                'token_value': 'refreshmeup112233',
                'grant_type': 'refresh_token',
                'client_secret': None,
                'redirect_uri': None,
                'scope': None,
                'token_url': 'www.token_url.com',
                'client_id': 'clientid112233'})
            assert self.caplog.records[0].levelname == "INFO"
            assert self.caplog.records[0].message == f"Application OAuth compliant. Detected: Refresh Token Flow"
            assert self.caplog.records[1].levelname == "INFO"
            assert self.caplog.records[1].message == f"REFRESH_TOKEN detected. Fetching new ACCESS_TOKEN and possibly a REFRESH_TOKEN"

        self.caplog.clear()
        client = OAuth2Authorization(None, {
            TOKEN_URL : "www.token_url.com",
            REFRESH_TOKEN : "refreshmeup112233",
            CLIENT_ID : "clientid112233"}, {})

        with patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization._process_endpoint_response", compare_response):
            client.authenticate()

    @patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization.fetch_renew_tokens", mock_fetch_renew_tokens)
    def test_client_credentials_flow(self):
        def compare_response(_, response):
            self.assertDictEqual(response, {
                'grant_type': 'client_credentials',
                'client_secret': 'clientsecret112233',
                'redirect_uri': None,
                'scope': None,
                'token_url': 'www.token_url.com',
                'client_id': 'clientid112233'})
            assert self.caplog.records[0].levelname == "INFO"
            assert self.caplog.records[0].message == f"Application OAuth compliant. Detected: Client-Credentials Flow"
            assert self.caplog.records[1].levelname == "INFO"
            assert self.caplog.records[1].message == f"Client-Credentials detected. Fetching new ACCESS_TOKEN and possibly a REFRESH_TOKEN"

        self.caplog.clear()
        client = OAuth2Authorization(None, {
            TOKEN_URL : "www.token_url.com",
            CLIENT_SECRET : "clientsecret112233",
            CLIENT_ID  : "clientid112233",
            GRANT_TYPE : "client_credentials"}, {})

        with patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization._process_endpoint_response", compare_response):
            client.authenticate()

    @patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization.fetch_renew_tokens", mock_fetch_renew_tokens)
    def test_authorization_flow(self):
        def compare_response(_, response):
            self.assertDictEqual(response, {
                'auth_type': 'code',
                'token_value': 'code112233',
                'grant_type': 'authorization_code',
                'client_secret': None,
                'redirect_uri': None,
                'scope': None,
                'token_url': 'www.token_url.com',
                'client_id': 'clientid112233'})
            assert self.caplog.records[0].levelname == "INFO"
            assert self.caplog.records[0].message == f"Application OAuth compliant. Detected: Authorization Flow"
            assert self.caplog.records[1].levelname == "INFO"
            assert self.caplog.records[1].message == f"CODE detected. Fetching new ACCESS_TOKEN and possibly a REFRESH_TOKEN"

        self.caplog.clear()
        client = OAuth2Authorization(None, {
            TOKEN_URL : "www.token_url.com",
            CODE : "code112233",
            CLIENT_ID : "clientid112233"}, {})

        with patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization._process_endpoint_response", compare_response):
            client.authenticate()

    @patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization.fetch_renew_tokens", mock_fetch_renew_tokens)
    def test_grant_type_override(self):
        def compare_response(_, response):
            self.assertDictEqual(response, {
                'auth_type': 'code',
                'token_value': 'code112233',
                'grant_type': 'overridden_grant',
                'client_secret': None,
                'redirect_uri': None,
                'scope': None,
                'token_url': 'www.token_url.com',
                'client_id': 'clientid112233'})
            assert self.caplog.records[0].levelname == "INFO"
            assert self.caplog.records[0].message == f"Application OAuth compliant. Detected: Authorization Flow"
            assert self.caplog.records[1].levelname == "INFO"
            assert self.caplog.records[1].message == f"CODE detected. Fetching new ACCESS_TOKEN and possibly a REFRESH_TOKEN"

        self.caplog.clear()
        client = OAuth2Authorization(None, {
            TOKEN_URL : "www.token_url.com",
            CODE : "code112233",
            CLIENT_ID : "clientid112233",
            GRANT_TYPE : "overridden_grant"}, {})

        with patch("fn_rest_api.lib.authentication_handler.OAuth2Authorization._process_endpoint_response", compare_response):
            client.authenticate()


class OAuthFetchRenewTokens(unittest.TestCase):

    def test_renew_tokens(self):
        def compare_response(method, url, headers, data, **retry_options):
            assert method == "post"
            assert url == "www.token_url.com"
            self.assertDictEqual(headers, {
                'content_type': 'application/ibm',
                'header_key1': 'header_value1',
                'header_key2': 'header_value2'})
            self.assertDictEqual(data, {
                'add_key1': 'add_value1',
                 'add_key2': 'add_value2',
                 'client_id': 'clientid112233',
                 'client_secret': 'secret123',
                 'code': 'code112233',
                 'redirect_uri': 'www.redirect.com',
                 'scope': 'bass treble mids'})
            self.assertDictEqual(retry_options, {})

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

    def test_defaults(self):
        def compare_response(method, url, headers, data, **retry_options):
            assert method == "post"
            assert url == "www.token_url.com"
            self.assertDictEqual(headers, {
                'content_type': 'application/x-www-form-urlencoded'})
            self.assertDictEqual(data, {
                 'client_id': 'clientid112233'})
            self.assertDictEqual(retry_options, {})

        mock_rc = MagicMock()
        mock_rc.execute = compare_response
        client = OAuth2Authorization(mock_rc, {}, {})
        client.fetch_renew_tokens(**{
            TOKEN_URL : "www.token_url.com",
            CLIENT_ID : "clientid112233"})

    def test_additional_attributes(self):
        def compare_response(method, url, headers, data, **retry_options):
            assert method == "post"
            assert url == "www.token_url.com"
            self.assertDictEqual(headers, {
                'content_type': 'application/x-www-form-urlencoded',
                "header_key1" : "header_value1",
                "header_key2" : "header_value2"})
            self.assertDictEqual(data, {
                 'client_id': 'clientid112233',
                 "add_key1" : "add_value1",
                "add_key2" : "add_value2"})
            self.assertDictEqual(retry_options, {})

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

    def test_retry(self):
        def compare_response(method, url, headers, data, **retry_options):
            assert method == "post"
            assert url == "www.token_url.com"
            self.assertDictEqual(headers, {
                'content_type': 'application/x-www-form-urlencoded'})
            self.assertDictEqual(data, {
                 'client_id': 'clientid112233'})
            self.assertDictEqual(retry_options, {
            "retry_tries" : 10,
            "retry_delay" : 9,
            "retry_backoff" : 7})

        mock_rc = MagicMock()
        mock_rc.execute = compare_response
        client = OAuth2Authorization(mock_rc, {}, {
            "retry_tries" : 10,
            "retry_delay" : 9,
            "retry_backoff" : 7})
        client.fetch_renew_tokens(**{
            TOKEN_URL : "www.token_url.com",
            CLIENT_ID : "clientid112233"})
