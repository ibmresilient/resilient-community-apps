
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
        print(len(incidents))
        # Drop all incidents which have a res_id custom attribute
        incidents = list(self.filter_existing_incidents(incidents))

        print(len(incidents))
        # Get the sdlp_incident_id field
        sdlp_id_type = self.rest_client.get('/types/{}/fields/{}'.format("incident", "sdlp_incident_id"))


    def filter_existing_incidents(self, incidents):
        for incident in incidents:
            if hasattr(incident['incident'], 'customAttributeGroup'):  # if there are customAttributeGroups
                for groupset in incident['incident'].customAttributeGroup:  # for each group
                    if hasattr(groupset, 'customAttribute'):  # if the group has a customAttribute object
                        for attribute in groupset['customAttribute']:  # Loop the customAttribute object to get an attribute
                            # If the attribute is the resilient one and has no value
                            if attribute.name == "resilient_incidentid" and attribute.value is None:
                                yield incident


    

