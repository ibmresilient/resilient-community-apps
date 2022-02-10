# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import os
import logging
import base64
import shutil
import traceback

from .jinja_common import JinjaEnvironment
from resilient_lib import validate_fields, write_to_tmp_file

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_symantec_dlp"
DEFAULT_POLLER_INTERVAL_SECONDS=60
DEFAULT_POLLER_LOOKBACK_SECONDS=600

SOAR_HEADER = "IBM SOAR"
CREATED_BY_SOAR = "Created by {}".format(SOAR_HEADER)
SYMANTEC_DLP_HEADER="From Symantec DLP:"


class SymantecDLPCommon():
    def __init__(self, rc, options):
        # Read the configuration options
        required_fields = ["sdlp_host", "sdlp_username", "sdlp_password", "sdlp_savedreportid"]
        validate_fields(required_fields, options)
        self.options = options._asdict() if isinstance(options, tuple) else options
        self.rc = rc
        self.api_version = options.get("api_version", "v2")
        self.server = options.get("sdlp_host")
        self.username = options.get("sdlp_username")
        self.password = options.get("sdlp_password")
        self.base_url = u"https://{0}/ProtectManager/webservices/{1}".format(self.server, self.api_version)

        self.headers = self._make_headers(self.username, self.password)

        self.verify = False if self.options.get('cafile').lower() == "false" else self.options.get('cafile')
        self.saved_report_id = options.get("sdlp_savedreportid")

        self.jina_env = JinjaEnvironment()

    def _make_headers(self, username, password):
        basic_auth  = "{0}:{1}".format(username, password)

        b64_basic_auth = base64.b64encode((basic_auth).encode('ascii'))
        headers = {'Authorization': b"Basic " + b64_basic_auth,
                   'Content-Type': "application/json"}
        return headers

    def _make_createdate_filter(self, last_poller_datetime):
        """Convert epoch to iso format "T" time.
        """
        last_poller_datetime_iso = last_poller_datetime.isoformat()

        # remove milliseconds
        return "{lookback_date}".format(lookback_date=last_poller_datetime_iso[:last_poller_datetime_iso.rfind('.')])

        
    def get_sdlp_incidents_in_save_report(self, saved_report_id, last_poller_time):
        """ Get the DLP incidents from a saved report query and return a list of DLP incidents 
            matching the query filter.
        Args:
            saved_report_id ([integer]): [ DLP saved report Id (stored in the app.config) ]

        Returns:
            [list]: [ list of Symantec DLP incident Ids ]
        """
        url = u"{0}/savedReport/{1}".format(self.base_url, saved_report_id)
        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()

        LOG.debug(r_json)
        #last_poller_time_iso = self._make_createdate_filter(last_poller_time)
        """    "filter": {
                {
                    "operandOne": {"name": "creationDate"},
                    "filterType": "localDateTime",
                    "operator": "GT",
                    "operandTwoValues": ["2022-02-01T01:02:32.282"]
                }
            },

        params = {
            "select": [
                {"name": "incidentId"}
            ]
            "orderBy": [{
                "field": {"name": "creationDate"},
                "order": "DESC"
            }],
            "page": {
                "type": "offset",
                "pageNumber": 1,
                "pageSize": 100
            }
        }
            """

        r_json["select"] = [ {"name": "incidentID"} ]
        r_json["page"] = {
                            "type": "offset",
                            "pageNumber": 1,
                            "pageSize": 10
                         }

        LOG.debug(r_json)
        url = u"{0}/incidents".format(self.base_url)
        response2 = self.rc.execute("POST", url, headers=self.headers, json=r_json, 
                                    verify=self.verify, proxies=self.rc.get_proxies())

        r2_json = response2.json()
        
        dlp_incidents = []
        incidents = r2_json.get("incidents", [])
        for incident in incidents:
            dlp_incidents.append(incident.get("incidentId"))
        return dlp_incidents

    def get_sdlp_components(self, incident_id):

        url = u"{0}/incidents/{1}/components".format(self.base_url, incident_id)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_component_data(self, incident_id, component_id):
        url = u"{0}/incidents/{1}/components/{2}".format(self.base_url, incident_id, component_id)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_editable_attributes(self, incident_id):
        """[ Get the Symantec DLP incident editable attributes (for example "severity" is editable)]

        Args:
            incident_id ([integer]): [ DLP incidentId ]

        Returns:
            [json]: [ list of editable incident attributes from Symantec DLP ]
        """
        url = u"{0}/incidents/{1}/editableAttributes".format(self.base_url, incident_id)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_incident_static_attributes(self, incident_id):
        """[ Get the Symantec DLP incident static attributes (For example "detectionDate" is static.)]

        Args:
            incident_id ([integer]): [ DLP incidentId ]

        Returns:
            [json]: [ list of static incident attributes from Symantec DLP ]
        """
        url = u"{0}/incidents/{1}/staticAttributes".format(self.base_url, incident_id)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_incident_custom_attributes(self):
        """[ Get the list of Symantec DLP custom attributes.  Custom attributes 
             ibm_soar_case_id and ibm_soar_case_url are created in DLP by the user 
             and are initially "unassigned".  After the DLP case is created in SOAR,
             the app updates these fields in DLP so that the user can get to the 
             corresponding case.  The custom attributes are also used as a filter 
             in the "DLP saved report so that only DLP incidents not in SOAR are 
             escalated. ]

        Args:
            incident_id ([integer]): [ DLP incidentId ]

        Returns:
            [list]: [ list of custom attributes from Symantec DLP ]
        """

        url = u"{0}/incidents/customAttributes".format(self.base_url)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        custom_attribute_list = r_json.get("customAttributesList", [])
        return  custom_attribute_list

    def get_sdlp_incident_history(self, incident_id):
        """[ Get the Symantec DLP incident history data ]

        Args:
            incident_id ([integer]): [ DLP incidentId ]

        Returns:
            [json]: [ list of history data from Symantec DLP ]
        """
        url = u"{0}/incidents/{1}/history".format(self.base_url, incident_id)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_incident_notes(self, incident_id):
        """[ Formulate the Symantec DLP incident URL ]

        Args:
            incident_id ([integer]): [ DLP incidentId ]

        Returns:
            [list]: [ list of note data from Symantec DLP ]
        """
        history_list = self.get_sdlp_incident_history(incident_id)
        notes = []
        for history_item in history_list:
            if history_item.get('incidentHistoryAction') == 'ADD_COMMENT':
                note = u"""<b>SYMANTEC_DLP_HEADER</b>
                        <br>
                        <b>User: </b>{user} added note at {time}
                        <br>
                        <b>Note detail</b>: <p>{detail}</p>
                        """.format(
                            user=history_item['dlpUserName'],
                            time=history_item['incidentHistoryDate'],
                            detail=history_item['incidentHistoryDetail']
                        )
                notes.append(note)
        return notes

    def send_note_to_sdlp(self, incident_id, note_text):
        url = u"{0}/incidents".format(self.base_url, incident_id)
        update_json = {
                        "incidentIds":[ incident_id ],
                        "incidentNotes":[{
                            "dateTime":"2022-02-10T20:49:58.47",
                            "note": note_text
                        }]
        }
        response = self.rc.execute("PATCH", url, headers=self.headers, json=update_json,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_custom_attribute_index(self, editable_attributes, custom_attribute_name):

        index = 0
        custom_attribute_groups = editable_attributes.get('customAttributeGroups')
        for group in custom_attribute_groups:
            if group.get('name') == 'custom_attribute_group.default':
                custom_attributes = group.get('customAttributes')
                for custom_attribute in custom_attributes:
                    if custom_attribute.get("name") == custom_attribute_name:
                        index = custom_attribute.get("index")
                        return index
        return index

    def patch_sdlp_incident_custom_attribute(self, incident_id, soar_case_id, soar_case_url):

        # Get the index of the custom attribute.  When updating the attribute the columnIndex needs to be 
        # sent to the PATCH call...you can't use the name.
        editable_attributes = self.get_sdlp_editable_attributes(incident_id)
        soar_case_id_column_index = self.get_custom_attribute_index(editable_attributes, 'ibm_soar_case_id')
        soar_case_url_column_index = self.get_custom_attribute_index(editable_attributes, 'ibm_soar_case_url')

        attributes_list = []
        if soar_case_id_column_index > 0:
            attributes_list.append({
                                    "columnIndex": soar_case_id_column_index,
                                    "value": soar_case_id
                                    })
        if soar_case_url_column_index > 0:
            attributes_list.append({
                                    "columnIndex": soar_case_url_column_index,
                                    "value": soar_case_url
                                    })
        url = u"{0}/incidents".format(self.base_url, incident_id)

        update_json = {
            "incidentIds":[ incident_id ],
            "incidentCustomAttributes": attributes_list
        }   
        response = self.rc.execute("PATCH", url, headers=self.headers, json=update_json,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def upload_sdlp_binaries(self, sdlp_incident_id, soar_case_id):
        """upload_dlp_binaries takes an incident and a resilient incident ID and then attempts to query DLP for any incident_binaries
        Any returning binaries are then sent to Resilient as an Artifact, retaining its name and extension type.
        
        :param incident: DLP Incident
        :type incident: Zeep object
        :param res_incident_id: A Resilient Incident ID to send the Artifacts too 
        :type res_incident_id: int
        """
        # Upload remaining parts such as the Attachments
        components = self.get_sdlp_components(sdlp_incident_id)

        for component in components:
            if component.get('componentType') != 'Attachment':
                continue
            component_id = component.get('componentId')
            component_data = self.get_sdlp_component_data(sdlp_incident_id, component_id)
            try:
                path_tmp_file, path_tmp_dir = write_to_tmp_file(component_data.get('content'))
                    
                artifact_uri = "/incidents/{}/artifacts/files".format(soar_case_id)
                self.res_rest_client.post_artifact_file(artifact_uri,
                                                        self.default_artifact_type_id,
                                                        path_tmp_file,
                                                        value=component.get('name'),
                                                        description="Binary File imported from Symantec DLP")

            except Exception as upload_ex:
                LOG.debug(traceback.format_exc())
                # Log the Connection error to the user
                LOG.error(u"Problem: %s", repr(upload_ex))
                LOG.error(u"[Symantec DLP] Encountered an exception when uploading a Binary to Resilient.")
    
            finally:
                # # Clean up the tmp_file 
                if path_tmp_dir and os.path.isdir(path_tmp_dir):
                    shutil.rmtree(path_tmp_dir)

    def get_sdlp_incident_payload(self, incident_id):
        """[Create the incident payload for creating a SOAR case from DLP incident data.]

        Args:
            incident_id ([]): [ DLP incident Id ]

        Returns:
            [json object]: [payload containing information on the Symantec DLP incident]
        """
        # Get the incident attributes
        sdlp_payload = {}
        sdlp_payload['notes'] = self.get_sdlp_incident_notes(incident_id)
        sdlp_payload['editableIncidentDetails'] = self.get_sdlp_editable_attributes(incident_id)
        sdlp_payload['staticIncidentDetails'] = self.get_sdlp_incident_static_attributes(incident_id)

        # Add the link back to the Symantec DLP incident URL
        sdlp_payload['sdlp_incident_url'] = self.get_sdlp_incident_url(incident_id)
        return sdlp_payload

    def get_sdlp_incident_url(self, incident_id):
        """[ Formulate the Syamntec DLP incident URL ]

        Args:
            incident_id ([type]): [DLP incidentId]

        Returns:
            [string]: [URL for DLP incident]
        """

        return "https://{0}/ProtectManager/IncidentDetail.do?value(variable_1)=incident.id&value(operator_1)=incident.id_in&value(operand_1)={1}".format(self.server, incident_id)
