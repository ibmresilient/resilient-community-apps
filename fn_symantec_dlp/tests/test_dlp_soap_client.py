# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
from fn_symantec_dlp.lib.dlp_soap_client import DLPSoapClient
import requests_mock
import resilient
location= "https://9.70.194.103:8443/ProtectManager/services/v2011/incidents"
import configparser
from resilient_circuits.app import AppArgumentParser
from fn_symantec_dlp.lib.dlp_soap_client import LOG
import mock
import pytest
import logging
logger = logging.getLogger('fn_symantec_dlp.lib.dlp_soap_client')

class TestDLPSOAPClient():
   
   
   def setup_method(self, method):
      """ setup any state tied to the execution of the given method in a
      class.  setup_method is invoked for every test method of a class.
      """
      opts = AppArgumentParser(config_file=resilient.get_config_file()).parse_args("", None)
      self.client = DLPSoapClient(app_configs=opts.get("fn_symantec_dlp", {}))

   def teardown_method(self, method):
      """ teardown any state that was previously setup with a setup_method
      call.
      """
      DLPSoapClient.class_vars_loaded=False

   
      
   def test_exception_is_thrown(cls):
      """ 
   test_exception_is_thrown; Used to ensure if we pass in some bad values an exception is raised
    and our desired error message is printed once

    Before anything happens, ensure DLPSoapClient.class_vars_loaded is false so we can load in bad values
   """
      # The setup_method will instantiate a DLPSoapClient 
      if DLPSoapClient.class_vars_loaded:
         DLPSoapClient.class_vars_loaded=False
      with mock.patch.object(logger, 'error') as mock_debug:
         print(mock_debug)
         cls.dummy_client = DLPSoapClient(app_configs={
         "sdlp_wsdl": "https://localhost:8443/",
         "sdlp_host": "https://localhost:8443/",
         "sdlp_username": "admin",
         "sdlp_password":"admin",
         "sdlp_savedreportid": 111,
         "sdlp_incident_endpoint": "urls"
      })
         
         assert bool(mock_debug.called)
         mock_debug.assert_any_call(u"[Symantec DLP] Encounted an exception when setting up the SOAP Client")
         # Modify the class and set vars loaded to false so the next test can load new ones
         DLPSoapClient.class_vars_loaded=False
   
   
   def test_incident_list_soap_call(cls):
      assert cls.client.class_vars_loaded
      assert cls.client.is_connected
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
         mock_url = "{host_url}ProtectManager/services/v2011/incidents".format(host_url=cls.client.host)
         m.post(mock_url, text=mock_resp)
         
         resp = cls.client.incident_list(saved_report_id=121, incident_creation_date_later_than='2019-07-20')

         assert resp is not None
         assert len(resp['incidentId'])


   
# def test_mocking():
    

#         text = """<?xml version="1.0" ?>
# <S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
#    <S:Body>
#       <ns5:incidentListResponse xmlns:ns2="http://www.vontu.com/enforce/export/incident/common/schema" xmlns:ns3="http://www.vontu.com/enforce/export/incident/schema" xmlns:ns4="http://www.vontu.com/v2011/enforce/webservice/incident/common/schema" xmlns:ns5="http://www.vontu.com/v2011/enforce/webservice/incident/schema" xmlns:ns6="http://www.vontu.com/v2011/enforce/webservice/incident">
#          <ns5:incidentId>121</ns5:incidentId>
#          <ns5:incidentId>122</ns5:incidentId>
#          <ns5:incidentId>123</ns5:incidentId>
#          <ns5:incidentId>124</ns5:incidentId>
#          <ns5:incidentLongId>121</ns5:incidentLongId>
#          <ns5:incidentLongId>122</ns5:incidentLongId>
#          <ns5:incidentLongId>123</ns5:incidentLongId>
#          <ns5:incidentLongId>124</ns5:incidentLongId>
#       </ns5:incidentListResponse>
#    </S:Body>
# </S:Envelope>
#     """
#         client = DLPSoapClient(app_configs={"sdlp_wsdl": "https://9.70.194.103:8443/ProtectManager/services/v2011/incidents?wsdl",
#                                             "sdlp_host": "https://9.70.194.103:8443/",
#                                             "sdlp_username": "Administrator",
#                                             "sdlp_password":"passwordprotect"})
#         with requests_mock.Mocker() as m:
#             m.post("https://9.70.194.103:8443/ProtectManager/services/v2011/incidents", text=text)
            
#             resp = client.incident_list(saved_report_id=121, incident_creation_date_later_than='2019-07-20')

#             assert resp is not None
#             resp2 = client.incident_list()

#             assert resp2 is not None


