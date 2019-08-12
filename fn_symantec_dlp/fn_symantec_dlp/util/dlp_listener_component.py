
import logging
from fn_symantec_dlp.lib.dlp_soap_client import DLPSoapClient
from resilient_circuits import ResilientComponent, template_functions
import datetime

log = logging.getLogger(__name__)

class DLPListener(ResilientComponent):

    def __init__(self, opts):
        super(DLPListener, self).__init__(opts)
        # A SOAP Client to interface with DLP Incident and Reporting API
        self.soap_client = DLPSoapClient(app_configs=opts.get("fn_symantec_dlp", {}))

        # A REST Client to interface with Resilient
        self.rest_client = self.rest_client()

    def start_poller(self):

        log.debug("Started Poller")
        # gather the list of incidents from a saved report
        res = DLPSoapClient.incident_list(savedReportId=121,
                                          incidentCreationDateLaterThan=datetime.datetime.now() - datetime.timedelta(days=14))

        # gather the incident_details for incidents returned
        incidents = DLPSoapClient.incident_detail(incidentId=res['incidentLongId'])

        