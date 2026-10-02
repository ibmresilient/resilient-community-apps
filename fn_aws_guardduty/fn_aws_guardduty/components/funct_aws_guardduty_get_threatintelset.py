# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v51.0.6.0.1543

"""Function to get all details about a ThreatIntelSet for AWS GuardDuty"""

import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_aws_guardduty.lib.aws_gd_client import AwsGdClient
import fn_aws_guardduty.util.config as config

PACKAGE_NAME = "fn_aws_guardduty"
FN_NAME = "aws_guardduty_get_threatintelset"
REQUIRED_FIELDS = ["aws_gd_threat_intel_set_id", "aws_gd_detector_id", "aws_gd_region"]

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'aws_guardduty_get_threatintelset'"""

    def __init__(self, opts):
        super().__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})
        self.opts = opts
        validate_fields(config.REQUIRED_CONFIG_SETTINGS, self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Retrieves the ThreatIntelSet that is specified by the ThreatIntelSet ID.
        Inputs:
            -   fn_inputs.aws_gd_threat_intel_set_id
            -   fn_inputs.aws_gd_detector_id
            -   fn_inputs.aws_gd_region
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(REQUIRED_FIELDS, fn_inputs)

        try:
            aws_gd_detector_id = getattr(fn_inputs, "aws_gd_detector_id", None)   #text
            aws_gd_threat_intel_set_id = getattr(fn_inputs, "aws_gd_threat_intel_set_id", None)   #text
            aws_gd_region = getattr(fn_inputs, "aws_gd_region", None)   #text

            self.LOG.info("aws_gd_detector_id: %s", aws_gd_detector_id)
            self.LOG.info("aws_gd_threat_intel_set_id: %s", aws_gd_threat_intel_set_id)
            self.LOG.info("aws_gd_region: %s", aws_gd_region)

            # Create the input payload
            input_parameters_specified = {"DetectorId": aws_gd_detector_id,
                                          "ThreatIntelSetId": aws_gd_threat_intel_set_id}

            # Instantiate AWS GuardDuty client object.
            aws_gd = AwsGdClient(self.opts, self.options, region=aws_gd_region)

            # Make the GET API call to GuardDuty service
            incident_response = aws_gd.get("get_threat_intel_set", **input_parameters_specified)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(incident_response)

            self.LOG.info("Complete")

        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
