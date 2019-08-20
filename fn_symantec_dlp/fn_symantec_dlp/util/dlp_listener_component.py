# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pylint: disable=C0303
import logging
import os
import tempfile
import json
import datetime
import uuid
import calendar
from resilient_circuits import ResilientComponent, template_functions
from zeep.helpers import serialize_object

from fn_symantec_dlp.lib.dlp_soap_client import DLPSoapClient

log = logging.getLogger(__name__)


class DLPListener(ResilientComponent):
    """DLPListener class which is used to Poll DLP and listen as new Incidents come occur.
    The DLP Listener is instantiated once and for each subsequent poll the start_poller function is targeted.
    """

    def __init__(self, opts):
        super(DLPListener, self).__init__(opts)
        # A SOAP Client to interface with DLP Incident and Reporting API
        self.soap_client = DLPSoapClient(app_configs=opts.get("fn_symantec_dlp", {}))

        # A REST Client to interface with Resilient
        self.rest_client = self.rest_client()
        self.add_filters_to_jinja(self)

    def start_poller(self):
        """start_poller begins the Polling process for DLP to search for any Incidents to bring to Resilient
        It calls all the other functions in this class as it filters out duplicate incidents, prepares new Incidents and uploads attachments
        """

        log.debug("Started Poller")
        # gather the list of incidents from a saved report
        res = DLPSoapClient.incident_list(saved_report_id=DLPSoapClient.dlp_saved_report_id,
                                          incident_creation_date_later_than=datetime.datetime.now() - datetime.timedelta(days=14))

        # gather the incident_details for incidents returned
        incidents = DLPSoapClient.incident_detail(incident_id=res['incidentLongId'])
        log.info("Now filtering out Incidents which already have a Resilient Incident ID")
        log.info("Number of Incidents before filtering: %d", len(incidents))

        # Drop all incidents which have a res_id custom attribute
        incidents = list(self.filter_existing_incidents(incidents))

        log.info("Number of Incidents after filtering: %d", len(incidents))
        # Get the sdlp_incident_id field
        sdlp_id_type = self.rest_client.get('/types/{}/fields/{}'.format("incident", "sdlp_incident_id"))

        for incident in incidents:
            # For each incident; Take in Incident ID's and check if theres an existing resilient incident
            if not self.does_incident_exist_in_res(sdlp_id_type, incident['incidentId']):
                # There is no resilient incident with the given DLP Incident ID
                # Create the incident
                log.info("Found no Resilient Incident with given DLP Incident ID %d, creating an incident.", incident['incidentId'])

                payload = self.prepare_incident_dto(incident)
                log.debug("Creating Incident")
                
                # Create the Incident
                new_incident = self.rest_client.post('/incidents', json.loads(payload,strict=False))
                log.info("Created new Resilient Incident with ID %d for DLP Incident with ID %d", new_incident['id'], incident['incidentId'])

                self.upload_dlp_binaries(incident, new_incident['id'])

                self.send_res_id_to_dlp(new_incident, incident['incidentId'])

    def send_res_id_to_dlp(self, new_incident, dlp_incident_id):
        """send_res_id_to_dlp takes a newly created incident from Resilient and attempts to send its Incident ID to the corressponding DLP Incident
        This reduces the amount of API calls made to Resilient on each Poll as any DLP Incidents with a resilient_incidentid are filtered out before we check Resilient

        :param new_incident: Resilient Incident
        :type new_incident: dict
        """
        headers = {'content-type': 'text/xml'}
        body = """<?xml version="1.0" encoding="UTF-8"?>
                        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sch="http://www.vontu.com/v2011/enforce/webservice/incident/schema" xmlns:sch1="http://www.vontu.com/v2011/enforce/webservice/incident/common/schema">
                        <soapenv:Header/>
                        <soapenv:Body>
                            <sch:incidentUpdateRequest>
                                <!--1 or more repetitions:-->
                                <updateBatch>
                                    <batchId>{batch}</batchId>
                                    <!--Zero or more repetitions:-->
                                    <incidentId>{dlp_id}</incidentId>
                                    <incidentAttributes>
                                    <!--Zero or more repetitions:-->
                                    <customAttribute>
                                        <sch1:name>resilient_incidentid</sch1:name>
                                        <!--Optional:-->
                                        <sch1:value>{resilient_id}</sch1:value>
                                    </customAttribute>
                                    </incidentAttributes>
                                </updateBatch>
                            </sch:incidentUpdateRequest>
                        </soapenv:Body>
                        </soapenv:Envelope>""".format(batch="_{}".format(uuid.uuid4()), resilient_id=new_incident['id'], dlp_id=dlp_incident_id)
        response = DLPSoapClient.session.post("https://9.70.194.103:8443/ProtectManager/services/v2011/incidents",
                                              data=body, headers=headers)
        response.raise_for_status()
        log.info("Sent new Resilient Incident ID back to the original DLP Incident as a custom attribute")

        

    def upload_dlp_binaries(self, incident, res_incident_id):
        """upload_dlp_binaries takes an incident and a resilient incident ID and then attempts to query DLP for any incident_binaries
        Any returning binaries are then sent to Resilient as an Attachment, retaining its name and extension type.
        
        :param incident: DLP Incident
        :type incident: Zeep object
        :param res_incident_id: A Resilient Incident ID to send the attachments too 
        :type res_incident_id: int
        """
        # Upload remaining parts such as the Attachments
        binaries = self.soap_client.incident_binaries(incident_id=incident['incidentId'], include_original_message=False,
                                                      include_all_components='?')
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
        """prepare_incident_dto uses a Jinja template located in the data/templates directory and prepares an incident DTO.
        A DLP Incident is parsed and artifacts are templated into the DTO which is then sent to create an incident.
        
        :param incident: DLP Incident
        :type incident: Zeep object
        :return: a dict with the dto ready to send
        :rtype: dict
        """

        # Gather Incident Notes 
        notes_to_be_added = []
        for historyItem in incident['incident']['incidentHistory']:
            if historyItem['actionType']['_value_1'] == "Note Added":
                    # Convert Date to a UTC time stamp for visual purposes
                    historyItem['date'] = historyItem['date'].strftime('%Y-%M-%dT%H:%M:%SZ')
                    notes_to_be_added.append(u"""<b>Note gathered from Symantec DLP Incident</b>
                        <br>
                        <b>Event Time: </b><p>{time}</p>
                        <br><br>
                        <b>Event Detail</b>: <p>{detail}</p>
                        <p> performed by user <b>{user}</b></p""".format(
                            time=historyItem['date'], 
                            detail=historyItem['detail'],
                            user=historyItem['user']
                        ))
    
        default_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, "data/templates")
        payload = self.map_values(
            template_file=os.path.abspath(default_dir + "/_dlp_incident_template.jinja2"),
            message_dict={"incident":
                              {"incident": serialize_object(incident['incident']),
                               "incidentId": incident['incidentId'],
                               "event_date": incident['incident']['eventDate'],
                               "notes": notes_to_be_added,
                               "detection_date": incident['incident']['detectionDate'],
                               "severity": self.return_res_severity(incident['incident']['severity'])}})
        return payload

    @staticmethod
    def return_res_severity(dlp_severity):
        if dlp_severity == 'high':
            return "High"
        elif dlp_severity == 'medium':
            return "Medium"
        else: 
            return "Low"

    @staticmethod
    def filter_existing_incidents(incidents):
        """filter_existing_incidents function used to filter out any DLP Incidents which already have an associated Resilient Incident ID. 
        Done to avoid duplication, the function iterates over a list of incidents, searching the customAttributes for a resilient_incidentid attribute.
        If this value is empty, we yield that incident back to the caller, if a value is set, do nothing.
        
        
        :param incidents: A number of incidents which did not have a resilient_incidentid customAttribute set
        :type incidents: generator
        """
        for incident in incidents:
            if hasattr(incident['incident'], 'customAttributeGroup'):  # if there are customAttributeGroups
                for groupset in incident['incident'].customAttributeGroup:  # for each group
                    if hasattr(groupset, 'customAttribute'):  # if the group has a customAttribute object
                        for attribute in groupset['customAttribute']:  # Loop the customAttribute object to get an attribute
                            # If the attribute is the resilient one and has no value
                            if attribute.name == "resilient_incidentid" and attribute.value is None:
                                yield incident

    def does_incident_exist_in_res(self, sdlp_id_type, sdlp_incident_id):
        """does_incident_exist_in_res function used to check if a given DLP incident has already been imported into Resilient. 
        
        :param sdlp_id_type: the sdlp_id custom field type acquired from the REST API, we use the name and ID properties
        :type sdlp_id_type: Custom Field
        :param sdlp_incident_id: The Incident ID from DLP
        :type sdlp_incident_id: int
        :return: returns a results object of results, in the code we perform a truth value check to determine if this function returned successfuly
        :rtype: list of results
        """
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
    @staticmethod
    def add_filters_to_jinja(self):
        ds_filter = {
            "regex_escape": self.regex_escape,
            "dt_to_milli_epoch": self.dt_to_milli_epoch
        }
        env = template_functions.environment()
        env.globals.update(ds_filter)

    def regex_escape(self, val):
        return val.replace('\\', r'\\')

    def dt_to_milli_epoch(self, dt):
        """dt_to_milli_epoch Jinja Helper function which takes
        a datetime object and attempts to strip to a millesecond epoch
        strips the timezone of the incoming datetime.
        
        :param dt: datetime object to be converted
        :type dt: [type]
        :return: millesecond epoch
        :rtype: int
        """
        try: 
            epoch = datetime.datetime.utcfromtimestamp(0)
            naive = dt.replace(tzinfo=None)

            return int((naive - epoch).total_seconds() * 1000.0)
        except Exception as e:
            log.debug("Encountered exception when converting datetime to an epoch; Error %s", e)
