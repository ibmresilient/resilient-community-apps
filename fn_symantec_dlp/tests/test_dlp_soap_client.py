# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
import resilient
import configparser
import mock
import pytest
import logging

import requests_mock

from resilient_circuits.app import AppArgumentParser

from fn_symantec_dlp.lib.dlp_soap_client import DLPSoapClient

logger = logging.getLogger('fn_symantec_dlp.lib.dlp_soap_client')


class TestDLPSOAPClient():
    """TestDLPSOAPClient class used to test the SOAP client
    Contains:
    Pytest Fixtures for setting up a Mocked or Live Client

    Lifecycle methods

    Tests
    """

    @pytest.fixture()
    def setup_live_dlp_client(self):
        opts = AppArgumentParser(
            config_file=resilient.get_config_file()).parse_args("", None)
        return DLPSoapClient(
            app_configs=opts.get("fn_symantec_dlp", {}))

    @pytest.fixture()
    @mock.patch('zeep.Client')
    def setup_mocked_dlp_connection(self, MockedZeep):
            return DLPSoapClient(app_configs={
                "sdlp_wsdl": "https://localhost:8443/",
                "sdlp_host": "https://localhost:8443/",
                "sdlp_username": "admin",
                "sdlp_password": "admin",
                "sdlp_savedreportid": 111,
                "sdlp_incident_endpoint": "urls"
            })

    def teardown_method(self, method):
        """ teardown any state that was previously setup with a setup_method
        call.
        """
        DLPSoapClient.class_vars_loaded = False


    def test_mocked_client_connection(self, setup_mocked_dlp_connection):
        client = setup_mocked_dlp_connection
        assert client.is_connected
        assert client.class_vars_loaded


    def test_exception_is_thrown(self):
        """ 
     test_exception_is_thrown; Used to ensure if we pass in some bad values an exception is raised
      and our desired error message is printed once

      Before anything happens, ensure DLPSoapClient.class_vars_loaded is false so we can load in bad values
     """
        # The setup_method will instantiate a DLPSoapClient
        if DLPSoapClient.class_vars_loaded:
            DLPSoapClient.class_vars_loaded = False
        with mock.patch('fn_symantec_dlp.lib.dlp_soap_client.LOG') as mock_debug:
            print(mock_debug)
            self.dummy_client = DLPSoapClient(app_configs={
                "sdlp_wsdl": "https://localhost:8443/",
                "sdlp_host": "https://localhost:8443/",
                "sdlp_username": "admin",
                "sdlp_password": "admin",
                "sdlp_savedreportid": 111,
                "sdlp_incident_endpoint": "urls"
            })

            assert bool(mock_debug.error.called)
            mock_debug.error.assert_called_with(
                "[Symantec DLP] Encountered an exception when setting up the SOAP Client"
                )
            # Modify the class and set vars loaded to false so the next test can load new ones
            DLPSoapClient.class_vars_loaded = False

     
    @pytest.mark.livetest
    def test_incident_list_soap_call(self, setup_live_dlp_client):
        client = setup_live_dlp_client
        assert client.class_vars_loaded
        assert client.is_connected
        # Mock Data
        mock_resp = """<?xml version="1.0" ?>
                     <S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
                        <S:Body>
                           <ns5:incidentListResponse xmlns:ns2="http://www.vontu.com/enforce/export/incident/common/schema" xmlns:ns3="http://www.vontu.com/enforce/export/incident/schema" xmlns:ns4="http://www.vontu.com/v2011/enforce/webservice/incident/common/schema" xmlns:ns5="http://www.vontu.com/v2011/enforce/webservice/incident/schema" xmlns:ns6="http://www.vontu.com/v2011/enforce/webservice/incident">
                              <ns5:incidentId>121</ns5:incidentId>
                              <ns5:incidentId>122</ns5:incidentId>
                              <ns5:incidentId>123</ns5:incidentId>
                              <ns5:incidentId>124</ns5:incidentId>
                              <ns5:incidentLongId>121</ns5:incidentLongId>
                              <ns5:incidentLongId>122</ns5:incidentLongId>
                              <ns5:incidentLongId>123</ns5:incidentLongId>
                              <ns5:incidentLongId>124</ns5:incidentLongId>
                           </ns5:incidentListResponse>
                        </S:Body>
                     </S:Envelope>"""

        with requests_mock.Mocker() as m:
            mock_url = "{host_url}ProtectManager/services/v2011/incidents".format(
                host_url=client.host)
            m.post(mock_url, text=mock_resp)

            resp = client.incident_list(
                saved_report_id=121, incident_creation_date_later_than='2019-07-20')

            assert resp is not None
            assert len(resp['incidentId'])
