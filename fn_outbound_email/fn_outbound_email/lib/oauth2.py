# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""OAuth2 support classes and functions for the Outbound email app"""
import sys
import requests
if sys.version_info[0] == 3:
    from urllib.parse import urlencode
else:
    from urllib import urlencode

from resilient_lib import validate_fields, RequestsCommon

FN_NAME = "fn_outbound_email"
DEFAULT_REDIRECT_URI = "https://localhost:8080/callback"

class OAuth2Error(Exception):
    """
    Class  for Errors in script.
    """
    pass

class OAuth2:
    """
    Class Responsible for handling OAuth2 authorization/authentication.

    """
    def __init__(self, opts, crsf_token=None):
        """

        :param fn_opts: The app.config values for the app.(str)
        :param crsf_token: Secret used in requests to make request more secure.(str)
        """
        fn_opts = opts.get(FN_NAME, {})
        self._redirect_uri = DEFAULT_REDIRECT_URI

        self._auth_url = fn_opts.get("auth_url")
        self._token_url = fn_opts.get("token_url")
        self._client_id = fn_opts.get("client_id")
        self._client_secret = fn_opts.get("client_secret")
        self._refresh_token = fn_opts.get("refresh_token")
        self._scope = fn_opts.get("scope")
        self._smtp_user = fn_opts.get("smtp_user")
        self._state = crsf_token

        self.validate_settings(fn_opts)
        # Add OAuth2 placeholders
        self.oauth2_string = None
        self.oauth2_token = None

        if fn_opts.get("tenant_id"):
            self._auth_url = self._auth_url.format(tenant_id=fn_opts["tenant_id"])
            self._token_url = self._token_url.format(tenant_id=fn_opts["tenant_id"])

        self.rc = RequestsCommon(opts={}, function_opts=fn_opts)

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

    def refresh_token(self):
        """"Refresh OAuth2 token.

        Run the refresh_token flow.

        :return "access_token": OAuth2 access token attribute [str]
        """
        url = self._token_url

        post_data = {
            # Use refresh token to renew access token.
            "client_id": self._client_id,
            "scope": self._scope,
            "client_secret": self._client_secret,
            "refresh_token": self._refresh_token,
            "grant_type": "refresh_token"
        }

        result = self.rc.execute_call_v2("POST", url, data=post_data)
        r_json = result.json()

        if "access_token" in r_json:
            self.oauth2_token = r_json["access_token"]
            return

        msg = u"Unable to authenticate: Error: {}\nDescription: {}"\
            .format(r_json.get("error"), r_json.get("error_description"))
        raise OAuth2Error(msg)

    def generate_oauth2_string(self):
        """Generate an OAuth2 authentication string for SMTP send.

        :return "auth_string": Authentication string for request [str]

        """
        auth_string = "user={0}\x01auth=Bearer {1}\x01\x01".format(self._smtp_user, self.oauth2_token)
        self.oauth2_string = auth_string


    def validate_settings(self, fn_opts):
        """Validate app config settings.

        :param fn_opts: App settings dict.
        """
        validate_fields([
            {"name": "auth_url"},
            {"name": "token_url"},
            {"name": "client_id"},
            {"name": "token_url"},
            {"name": "client_secret"},
            {"name": "scope"}],
        fn_opts)
        if "{tenant_id}" in fn_opts.get("auth_url") or "{tenant_id}" in fn_opts.get("token_url"):
            validate_fields([
                {"name": "tenant_id"}],
                fn_opts)

