# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019
# pylint: disable=C0303
""" Helper Module used to handle all the needed operations for gathering Incidents
DLPListener is the class which performs all operations needed with DLP such as starting the poller, preparing and sending results.
It HAS-A instance of DLPSoapClient to delagate any API operations to.
"""
import logging
import os
import tempfile
import json
import datetime
import uuid
import traceback
import shutil
from resilient_circuits import ResilientComponent, template_functions
from resilient_lib import build_incident_url, build_resilient_url, str_to_bool

from zeep.helpers import serialize_object

from fn_symantec_dlp.lib.dlp_soap_client import DLPSoapClient

LOG = logging.getLogger(__name__)


class DLPListener(ResilientComponent):
    """DLPListener class which is used to Poll DLP for Incidents and then import them into Resilient.
    The DLP Listener is instantiated once and for each subsequent poll the start_poller function is targeted.
    """

    def __init__(self, opts):
        super(DLPListener, self).__init__(opts)
        # A SOAP Client to interface with DLP Incident and Reporting API
        self.dlp_opts = opts.get("fn_symantec_dlp", {})
        self.soap_client = DLPSoapClient(app_configs=self.dlp_opts)
        self.should_search_res = str_to_bool(self.dlp_opts.get("sdlp_should_search_res"))
        # A REST Client to interface with Resilient
        self.res_rest_client = ResilientComponent.rest_client(self)
        self.default_artifact_type_id = 16 # When uploading DLP Binaries as attachments, they will be uploaded at 'Other File'
        DLPListener.add_filters_to_jinja()

    def start_poller(self):
        """start_poller begins the Polling process for DLP to search for any Incidents to bring to Resilient
        It calls all the other functions in this class as it filters out duplicate incidents, prepares new Incidents and uploads attachments
        """

        LOG.debug("Started Poller")
        # gather the list of incidents from a saved report
        res = DLPSoapClient.incident_list(saved_report_id=DLPSoapClient.dlp_saved_report_id,
                                          incident_creation_date_later_than=datetime.datetime.now() - datetime.timedelta(days=14))

        # gather the incident_details for incidents returned
        incidents = DLPSoapClient.incident_detail(incident_id=res['incidentLongId'])
        LOG.info("Now filtering out Incidents which already have a Resilient Incident ID")
        LOG.info("Number of Incidents before filtering: %d", len(incidents))

        # Drop all incidents which have a res_id custom attribute
        incidents = list(self.filter_existing_incidents(incidents))

        LOG.info("Number of Incidents after filtering: %d", len(incidents))
        # Get the sdlp_incident_id field
        sdlp_id_type = self.res_rest_client.get('/types/{}/fields/{}'.format("incident", "sdlp_incident_id"))

        for incident in incidents:
            # For each incident; Take in Incident ID's and check if theres an existing resilient incident
            if not self.does_incident_exist_in_res(sdlp_id_type, incident['incidentId']):
                # There is no resilient incident with the given DLP Incident ID
                # Create the incident
                LOG.info("Found no Resilient Incident with given DLP Incident ID %d, creating an incident.", incident['incidentId'])

                payload = self.prepare_incident_dto(incident, notes_to_be_added=self.gather_incident_notes(incident))
                
                # Create the Incident
                new_incident = self.res_rest_client.post('/incidents', json.loads(payload, strict=False))
                LOG.info("Created new Resilient Incident with ID %d for DLP Incident with ID %d", new_incident['id'], incident['incidentId'])

                self.upload_dlp_binaries(incident, new_incident['id'])
                self.submit_summary_note(payload, incident, new_incident['id'])

                self.send_res_id_to_dlp(new_incident, incident['incidentId'])
        LOG.info("Finished processing all Incidents in Saved Report %s", self.soap_client.dlp_saved_report_id)

    def send_res_id_to_dlp(self, new_incident, dlp_incident_id):
        """send_res_id_to_dlp takes a newly created incident from Resilient and attempts to send its Incident ID to the corressponding DLP Incident
        This reduces the amount of API calls made to Resilient on each Poll as any DLP Incidents with a resilient_incidentid are filtered out before we check Resilient

        :param new_incident: Resilient Incident
        :type new_incident: dict
        """

        resilient_incident_url = build_incident_url(
            url=build_resilient_url(self.opts.get('host'), self.opts.get('port')), incidentId=new_incident['id'])
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
                                        <sch1:name>resilient_incident_id</sch1:name>
                                        <!--Optional:-->
                                        <sch1:value>{resilient_id}</sch1:value>
                                    </customAttribute>
                                    <customAttribute>
                                        <sch1:name>resilient_incident_url</sch1:name>
                                        <!--Optional:-->
                                        <sch1:value>{resilient_url}</sch1:value>
                                    </customAttribute>
                                    </incidentAttributes>
                                </updateBatch>
                            </sch:incidentUpdateRequest>
                        </soapenv:Body>
                        </soapenv:Envelope>""".format(
                            batch="_{}".format(uuid.uuid4()), 
                            resilient_id=new_incident['id'], 
                            dlp_id=dlp_incident_id, 
                            resilient_url=resilient_incident_url)

        response = DLPSoapClient.session.post(DLPSoapClient.sdlp_incident_endpoint,
                                              data=body, headers=headers)

        response.raise_for_status()
        LOG.info("Sent new Resilient Incident ID back to the original DLP Incident as a custom attribute")

        

    def upload_dlp_binaries(self, incident, res_incident_id):
        """upload_dlp_binaries takes an incident and a resilient incident ID and then attempts to query DLP for any incident_binaries
        Any returning binaries are then sent to Resilient as an Artifact, retaining its name and extension type.
        
        :param incident: DLP Incident
        :type incident: Zeep object
        :param res_incident_id: A Resilient Incident ID to send the Artifacts too 
        :type res_incident_id: int
        """
        # Upload remaining parts such as the Attachments
        binaries = self.soap_client.incident_binaries(incident_id=incident['incidentId'], include_original_message=False)
        if binaries:
            for component in binaries['Component']:
                try:

                    with tempfile.NamedTemporaryFile(mode="w+b", delete=False) as temp_upload_file:
                        temp_upload_file.write(component['content'])

                        temp_upload_file.close()
                        artifact_uri = "/incidents/{}/artifacts/files".format(res_incident_id)
                        self.res_rest_client.post_artifact_file(artifact_uri,
                                                                16,
                                                                temp_upload_file.name,
                                                                value=component['name'],
                                                                description="Binary File imported from Symantec DLP")
                    # path_tmp_file, path_tmp_dir = write_to_tmp_file(component['content'])
                    
                    # artifact_uri = "/incidents/{}/artifacts/files".format(res_incident_id)
                    # self.res_rest_client.post_artifact_file(artifact_uri,
                    #                                         self.default_artifact_type_id,
                    #                                         path_tmp_file,
                    #                                         value=component['name'],
                    #                                         description="Binary File imported from Symantec DLP")

                except Exception as upload_ex:
                    LOG.debug(traceback.format_exc())
                    # Log the Connection error to the user
                    LOG.error(u"Problem: %s", repr(upload_ex))
                    LOG.error(u"[Symantec DLP] Encountered an exception when uploading a Binary to Resilient.")
    
                finally:
                    # # Clean up the tmp_file 
                    # if path_tmp_dir and os.path.isdir(path_tmp_dir):
                    #     shutil.rmtree(path_tmp_dir)
                    os.unlink(temp_upload_file.name)

    def prepare_incident_dto(self, incident, notes_to_be_added):
        """prepare_incident_dto uses a Jinja template located in the data/templates directory and prepares an incident DTO.
        A DLP Incident is parsed and artifacts are templated into the DTO which is then sent to create an incident.
        
        :param incident: DLP Incident
        :type incident: Zeep object
        :return: a dict with the dto ready to send
        :rtype: dict
        """

        default_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, "data/templates")
        payload = self.map_values(
            template_file=os.path.abspath(default_dir + "/_dlp_incident_template.jinja2"),
            message_dict={"incident":
                              {"incident": serialize_object(incident['incident']),
                               "incidentId": incident['incidentId'],
                               "event_date": incident['incident']['eventDate'],
                               "notes": notes_to_be_added,
                               "detection_date": incident['incident']['detectionDate'],
                               "severity": self.return_res_severity(incident['incident']['severity']),
                               "dlp_incident_url": self.build_dlp_url(incidentid=incident['incidentId'], host=self.soap_client.host)}})
        return payload

    @staticmethod
    def build_dlp_url(incidentid, host):
        """build_dlp_url helper function used to compose a URL to the DLP Incident
        
        :param incidentid: the DLP Incident ID
        :type incidentid: int
        :param host: The Host of the DLP Installation
        :type host: string
        :return: The full URL for the Incident
        :rtype: string
        """
        
        return "{host}/ProtectManager/IncidentDetail.do?value(variable_1)=incident.id&value(operator_1)=incident.id_in&value(operand_1)={incidentId}".format(
            host=host, incidentId=incidentid)


    @staticmethod
    def gather_incident_notes(incident):
        """gather_incident_notes helper function used to extract all Notes from the DLP Incident
        Searches the IncidentHistory object for items of type "Note Added" and extracts these.
        
        :param incident: the DLP Incident
        :type incident: dict or Zeep object
        """


        # Gather Incident Notes
        notes_to_be_added = []
        for history_item in incident['incident']['incidentHistory']:
            if history_item['actionType']['_value_1'] == "Note Added":
                # Convert Date to a UTC time stamp for visual purposes
                if isinstance(history_item['date'], datetime.datetime):
                    history_item['date'] = history_item['date'].strftime('%Y-%M-%dT%H:%M:%SZ')
                #historyItem['date'] = historyItem['date'].strftime('%Y-%M-%dT%H:%M:%SZ')
                notes_to_be_added.append(u"""<b>Note gathered from Symantec DLP Incident</b>
                        <br>
                        <b>Event Time: </b><p>{time}</p>
                        <br><br>
                        <b>Event Detail</b>: <p>{detail}</p>
                        <p> performed by user <b>{user}</b></p""".format(
                            time=history_item['date'],
                            detail=history_item['detail'],
                            user=history_item['user']
                        ))
        return notes_to_be_added

    @staticmethod
    def return_res_severity(dlp_severity):
        """return_res_severity takes in a DLP severity and attempts to map it to one of the default Res severities
        
        :param dlp_severity: the dlp severity (lowercase)
        :type dlp_severity: string
        :return: The resultant Resilient Severity 
        :rtype: string
        """
        if dlp_severity == 'high':
            return "High"
        elif dlp_severity == 'medium':
            return "Medium"
        
        return "Low"

    @staticmethod
    def filter_existing_incidents(incidents):
        """filter_existing_incidents function used to filter out any DLP Incidents which already have an associated Resilient Incident ID. 
        Done to avoid duplication, the function iterates over a list of incidents, searching the customAttributes for a resilient_incidentid attribute.
        If this value is empty, we yield that incident back to the caller, if a value is set, do nothing.
        
        
        :param incidents: A number of incidents which did not have a resilient_incidentid customAttribute set
        :type incidents: dict or Zeep Object
        :return: returns a generator of all the matching incidents which can then be cast to an iterable 
        :rtype: generator
        """
        for incident in incidents:
            if hasattr(incident['incident'], 'customAttributeGroup'):  # if there are customAttributeGroups
                for groupset in incident['incident'].customAttributeGroup:  # for each group
                    if hasattr(groupset, 'customAttribute'):  # if the group has a customAttribute object
                        for attribute in groupset['customAttribute']:  # Loop the customAttribute object to get an attribute
                            # If the attribute is the resilient one and has no value
                            if attribute.name == "resilient_incident_id" and attribute.value is None:
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
        # If should_search_res app.config is false or undefined; return false so incident is created without searching res
        if not self.should_search_res:
            return False
        # For a given Incident; Take in Incident's ID and check if theres an existing resilient incident
        search_ex_dto = {
            "org_id": self.res_rest_client.org_id,
            "query": u"incident.{}.{}: {}".format(sdlp_id_type['id'], sdlp_id_type['name'], sdlp_incident_id),
            "types": [
                "incident"
            ]
            }
        res = self.res_rest_client.search(search_ex_dto)
        return res['results']

    @staticmethod
    def map_values(template_file, message_dict):
        """Map_Values is used to :
        Take in a forwarded Event from DLP
        Import a Jinja template
        Map Event data to a new Incidents data including artifact data"""
        LOG.debug("Attempting to map message to an IncidentDTO. Message provided : %d", message_dict)
        with open(template_file, 'r') as template:

            incident_template = template.read()
            incident_data = template_functions.render(incident_template, message_dict)
            LOG.debug(incident_data)
            return incident_data

    def add_filters_to_jinja():
        """add_filters_to_jinja used to setup the jinja filters as a part of the environment
        """
        ds_filter = {
            "regex_escape": DLPListener.regex_escape,
            "dt_to_milli_epoch": DLPListener.dt_to_milli_epoch
        }
        env = template_functions.environment()
        env.globals.update(ds_filter)

    @staticmethod
    def regex_escape(val):
        """regex_escape jinja filter used to escape filepaths
        
        :param val: a string to be escaped
        :type val: string
        :return: The input string with any '\\' chars escaped
        :rtype: string
        """
        return val.replace('\\', r'\\')

    @staticmethod
    def dt_to_milli_epoch(dt):
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
            LOG.debug("Encountered exception when converting datetime to an epoch; Error %s", e)
            return 0

    def prepare_incident_summary_note(self, incident, payload):
        """prepare_incident_summary_note is used to prepare a final summary note for the incident
        This is a good place to place artifacts which may not suit the artifact tab such as the User Justification
        """

        return u"""<b> A Symantec DLP Incident has been imported into Resilient</b>
        <p>Incident Notes, Artifacts and Attachments found (if any) have been imported into this Incident.</p>
        <p>Status Type for this Incident: <b>{status}</b></p>
        <p>Blocked Status for this Action: <b>{blocked_status}</b></p>
        <p>The User provided this as a User Justification: <b>{user_justification}</b> </p>
        <p>The Incident was detected with the detection server: <b>{detection_server}</b></p>
        <br><br>
        <p>After parsing the Incident; <b>{num_of_artifacts}</b> artifacts were found. </p>
        <p>Notes Imported: <b>{num_of_notes}</b></p>""".format(
            status=incident['incident']['status'],
            blocked_status=incident['incident']['blockedStatus'],
            user_justification=incident['incident']['userJustification'],
            detection_server=incident['incident']['detectionServer'],
            num_of_artifacts=len(json.loads(payload, strict=False)["artifacts"]),
            num_of_notes=len(self.gather_incident_notes(incident))
        )
    
    def submit_summary_note(self, payload, incident, new_incident_id):
        self.res_rest_client.post('/incidents/{}/comments'.format(new_incident_id), 
            {"text":{"format":"html", "content": self.prepare_incident_summary_note(incident, payload)}})
