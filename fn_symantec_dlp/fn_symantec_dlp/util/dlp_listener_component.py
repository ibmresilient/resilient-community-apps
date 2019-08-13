
import logging
import os
import tempfile
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

        for incident in incidents:
            # For each incident; Take in Incident ID's and check if theres an existing resilient incident
            if not self.does_incident_exist_in_res(sdlp_id_type):
                # There is no resilient incident with the given DLP Incident ID
                # Create the incident
                log.debug("Found no Resilient incident with the given DLP Incident ID, creating an incident.")
                incident_to_create = incidents[0]
                # Prepare a Jinja Payload with the Artifacts
                incident_create_dto = {
                    "name": "Incident from DLP",
                    "discovered_date": round(incident_to_create['incident']['eventDate'].timestamp()*1000),
                    "properties": {
                        sdlp_id_type['name']: 119
                    },
                    "comments": [
                        {
                            "text": {
                                "format": "text",
                                "content": incident_to_create['incident']['incidentHistory'][0]['detail']
                            },
                            "create_date": round(incident_to_create['incident']['eventDate'].timestamp()*1000)#round(incident_to_create['incident']['incidentHistory'][1]['date'].timestamp()*1000)
                        }
                    ]
                }
                default_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, "data/templates")

                payload = self.map_values(
                    template_file=os.path.abspath(default_dir+"/_dlp_incident_template.jinja2"),
                    message_dict={"incident": {"eventDate": incident['incident']['eventDate'].timestamp()*1000}})

                    # {
                    #     "incident": thing,
                    #     "res_severity": thing,
                    # }

                # Create the Incident
                # self.rest_client.post('/incidents',
                # incident_create_dto)




    @staticmethod
    def filter_existing_incidents(incidents):
        for incident in incidents:
            if hasattr(incident['incident'], 'customAttributeGroup'):  # if there are customAttributeGroups
                for groupset in incident['incident'].customAttributeGroup:  # for each group
                    if hasattr(groupset, 'customAttribute'):  # if the group has a customAttribute object
                        for attribute in groupset['customAttribute']:  # Loop the customAttribute object to get an attribute
                            # If the attribute is the resilient one and has no value
                            if attribute.name == "resilient_incidentid" and attribute.value is None:
                                yield incident

    def does_incident_exist_in_res(self, sdlp_id_type):
        # For each incident; Take in Incident ID's and check if theres an existing resilient incident
        search_ex_dto = {
            "org_id": self.rest_client.org_id,
            "query": u"incident.{}.{}: 119".format(sdlp_id_type['id'], sdlp_id_type['name']),
            "types": [
              "incident"
            ]
          }
        res = self.rest_client.search(search_ex_dto)
        return res['results']

    @staticmethod
    def map_values(template_file, message_dict):
        """Map_Values is used to :
        Take in a forwarded Event from DLP
        Import a Jinja template
        Map Event data to a new Incidents data including artifact data"""
        log.debug("Attempting to map message to an IncidentDTO. Message provided : {}".format(message_dict))
        with open(template_file, 'r') as template:

            incident_template = template.read()
            incident_data = template_functions.render(incident_template, message_dict)
            log.debug(incident_data)
            return incident_data

