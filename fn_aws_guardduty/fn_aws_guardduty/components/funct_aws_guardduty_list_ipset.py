# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v51.0.6.0.1543

"""Function to list all IPSets for AWS GuardDuty"""

import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_aws_guardduty.lib.aws_gd_client import AwsGdClient
import fn_aws_guardduty.util.config as config

PACKAGE_NAME = "fn_aws_guardduty"
FN_NAME = "aws_guardduty_list_ipset"
REQUIRED_FIELDS = ["aws_gd_detector_id", "aws_gd_region"]

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'aws_guardduty_list_ipset'"""

    def __init__(self, opts):
        super().__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Lists the IPSets of the GuardDuty service specified by the detector ID.
        Inputs:
            -   fn_inputs.aws_gd_max_results
            -   fn_inputs.aws_gd_region
            -   fn_inputs.aws_gd_detector_id
            -   fn_inputs.aws_gd_next_token
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(REQUIRED_FIELDS, fn_inputs)
        try:
            aws_gd_detector_id = getattr(fn_inputs, "aws_gd_detector_id", None)   #text
            aws_gd_next_token = getattr(fn_inputs, "aws_gd_next_token", None)   #text
            aws_gd_region = getattr(fn_inputs, "aws_gd_region", None)   #text
            aws_gd_max_results = getattr(fn_inputs, "aws_gd_max_results", None)   #number

            self.LOG.info("aws_gd_detector_id: %s", aws_gd_detector_id)
            self.LOG.info("aws_gd_next_token: %s", aws_gd_next_token)
            self.LOG.info("aws_gd_region: %s", aws_gd_region)
            self.LOG.info("aws_gd_max_results: %d", aws_gd_max_results)

            # Create the input payload
            input_parameters_specified = {"DetectorId": aws_gd_detector_id}

            if aws_gd_max_results is not None:
                input_parameters_specified["MaxResults"] = aws_gd_max_results

            if aws_gd_next_token is not None:
                input_parameters_specified["NextToken"] = aws_gd_next_token

            # Instantiate AWS GuardDuty client object.
            aws_gd = AwsGdClient(self.opts, self.options, region=aws_gd_region)

            # Make the GET API call to GuardDuty service
            incident_response = aws_gd.get("list_ip_sets", **input_parameters_specified)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(incident_response)

            self.LOG.info("Complete")

        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
