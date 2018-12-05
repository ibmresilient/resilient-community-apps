from .mock_response import give_response
from fn_cloud_foundry.util.authentication.ibm_cf_bearer import IBMCloudFoundryAuthenticator

import pytest
import json

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestAuthenticator:
    @patch("fn_cloud_foundry.util.authentication.ibm_cf_bearer.requests.get")
    @patch("fn_cloud_foundry.util.authentication.ibm_cf_bearer.requests.post")
    def test_authenticator_success(self, post, get):
        """
        Test that in event of success all get's processed as expected.
        """
        get.return_value = give_response(200, {"authorization_endpoint": "test an end"})
        post.return_value = give_response(200, {
            "token_type": "say",
            "access_token": "melon"
        })
        auth = IBMCloudFoundryAuthenticator("url", {"cf_api_apikey": "apikey"})
        auth.get_token()
        assert auth.get_headers() == {"Authorization": "say melon"}

    @patch("fn_cloud_foundry.util.authentication.ibm_cf_bearer.requests.get")
    @patch("fn_cloud_foundry.util.authentication.ibm_cf_bearer.requests.post")
    def test_authenticator_details_error(self, post, get):
        """
        If details won't be returned fail.
        """
        get.return_value = give_response(404, {"authorization_endpoint": "test an end"})
        post.return_value = give_response(200, {
            "token_type": "say",
            "access_token": "melon"
        })
        with pytest.raises(ValueError):
            auth = IBMCloudFoundryAuthenticator("url", {"cf_api_apikey": "apikey"})
            auth.get_token()

    @patch("fn_cloud_foundry.util.authentication.ibm_cf_bearer.requests.get")
    @patch("fn_cloud_foundry.util.authentication.ibm_cf_bearer.requests.post")
    def test_authenticator_token_error(self, post, get):
        """
        Fail if token isn't returned.
        """
        get.return_value = give_response(200, {"authorization_endpoint": "test an end"})
        post.return_value = give_response(404, {
            "token_type": "say",
            "access_token": "melon"
        })
        with pytest.raises(ValueError):
            auth = IBMCloudFoundryAuthenticator("url", {"cf_api_apikey": "apikey"})
            auth.get_token()

    def test_authenticator_auth_error(self):
        """
        Fail if keys are not provided.
        """
        with pytest.raises(KeyError):
            auth = IBMCloudFoundryAuthenticator("url", {"cf_api": "apikey"})
            auth.get_token()
