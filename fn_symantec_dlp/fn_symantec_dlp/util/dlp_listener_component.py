
import logging
import os
import tempfile
import json
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
            if not self.does_incident_exist_in_res(sdlp_id_type, incident['incidentId']):
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

                payload = self.prepare_incident_dto(incident)
                log.debug("Creating Incident")
                jsonpayload = json.loads(payload)
                # Create the Incident
                new_incident = self.rest_client.post('/incidents', json.loads(payload))

                self.upload_dlp_binaries(incident, new_incident['id'])

    def upload_dlp_binaries(self, incident, res_incident_id):
        # Upload remaining parts such as the Attachments
        binaries = self.soap_client.incident_binaries(incidentId=incident['incidentId'], includeOriginalMessage=False,
                                                      includeAllComponents='?')
        if binaries:
            for component in binaries['Component']:
                try:
                    with tempfile.NamedTemporaryFile(mode="w+b", delete=False) as temp_upload_file:
                        temp_upload_file.write(component['content'])

                        temp_upload_file.close()
                        self.rest_client.post_attachment('/incidents/{}/attachments'.format(res_incident_id),
                                                         temp_upload_file.name, component['name'])
                finally:
                    os.unlink(temp_upload_file.name)

    def prepare_incident_dto(self, incident):
        from zeep.helpers import serialize_object
        default_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, "data/templates")
        payload = self.map_values(
            template_file=os.path.abspath(default_dir + "/_dlp_incident_template.jinja2"),
            message_dict={"incident": {"incident": serialize_object(incident['incident']), "incidentId": incident['incidentId'], "eventDate": round(incident['incident']['eventDate'].timestamp() * 1000)}})
        return payload

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

    def does_incident_exist_in_res(self, sdlp_id_type, sdlp_incident_id):
        # For each incident; Take in Incident ID's and check if theres an existing resilient incident
        search_ex_dto = {
            "org_id": self.rest_client.org_id,
            "query": u"incident.{}.{}: {}".format(sdlp_id_type['id'], sdlp_id_type['name'], sdlp_incident_id),
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

