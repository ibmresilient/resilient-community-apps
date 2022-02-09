# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging
import base64
from readline import redisplay

from .jinja_common import JinjaEnvironment
from resilient_lib import validate_fields

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_symantec_dlp"
DEFAULT_POLLER_INTERVAL_SECONDS=60
DEFAULT_POLLER_LOOKBACK_SECONDS=600

SOAR_HEADER = "IBM SOAR"
CREATED_BY_SOAR = "Created by {}".format(SOAR_HEADER)
SYMANTEC_DLP_HEADER="From Symantec DLP"


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
        """ Return the list of ins matching the filter 
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

    def get_sdlp_editable_attributes(self, incident_id):

        url = u"{0}/incidents/{1}/editableAttributes".format(self.base_url, incident_id)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_incident_static_attributes(self, incident_id):

        url = u"{0}/incidents/{1}/staticAttributes".format(self.base_url, incident_id)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_incident_custom_attributes(self):

        url = u"{0}/incidents/customAttributes".format(self.base_url)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        custom_attribute_list = r_json.get("customAttributesList", [])
        return  custom_attribute_list

    def get_sdlp_incident_history(self, incident_id):

        url = u"{0}/incidents/{1}/history".format(self.base_url, incident_id)

        response = self.rc.execute("GET", url, headers=self.headers,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_incident_notes(self, incident_id):
        history_list = self.get_sdlp_incident_history(incident_id)
        notes = []
        for history_item in history_list:
            if history_item.get('incidentHistoryAction') == 'ADD_COMMENT':
                note = u"""<b>Note from Symantec DLP:</b>
                        <br>
                        <b>User:</b>{user} added note at {time}
                        <br><br>
                        <b>Note detail</b>: <p>{detail}</p>
                        """.format(
                            user=history_item['dlpUserName'],
                            time=history_item['incidentHistoryDate'],
                            detail=history_item['incidentHistoryDetail']
                        )
                notes.append(note)
        return notes

    def set_sdlp_update_incident_custom_attribute(self, incident_id, soar_case_id, soar_case_url):

        url = u"{0}/incidents".format(self.base_url, incident_id)

        update_json = {
            "incidentIds":[ incident_id ],
            "incidentCustomAttributes":[
                { 
                    "columnIndex": 18,
                    "value": soar_case_id
                },
                {
                    "columnIndex": 17,
                    "value": soar_case_url
                }
            ]
        }   
        response = self.rc.execute("PATCH", url, headers=self.headers, json=update_json,
                                    verify=self.verify, proxies=self.rc.get_proxies())
        r_json = response.json()
        return r_json

    def get_sdlp_incident_payload(self, incident_id):
        """[summary]

        Args:
            incident_id ([]): [descrip]

        Returns:
            [json object]: [payload containing information on the Symantec DLP incident]
        """
        # Get the incident attributes
        sdlp_payload = {}
        sdlp_payload['notes'] = self.get_sdlp_incident_notes(incident_id)
        sdlp_payload['editableIncidentDetails'] = self.get_sdlp_editable_attributes(incident_id)
        sdlp_payload['staticIncidentDetails'] = self.get_sdlp_incident_static_attributes(incident_id)

        # Add the link back to the Symantec incident URL
        sdlp_payload['sdlp_incident_url'] = self.get_sdlp_incident_url(incident_id)
        return sdlp_payload

    def get_sdlp_incident_url(self, incident_id):
        """[summary]

        Args:
            incident_id ([type]): [DLP incidentId]

        Returns:
            [type]: [URL for DLP incident]
        """

        return "https://{0}/ProtectManager/IncidentDetail.do?value(variable_1)=incident.id&value(operator_1)=incident.id_in&value(operand_1)={1}".format(self.server, incident_id)
