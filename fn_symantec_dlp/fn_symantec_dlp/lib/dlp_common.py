# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
from difflib import restore
import os
import ntpath
import datetime
import logging
import base64
from re import L
import shutil
import traceback

from resilient_lib import IntegrationError, validate_fields, write_to_tmp_file, readable_datetime, str_to_bool
from fn_symantec_dlp.lib.constants import FROM_SYMANTEC_DLP_COMMENT_HDR, FROM_SOAR_COMMENT_HDR
from .jinja_common import JinjaEnvironment

LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_symantec_dlp"
SDLP_DEFAULT_PAGE_SIZE = 100
default_artifact_type_id = 16 # When uploading DLP Binaries as attachments, they will be uploaded at 'Other File'

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
        self.base_url = f"https://{self.server}/ProtectManager/webservices/{self.api_version}"
        self.headers = self._make_headers(self.username, self.password)
        self.verify = str_to_bool(options.get("cafile", "false"))
        self.saved_report_id = options.get("sdlp_saved_report_id")
        self.proxies = rc.get_proxies() or {}

        self.jina_env = JinjaEnvironment()

    def _make_headers(self, username: str, password: str):
        """ Build the header for a Symantec DLP REST API request call using basic auth formatting.
        Args:
            username ([string]): [ username for DLP Enforce Server account]
            password ([string]): [ password for DLP Enforce Server account ]
        Returns:
            [json object]: [ Python requests authorization header]
        """
        b64_basic_auth = base64.b64encode((f"{username}:{password}").encode('ascii'))
        return {'Authorization': b"Basic " + b64_basic_auth,
            'Content-Type': "application/json"}

    def get_sdlp_incidents_in_save_report(self, saved_report_id: int, last_poller_time):
        """ Get the DLP incidents from a saved report query and return a list of DLP incidents 
            matching the query filter.
        Args:
            saved_report_id ([integer]): [ DLP saved report Id (stored in the app.config) ]
        Returns:
            [list]: [ list of Symantec DLP incident Ids ]
        """
        # Get the query filter used for the saved report.
        r_json = self.rc.execute(
            "GET",
            f"{self.base_url}/savedReport/{saved_report_id}",
            headers=self.headers,
            verify=self.verify,
            proxies=self.proxies
        ).json()
        LOG.debug(r_json)

        # Setup incident query filters
        page_number = 1
        if last_poller_time:
            # Query since last poll time if specified
            last_poller_datetime_string = readable_datetime(last_poller_time, milliseconds=True, rtn_format='%Y-%m-%dT%H:%M:%S')
            time_filter = {'filterType': 'localDateTime',
                'operandOne': {'name': 'detectionDate'},
                'operator': 'GTE',
                'operandTwoValues': [last_poller_datetime_string]}
            if r_json.get("filter", {}).get("filters"):
                r_json['filter']['filters'].append(time_filter)
            else:
                r_json['filter'] = {'filters': {}}
                r_json['filter']['filters'] = time_filter

        r_json['select'] = [{'name': 'incidentID'}, {'name': 'detectionDate'}]
        r_json['page'] = {'type': "offset",
            'pageNumber': page_number,
            'pageSize': SDLP_DEFAULT_PAGE_SIZE}
        LOG.debug(r_json)

        not_complete = True
        dlp_incidents = []
        while not_complete:
            # Get first page of incidents
            r2_json = self.rc.execute(
                "POST",
                f"{self.base_url}/incidents",
                headers=self.headers,
                json=r_json,
                verify=self.verify,
                proxies=self.proxies
            ).json()
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

    def get_sdlp_components(self, incident_id: int):
        """[ Get the Symantec DLP incident components ]
        Args:
            incident_id ([integer]): [ DLP incidentId ]
        Returns:
            [json]: [ list of incident components ]
        """
        return self.rc.execute(
            "GET",
            f"{self.base_url}/incidents/{incident_id}/components",
            headers=self.headers,
            verify=self.verify,
            proxies=self.proxies
        ).json()

    def get_sdlp_component_data(self, incident_id: int, component_id: int):
        """[ Get the Symantec DLP incident component data ]
        Args:
            incident_id ([integer]): [ DLP incidentId ]
            component_id ([integer]): [ DLP componentId ]
        Returns:
            [json]: [ DLP incident component data ]
        """
        response = self.rc.execute(
            "GET",
            f"{self.base_url}/incidents/{incident_id}/components/{component_id}",
            headers=self.headers,
            verify=self.verify,
            proxies=self.proxies
        )

        error_msg = ""
        if response.status_code >= 300:
            resp = response.json()
            error_msg = f"Symantec DLP Error: {response.status_code}: {resp.get('message')}"
        LOG.debug(response)

        try:
            content = response.content
        except Exception:
            content = ""

        return content, error_msg

    def get_sdlp_editable_attributes(self, incident_id: int):
        """[ Get the Symantec DLP incident editable attributes (for example "severity" is editable)]
        Args:
            incident_id ([integer]): [ DLP incidentId ]
        Returns:
            [json]: [ list of editable incident attributes from Symantec DLP ]
        """
        return self.rc.execute(
            "GET",
            f"{self.base_url}/incidents/{incident_id}/editableAttributes",
            headers=self.headers,
            verify=self.verify,
            proxies=self.proxies
        ).json()

    def get_sdlp_incident_static_attributes(self, incident_id: int):
        """[ Get the Symantec DLP incident static attributes (For example "detectionDate" is static.)]
        Args:
            incident_id ([integer]): [ DLP incidentId ]
        Returns:
            [json]: [ list of static incident attributes from Symantec DLP ]
        """
        return self.rc.execute(
            "GET",
            f"{self.base_url}/incidents/{incident_id}/staticAttributes",
            headers=self.headers,
            verify=self.verify,
            proxies=self.proxies
        ).json()

    def get_sdlp_incident_custom_attributes(self):
        """[ Get the list of Symantec DLP custom attributes. Custom attributes
             ibm_case_id and ibm_soar_case_url are created in DLP by the user
             and are initially "unassigned". After the DLP case is created in SOAR,
             the app updates these fields in DLP so that the user can get to the
             corresponding case. The custom attributes are also used as a filter
             in the "DLP saved report so that only DLP incidents not in SOAR are
             escalated. ]
        Args:
            incident_id ([integer]): [ DLP incidentId ]
        Returns:
            [list]: [ list of custom attributes from Symantec DLP ]
        """
        response = self.rc.execute(
            "GET",
            f"{self.base_url}/incidents/customAttributes",
            headers=self.headers,
            verify=self.verify,
            proxies=self.proxies
        ).json()
        return response.get("customAttributesList", [])

    def get_sdlp_incident_history(self, incident_id: int):
        """[ Get the Symantec DLP incident history data ]
        Args:
            incident_id ([integer]): [ DLP incidentId ]
        Returns:
            [json]: [ list of history data from Symantec DLP ]
        """
        return self.rc.execute(
            "GET",
            f"{self.base_url}/incidents/{incident_id}/history",
            headers=self.headers,
            verify=self.verify,
            proxies=self.proxies
        ).json()

    def get_sdlp_incident_statuses(self):
        """[ Get the Symantec DLP incident statuses data ]
        Args:
        Returns:
            [json]: [ list of history data from Symantec DLP ]
        """
        return self.rc.execute(
            "GET",
            f"{self.base_url}/incidents/statuses",
            headers=self.headers,
            verify=self.verify,
            proxies=self.proxies
        ).json()

    def get_sdlp_incident_notes(self, incident_id: int):
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
                notes.append(f"""<b>{FROM_SYMANTEC_DLP_COMMENT_HDR} ({history_item.get('incidentHistoryDate')})</b>
                    <br>
                    User: {history_item.get('dlpUserName')}
                    <br>
                    Note detail: <p>{history_item.get('incidentHistoryDetail')}</p>""")
        # Reverse the order so older notes are added first
        notes.reverse()
        return notes

    def send_note_to_sdlp(self, incident_id: int, note_text: str):
        """Send a note to DLP
        Args:
            incident_id (integer): DLP incidentId
            note_text (string): note text
        Returns:
            json : incident that was updated
        """
        update_json = {
            "incidentIds":[incident_id],
            "incidentNotes":[{
                "dateTime": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-4],
                "note": f"{FROM_SOAR_COMMENT_HDR}:\n{note_text}"
            }]
        }
        return self.rc.execute(
            "PATCH",
            f"{self.base_url}/incidents",
            headers=self.headers,
            json=update_json,
            verify=self.verify,
            proxies=self.proxies
        ).json()

    def get_incident_status_name(self, sdlp_incident_payload):
        """Get the incident status name from DLP incident payload
        Args:
            sdlp_incident_payload ([json]): [json object containing DLP incident detail and info]
        Returns:
            [string]: [incidentStatusName field from the 'editableIncidentDetails' json object from DLP]
        """
        return sdlp_incident_payload.get('editableIncidentDetails', {}).get('infoMap', {}).get('incidentStatusName')

    def get_incident_status_index(self, incident_status: str):
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

    def update_sdlp_incident_editable_details(self, incident_id: int, incident_status_name: str, incident_severity: str):
        """[ Patch the Symantec DLP incident status name and status Id in DLP ]
        Args:
            incident_id ([integer]): [ DLP incidentId ]
            incident_status_name ([string]): [DLP incident status name]
        Returns:
            [json]: [ list of DLP incident ids that were updated ]
        """
        # Seems like a bug in DLP: DLP returns the value of "incident.status.New" for "New" incident status.
        # We want the SOAR and DLP UI to look consistent, so substitute the buggy name when sending the JSON to DLP.
        update_json = {"incidentIds":[ incident_id ] }

        if incident_status_name:
            sdlp_status = "incident.status.New" if incident_status_name == "New" else incident_status_name
            incident_status_id = self.get_incident_status_index(sdlp_status)
            if incident_status_id <= 0:
                raise IntegrationError(f"Symantec DLP incident status name {incident_status_name} not found in DLP")
            update_json["incidentStatusId"] = incident_status_id

        if incident_severity:
            update_json["severity"] = incident_severity

        return self.rc.execute(
            "PATCH",
            f"{self.base_url}/incidents",
            headers=self.headers,
            json=update_json,
            verify=self.verify,
            proxies=self.proxies
        ).json()

    def get_custom_attribute_index(self, editable_attributes, custom_attribute_name: str):
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

    def patch_sdlp_incident_custom_attribute(self, incident_id: int, soar_case_id: int, soar_case_url: str):
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
        # Get the index of the custom attribute. When updating the attribute the columnIndex needs to be
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

        update_json = {
            "incidentIds":[incident_id],
            "incidentCustomAttributes": attributes_list
        }
        return self.rc.execute(
            "PATCH",
            f"{self.base_url}/incidents",
            headers=self.headers,
            json=update_json,
            verify=self.verify,
            proxies=self.proxies
        ).json()

    def upload_sdlp_binaries(self, sdlp_incident_id: int, soar_case_id: int, soar_rest_client, attachment_upload_type: str="artifact"):
        """upload_dlp_binaries takes an incident and a SOAR incident ID and then attempts to query DLP for any incident_binaries
        Any returning binaries are then sent to SOAR as an Artifact or an Attachment, retaining its name and extension type.
        """
        # Upload remaining parts such as the Attachments
        components = self.get_sdlp_components(sdlp_incident_id)
        LOG.debug(f"Symantec DLP incident: {sdlp_incident_id} Components: {components}")
        artifact_type_id = default_artifact_type_id

        artifact_name_list = []
        for component in components:
            if (component.get('messageComponentTypeName') and component.get('messageComponentTypeName') != 'Attachment')\
                or (component.get('componentType') and component.get('componentType') != 'Attachment'):
                continue
            component_id = component.get('componentId') or component.get('messageComponentId')
            component_data, error_msg = self.get_sdlp_component_data(sdlp_incident_id, component_id)
            LOG.debug(f"Component Data: {component_data}")
            if error_msg:
                # 404 not found error would fall through here if the attachment is not uploaded to the enforce server.
                LOG.info(error_msg)
                continue
            if component_data:
                try:
                    # Write the data to a file
                    path_tmp_file, path_tmp_dir = write_to_tmp_file(component_data)
                    LOG.debug(f"Temp file path: {path_tmp_file}")

                    # Post the file to SOAR incidents
                    binary_filepath = component.get("messageComponentName") or component.get('name')
                    # Check if specified to upload as a SOAR incident artifact file
                    if attachment_upload_type == "artifact":
                        soar_rest_client.post_artifact_file(uri=f"/incidents/{soar_case_id}/artifacts/files",
                            artifact_type=artifact_type_id,
                            artifact_filepath=path_tmp_file,
                            value=binary_filepath,
                            description=f"Binary File imported from Symantec DLP:\n {binary_filepath}")
                    else: # Upload as an SOAR incident attachment
                        soar_rest_client.post_attachment(uri=f"/incidents/{soar_case_id}/attachments",
                            filepath=path_tmp_file,
                            filename=binary_filepath)

                    artifact_name_list.append(binary_filepath)
                except Exception as upload_ex:
                    LOG.debug(traceback.format_exc())
                    # Log the Connection error to the user
                    LOG.error("Problem: %s", repr(upload_ex))
                    LOG.error("[Symantec DLP] Encountered an exception when uploading a Binary to SOAR.")

                finally:
                    # # Clean up the tmp file
                    if path_tmp_dir and os.path.isdir(path_tmp_dir):
                        shutil.rmtree(path_tmp_dir)
            else:
                LOG.info(f"Component with id: {component_id} did not return any data.")

        return artifact_name_list

    def get_sdlp_incident_payload(self, incident_id: int):
        """[ Create the incident payload for creating a SOAR case from DLP incident data. ]
        Args:
            incident_id ([integer]): [ DLP incident Id ]
        Returns:
            [json object]: [ payload containing information on the Symantec DLP incident ]
        """
        # Get the incident attributes
        sdlp_payload = {
            'notes': self.get_sdlp_incident_notes(incident_id),
            'editableIncidentDetails': self.get_sdlp_editable_attributes(incident_id),
            'staticIncidentDetails': self.get_sdlp_incident_static_attributes(incident_id),
            'sdlp_incident_url': self.get_sdlp_incident_url(incident_id)
        }
        LOG.debug(sdlp_payload)
        return sdlp_payload

    def get_sdlp_incident_editable_detail_payload(self, incident_id: int):
        """[ Create the incident payload for creating a SOAR case from DLP incident data. ]
        Args:
            incident_id ([integer]): [ DLP incident Id ]
        Returns:
            [json object]: [ payload containing information on the Symantec DLP incident ]
        """
        # Get the incident attributes
        return {'editableIncidentDetails': self.get_sdlp_editable_attributes(incident_id)}

    def update_sdlp_incident(self, sdlp_update_payload):
        """ Update (patch) the DLP incident
        Args:
            sdlp_update_payload (json): json payload of incident attributes to update
        Returns:
            _type_: _description_
        """
        return self.rc.execute(
            "PATCH",
            f"{self.base_url}/incidents",
            headers=self.headers,
            json=sdlp_update_payload,
            verify=self.verify,
            proxies=self.proxies
        ).json()

    def get_sdlp_incident_url(self, incident_id: int):
        """[ Formulate the Symantec DLP incident URL ]
        Args:
            incident_id ([type]): [DLP incidentId]
        Returns:
            [string]: [URL for DLP incident]
        """
        return f"https://{self.server}/ProtectManager/IncidentDetail.do?value(variable_1)=incident.id&value(operator_1)=incident.id_in&value(operand_1)={incident_id}"
