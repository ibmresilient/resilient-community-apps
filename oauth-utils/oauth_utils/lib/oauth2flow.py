# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""OAuth2 support classes and functions for the Outbound email app"""
import sys
import requests
if sys.version_info[0] == 3:
    from urllib.parse import urlencode
else:
    from urllib import urlencode

from oauth_utils.lib.helpers import validate_fields

REDIRECT_URI = "https://localhost:{}/callback"


class OAuth2Error(Exception):
    """
    Class  for Errors in script.
    """
    pass

class OAuth2Flow:
    """
    Class Responsible for handling OAuth2 authorization/authentication.

    """
    def __init__(self, fn_opts, crsf_token=None, port=None):
        """

        :param fn_opts: The app.config values for the app.(str)
        :param crsf_token: Secret used in requests to make request more secure.(str)
        """
        if port is None:
            port = 8080

        self._redirect_uri = REDIRECT_URI.format(port if port else 8080)

        self._auth_url = fn_opts.get("auth_url")
        self._token_url = fn_opts.get("token_url")
        self._client_id = fn_opts.get("client_id")
        self._client_secret = fn_opts.get("client_secret")
        self._refresh_token = fn_opts.get("refresh_token")
        self._scope = fn_opts.get("scope")
        self._state = crsf_token

        if fn_opts.get("tenant_id"):
            self._auth_url = self._auth_url.format(tenant_id=fn_opts["tenant_id"])
            self._token_url = self._token_url.format(tenant_id=fn_opts["tenant_id"])

    def get_authorization_url(self):
        """
        Get the OAuth2 authorization url for 1st leg of OAuth2 authorization
        The url which will be opened in a browser by the main thread.

        :return auth_url: The URL for 1st leg of OAuth2.
        """
        params= {
            "state": self._state,
            "scope": self._scope,
            "client_id": self._client_id,
            "response_type": "code",
            "response_mode": "query"
        }
        params.update({"redirect_uri": self._redirect_uri})

        # The urlencode() function doesn't work with non-ASCII unicode characters.
        # Encode the parameters as ASCII bytes first.
        params = {key.encode("utf-8"):value.encode("utf-8") for (key, value) in params.items()}

        auth_url = self._auth_url + '?' + urlencode(params)

        return auth_url

    def authenticate(self, auth_code):
        """
        Send token request and return the access_token and refresh_token. The access token and refresh token will be

        :param auth_code: An authorization code you retrieved in the 1st leg of OAuth2. [str]
        :return: refresh_token: The refresh token received in 2nd leg of OAuth2 response. [str]
        """
        data = {
            "grant_type": "authorization_code",
            "code": auth_code,
            "client_id": self._client_id,
            "client_secret": self._client_secret,
        }
        data.update({"redirect_uri": self._redirect_uri})

        response = requests.post(self._token_url, data=data)

        token_response = response.json()

        if "refresh_token" not in token_response:
            raise OAuth2Error("A refresh token was not returned")

        return token_response["refresh_token"]

    def validate_settings(self, fn_opts, use_app_config=True):
        """Validate app config settings.

        :param fn_opts: App settings dict.
        :param use_app_config: Use app.config or command-line to read parameters .
        """
        missing_fields = validate_fields([
            "auth_url",
            "token_url",
            "client_id",
            "client_secret",
            "scope"
        ],
            fn_opts
        )

        if missing_fields:
            plural = True if len(missing_fields) > 1 else False
            required_err_msg = "Parameter{s} '{0}' {ia} required {cf} and {ia} not set. You must set {tv} to run this " \
                               "function."\
                .format(', '.join(missing_fields), s='s' if plural else '', ia='are' if plural else 'is',
                        tv='these values' if plural else 'this value', cf='in the app.config' if use_app_config
                else 'on the command-line')
            raise ValueError(required_err_msg)
