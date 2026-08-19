# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""OAuth2 support classes and functions for the Outbound email app"""
import sys
if sys.version_info[0] == 3:
    from urllib.parse import urlencode
else:
    from urllib import urlencode

from resilient_lib import validate_fields, RequestsCommon

FN_NAME = "fn_outbound_email"

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

        self.rc = RequestsCommon(opts={}, function_opts=fn_opts)

    def refresh_access_token(self):
        """"Refresh OAuth2 token.

        Run the refresh_token flow to get a new access token.

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

        msg = f'Unable to authenticate: Error: {r_json.get("error")}\nDescription: {r_json.get("error_description")}'
        raise OAuth2Error(msg)

    def generate_oauth2_string(self):
        """Generate an OAuth2 authentication string for SMTP send.

        :return "auth_string": Authentication string for request [str]

        """
        auth_string = f"user={self._smtp_user}\x01auth=Bearer {self.oauth2_token}\x01\x01"
        self.oauth2_string = auth_string


    def validate_settings(self, fn_opts):
        """Validate app config settings.

        :param fn_opts: App settings dict.
        """
        validate_fields([
            {"name": "token_url"},
            {"name": "client_id"},
            {"name": "token_url"},
            {"name": "client_secret"},
            {"name": "scope"},
            {"name": "refresh_token"}],
        fn_opts)
