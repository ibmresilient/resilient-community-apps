# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Findings poller class for AWS GuardDuty """
import logging
import time
import datetime as dt
from fn_aws_guardduty.lib.aws_gd_cli_man import AwsGdCliMan
import fn_aws_guardduty.util.config as config
from fn_aws_guardduty.lib.helpers import FCrit, get_lastrun_unix_epoch
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

                        if len(res_svc.find_resilient_incident_for_req(finding, gd_region, ["Id", "DetectorId"])) == 0:
                            LOG.info("AWS GuardDuty Finding ID %s in region %s discovered: %s, escalating to Resilient",
                                     finding["Id"], finding["Region"], finding.get("Title", "No Title Provided"))

                            # Instantiate object to generate Resilient incident payload and data tables from finding.
                            finding_payload = ParseFinding(finding, gd_region)

                            # Create incident and return response
                            i_response = res_svc.create_incident(finding_payload.payload)

                            if i_response is not None:
                                # Create data tables.
                                if finding_payload.data_tables:
                                    res_svc.add_datatables(i_response['id'], finding_payload.data_tables)
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

    def set_criteria(self):
        """
        Create criteria to filter findings data from GuardDuty.

        :return fc: Return criterion dict
        """
        f_criteria = FCrit()
        # Only return current findings omit archived findings.
        f_criteria.set_archived(value="false")
        # Add severity criterion if setting enabled.
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
