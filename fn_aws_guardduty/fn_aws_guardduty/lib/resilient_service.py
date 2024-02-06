# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Functions accessing Resilient """
import logging
import re

import resilient
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

    def find_resilient_incident_for_req(self, finding, region, f_fields):
        """
        Check if any Resilient incidents with the GuardDuty finding ID.

        :param finding: GuardDuty finding payload.
        :param region: The GuardDuty region with the finding.
        :param f_fields: The GuardDuty finding fields used to query Resilient.
        :return: Return list of incidents with finding id set
        """
        r_incidents = []
        query_uri = "/incidents/query?return_level=normal"
        # Create query.
        query = IQuery()
        # Add conditions for fields.
        query.add_conditions(gd_obj=finding, fields=f_fields)
        # Add condition for region.
        query.add_conditions(gd_obj=region, fields="Region")
        try:
            r_incidents = self.rest_client().post(query_uri, query)
        except SimpleHTTPException:
            # Some versions of Resilient 30.2 onward have a bug that prevents query for numeric fields.
            # To work around this issue, let's try a different query, and filter the results. (Expensive!)
            query_uri = "/incidents/query?return_level=normal&field_handle={}".format(finding["Id"])
            # Add condition for 'region' to f_fields.
            f_fields.append("Region")
            # Create query.
            query = IQuery()
            # Add alt conditions for fields.
            query.add_alt_conditions(fields=f_fields)
            try:
                r_incidents_tmp = self.rest_client().post(query_uri, query)

            except Exception as err:
                raise Exception("Exception '{}' while trying to get list of Resilient incidents.".format(err))

            r_incidents = [r_inc for r_inc in r_incidents_tmp
                           if r_inc["properties"].get(const.CUSTOM_FIELDS_MAP["Id"]) == finding["Id"]]

        return r_incidents

    def create_incident(self, data):
        """
        Create Resilient Incident.

        :param data: Formatted DTO for Incident
        :return: Return response from Resilient
        """
        LOG.info("Creating incident.")
        try:
            resilient_client = self.rest_client()

            uri = "/incidents"
            # create Incident itself first
            incident_response = resilient_client.post(uri=uri, payload=data)

            return incident_response

        except SimpleHTTPException as ex:
            LOG.error("Something went wrong when attempting to create the Incident: %s", ex)

    def add_datatables(self, incident_id, tables):
        """Add data tables to Resilient Incident.

        :param incident_id: Incident ID from incident creation.
        :param tables: Data table data.
        """
        LOG.info("Creating data tables.")
        try:
            resilient_client = self.rest_client()

            for table_id, contents in tables.items():
                # Loop though Resilient table ids and related data table content.
                if contents:
                    if table_id in const.DATA_TABLE_IDS:
                        # Table data, add row to specified data table
                        uri = '/incidents/{0}/table_data/{1}/row_data'.format(incident_id, table_id)
                        LOG.debug("Attempting to create table with the following: %s", uri)

                        for content in contents:
                            resilient_client.post(uri=uri, payload=content)

        except SimpleHTTPException as ex:
            LOG.error('Something went wrong when attempting to create the Incident: %s', ex)

    def find_resilient_artifacts_for_incident(self, incident_id):
        """Return list of existing artifacts for a Resilient Incident ID.

        :param incident_id: Incident ID from incident creation.
        :return: Return dict of artifacts with key=artifact value, value=artifact type.
        """
        r_artifacts = {}
        artifact_types = list(const.ARTIFACT_TYPES_MAP.keys())
        resilient_client = self.rest_client()
        artifacts_uri = '/incidents/{}/artifacts'.format(incident_id)
        artifact_results = resilient_client.get(uri=artifacts_uri)

        if artifact_results is not None:
            for artifact_result in artifact_results:
                artifact_desc = artifact_result.get('description')
                # Match artifact type at beginning of description e.g. artifact_desc = "\'IP Address\' ... "
                artifact_type = next((t for t in artifact_types if re.match("\'"+t+"\'", artifact_desc)), None)
                if artifact_type:
                    r_artifacts[artifact_result['value']] = artifact_type

        return r_artifacts

    def add_comment(self, incident_id, note):
        """
        Add a comment to the specified Resilient Incident by ID

        :param incident_id:  Incident ID from incident creation.
        :param note: Content to be added as a note.
        """
        try:
            uri = '/incidents/{}/comments'.format(incident_id)
            resilient_client = self.rest_client()

            comment_response = resilient_client.post(uri=uri, payload=note)

            return comment_response

        except SimpleHTTPException as ex:
            LOG.error("Failed to add note for incident %d: %s", incident_id, ex)

    def page_incidents(self, region=None, f_fields=None):
        """
        Get paged list of Resilinet incidents using a filter to filter incidents returned.

        :param region: GuardDuty region
        :param f_fields: List of fields to use in the query filter.
        :return: Yield matching incident payload dicts.
        """
        query_uri = "/incidents/query_paged?return_level=normal"
        query = IQuery(paged=True)
        # Add query for region.
        query.add_conditions(region, "Region")
        query.add_alt_conditions(f_fields)
        try:
            paged_results = self.rest_client().post(query_uri, query)

            while paged_results.get('data'):
                data = paged_results.get('data')

                for result in data:
                    yield result

                query["start"] = len(data) + query["start"]

                paged_results = self.rest_client().post(query_uri, query)

        except Exception as err:
            LOG.error("Got Exception '%s' while trying to get list of Resilient incidents.", err)
            raise Exception(err)

    def update_incident_properties(self, incident_id, fields):
        """ Update Resilient incident custom property or fields.

        :param incident_id: Incident ID.
        :param fields: Property fields to be updates.
        :return: response object
        """
        try:
            response = None
            resilient_client = self.rest_client()
            uri = "/incidents/{}".format(incident_id)

            previous_object = resilient_client.get(uri)
            patch = resilient.Patch(previous_object)

            properties = fields.get("properties")

            if properties:
                for field in properties:
                    if field not in previous_object["properties"]:
                        raise ValueError("Invalid property parameter {}".format(field))

                    patch.changes[field] = \
                        resilient.patch.Change(field, properties[field], previous_object["properties"][field])
            else:
                for field in fields:
                    patch.add_value(field, fields[field])

            response = resilient_client.patch(uri, patch)

        except SimpleHTTPException as ex:
            LOG.error('Something went wrong when attempting to patch the Incident: %s', ex)

        return response
