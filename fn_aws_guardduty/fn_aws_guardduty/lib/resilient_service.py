# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Functions accessing Resilient """
import logging

from resilient_circuits import ResilientComponent
from resilient import SimpleHTTPException
from fn_aws_guardduty.lib.helpers import IQuery
from fn_aws_guardduty.util import const

LOG = logging.getLogger(__name__)


class ResSvc(ResilientComponent):
    """
    Resilient Rest helper service.
    """

    def __init__(self, opts, options):
        super(ResSvc, self).__init__(opts)
        self.opts = opts
        self.options = options

    def _find_resilient_artifacts_for_incident(self, incident_id):
        """
        Return list of artifacts for the given Incident ID.

        :param incident_id: Resilient incident id
        :return r_artifacts: Return list of artifacts or empty list.
        """
        r_artifacts = {}
        resilient_client = self.rest_client()
        artifacts_uri = '/incidents/{}/artifacts'.format(incident_id)
        a_response = resilient_client.get(uri=artifacts_uri)

        if a_response is not None:
            for artifact_result in a_response:
                artifact_type = artifact_result.get('description')
                if artifact_type in const.ARTIFACT_TYPES_MAP:
                    r_artifacts[artifact_result['value']] = artifact_type

        return r_artifacts

    def find_resilient_incident_for_req(self, finding, f_fields):
        """
        Check if any Resilient incidents with the GuardDuty finding ID.

        :param finding_id: GuardDuty finding id
        :return: Return list of incidents with finding id set
        """
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = IQuery(finding, f_fields)
        try:
            r_incidents = self.rest_client().post(query_uri, query)
        except SimpleHTTPException:
            # Some versions of Resilient 30.2 onward have a bug that prevents query for numeric fields.
            # To work around this issue, let's try a different query, and filter the results. (Expensive!)
            query_uri = "/incidents/query?return_level=normal&field_handle={}".format(finding["Id"])
            query = IQuery(finding, f_fields, alt=True)

            try:
                r_incidents_tmp = self.rest_client().post(query_uri, query)

            except Exception as err:
                raise Exception("Exception '{}' while trying to get list of Resilient incidents.".format(err))

            r_incidents = [r_inc for r_inc in r_incidents_tmp
                           for f in f_fields if r_inc["properties"].get(f) == finding[f]]

        return r_incidents

    def create_incident(self, data):
        """
        Create Resilient Incident.

        :param data: Formatted DTO for Incident
        :return: Return response from Resilient
        """
        try:
            resilient_client = self.rest_client()

            uri = "/incidents"
            # create Incident itself first
            incident_response = resilient_client.post(uri=uri, payload=data)

            return incident_response

        except SimpleHTTPException as ex:
            LOG.error("Something went wrong when attempting to create the Incident: %s", ex)

    def create_artifacts(self, incident_id, artifacts):
        """Create artifacts for Resilient Incident

        :param incident_id: Incident ID from incident creation.
        :param artifacts: Artifact payload data.
        """
        try:
            resilient_client = self.rest_client()
            artifact_uri = '/incidents/{}/artifacts'.format(incident_id)

            # set up Artifact payload skeleton
            artifact_payload = {
                'type': {
                    'name': 'String',
                },
                'description': {
                    'format': 'text',
                }
            }

            # find artifacts that are already associated with this Incident
            existing_artifacts = self._find_resilient_artifacts_for_incident(incident_id)

            # loop through Artifacts provided with this Threat
            for artifact_id, (artifact_type, gd_key, path) in artifacts.items():
                # if this Artifact doesn't match an existing value and type
                if artifact_id not in existing_artifacts or existing_artifacts[artifact_id] != artifact_type:
                    # populate payload with ID and type
                    desc = "'{}' extracted from GuardDuty from finding property '{}' at path '{}'."\
                        .format(artifact_type, gd_key, path)
                    artifact_payload['value'] = artifact_id
                    artifact_payload['type']['name'] = const.ARTIFACT_TYPE_API_NAME.get(artifact_type, "String")
                    artifact_payload['description']['content'] = desc
                    # attach new Artifact to Incident
                    resilient_client.post(uri=artifact_uri, payload=artifact_payload)

        except SimpleHTTPException as ex:
            LOG.info(u'Something went wrong when attempting to update the Incident: {}'.format(ex))
            raise ex

    def add_datatables(self, incident_id, tables):
        """Add data tables to incident Resilient Incident.

        :param incident_id: Incident ID from incident creation.
        :param tables: Data table data.
        """
        try:
            resilient_client = self.rest_client()

            for table_id, contents in tables.items():
                if contents:
                    if table_id in const.DATA_TABLE_IDS:
                        # Table data, add row to specified data table
                        uri = '/incidents/{0}/table_data/{1}/row_data'.format(incident_id, table_id)
                        LOG.info("Attempting to create table with the following: %s", uri)

                        for content in contents:
                            resilient_client.post(uri=uri, payload=content)

        except SimpleHTTPException as ex:
            LOG.error('Something went wrong when attempting to create the Incident: %s', ex)
