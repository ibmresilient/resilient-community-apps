# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
import logging
from multiprocessing.sharedctypes import Value
from unittest import mock
import pytest

from urllib import parse
from unittest.mock import patch
from resilient_lib import RequestsCommon

from fn_teams.lib import constants
from fn_teams.lib.microsoft_authentication import MicrosoftAuthentication

PACKAGE_NAME = "fn_teams"
MOCK_ID_VALUE = "abc123"
APP_CONFIG = {
    "directory_id"   : "1d8a5928-8678-408e-ab06-50ca7e01766a",
    "application_id" : "18d10049-72e3-4652-ac9f-d9b13f24303c",
    "secret_value"   : "oCN8Q~1I0dFCI_x1kI6EseRxeTmNazVJboA0ZaMF"}


@pytest.fixture(scope="function")
def required_parameters():
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    log.addHandler(logging.StreamHandler())
    yield {"rc" : RequestsCommon(), "logger" : log}


@pytest.fixture(scope="function")
def mocked_authenticator(required_parameters):
    app_config = {
        "directory_id"   : MOCK_ID_VALUE,
        "application_id" : MOCK_ID_VALUE,
        "secret_value"   : MOCK_ID_VALUE}
    yield MicrosoftAuthentication(required_parameters, app_config)


class MockMSAL:
    def __init__(self, *args, **kwargs):
        assert args[0] == kwargs.get("client_credential")
        assert kwargs.get("authority") == parse.urljoin(constants.AUTH_URL, MOCK_ID_VALUE)

    def acquire_token_for_client(self, scopes):
        if scopes == [
        parse.urljoin(constants.BASE_URL, constants.DEFAULT_SCOPE)]:
            return {"access_token" : "access_token 123"}
        else:
            return {}


@pytest.mark.livetest
def test_connect_endpoint(required_parameters):
    authenticator = MicrosoftAuthentication(required_parameters, APP_CONFIG)
    header = authenticator.authenticate()
    assert header
    assert "Authorization" in header
    assert "Content-type" in header
    assert header.get("Authorization")
    assert header.get("Content-type") == "application/json"


def test_authenticator_initialization(mocked_authenticator):
    assert mocked_authenticator.required_parameters.get("scope") == constants.DEFAULT_SCOPE
    assert mocked_authenticator.required_parameters.get("application_id") == MOCK_ID_VALUE
    assert mocked_authenticator.required_parameters.get("secret_value") == MOCK_ID_VALUE
    assert mocked_authenticator.required_parameters.get("directory_id") == parse.urljoin(
            constants.AUTH_URL, MOCK_ID_VALUE)


def test_generate_header(mocked_authenticator):
    header = mocked_authenticator._generate_header("ID123")
    assert header
    assert "Authorization" in header
    assert "Content-type" in header
    assert header.get("Authorization")
    assert header.get("Content-type") == "application/json"
    assert header == {
        'Authorization': 'Bearer ID123',
        'Content-type': 'application/json'}


@patch('msal.ConfidentialClientApplication', side_effect=MockMSAL)
def test_generate_bearer_id(msal, mocked_authenticator):
    response = mocked_authenticator._generate_bearer_id()
    assert response
    assert response == "access_token 123"