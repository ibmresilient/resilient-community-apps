
import logging
import resilient_circuits.template_functions as template_functions

import zeep
from requests import Session
from requests.auth import HTTPBasicAuth, AuthBase
import requests_mock
from zeep.transports import Transport
from fn_symantec_dlp.lib.dlp_soap_client import DLPSoapClient

from circuits import Component, Event, Timer, handler
from resilient_circuits import ResilientComponent

log = logging.getLogger(__name__)


class DLPListener(ResilientComponent):

    def __init__(self, opts):
        super(DLPListener, self).__init__(opts)
        # A SOAP Client to interface with DLP Incident and Reporting API
        self.soap_client = DLPSoapClient(app_configs=opts.get("fn_symantec_dlp", {}))

        # A REST Client to interface with Resilient
        self.rest_client = self.rest_client()
        #print(self.soap_client.service.incidentList(savedReportId=121,incidentCreationDateLaterThan='2019-07-20'))
        #incident_list = self.soap_client.service.incidentList(savedReportId=121,incidentCreationDateLaterThan='2019-07-20')
        # for id in incident_list['incidentId']:
        #     if id == 121:
        #         incident_detail = self.soap_client.service.incidentDetail(incidentId=id)
        #         print(incident_detail)
        #         binaries = self.soap_client.service.incidentBinaries(incidentId=id,includeOriginalMessage=False, includeAllComponents='?') 
     
    