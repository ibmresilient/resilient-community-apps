# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_guardium_integration.lib.grd_rest_endpoints_service import GrdRestEndpoint
from fn_guardium_integration.lib.resilient_rest_services import ResilientRestService
from resilient_lib import validate_fields


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'function_guardium_block_user"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts_data = opts
        self.options = opts.get("fn_guardium_integration", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_guardium_integration", {})

    @function("function_guardium_block_user")
    def _function_guardium_block_user_function(self, event, *args, **kwargs):
        """Function: A function to block the user access to the Database."""
        try:

            # Get the function parameters:
            guardium_username = kwargs.get("guardium_username")  # text

            # Validating app.config params
            validate_fields(["q_radar_block_group", "block_policy_name"], self.options)

            # Get Config parameters
            group = self.options.get("q_radar_block_group")
            policy_name = self.options.get("block_policy_name")

            log = logging.getLogger(__name__)
            log.info(u"Data Base user to be blocked: %s", guardium_username)
            log.info(u"Blocking User Group : %s", group)
            log.info(u"Block user group policy name: %s", policy_name)

            yield StatusMessage(u"Started: Blocking Guardium user")
            resilient_object = ResilientRestService(self.opts_data, self.options, log)
            grd_rest_object = GrdRestEndpoint(self.options, resilient_object.client_secret, resilient_object.unique_id,
                                              log)
            if not resilient_object.client_secret:
                raise ValueError(u"Guardium client secret not generated, please run `Generate Guardium Client Secret`")

            # Checking weather policy is already installed or not
            installed_policy = grd_rest_object.list_policy_installed()
            installed_msg = installed_policy.get("Message")

            if installed_msg.find(policy_name) != -1:
                # Adding user name to QRadarBlockingConnection Group
                grd_rest_object.create_member_to_group_by_desc(group_desc=group, member=guardium_username)

                # Re Installing the policy.
                if resilient_object.unit_type == "standalone":
                    target_host = ""
                else:
                    target_host = "all_managed"

                re_install_res = grd_rest_object.reinstall_policy(policy=policy_name, api_target_host=target_host)

                msg = re_install_res.get("Message") if "Message" in re_install_res else re_install_res.get(
                    'ErrorMessage')
                function_msg = u"Successfully blocked user: {}. {}".format(guardium_username, msg)
            else:
                yield StatusMessage(u"Warning: Without installed policy bocking user access not possible.")
                function_msg = """Warning - policy: {}, is not installed in the system, without installed policy 
                blocking user to access to DB is not possible.""".format(policy_name)

            yield StatusMessage(u"Completed: Blocking Guardium user action.")

            results = {
                "content": function_msg
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as er_msg:
            yield FunctionError(er_msg)
