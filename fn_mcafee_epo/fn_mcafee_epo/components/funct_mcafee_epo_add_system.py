# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "mcafee_epo_add_system"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_add_system'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Add a system to the ePO server
        Inputs:
            -   fn_inputs.mcafee_epo_flatten_tree_structure
            -   fn_inputs.mcafee_epo_system_name_or_id
            -   fn_inputs.mcafee_epo_allow_duplicates
            -   fn_inputs.mcafee_epo_push_agent_install_path
            -   fn_inputs.mcafee_epo_group_id
            -   fn_inputs.mcafee_epo_push_agent_skip_if_installed
            -   fn_inputs.mcafee_epo_push_agent
            -   fn_inputs.mcafee_epo_push_agent_password
            -   fn_inputs.mcafee_epo_push_agent_force_install
            -   fn_inputs.mcafee_epo_push_agent_suppress_ui
            -   fn_inputs.mcafee_epo_delete_if_removed
            -   fn_inputs.mcafee_epo_push_agent_username
            -   fn_inputs.mcafee_epo_push_agent_domain_name
            -   fn_inputs.mcafee_epo_push_agent_package_path
            -   fn_inputs.mcafee_epo_uninstall
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Validate parameters
        validate_fields(["mcafee_epo_system_name_or_id", "mcafee_epo_group_id"], fn_inputs)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "system.importSystem",
            {"names": fn_inputs.mcafee_epo_system_name_or_id,
             "branchNodeID": int(fn_inputs.mcafee_epo_group_id),
             "allowDuplicates": bool(fn_inputs.mcafee_epo_allow_duplicates) if hasattr(fn_inputs, "mcafee_epo_allow_duplicates") else False,
             "uninstallRemoved": bool(fn_inputs.mcafee_epo_uninstall) if hasattr(fn_inputs, "mcafee_epo_uninstall") else True,
             "pushAgent": bool(fn_inputs.mcafee_epo_push_agent) if hasattr(fn_inputs, "mcafee_epo_push_agent") else False,
             "pushAgentForceInstall": bool(fn_inputs.mcafee_epo_push_agent_force_install) if hasattr(fn_inputs, "mcafee_epo_push_agent_force_install") else False,
             "pushAgentSkipIfInstalled": bool(fn_inputs.mcafee_epo_push_agent_skip_if_installed) if hasattr(fn_inputs, "mcafee_epo_push_agent_skip_if_installed") else True,
             "pushAgentSuppressUI": bool(fn_inputs.mcafee_epo_push_agent_suppress_ui) if hasattr(fn_inputs, "mcafee_epo_push_agent_suppress_ui") else False,
             "pushAgentInstallPath": fn_inputs.mcafee_epo_push_agent_install_path if hasattr(fn_inputs, "mcafee_epo_push_agent_install_path") else None,
             "pushAgentPackagePath": fn_inputs.mcafee_epo_push_agent_package_path if hasattr(fn_inputs, "mcafee_epo_push_agent_package_path") else None,
             "pushAgentDomainName": fn_inputs.mcafee_epo_push_agent_domain_name if hasattr(fn_inputs, "mcafee_epo_push_agent_domain_name") else None,
             "pushAgentUserName": fn_inputs.mcafee_epo_push_agent_username if hasattr(fn_inputs, "mcafee_epo_push_agent_username") else None,
             "pushAgentPassword": fn_inputs.mcafee_epo_push_agent_password if hasattr(fn_inputs, "mcafee_epo_push_agent_password") else None,
             "deleteIfRemoved": bool(fn_inputs.mcafee_epo_delete_if_removed) if hasattr(fn_inputs, "mcafee_epo_delete_if_removed") else True,
             "flattenTreeStructure": bool(fn_inputs.mcafee_epo_flatten_tree_structure) if hasattr(fn_inputs, "mcafee_epo_flatten_tree_structure") else False
             }
        )

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(response)
