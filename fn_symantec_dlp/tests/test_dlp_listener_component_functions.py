# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
from fn_symantec_dlp.util.dlp_listener_component import DLPListener
from fn_symantec_dlp.lib.dlp_soap_client import DLPSoapClient
import requests_mock
from resilient_circuits import ResilientComponent
import resilient
import pytest
import mock

class TestDLPListener():

   
    @pytest.mark.parametrize("dlp_host", [
        ("my-soc-instance.acme.com"),
        ("dlp-installation.soc.company.com")
    ])
    def test_build_dlp_url(self, dlp_host):
        
        url = DLPListener.build_dlp_url(incidentid=111, host=dlp_host)
        assert url is not None
        assert "ProtectManager" in url
        assert dlp_host in url

    @pytest.mark.parametrize("dlp_severity", [
        ("high"),
        ("medium"),
        ('low'),
        ('unknown')
    ])
    def test_return_res_severity(self, dlp_severity):
       
        severity = DLPListener.return_res_severity(dlp_severity=dlp_severity)
        assert severity is not None
        assert severity.lower() == dlp_severity or severity == "Low"
