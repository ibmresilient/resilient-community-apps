# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import os
import datetime
import logging
import base64
import shutil
import traceback

from resilient_lib import IntegrationError, validate_fields, write_to_tmp_file, readable_datetime, str_to_bool
from fn_symantec_dlp.lib.constants import FROM_SYMANTEC_DLP_COMMENT_HDR
from .jinja_common import JinjaEnvironment

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_symantec_dlp"
SDLP_DEFAULT_PAGE_SIZE=100

class SymantecDLPCommon():
    def __init__(self, rc, options):
        # Read the configuration options
        required_fields = ["sdlp_host", "sdlp_username", "sdlp_password", "sdlp_saved_report_id"]
        validate_fields(required_fields, options)
        self.options = options._asdict() if isinstance(options, tuple) else options
        self.rc = rc
        self.api_version = options.get("api_version", "v2")
        self.server = options.get("sdlp_host")
        self.username = options.get("sdlp_username")
        self.password = options.get("sdlp_password")
        self.base_url = u"https://{0}/ProtectManager/webservices/{1}".format(self.server, self.api_version)
        self.headers = self._make_headers(self.username, self.password)
        self.verify = str_to_bool(options.get("cafile", "false"))
        self.saved_report_id = options.get("sdlp_saved_report_id")

        self.jina_env = JinjaEnvironment()

    def _make_headers(self, username, password):
        """ Build the header for a Symantec DLP REST API request call using basic auth formatting.

        Args:
            username ([string]): [ username for DLP Enforce Server account]
            password ([string]): [ password for DLP Enforce Server account ]

        Returns:
            [json object]: [ Python requests authorization header]
        """
        basic_auth  = "{0}:{1}".format(username, password)

        b64_basic_auth = base64.b64encode((basic_auth).encode('ascii'))
        headers = {'Authorization': b"Basic " + b64_basic_auth,
                   'Content-Type': "application/json"}
        return headers

        
    def get_sdlp_incidents_in_save_report(self, saved_report_id, last_poller_time):
        """ Get the DLP incidents from a saved report query and return a list of DLP incidents 
            matching the query filter.
        Args:
            saved_report_id ([integer]): [ DLP saved report Id (stored in the app.config) ]

        Returns:
            [list]: [ list of Symantec DLP incident Ids ]
        """
        # Get the query filter used for the saved report.
        url = u"{0}/savedReport/{1}".format(self.base_url, saved_report_id)
        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()

        LOG.debug(r_json)
        
        # Setup incident query filters
        page_number = 1
        if last_poller_time:
            # Query since last poll time if specified
            last_poller_datetime_string = readable_datetime(last_poller_time, milliseconds=True, rtn_format='%Y-%m-%dT%H:%M:%S')
            time_filter = { 'filterType': 'localDateTime', 
                            'operandOne': {'name': 'detectionDate'}, 
                            'operator': 'GTE', 
                            'operandTwoValues': [ last_poller_datetime_string ]}
            r_json['filter']['filters'].append(time_filter)
        
        r_json['select'] = [ {'name': 'incidentID'}, {'name': 'detectionDate'} ]
        r_json['page'] = { 'type': "offset",
                           'pageNumber': page_number,
                           'pageSize': SDLP_DEFAULT_PAGE_SIZE
        }
        LOG.debug(r_json)

        not_complete = True
        dlp_incidents = []
        url = u"{0}/incidents".format(self.base_url)
        while not_complete:
            # Get first page of incidents
            response2 = self.rc.execute("POST", url, headers=self.headers, json=r_json, 
                                    verify=self.verify, proxies=self.rc.get_proxies())

            r2_json = response2.json()
            if not r2_json:
                not_complete = False
                break

            # Collect incidents in a list
            incidents = r2_json.get("incidents", [])
            for incident in incidents:
                dlp_incidents.append(incident.get("incidentId"))

            # Set up for next page
            page_number += 1
            r_json["page"]["pageNumber"] = page_number

        return dlp_incidents

    def get_sdlp_components(self, incident_id):
        """[ Get the Symantec DLP incident components ]

        Args:
            incident_id ([integer]): [ DLP incidentId ]

        Returns:
            [json]: [ list of incident components ]
        """
        url = u"{0}/incidents/{1}/components".format(self.base_url, incident_id)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_component_data(self, incident_id, component_id):
        """[ Get the Symantec DLP incident component data ]

        Args:
            incident_id ([integer]): [ DLP incidentId ]
            incident_id ([integer]): [ DLP componentId ]

        Returns:
            [json]: [ DLP incident component data ]
        """
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
             ibm_case_id and ibm_soar_case_url are created in DLP by the user 
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

    def get_sdlp_incident_statuses(self):
        """[ Get the Symantec DLP incident statuses data ]

        Args:

        Returns:
            [json]: [ list of history data from Symantec DLP ]
        """
        url = u"{0}/incidents/statuses".format(self.base_url)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_incident_notes(self, incident_id):
        """[ Get the list of DLP incident notes and format for posting in SOAR ]

        Args:
            incident_id ([integer]): [ DLP incidentId ]

        Returns:
            [list]: [ list of note data from Symantec DLP ]
        """
        history_list = self.get_sdlp_incident_history(incident_id)
        notes = []
        for history_item in history_list:
            if history_item.get('incidentHistoryAction') == 'ADD_COMMENT':
                note = u"""<b>{comment_header}</b>
                        <br>
                        <b>User: </b>{user} added note at {time}
                        <br>
                        <b>Note detail</b>: <p>{detail}</p>
                        """.format(
                            comment_header=FROM_SYMANTEC_DLP_COMMENT_HDR,
                            user=history_item['dlpUserName'],
                            time=history_item['incidentHistoryDate'],
                            detail=history_item['incidentHistoryDetail']
                        )
                notes.append(note)
        # Reverse the order so older notes are added first
        notes.reverse()
        return notes

    def send_note_to_sdlp(self, incident_id, note_text):
        """Send a note to DLP

        Args:
            incident_id (integer): DLP incidentId
            note_text (string): note text

        Returns:
            json : incident that was updated
        """
        url = u"{0}/incidents".format(self.base_url)
        note_date_time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        update_json = {
                        "incidentIds":[ incident_id ],
                        "incidentNotes":[{
                            "dateTime": note_date_time,
                            "note": note_text
                        }]
        }
        response = self.rc.execute("PATCH", url, headers=self.headers, json=update_json,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_incident_status_name(self, sdlp_incident_payload):
        """Get the incident status name from DLP incident payload

        Args:
            sdlp_incident_payload ([json]): [json object containing DLP incident detail and info]

        Returns:
            [string]: [incidentStatusName field from the 'editableIncidentDetails' json object from DLP]
        """
        editable_incident_details = sdlp_incident_payload.get('editableIncidentDetails')
        info_map = editable_incident_details.get('infoMap')
        incident_status_name = info_map.get('incidentStatusName')
        return incident_status_name

    def get_incident_status_index(self, incident_status):
        """Get the incident status index from DLP incident payload

        Args:
            incident_status ([string]): [ DLP incident status name ]

        Returns:
            [string]: ['id' field corresponding to the incident status from the incident/statuses endpoint]
        """
        statuses = self.get_sdlp_incident_statuses()
        index = 0 
        for status in statuses:
            if status.get('name') == incident_status:
                index = status.get('id')
        return index

    def update_sdlp_status(self, incident_id, incident_status_name):
        """[ Patch the Symantec DLP incident status name and status Id in DLP ]

        Args:
            incident_id ([integer]): [ DLP incidentId ]
            incident_status_name ([string]): [DLP incident status name]
        Returns:
            [json]: [ list of DLP incident ids that were updated ]
        """

        incident_status_id = self.get_incident_status_index(incident_status_name)
        if incident_status_id <= 0:
            raise IntegrationError("Symantec DLP incident status name {0} not found in DLP".format(incident_status_name))

        update_json = {
           "incidentIds":[ incident_id ],
           "incidentStatusName": incident_status_name,
           "incidentStatusId": incident_status_id
        }

        url = u"{0}/incidents".format(self.base_url)

        response = self.rc.execute("PATCH", url, headers=self.headers, json=update_json,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_custom_attribute_index(self, editable_attributes, custom_attribute_name):
        """Return the index of the "editable" custom attribute.  
        The index is needed to update the attribute in DLP.

        Args:
            editable_attributes (json): list of editable incident attributes
            custom_attribute_name (string): custom attribute name

        Returns:
            integer: return the index of the custom attribute
        """
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

    def patch_sdlp_incident_custom_attribute(self, incident_id, soar_case_id, soar_case_url, ):
        """ Patch the Symantec DLP incident with the custom attributes containing the SOAR case ID
            and URL

        Args:
            incident_id ([integer]): [ DLP incident Id]
            soar_case_id ([integer]): [ SOAR Case ID]]
            soar_case_url ([string]): [ URL that links to the SOAR incident ]

        Returns:
            [json object]: [ json object containing the DLP incidentId of the incident whose 
            "ibm_soar_case_id" and "ibm_soar_case_url" custom attributes are updated to the specified
            SOAR values. ]
        """
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
        url = u"{0}/incidents".format(self.base_url)

        update_json = {
            "incidentIds":[ incident_id ],
            "incidentCustomAttributes": attributes_list
        }   
        response = self.rc.execute("PATCH", url, headers=self.headers, json=update_json,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def upload_sdlp_binaries(self, soar_rest_client, sdlp_incident_id, soar_case_id):
        """upload_dlp_binaries takes an incident and a resilient incident ID and then attempts to query DLP for any incident_binaries
        Any returning binaries are then sent to Resilient as an Artifact, retaining its name and extension type.
        """
        # Upload remaining parts such as the Attachments
        components = self.get_sdlp_components(sdlp_incident_id)

        artifact_name_list = []
        for component in components:
            if component.get('componentType') != 'Attachment':
                continue
            component_id = component.get('componentId')
            component_data = self.get_sdlp_component_data(sdlp_incident_id, component_id)
            try:
                path_tmp_file, path_tmp_dir = write_to_tmp_file(component_data.get('content'))
                    
                artifact_uri = "/incidents/{}/artifacts/files".format(soar_case_id)
                soar_rest_client.post_artifact_file(artifact_uri,
                                                    soar_rest_client.get('default_artifact_type_id'),
                                                    path_tmp_file,
                                                    value=component.get('name'),
                                                    description="Binary File imported from Symantec DLP")
                artifact_name_list.append(component.get('name'))

            except Exception as upload_ex:
                LOG.debug(traceback.format_exc())
                # Log the Connection error to the user
                LOG.error(u"Problem: %s", repr(upload_ex))
                LOG.error(u"[Symantec DLP] Encountered an exception when uploading a Binary to Resilient.")
    
            finally:
                # # Clean up the tmp_file 
                if path_tmp_dir and os.path.isdir(path_tmp_dir):
                    shutil.rmtree(path_tmp_dir)

        return artifact_name_list

    def get_sdlp_incident_payload(self, incident_id):
        """[ Create the incident payload for creating a SOAR case from DLP incident data. ]

        Args:
            incident_id ([integer]): [ DLP incident Id ]

        Returns:
            [json object]: [ payload containing information on the Symantec DLP incident ]
        """
        # Get the incident attributes
        sdlp_payload = {}
        sdlp_payload['notes'] = self.get_sdlp_incident_notes(incident_id)
        sdlp_payload['editableIncidentDetails'] = self.get_sdlp_editable_attributes(incident_id)
        sdlp_payload['staticIncidentDetails'] = self.get_sdlp_incident_static_attributes(incident_id)

        # Add the link back to the Symantec DLP incident URL
        sdlp_payload['sdlp_incident_url'] = self.get_sdlp_incident_url(incident_id)
        return sdlp_payload

    def get_sdlp_incident_editable_detail_payload(self, incident_id):
        """[ Create the incident payload for creating a SOAR case from DLP incident data. ]

        Args:
            incident_id ([integer]): [ DLP incident Id ]

        Returns:
            [json object]: [ payload containing information on the Symantec DLP incident ]
        """
        # Get the incident attributes
        sdlp_payload = {}
        sdlp_payload['editableIncidentDetails'] = self.get_sdlp_editable_attributes(incident_id)

        return sdlp_payload

    def update_sdlp_incident(self, sdlp_update_payload):
        """ Update (patch) the DLP incident

        Args:
            sdlp_update_payload (json): json payload of incident attributes to update

        Returns:
            _type_: _description_
        """
        url = u"{0}/incidents".format(self.base_url)

        response = self.rc.execute("PATCH", url, headers=self.headers, json=sdlp_update_payload,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_incident_url(self, incident_id):
        """[ Formulate the Syamntec DLP incident URL ]

        Args:
            incident_id ([type]): [DLP incidentId]

        Returns:
            [string]: [URL for DLP incident]
        """

        return "https://{0}/ProtectManager/IncidentDetail.do?value(variable_1)=incident.id&value(operator_1)=incident.id_in&value(operand_1)={1}".format(self.server, incident_id)
