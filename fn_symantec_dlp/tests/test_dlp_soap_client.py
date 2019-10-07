# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
import uuid
import os
import logging

import mock
import pytest

import resilient

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
                "sdlp_incident_endpoint": "http://localhost:8443/ProtectManager/services/v2011/incidents"
            })

    def teardown_method(self, method):
        """ teardown any state that was previously setup with a setup_method
        call.
        """
        DLPSoapClient.class_vars_loaded = False


    def test_mocked_client_connection(self, setup_mocked_dlp_connection):
        """test_mocked_client_connection ensure the mocked connection done through a fixture has been setup
        """
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
                "sdlp_incident_endpoint": "https://localhost:8443/ProtectManager/services/v2011/incidents"
            })

            assert bool(mock_debug.error.called)
            mock_debug.error.assert_called_with(
                "[Symantec DLP] Encountered an exception when setting up the SOAP Client"
                )
            # Modify the class and set vars loaded to false so the next test can load new ones
            DLPSoapClient.class_vars_loaded = False

     
    @pytest.mark.livetest
    def test_incident_list_soap_call(self, setup_live_dlp_client):
        """test_incident_list_soap_call test used to test parts of the underlying workings for test_incident_list_soap_call
        Mocks the actual SOAP call so the DLP Server is not affected but validates that app.config values against a real instance.
        """
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

    @mock.patch('fn_symantec_dlp.lib.dlp_soap_client.DLPSoapClient.soap_client.service.incidentBinaries')
    def test_incident_binaries_call(self, mocked_soap_call, setup_mocked_dlp_connection):
        """test_incident_binaries_call test used to test parts of the underlying workings for test_incident_binaries_call
        Mocks the generated SOAP function and tests to ensure this function was called with the right value and only once
        """
        client = setup_mocked_dlp_connection
        resp = client.incident_binaries(123)
        assert resp
        mocked_soap_call.assert_called_with(incidentId=123, includeAllComponents='?', includeOriginalMessage=False)

    @mock.patch('fn_symantec_dlp.lib.dlp_soap_client.DLPSoapClient.soap_client.service.listIncidentStatus')
    def test_incident_status_call(self, mocked_soap_call):
        """test_incident_status_call test used to test the return_value for incident_status
        Mocks the generated SOAP function and tests to ensure 'Closed' is in the list
        """
        mocked_soap_call.return_value = "['Closed', 'New']"
        resp = DLPSoapClient.incident_status()

        assert resp
        assert 'Closed' in resp
    
    @mock.patch('fn_symantec_dlp.lib.dlp_soap_client.DLPSoapClient.soap_client.service.incidentDetail')
    def test_incident_detail_call(self, mocked_soap_call):
        """test_incident_detail_call test used to test parts of the underlying workings for incident_detail
        Mocks the generated SOAP function and tests to ensure this function was called with the right value and only once
        """
        resp = DLPSoapClient.incident_detail(incident_id=999)
        assert resp
        mocked_soap_call.assert_called_with(incidentId=999)
        mocked_soap_call.assert_called_once()

    def test_map_values_call(self):
        """test_map_values_call used to ensure that when a payload is made with jinja, that it has a batchId, needed by the DLP API
        """
        batch = "_{}".format(uuid.uuid4())
        incident_id = 999
        default_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, "fn_symantec_dlp/data/templates")
        resp = DLPSoapClient.map_values(template_file=os.path.abspath(default_dir + "/_dlp_update_incident_xml_template.jinja2"),
                                        message_dict={
                                            "batchId":batch,
                                            "dlp_id":incident_id})
        assert resp
        assert batch in resp

    @mock.patch('fn_symantec_dlp.lib.dlp_soap_client.DLPSoapClient.soap_client.service.listCustomAttributes')
    def test_custom_attributes_call(self, mocked_soap_call):
        resp = DLPSoapClient.list_custom_attributes()
        assert resp 

    def test_update_incident_call(self, setup_mocked_dlp_connection):
        mock_response = """<?xml version=\'1.0\' encoding=\'UTF-8\'?>
        <S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
            <S:Body>
            <ns5:incidentUpdateResponse xmlns:ns2="http://www.vontu.com/enforce/export/incident/common/schema" xmlns:ns3="http://www.vontu.com/enforce/export/incident/schema" xmlns:ns4="http://www.vontu.com/v2011/enforce/webservice/incident/common/schema" xmlns:ns5="http://www.vontu.com/v2011/enforce/webservice/incident/schema" xmlns:ns6="http://www.vontu.com/v2011/enforce/webservice/incident">
            <batchResult>
                <batchId>_f65699c5-d601-4834-b15d-5361725e199f</batchId>
                <statusCode>SUCCESS</statusCode>
            </batchResult>
            </ns5:incidentUpdateResponse>
            </S:Body>
        </S:Envelope>"""
        with requests_mock.Mocker() as m:
            mock_url = "{host_url}ProtectManager/services/v2011/incidents".format(
                host_url=setup_mocked_dlp_connection.host)
            res = m.post(mock_url, text=mock_response)
            resp = setup_mocked_dlp_connection.update_incident(incident_id=1, status="Closed")

            assert resp is not None
            assert b"<statusCode>SUCCESS</statusCode>" in resp.content

    def test_update_incident_call_failure(self, setup_mocked_dlp_connection):
        mock_response = """<?xml version=\'1.0\' encoding=\'UTF-8\'?>
        <S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
            <S:Body>
            <ns5:incidentUpdateResponse xmlns:ns2="http://www.vontu.com/enforce/export/incident/common/schema" xmlns:ns3="http://www.vontu.com/enforce/export/incident/schema" xmlns:ns4="http://www.vontu.com/v2011/enforce/webservice/incident/common/schema" xmlns:ns5="http://www.vontu.com/v2011/enforce/webservice/incident/schema" xmlns:ns6="http://www.vontu.com/v2011/enforce/webservice/incident">
            <batchResult>
                <batchId>_f65699c5-d601-4834-b15d-5361725e199f</batchId>
                <statusCode>VALIDATION_ERROR</statusCode>
            </batchResult>
            </ns5:incidentUpdateResponse>
            </S:Body>
        </S:Envelope>"""
    
        with requests_mock.Mocker() as m:
            mock_url = "{host_url}ProtectManager/services/v2011/incidents".format(
                host_url=setup_mocked_dlp_connection.host)
            m.post(mock_url, text=mock_response)
            setup_mocked_dlp_connection.update_incident(incident_id=1, status="Closed")
            
    
            