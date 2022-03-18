# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from pickletools import read_bytes4
from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME, POLICY_DETAILS, get_hive_options
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "reaqta_create_policy"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'reaqta_create_policy'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create an alert trigger based on a program's SHA256 hash
        Inputs:
            -   fn_inputs.reaqta_policy_title
            -   fn_inputs.reaqta_policy_block
            -   fn_inputs.reaqta_policy_included_groups
            -   fn_inputs.reaqta_policy_excluded_groups
            -   fn_inputs.reaqta_sha256
            -   fn_inputs.reaqta_policy_description
            -   fn_inputs.reaqta_policy_enabled
            -   fn_inputs.reaqta_hives
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields([
                        "reaqta_policy_title",
                        "reaqta_sha256",
                        "reaqta_policy_enabled",
                        "reaqta_policy_block"
                       ],
                       fn_inputs)

        # collect the hives to set this policy
        inputs_dict = fn_inputs._asdict()
        hives = []
        if inputs_dict.get("reaqta_hives"):
            hives = [hive.strip() for hive in inputs_dict.get("reaqta_hives", "").split(",")]
        elif self.options.get("policy_hives"):
            hives = [hive.strip() for hive in self.options.get("policy_hives", "").split(",")]
        else:
            err_msg = "No hive information specified"


        results = []
        for hive in hives:
            hive_settings = get_hive_options(hive, self.opts)
            if not hive_settings:
                err_msg = "Hive section not found: {}".format(hive)
                yield self.status_message(err_msg)
            else:
                app_common = AppCommon(self.rc, hive_settings)
                response, err_msg = app_common.create_policy(inputs_dict)

                result = response.json() if not err_msg else None
                if result:
                    # create the url for the policy created
                    result['policy_url'] = app_common.make_linkback_url(result.get('id'),
                                                                        linkback_url=POLICY_DETAILS)
                    results.append(result)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=True if not err_msg else False, reason=err_msg)
