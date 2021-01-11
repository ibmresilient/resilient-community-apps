# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Findings poller class for AWS GuardDuty """
import logging
import pprint
import time
import datetime as dt
import copy
from fn_aws_guardduty.lib.aws_gd_cli_man import AwsGdCliMan
import fn_aws_guardduty.util.config as config
from fn_aws_guardduty.lib.helpers import FCrit, get_lastrun_unix_epoch, search_json
from fn_aws_guardduty.util import const
from fn_aws_guardduty.lib.resilient_service import ResSvc

LOG = logging.getLogger(__name__)
# Refresh region information interval in minutes
REGIONS_INTERVAL_DEFAULT = 60
# Multiplier to convert minutes to seconds.
WAIT_MULTIPLIER = 60


class AwsGdPoller():
    """Component that polls for new findings from AWS GuardDuty"""

    def __init__(self, opts, options, polling_interval):
        """constructor provides access to the configuration options"""
        self.opts = opts
        self.function_opts = options
        self.polling_interval = polling_interval
        # Amount of time (minutes) to wait to refresh regions information, use default if not set.
        self.regions_interval = int(self.function_opts.get("aws_gd_regions_interval", REGIONS_INTERVAL_DEFAULT))
        # GuardDuty severity threshold
        self.aws_gd_severity_threshold = int(self.function_opts.get("aws_gd_severity_threshold")) \
            if self.function_opts.get("aws_gd_severity_threshold") else None
        self.aws_gd_lookback_interval = int(self.function_opts.get("aws_gd_lookback_interval")) \
            if self.function_opts.get("aws_gd_lookback_interval") else None
        # Use last_update to ensure full list of findings returned only on initial run loop
        # Subsequently only return findings created/updated since last execution.
        self.last_update = None

    def run(self):
        """Run polling thread, alternately check for new data and wait"""
        # Get GuardDuty client.
        # Instantiate GuardDuty client manager object.
        aws_cli_man = AwsGdCliMan(self.opts, self.function_opts)
        # Instantiate Resilient helper service object.
        res_svc = ResSvc(self.opts, self.function_opts)

        while not config.STOP_THREAD:
            # Set criteria to filter findings results.
            f_criteria = self.set_criteria()
            # Loop over accessible GuardDuty regions and get available DetectorIds.
            for gd_region, gd_client_info in aws_cli_man.clients.items():
                aws_gd = gd_client_info["client"]
                detectors = gd_client_info["detectors"]

                if not detectors:
                    # No cached detector info see if any available detectors available for the specified AWS Region.
                    detectors = aws_gd.get("list_detectors")
                    if not detectors:
                        LOG.debug("No GuardDuty detectors found in region %s.", gd_region)
                        # Detectors still not detected skip detected.
                        continue


                # Get the DetectorId for the specified AWS Region.
                detectorid = detectors[0]

                # Get list of findings ids if any for DetectorId
                findings_list = aws_gd.get("list_findings", DetectorId=detectorid, FindingCriteria=f_criteria)

                if not findings_list:
                    LOG.debug("No GuardDuty findings found for detector ID %s  in region %s.", detectorid, gd_region)
                    continue

                LOG.debug("Getting GuardDuty findings found for detector ID %s  in region %s.",detectorid, gd_region)

                try:
                    ### BEGIN Processing findings
                    # Iterate over finding ids to get properties.
                    for fid in findings_list:

                        finding = aws_gd.get("get_findings", DetectorId=detectorid, FindingIds=[fid])[0]

                        if len(res_svc.find_resilient_incident_for_req(finding, ["Id", "Region"])) == 0:
                            LOG.info("AWS GuardDuty Finding ID %s in region %s discovered: %s, escalating to Resilient",
                                     finding["Id"], finding["Region"], finding.get("Title", "No Title Provided"))

                            # Add Incident Fields to incident payload.
                            i_payload = self.make_incident_fields(finding)

                            # Get any artifact data from finding.
                            artifact_data = self.get_artifact_data(finding)

                            # Add any artifacts from finding to incident payload.
                            if artifact_data:
                                i_payload = self.add_artifacts_to_payload(i_payload, artifact_data)

                            # Add finding json as a note to incident payload.
                            i_payload = self.add_note_to_payload(i_payload, finding)

                            # Assemble Data tables for incident
                            i_tables = self.build_data_tables(finding)

                            # Create incident and return response
                            i_response = res_svc.create_incident(i_payload)

                            if i_response is not None:
                                # Create data tables.
                                if i_tables:
                                    res_svc.add_datatables(i_response['id'], i_tables)
                        else:
                            LOG.info("Incident already exists for AWS GuardDuty Incident %d", finding["Id"])

                except TypeError as ex:
                    LOG.error(ex)

            # Break out of loop before sleep if stop thread flag set.
            if config.STOP_THREAD:
                break

            # Amount of time (seconds) * WAIT_MULTIPLIER to wait to check cases again.
            time.sleep(int(self.polling_interval) * WAIT_MULTIPLIER)

            # Refresh clients info if time since refresh > refresh interval. This is to ensure we have
            # latest detector ids for the regions.
            now = dt.datetime.now()
            if (now - aws_cli_man.timestamp).total_seconds() > (self.regions_interval * WAIT_MULTIPLIER):
                aws_cli_man.refresh_clients()


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
        for prop_l1 in const.CUSTOM_FIELDS_MAP:
            if isinstance(const.CUSTOM_FIELDS_MAP[prop_l1], dict):
                for prop_l2 in const.CUSTOM_FIELDS_MAP[prop_l1]:
                    r_fields["properties"][const.CUSTOM_FIELDS_MAP[prop_l1][prop_l2]] = \
                        finding.get(prop_l1, {}).get(prop_l2)
            else:
                r_fields["properties"][const.CUSTOM_FIELDS_MAP[prop_l1]] = finding.get(prop_l1)

        return r_fields

    def make_incident_name(self, finding):
        """
        Create Resilient Incident name from finding.

        :param finding: Finding Payload from Poller
        :return iname: String for Incident Name to be used in Search / Incident Creation
        """
        # Fill event summary when blank
        i_title = finding.get("Title", "No Title Provided.") or "No Title Provided."

        iname = "AWS GuardDuty: {}".format(i_title)
        LOG.debug("Incident Label Assembled: %s", iname)

        return iname

    def make_incident_description(self, finding):
        """
        Make Incident description text from GuardDuty finding description.

        :param finding: Raw GuardDuty Payload
        :return: Return formatted Description for Incident DTO
        """
        i_desc = finding.get("Description", "AWS GuardDuty finding --") or "AWS GuardDuty finding --"
        return {"format": "text", "content": i_desc}

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

        if not isinstance(finding_severity, (int, float)) or not 1.0 <= finding_severity <= 8.9:
            raise ValueError("Incorrect value '{}' set for severity level.".format(finding_severity))
        if 1.0 <= finding_severity <= 3.9:
            resilient_severity = "Low"
        elif 4.0 <= finding_severity <= 6.9:
            resilient_severity = "Medium"
        elif 7.0 <= finding_severity <= 8.9:
            resilient_severity = "High"

        return resilient_severity

    def set_criteria(self):
        """
        Create criteria to filter findings data from GuardDuty.

        :return fc: Return criterion dict
        """
        f_criteria = FCrit()
        # Add severity criterion if setting enabled.
        if self.aws_gd_severity_threshold:
            f_criteria.set_severity(self.aws_gd_severity_threshold)
        if self.aws_gd_lookback_interval:
            # Set criteria for findings updated since lookback interval.
            f_criteria.set_update(get_lastrun_unix_epoch(self.aws_gd_lookback_interval))
        else:
            if self.last_update:
                # Set criteria for findings updated since last run through loop.
                f_criteria.set_update(get_lastrun_unix_epoch(self.last_update))
            else:
                # First run no criterion set for updates, fetch all may take a long time.
                LOG.info("First Run in progress - this may take a while.")
            self.last_update = dt.datetime.now()

        return f_criteria

    def get_artifact_data(self, finding):
        """
        Add artifact types and values to an artifacts_data payload.

        Example payload entry:
            {'10.0.0.1':
                ('IP Address', 'PrivateIpAddress', '["Resource"]["InstanceDetails"]["NetworkInterfaces"]["0"]')
            }
        :param finding: The finding json content to seach for artifacts.
        :return artifact_data: Dict of artifacts data.
        """
        artifact_data = {}
        for artifact_type, gd_keys in const.ARTIFACT_TYPES_MAP.items():
            for gd_key in gd_keys:
                for (artifact_value, path) in search_json(finding, gd_key):
                    LOG.debug(u'artifact type %s (%s) ID %s, at path %s',artifact_type, gd_key, artifact_value, path)
                    if artifact_value in artifact_data:
                        # Artifact value aleady found skip.
                        continue
                    artifact_data[artifact_value] = (artifact_type, gd_key, path)



        return artifact_data

    def add_artifacts_to_payload(self, i_payload, artifact_data):
        """Add artifacts to Resilient Incident payload.

        :param i_payload: Incident payload.
        :param artifact_data: Artifact data from finding.
        """
        i_payload["artifacts"] = []

        # Set up Artifact payload skeleton.
        artifact_payload = {
            'type': {
                'name': 'String',
            },
            'description': {
                'format': 'text',
            }
        }


        # Loop through Artifact data provided with the finding.
        for artifact_value, (artifact_type, gd_key, path) in artifact_data.items():
            # Populate payload with ID and type and description.
            artifact = copy.deepcopy(artifact_payload)
            desc = "'{}' extracted from GuardDuty from finding property '{}' at path '{}'." \
                .format(artifact_type, gd_key, path)
            artifact['value'] = artifact_value
            artifact['type']['name'] = const.ARTIFACT_TYPE_API_NAME.get(artifact_type, "String")
            artifact['description']['content'] = desc
            i_payload["artifacts"].append(artifact)

        return i_payload

    def add_note_to_payload(self, i_payload, finding):
        """
        Add a comment/note to the specified Resilient Incident payload.

        :param i_payload: Incident payload.
        :param finding: Raw GuardDuty json to be added as a Resilient incident note.
        """
        i_payload["comments"] = []
        heading = "AWS GuardDuty finding Payload:\n"

        note = {
            'format': 'text',
            'content': '{}{}'.format(heading, pprint.pformat(finding, indent=4))
        }

        i_payload["comments"].append({'text': note})

        return i_payload

    def build_data_tables(self, finding):
        """
        Assemble the Data Table for an incident from a GuardDuty finding json payload

        :param finding: GuardDuty finding data from query.
        :return  Returns assembled LIST of DICTs by Resilient data table ID with Data Table column names and values.

        Example Format of returned data including Resilient POST data:

            {
              "gd_action_details":[
                {
                  "cells":{
                    "action_type":{
                      "value":"NETWORK_CONNECTION"
                    },
                    "protocol":{
                      "value":"TCP"
                    },
                    ...
                    ...
                  }
                }
              ],
              "gd_resource_affected":[
                {
                  "cells":{
                    "resource_type":{
                      "value":"Instance"
                    },
                    "instance_id":{
                      "value":"i-99999999"
                    },
                    ...
                    ...
                  }
                }
              ]
            }

        """
        data_tables = {}
        for table_id in const.DATA_TABLE_IDS:
            data_table = []
            table_row = {}
            for section in const.DATA_TABLE_FIELDS_MAP[table_id]:
                path = section["path"]
                for key, val in section["fields"].items():
                    table_copy = data_table[:]
                    value = None
                    # Search for key at path.
                    search_json(finding, key, path=path)
                    result = search_json(finding, key, path=path)
                    if result:
                        if isinstance(result, dict) and result.get("msg"):
                            LOG.debug("%s for finding data %s.", result.get("msg"),
                                      result.get("path"))
                        elif isinstance(result, list):
                            (value, _) = result.pop()
                            # Convert boolean values to string 'True' or 'False'
                            if isinstance(value, bool):
                                value = "{}".format(value)
                            table_row[val] = {"value" : value}
                    table_copy.append({"cells" : table_row})

            data_table = table_copy

            LOG.info("Data Table Assembled with %d rows for table id '%s'.", len(data_table), table_id)

            data_tables.update({table_id : data_table})

            LOG.debug(pprint.pformat(data_table, indent=4))

        return data_tables
