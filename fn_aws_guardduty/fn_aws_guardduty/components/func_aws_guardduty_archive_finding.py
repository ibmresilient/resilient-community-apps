# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_aws_guardduty.lib.aws_gd_client import AwsGdClient
import fn_aws_guardduty.util.config as config

PACKAGE_NAME = "fn_aws_guardduty"
REQUIRED_FIELDS = ["aws_gd_finding_id", "aws_gd_detector_id", "aws_gd_region"]

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'func_aws_guardduty_archive_finding''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})
        self.opts = opts
        validate_fields(config.REQUIRED_CONFIG_SETTINGS, self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})
        self.opts = opts
        validate_fields(config.REQUIRED_CONFIG_SETTINGS, self.options)

    @function("func_aws_guardduty_archive_finding")
    def _func_aws_guardduty_archive_finding_function(self, event, *args, **kwargs):
        """Function: Archive an AWS GuardDuty finding.

        :param aws_gd_finding_id: An AWS GuardDuty finding ID.
        :param aws_gd_detector_id: An AWS GuardDuty detector ID.
        :param aws_gd_region: An AWS GuardDuty region ID.
        """
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'func_aws_guardduty_archive_finding' running in workflow '{0}'".format(wf_instance_id))

            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the function parameters:
            aws_gd_region = kwargs.get("aws_gd_region")  # text
            aws_gd_finding_id = kwargs.get("aws_gd_finding_id")  # text
            aws_gd_detector_id = kwargs.get("aws_gd_detector_id")  # text

            validate_fields(REQUIRED_FIELDS, kwargs)

            log = logging.getLogger(__name__)
            log.info("aws_gd_region: %s", aws_gd_region)
            log.info("aws_gd_finding_id: %s", aws_gd_finding_id)
            log.info("aws_gd_detector_id: %s", aws_gd_detector_id)

            # Instantiate AWS GuardDuty client object.
            aws_gd = AwsGdClient(self.opts, self.options, region=aws_gd_region)

            result = aws_gd.post("archive_findings", DetectorId=aws_gd_detector_id, FindingIds=[aws_gd_finding_id])

            results = rp.done(True, result)

            yield StatusMessage("Finished 'func_aws_guardduty_archive_finding' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
