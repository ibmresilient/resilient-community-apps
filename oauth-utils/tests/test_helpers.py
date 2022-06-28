# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Test oauth-utils helper functions"""
import pytest
from mock import patch
from shutil import rmtree
from oauth_utils.lib.helpers import *
from argparse import Namespace

"""
Suites of tests to test the OAuth-utils Helper functions
"""
SHARED_MOCK_DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "mock_data")
MOCK_APP_CONFIG = os.path.join(SHARED_MOCK_DATA_DIR, "mock_app_config")
MOCK_APP_CONFIG_BLANKS = os.path.join(SHARED_MOCK_DATA_DIR, "mock_app_config_blanks")
class TestOAuthUtilsHelpers:
    """Test helper functions"""

    @pytest.fixture(scope='session')
    def tmp_config_file(self, tmpdir_factory):
        tmp_config_dir = tmpdir_factory.mktemp(".resilient")
        tmp_config_file = os.path.expanduser(os.path.join(
            str(tmp_config_dir), DEFAULT_CONFIG_FILENAME))
        yield tmp_config_file
        rmtree(str(tmp_config_dir))

    """Test get_config_file function"""

    @pytest.mark.parametrize("filename", [
        (None),
        (MOCK_APP_CONFIG)
    ])
    def test_get_config_file(self, monkeypatch, tmp_config_file, filename):
        if not filename:
            monkeypatch.setenv("APP_CONFIG_FILE", tmp_config_file)
        result = get_config_file(filename=filename)
        if not filename:
            assert result == tmp_config_file
        else:
            assert result == filename

    """Test set_configs function"""
    @pytest.mark.parametrize("scope, client_id, client_secret, token_url, auth_url, expected_results", [
        ("", "", "", "", "", {
            "scope": "",
            "client_id": "",
            "client_secret": "",
            "token_url": "",
            "auth_url": ""
        }),
        ("https://test.ibm.com/SMTP.Send", "1234567a-abc8-90d1-2efa3-123456789abcd",
         "ABCDEF-123456789abcd_2efa3", "https://test.ibm.com/oauth2/token", "https://test.ibm.com/oauth2/auth", {
             'scope': 'https://test.ibm.com/SMTP.Send',
             'client_id': '1234567a-abc8-90d1-2efa3-123456789abcd',
             'client_secret': 'ABCDEF-123456789abcd_2efa3',
             'token_url': 'https://test.ibm.com/oauth2/token',
             'auth_url': 'https://test.ibm.com/oauth2/auth'
        })
    ])
    def test_set_configs(self, scope, client_id, client_secret, token_url, auth_url, expected_results):
        opts = {
            "scope": scope,
            "client_id": client_id,
            "client_secret": client_secret,
            "token_url": token_url,
            "auth_url": auth_url
        }
        script_args = Namespace(**opts)
        result = set_configs(script_args)
        assert set_configs(script_args) == expected_results

    """Test get_configs function"""
    @pytest.mark.parametrize("app_config, expected_results", [
        (MOCK_APP_CONFIG_BLANKS, {
            "scope": "",
            "client_id": "",
            "client_secret": "",
            "token_url": "",
            "auth_url": ""
        }),
        (MOCK_APP_CONFIG, {
             'scope': 'https://test.ibm.com/SMTP.Send',
             'client_id': '1234567a-abc8-90d1-2efa3-123456789abcd',
             'client_secret': 'ABCDEF-123456789abcd_2efa3',
             'token_url': 'https://test.ibm.com/oauth2/token',
             'auth_url': 'https://test.ibm.com/oauth2/auth'
        })
    ])
    def test_get_configs(self, app_config, expected_results):

        result = get_configs(path_config_file=app_config)
        assert result == expected_results

    """Test validate_fields function"""
    @pytest.mark.parametrize("scope, client_id, client_secret, token_url, auth_url", [
        ("https://test.ibm.com/SMTP.Send", "1234567a-abc8-90d1-2efa3-123456789abcd", "ABCDEF-123456789abcd_2efa3",
         "https://test.ibm.com/oauth2/token", "https://test.ibm.com/oauth2/auth"
         )
    ])
    def test_validate_fields(self, scope, client_id, client_secret, token_url, auth_url):
        opts = {
            "scope": scope,
            "client_id": client_id,
            "client_secret": client_secret,
            "token_url": token_url,
            "auth_url": auth_url
        }
        validate_fields(list(opts.keys()), opts)

    """ Test validate_fields with empty values"""
    @pytest.mark.parametrize("scope, client_id, client_secret, token_url, auth_url, expected_results", [
        ("",  "1234567a-abc8-90d1-2efa3-123456789abcd", "ABCDEF-123456789abcd_2efa3", "https://test.ibm.com/oauth2/token",
         "https://test.ibm.com/oauth2/auth",
         "'scope' is mandatory and is not set. You must set this value to run this function"),
        ("https://test.ibm.com/SMTP.Send", "", "ABCDEF-123456789abcd_2efa3", "https://test.ibm.com/oauth2/token",
         "https://test.ibm.com/oauth2/auth",
         "'client_id' is mandatory and is not set. You must set this value to run this function"),
        ("https://test.ibm.com/SMTP.Send", "1234567a-abc8-90d1-2efa3-123456789abcd", "", "https://test.ibm.com/oauth2/token",
         "https://test.ibm.com/oauth2/auth",
         "'client_secret' is mandatory and is not set. You must set this value to run this function"),
        ("https://test.ibm.com/SMTP.Send", "1234567a-abc8-90d1-2efa3-123456789abcd", "ABCDEF-123456789abcd_2efa3",
         "", "https://test.ibm.com/oauth2/auth",
         "'token_url' is mandatory and is not set. You must set this value to run this function"),
        ("https://test.ibm.com/SMTP.Send", "1234567a-abc8-90d1-2efa3-123456789abcd", "ABCDEF-123456789abcd_2efa3",
         "https://test.ibm.com/oauth2/token", "",
         "'auth_url' is mandatory and is not set. You must set this value to run this function")
    ])
    def test_validate_fields_empty(self, scope, client_id, client_secret, token_url, auth_url, expected_results):
        opts = {
            "scope": scope,
            "client_id": client_id,
            "client_secret": client_secret,
            "token_url": token_url,
            "auth_url": auth_url
        }
        with pytest.raises(ValueError) as e:
            validate_fields(list(opts.keys()), opts)
        assert str(e.value) == expected_results