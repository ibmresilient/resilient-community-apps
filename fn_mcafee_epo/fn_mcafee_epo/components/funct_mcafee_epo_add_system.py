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

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate parameters
        validate_fields(["mcafee_epo_system_name_or_id", "mcafee_epo_group_id"], fn_inputs)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "system.importSystem",
            {"names": fn_inputs.mcafee_epo_system_name_or_id,
             "branchNodeID": fn_inputs.mcafee_epo_group_id,
             "allowDuplicates": getattr(fn_inputs, "mcafee_epo_allow_duplicates", False),
             "uninstallRemoved": getattr(fn_inputs, "mcafee_epo_uninstall", True),
             "pushAgent": getattr(fn_inputs, "mcafee_epo_push_agent", False),
             "pushAgentForceInstall": getattr(fn_inputs, "mcafee_epo_push_agent_force_install", False),
             "pushAgentSkipIfInstalled": getattr(fn_inputs, "mcafee_epo_push_agent_skip_if_installed", True),
             "pushAgentSuppressUI": getattr(fn_inputs, "mcafee_epo_push_agent_suppress_ui", False),
             "pushAgentInstallPath": getattr(fn_inputs, "mcafee_epo_push_agent_install_path", None),
             "pushAgentPackagePath": getattr(fn_inputs, "mcafee_epo_push_agent_package_path", None),
             "pushAgentDomainName": getattr(fn_inputs, "mcafee_epo_push_agent_domain_name", None),
             "pushAgentUserName": getattr(fn_inputs, "mcafee_epo_push_agent_username", None),
             "pushAgentPassword": getattr(fn_inputs, "mcafee_epo_push_agent_password", None),
             "deleteIfRemoved": getattr(fn_inputs, "mcafee_epo_delete_if_removed", True),
             "flattenTreeStructure": getattr(fn_inputs, "mcafee_epo_flatten_tree_structure", False)}
        )

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
