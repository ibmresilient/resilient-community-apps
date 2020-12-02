# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Findings poller for AWS GuardDuty """

import logging
import time

from fn_aws_guardduty.lib.aws_gd_client import AwsGdClient
from resilient import SimpleHTTPException
import fn_aws_guardduty.util.config as config


LOG = logging.getLogger(__name__)
# Map GuardDuty finding fields to Resilient Incident custom fields.
CUSTOM_FIELDS_MAP = {
    "Id": "aws_guardduty_finding_id",
    "Arn": "aws_guardduty_finding_arn",
    "Type": "aws_guardduty_finding_type",
    "Region": "aws_guardduty_region",
    "Resource": {
        "ResourceType": "aws_guardduty_resource_type"
    },
    "Service": {
        "DetectorId": "aws_guardduty_detector_id",
    }
}
# Multiplier to convert minutes to seconds.
WAIT_MULTIPLIER = 60

class AwsGdPoller():
    """Component that polls for new findings from AWS GuardDuty"""

    def __init__(self, opts, options, rest_client, polling_interval):
        """constructor provides access to the configuration options"""
        self.opts = opts
        self.function_opts = options
        self.rest_client = rest_client
        self.polling_interval = polling_interval

    def run(self):
        """Run polling thread, alternately check for new data and wait"""
        # Get GuardDuty client.

        aws_gd = AwsGdClient(self.opts, self.function_opts)

        # Get the DetectorId for the specified AWS Region.
        detector = aws_gd.get("list_detectors")
        if detector:
            detectorid = detector[0]

        while not config.STOP_THREAD:
            # Get list of findings ids if any for DetectorId
            findings_list = aws_gd.get("list_findings", DetectorId=detectorid)

            if not findings_list:
                LOG.info("No findings found for detector ID  %s.", detectorid)
            else:
                try:
                    ### BEGIN Processing findings
                    # Iterate over finding ids to get properties.
                    for fid in findings_list:
                        finding = aws_gd.get("get_findings", DetectorId=detectorid, FindingIds=[fid])[0]
                        LOG.info("AWS GuardDuty Finding ID %s in region %s discovered: %s", finding["Id"],
                                 finding["Region"], finding.get("Title", "No Title Provided"))
                        if len(self._find_resilient_incident_for_req(finding["Id"], CUSTOM_FIELDS_MAP["Id"])) == 0:

                            # Get Extra Incident Fields
                            i_fields = self.make_incident_fields(finding)

                            # Create incident and return response
                            i_response = self.create_incident(i_fields)

                        else:
                            LOG.info("Incident already exists for AWS GuardDuty Incident %d", finding["Id"])

                except TypeError as ex:
                    LOG.error(ex)

            # Break out of loop before sleep if stop thread flag set.
            if config.STOP_THREAD:
                break
            # Use a timeout value of polling_interval (in secs) * WAIT_MULTIPLIER + TIMEOUT_WAIT secs to wait for
            # all threads to end.
            # Amount of time (seconds) * WAIT_MULTIPLIER to wait to check cases again.
            time.sleep(int(self.polling_interval) * WAIT_MULTIPLIER)


    def make_incident_name(self, finding):
        """
        Create Resilient Incident name from finding.

        :param finding: Finding Payload from Poller
        :return iname: String for Incident Name to be used in Search / Incident Creation
        """
        # Fill event summary when blank
        i_title = finding.get("Title", "No Title Provided")

        iname = "AWS GuardDuty: {}".format(i_title)
        LOG.debug("Incident Label Assembled: %s", iname)

        return iname


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


    def make_incident_fields(self, finding):
        """
        Assemble the Incident DTO Payload / Fields from GuardDuty finding Payload.

        :param finding: Finding payload from GuardDuty.
        :return: Incident DTO payload
        """
        # Create Placeholder with lists as values
        r_fields = {
            "name": self.make_incident_name(finding),
            "description": self.make_incident_description(finding),
            "discovered_date": finding.get("CreatedAt"),
            "severity_code": self.map_severity(finding.get("Severity", "Low")),
            "properties": {},
        }
        # Use mapping to get incident field values from finding payload.
        for prop_l1 in CUSTOM_FIELDS_MAP:
            if isinstance(CUSTOM_FIELDS_MAP[prop_l1], dict):
                for prop_l2 in CUSTOM_FIELDS_MAP[prop_l1]:
                    r_fields["properties"][CUSTOM_FIELDS_MAP[prop_l1][prop_l2]] = finding.get(prop_l1, {}).get(prop_l2)
            else:
                r_fields["properties"][CUSTOM_FIELDS_MAP[prop_l1]] = finding.get(prop_l1)

        return r_fields


    def make_incident_description(self, finding):
        """
        Make Incident description text from GuardDuty finding description.

        :param finding: Raw GuardDuty Payload
        :return: Return formatted Description for Incident DTO
        """
        i_desc = finding.get("Description", "AWS GuardDuty Incident - Lacks a description")
        return {"format": "text", "content": i_desc}


    def _find_resilient_incident_for_req(self, finding_id, idtype):
        """
        Check if any Resilient incidents with the GuardDuty finding ID.

        :param finding_id: GuardDuty finding id
        :return: Return list of incidents with finding id set
        """
        r_incidents = []
        query_uri = "/incidents/query?return_level=partial"
        query = {
            "filters": [{
                "conditions": [
                    {
                        "field_name": "properties.{}".format(idtype),
                        "method": "equals",
                        "value": finding_id
                    },
                    {
                        "field_name": "plan_status",
                        "method": "equals",
                        "value": 'A'
                    }
                ]
            }],
            "sorts": [{
                "field_name": "create_date",
                "type": "desc"
            }]
        }
        try:
            r_incidents = self.rest_client().post(query_uri, query)
        except SimpleHTTPException:
            # Some versions of Resilient 30.2 onward have a bug that prevents query for numeric fields.
            # To work around this issue, let's try a different query, and filter the results. (Expensive!)
            query_uri = "/incidents/query?return_level=normal&field_handle={}".format(finding_id)
            query = {
                "filters": [{
                    "conditions": [
                        {
                            "field_name": "properties.{}".format(idtype),
                            "method": "has_a_value"
                        },
                        {
                            "field_name": "plan_status",
                            "method": "equals",
                            "value": 'A'
                        }
                    ]
                }]
            }

            try:
                r_incidents_tmp = self.rest_client().post(query_uri, query)

            except Exception as err:
                raise Exception("Exception '{}' while trying to get list of Resilient incidents.".format(err)) from err

            r_incidents = [r_inc for r_inc in r_incidents_tmp
                           if r_inc["properties"].get(idtype) == finding_id]

        return r_incidents


    def map_severity(self, finding_severity):
        """
        Map GuardDuty finding severity to Resilient Severity.

        In GuardDuty the value of the severity can fall anywhere within the 1.0 to 8.9 range.
            High 7.0 - 8.9 -> High
            4.0 - 6.9 -> Medium
            1.0 = 3.9 -> Low

        :param finding_severity: GuardDuty finding severity
        :return resilient_severity: Resilient severity string
        """
        resilient_severity = None
        if 1.0 <= finding_severity <= 3.9:
            resilient_severity = "Low"
        elif 4.0 <= finding_severity <= 6.9:
            resilient_severity = "Medium"
        elif 7.0 <= finding_severity <= 8.9:
            resilient_severity = "High"
        return resilient_severity
