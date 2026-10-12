# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v51.0.6.0.1543

"""Function to create a new ThreatIntelSet for AWS GuardDuty"""

import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_aws_guardduty.lib.helpers import extract_key_value_pairs
from fn_aws_guardduty.lib.aws_gd_client import AwsGdClient
import fn_aws_guardduty.util.config as config

PACKAGE_NAME = "fn_aws_guardduty"
FN_NAME = "aws_guardduty_create_threatintelset"
REQUIRED_FIELDS = ["aws_gd_format", "aws_gd_name", "aws_gd_detector_id", "aws_gd_region", "aws_gd_activate", "aws_gd_location"]

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'aws_guardduty_create_threatintelset'"""

    def __init__(self, opts):
        super().__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})
        self.opts = opts
        validate_fields(config.REQUIRED_CONFIG_SETTINGS, self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Creates a new ThreatIntelSet. ThreatIntelSets consist of known malicious IP addresses. GuardDuty generates findings based on ThreatIntelSets. Only users of the administrator account can use this operation.
        Inputs:
            -   fn_inputs.aws_gd_format
            -   fn_inputs.aws_gd_name
            -   fn_inputs.aws_gd_tags
            -   fn_inputs.aws_gd_client_token
            -   fn_inputs.aws_gd_activate
            -   fn_inputs.aws_gd_region
            -   fn_inputs.aws_gd_detector_id
            -   fn_inputs.aws_gd_location
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(REQUIRED_FIELDS, fn_inputs)

        try:
            aws_gd_format = getattr(fn_inputs, "aws_gd_format", None)   #text
            aws_gd_name = getattr(fn_inputs, "aws_gd_name", None)   #text
            aws_gd_activate = getattr(fn_inputs, "aws_gd_activate", None)   #boolean
            aws_gd_region = getattr(fn_inputs, "aws_gd_region", None)   #text
            aws_gd_detector_id = getattr(fn_inputs, "aws_gd_detector_id", None)   #text
            aws_gd_location = getattr(fn_inputs, "aws_gd_location", None)   #text
            aws_gd_client_token = getattr(fn_inputs, "aws_gd_client_token", None)   #text
            aws_gd_tags = getattr(fn_inputs, "aws_gd_tags", None)   #text

            self.LOG.info("aws_gd_format: %s", aws_gd_format)
            self.LOG.info("aws_gd_name: %s", aws_gd_name)
            self.LOG.info("aws_gd_activate: %s", aws_gd_activate)
            self.LOG.info("aws_gd_region: %s", aws_gd_region)
            self.LOG.info("aws_gd_detector_id: %s", aws_gd_detector_id)
            self.LOG.info("aws_gd_location: %s", aws_gd_location)
            self.LOG.info("aws_gd_client_token: %s", aws_gd_client_token)
            self.LOG.info("aws_gd_tags: %s", aws_gd_tags)

            # Create the input payload
            input_parameters_specified = {"DetectorId" : aws_gd_detector_id,
                                          "Name" : aws_gd_name,
                                          "Format" : aws_gd_format,
                                          "Location" : aws_gd_location,
                                          "Activate" : aws_gd_activate}

            if aws_gd_client_token is not None:
                input_parameters_specified["ClientToken"] = aws_gd_client_token
            if aws_gd_tags is not None:
                aws_gd_tags_dict = extract_key_value_pairs(aws_gd_tags)
                input_parameters_specified["Tags"] = aws_gd_tags_dict

            # Instantiate AWS GuardDuty client object.
            aws_gd = AwsGdClient(self.opts, self.options, region=aws_gd_region)

            # Make the Post API call to GuardDuty service
            incident_response = aws_gd.post("create_threat_intel_set", **input_parameters_specified)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(incident_response)

            self.LOG.info("Complete")

        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
