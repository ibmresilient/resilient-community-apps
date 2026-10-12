# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v51.0.6.0.1543

"""Function to update an existing IPSet for AWS GuardDuty"""

import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_aws_guardduty.lib.aws_gd_client import AwsGdClient
import fn_aws_guardduty.util.config as config

PACKAGE_NAME = "fn_aws_guardduty"
FN_NAME = "aws_guardduty_update_ipset"
REQUIRED_FIELDS = ["aws_gd_detector_id", "aws_gd_region", "aws_gd_ip_set_id"]

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'aws_guardduty_update_ipset'"""

    def __init__(self, opts):
        super().__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})
        self.opts = opts
        validate_fields(config.REQUIRED_CONFIG_SETTINGS, self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Updates the IPSet specified by the IPSet ID.
        Inputs:
            -   fn_inputs.aws_gd_new_location
            -   fn_inputs.aws_gd_bucket_owner
            -   fn_inputs.aws_gd_region
            -   fn_inputs.aws_gd_detector_id
            -   fn_inputs.aws_gd_new_activate
            -   fn_inputs.aws_gd_new_name
            -   fn_inputs.aws_gd_ip_set_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(REQUIRED_FIELDS, fn_inputs)

        try:
            aws_gd_detector_id = getattr(fn_inputs, "aws_gd_detector_id", None)   #text
            aws_gd_ip_set_id = getattr(fn_inputs, "aws_gd_ip_set_id", None)   #text
            aws_gd_region = getattr(fn_inputs, "aws_gd_region", None)   #text
            aws_gd_new_location = getattr(fn_inputs, "aws_gd_new_location", None)   #text
            aws_gd_new_name = getattr(fn_inputs, "aws_gd_new_name", None)   #text
            aws_gd_new_activate = getattr(fn_inputs, "aws_gd_new_activate", None)   #boolean
            aws_gd_bucket_owner = getattr(fn_inputs, "aws_gd_bucket_owner", None)   #text

            self.LOG.info("aws_gd_detector_id: %s", aws_gd_detector_id)
            self.LOG.info("aws_gd_ip_set_id: %s", aws_gd_ip_set_id)
            self.LOG.info("aws_gd_region: %s", aws_gd_region)
            self.LOG.info("aws_gd_new_location: %s", aws_gd_new_location)
            self.LOG.info("aws_gd_new_name: %s", aws_gd_new_name)
            self.LOG.info("aws_gd_new_activate: %s", aws_gd_new_activate)
            self.LOG.info("aws_gd_bucket_owner: %s", aws_gd_bucket_owner)

            # Create the input payload
            input_parameters_specified = {"DetectorId" : aws_gd_detector_id,
                                          "IpSetId" : aws_gd_ip_set_id}

            if aws_gd_new_name is not None:
                input_parameters_specified["Name"] = aws_gd_new_name
            if aws_gd_new_activate is not None:
                input_parameters_specified["Activate"] = aws_gd_new_activate
            if aws_gd_new_location is not None:
                input_parameters_specified["Location"] = aws_gd_new_location
            if aws_gd_bucket_owner is not None:
                input_parameters_specified["ExpectedBucketOwner"] = aws_gd_bucket_owner

            # Instantiate AWS GuardDuty client object.
            aws_gd = AwsGdClient(self.opts, self.options, region=aws_gd_region)

            # Make the Post API call to GuardDuty service
            incident_response = aws_gd.post("update_ip_set", **input_parameters_specified)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(incident_response)

            self.LOG.info("Complete")

        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
