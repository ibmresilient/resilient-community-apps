# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

import logging
import resilient
from resilient import SimpleHTTPException
from resilient_lib import IntegrationError, write_file_attachment, write_to_tmp_file
from fn_harfanglab_edr.lib.constants import HARFANGLAB_ALERT_ID, FROM_HARFANGLAB_EDR_COMMENT_HDR, HARFANGLAB_AGENT_DATATABLE_NAME
import csv
import os
import shutil

LOG = logging.getLogger(__name__)


class ResilientCommon():

    def __init__(self, rest_client):
        self.rest_client = rest_client

    def find_incident(self, harfanglab_alert_id):
        """Find a Resilient incident which contains a custom field associated with a HarfangLab EDR Security event

        Args:
            harfanglab_alert_id ([str]): [HarfangLab security event id]

        Returns:
            [dict]: [API results of the first incident found]
        """
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = {
            'filters': [{
                'conditions': [
                    {
                        'field_name': f'properties.{HARFANGLAB_ALERT_ID}',
                        'method': 'equals',
                        'value': f'{harfanglab_alert_id}'
                    }
                ]
            }],
            "sorts": [{
                "field_name": "create_date",
                "type": "desc"
            }]
        }
        LOG.debug(query)

        try:
            r_incidents = self.rest_client.post(query_uri, query)
        except SimpleHTTPException as err:
            LOG.error(str(err))
            r_incidents = None

        return r_incidents[0] if r_incidents else None

    def create_incident(self, incident_payload):
        """
        Create a new Resilient incident by rendering a jinja2 template
        :param incident_payload: incident content (json object)

        :return: Resilient incident
        """
        try:
            # Post incident to Resilient
            incident = self.rest_client.post("/incidents", incident_payload)
            return incident
        except Exception as err:
            raise IntegrationError(str(err))

    def close_incident(self, incident_id, incident_payload):
        """Close an incident, applying a template for the required and optional fields needed
              during the close process

        Args:
            incident_id ([dict]): [Resilient incident id]
            incident_payload ([dict]): [HarfangLab EDR incident data]

        Raises:
            IntegrationError: [catch any errors]

        Returns:
            [dict]: [returned Resilient data]
        """

        try:
            result = self._patch_incident(incident_id, incident_payload)
            return result

        except Exception as err:
            raise IntegrationError(err)

    def update_incident(self, incident_id, incident_payload):
        """Update an incident

        Args:
            incident_id ([dict]): [Resilient incident id]
            incident_payload ([dict]): [HarfangLab EDR incident data]

        Raises:
            IntegrationError: [catch any errors]

        Returns:
            [dict]: [returned Resilient data]
        """

        try:
            result = self._patch_incident(incident_id, incident_payload)
            return result

        except Exception as err:
            raise IntegrationError(err)

    def _patch_incident(self, incident_id, incident_payload):
        """Patch an incident

        Args:
            incident_id ([dict]): [Resilient incident id]
            incident_payload ([dict]): [HarfangLab EDR incident data]

        Raises:
            IntegrationError: [catch any errors]

        Returns:
            [dict]: [returned Resilient data]
        """
        try:
            # Update incident
            incident_url = "/incidents/{0}".format(incident_id)
            incident = self.rest_client.get(incident_url)
            patch = resilient.Patch(incident)

            # Iterate over payload dict.
            for name, _ in incident_payload.items():
                if name == 'properties':
                    for field_name, field_value in incident_payload['properties'].items():
                        patch.add_value(field_name, field_value)
                else:
                    payload_value = incident_payload.get(name)
                    patch.add_value(name, payload_value)

            patch_result = self.rest_client.patch(incident_url, patch)
            result = self._chk_status(patch_result)
            # add back the incident id
            result['id'] = incident_id
            return result

        except Exception as err:
            raise IntegrationError(err)

    def create_incident_comment(self, incident_id, note):
        """
        Add a comment to the specified Resilient Incident by ID
        :param incident_id:  Resilient Incident ID
        :param note: Content to be added as note
        :return: Response from Resilient for debug
        """
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)
            comment = f'<b>{FROM_HARFANGLAB_EDR_COMMENT_HDR}:</b><br>{note}'

            note_json = {
                'format': 'html',
                'content': comment
            }
            payload = {'text': note_json}

            return self.rest_client.post(uri=uri, payload=payload)

        except Exception as err:
            raise IntegrationError(err)

    def get_incident_comments(self, incident_id):
        try:
            uri = u'/incidents/{0}/comments'.format(incident_id)

            comment_response = self.rest_client.get(uri=uri)
            return comment_response

        except Exception as err:
            raise IntegrationError(err)

    def add_agent_information(self, incident_id, row_payload):
        try:
            uri = u'/incidents/{0}/table_data/{1}/row_data'.format(
                incident_id, HARFANGLAB_AGENT_DATATABLE_NAME)

            return self.rest_client.post(uri=uri, payload=row_payload)

        except Exception as err:
            raise IntegrationError(err)

    def add_csv_file_to_incident_attachments(self, incident_id, filename, to_csv):

        if incident_id and to_csv and filename and len(to_csv) > 0:

            try:
                path_tmp_file, path_tmp_dir = write_to_tmp_file(
                    ''.encode(), filename)

                keys = to_csv[0].keys()

                with open(path_tmp_file, 'w', newline='') as output_file:
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(to_csv)

                with open(path_tmp_file, "rb") as data_stream:
                    res = write_file_attachment(
                        self.rest_client, filename, data_stream, incident_id)

            except Exception as e:
                raise Exception(f'Failed to write CSV: {str(e)}')

            finally:
                if path_tmp_dir and os.path.isdir(path_tmp_dir):
                    shutil.rmtree(path_tmp_dir)

    def _chk_status(self, resp, rc=200):
        """
        check the return status. If return code is not met, raise IntegrationError,
        if success, return the json payload
        :param resp:
        :param rc:
        :return:
        """
        if hasattr(resp, "status_code"):
            if isinstance(rc, list):
                if resp.status_code < rc[0] or resp.status_code > rc[1]:
                    raise IntegrationError(
                        u"status code failure: {0}".format(resp.status_code))
            elif resp.status_code != rc:
                raise IntegrationError(
                    u"status code failure: {0}".format(resp.status_code))

            return resp.json()

        return {}
