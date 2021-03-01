# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Findings poller class for AWS GuardDuty """
import logging
import os
import time
import datetime as dt
from resilient import SimpleHTTPException
from resilient_lib import close_incident
from fn_aws_guardduty.lib.aws_gd_cli_man import AwsGdCliMan
import fn_aws_guardduty.util.config as config
from fn_aws_guardduty.util import const
from fn_aws_guardduty.lib.helpers import FCrit, get_lastrun_unix_epoch, load_template
from fn_aws_guardduty.lib.resilient_service import ResSvc
from fn_aws_guardduty.lib.parse_finding import ParseFinding

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
        self.close_incident_template = self.function_opts.get("aws_gd_close_incident_template")
        if self.close_incident_template and not os.path.isfile(self.close_incident_template):
            LOG.error("User defined JSON template %s not accessible.", self.close_incident_template)
            raise IOError("User defined JSON template {} not accessible.".format(self.close_incident_template))

        # Use last_update to ensure full list of findings returned only on initial run loop
        # Subsequently only return findings created/updated since last execution.
        self.last_update = None
        # Use initial_lookback if new region added and aws_gd_lookback_interval specified.
        self.initial_lookback = None

    def run(self):
        """Run polling thread, alternately check for new data and wait"""
        # Get GuardDuty client.
        # Instantiate GuardDuty client manager object.
        aws_cli_man = AwsGdCliMan(self.opts, self.function_opts)
        # Instantiate Resilient helper service object.
        res_svc = ResSvc(self.opts, self.function_opts)

        while not config.STOP_THREAD:
            LOG.info("Polling GuardDuty for new and updated findings.")
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

                LOG.info("Polling for region - %s.", gd_region)

                # Get the DetectorId for the specified AWS Region.
                detectorid = detectors[0]
                criteria = f_criteria
                if gd_client_info.get("is_new", False):
                    criteria = self.set_criteria(new_region=True)
                    del gd_client_info["is_new"]
                # Get list of findings ids if any for DetectorId
                findings_list = aws_gd.get("list_findings", DetectorId=detectorid, FindingCriteria=criteria)

                if not findings_list:
                    LOG.debug("No GuardDuty finding updates found for detector ID %s  in region %s.", detectorid, gd_region)
                    #continue
                else:
                    LOG.debug("Processing GuardDuty finding updates for detector ID %s  in region %s.",detectorid, gd_region)

                    try:
                        ### BEGIN Processing findings
                        # Iterate over finding ids to get properties.
                        for fid in findings_list:
                            finding_data = aws_gd.get("get_findings", DetectorId=detectorid, FindingIds=[fid])

                            if not isinstance(finding_data, list):
                                LOG.error("Got unexpected result when attempting to retrieve details for AWS GuardDuty "
                                          "finding ID %s.", fid)
                                continue

                            if not finding_data:
                                LOG.error("Unable to retrieve details for AWS GuardDuty finding ID %s.", fid)
                                continue

                            finding = finding_data[0]

                            incident_for_req = \
                                res_svc.find_resilient_incident_for_req(finding, gd_region, ["Id", "DetectorId"])

                            num_incidents = len(incident_for_req)

                            if num_incidents == 0:
                                # No corresponding Resilient incident exists.
                                LOG.info("AWS GuardDuty Finding ID '%s' of type '%s' in region '%s' discovered: '%s',",
                                         finding["Id"], finding["Type"], finding["Region"],
                                         finding.get("Title", "No Title Provided"))
                                LOG.info("Escalating finding to Resilient.")
                                # Instantiate object to generate Resilient incident payload and data tables from finding.
                                finding_payload = ParseFinding(finding, gd_region)

                                # Create incident and return response
                                i_response = res_svc.create_incident(finding_payload.payload)

                                if i_response:
                                    LOG.info("Incident '{}' successfully created for finding '{}' in region '{}'."
                                             .format(i_response['id'], finding["Id"], gd_region))
                                    # Create data tables.
                                    if finding_payload.data_tables:
                                        res_svc.add_datatables(i_response['id'], finding_payload.data_tables)

                            elif num_incidents == 1:
                                if incident_for_req[0]["properties"][const.CUSTOM_FIELDS_MAP["UpdatedAt"]] \
                                    != finding["UpdatedAt"]:
                                    # GuardDuty finding updated but corresponding incident not yet refreshed
                                    # trigger update rule on resilient.
                                    LOG.info("New updates detected for existing AWS GuardDuty incident %d.", finding["Id"])
                                    incident_id = incident_for_req[0]["id"]
                                    fields = {
                                        "properties": {
                                            "aws_guardduty_trigger_refresh": True
                                        }
                                    }
                                    res_svc.update_incident_properties(incident_id, fields)
                                    # Reset flag to False.
                                    fields = {
                                        "properties": {
                                            "aws_guardduty_trigger_refresh": False
                                        }
                                    }
                                    res_svc.update_incident_properties(incident_id, fields)
                                else:
                                    LOG.info("Incident already exists for AWS GuardDuty finding ID %d and is up to date",
                                             finding["Id"])
                            elif num_incidents > 1:
                                LOG.error("Something went wrong, there are %s open Resilient Incidents matching AWS "
                                          "GuardDuty finding ID %s.", num_incidents, finding["Id"])

                    except TypeError as ex:
                        LOG.error(ex)

                # Resolve archived finding with still opened Resilient incident.
                self.resolve_archived_findings(res_svc, aws_gd, gd_region, detectorid)

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

    def set_criteria(self, new_region=False):
        """
        Create criteria to filter findings data from GuardDuty.

        :param new_region: Optional boolean if new regions accessible..
        :return fc: Return criterion dict
        """
        f_criteria = FCrit()
        # Only return current findings omit archived findings.
        f_criteria.set_archived(value="false")
        # Add severity criterion if setting enabled.
        if self.aws_gd_severity_threshold:
            f_criteria.set_severity(self.aws_gd_severity_threshold)

        if new_region:
            if self.initial_lookback:
                # Set criteria for findings from inital lookback interval.
                f_criteria.set_update(self.initial_lookback)
            LOG.info("First Run for a new client in progress - this may take a while.")
        elif self.last_update:
            # Set criteria for findings updated since last run through loop.
            f_criteria.set_update(get_lastrun_unix_epoch(self.last_update))
        elif self.aws_gd_lookback_interval:
            # Set criteria for previous findings in lookback interval epoch value.
            self.initial_lookback = get_lastrun_unix_epoch(self.aws_gd_lookback_interval)
            f_criteria.set_update(self.initial_lookback)
        else:
            # First run no criterion set for updates, fetch all may take a long time.
            LOG.info("First Run in progress - this may take a while.")

        self.last_update = dt.datetime.now()

        return f_criteria

    def resolve_archived_findings(self, res_svc, aws_gd, region, detectorid):
        """
        Close open Resilient incidents if the corresponing finding has been archived in GuardDuty.
        :param res_svc: Resilient helper service object.
        :param aws_gd: GuardDuty client object for region 'region'.
        :param region: GuardDuty region.
        :param detectorid: GuardDuty detector id.
        """
        # Get open Resilient incidents in region as dict of finding id keys and resilient id values.
        res_open_findings = {inc["properties"]["aws_guardduty_finding_id"]:inc["id"]
                             for inc in res_svc.page_incidents(region=region, f_fields=["Id", "DetectorId"])}

        # Set filter to return only current (non-archived) findings.
        f_criteria = FCrit()
        f_criteria.set_archived(value="false")

        # Get a list of current finding ids.
        gd_open_findings = aws_gd.get("list_findings", DetectorId=detectorid, FindingCriteria=f_criteria)

        # Determine finding ids from Resilient open incidents list not in GuardDuty current incident list.
        fid_diff = list(set(res_open_findings.keys()).difference(gd_open_findings))
        for fid in fid_diff:
            incident_id = res_open_findings[fid]
            # Retrieve finding details and check if it has been archived.
            finding_data = aws_gd.get("get_findings", DetectorId=detectorid, FindingIds=[fid])
            if not isinstance(finding_data, list):
                LOG.error("Got unexpected result when attempting to retrieve details for AWS GuardDuty finding ID %s.",
                          fid)
                continue

            if not finding_data:
                LOG.error("Unable to retrieve details for AWS GuardDuty finding ID %s which has a corresponding "
                          "Resilient incident with ID %d.", fid, incident_id)
                continue

            finding = finding_data[0]

            if isinstance(finding["Service"]["Archived"], bool) and finding["Service"]["Archived"]:
                # Finding is archived, close corresponding Resilient incident.
                incident_close_status = load_template(const.CLOSE_INCIDENT_TEMPLATE, self.close_incident_template)
                LOG.info("Closing incident %d for archived finding %s.", incident_id, fid)
                # Reset 'aws_guardduty_archived' property to 'True' to prevent triggering of automatic rule.

                fields = {
                    "properties": {
                        "aws_guardduty_archived": "True"
                    }
                }
                res_svc.update_incident_properties(incident_id, fields)
                try:
                    close_incident(res_svc.rest_client(), incident_id, incident_close_status)
                except Exception as ex:
                    LOG.error('Something went wrong when attempting to close the Incident: %s', ex)
