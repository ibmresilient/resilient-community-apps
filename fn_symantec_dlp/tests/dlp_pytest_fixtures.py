# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
import resilient
import configparser
import mock
import pytest
from resilient_circuits.app import AppArgumentParser

from fn_symantec_dlp.lib.dlp_soap_client import DLPSoapClient

@pytest.fixture(scope="module")
def setup_live_dlp_client():
    opts = AppArgumentParser(
        config_file=resilient.get_config_file()).parse_args("", None)
    return DLPSoapClient(
        app_configs=opts.get("fn_symantec_dlp", {}))

@pytest.fixture(scope="module")
@mock.patch('zeep.Client')
def setup_mocked_dlp_connection(MockedZeep):
        return DLPSoapClient(app_configs={
            "sdlp_wsdl": "https://localhost:8443/",
            "sdlp_host": "https://localhost:8443/",
            "sdlp_username": "admin",
            "sdlp_password": "admin",
            "sdlp_savedreportid": 111,
            "sdlp_incident_endpoint": "urls"
        })
