# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_ansible.lib.ansible_api import run_playbook, cleanup_artifact_dir, PACKAGE_NAME

FN_NAME = "fn_ansible_module"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_ansible_module'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        validate_fields(["runner_dir", "artifact_dir"], self.options)

        self.runner_dir = self.options.get("runner_dir")
        self.artifact_dir = self.options.get("artifact_dir")
        self.artifact_retention_num = int(self.options.get("artifact_retention_num", 0))

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Run an Ansible Module
        Inputs:
            -   fn_inputs.ansible_hosts
            -   fn_inputs.ansible_parameters
            -   fn_inputs.ansible_module
        """
        try:
            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            # Validate required fields
            validate_fields(["ansible_module", "ansible_hosts"], fn_inputs)
            
            # Get the function parameters:
            ansible_module = getattr(fn_inputs, "ansible_module", None)  # text
            ansible_parameters = getattr(fn_inputs, "ansible_parameters", None)  # text
            ansible_hosts = getattr(fn_inputs, "ansible_hosts", None) # text

            self.LOG.info("Ansible Module: %s", ansible_module)
            self.LOG.info("Ansible Hosts: %s", ansible_hosts)
            self.LOG.info("Ansible Parameters: %s", ansible_parameters)
            
            if ansible_parameters:
                # module args use the format name=value name=value
                ansible_parameters = ansible_parameters.replace(';', ' ')

            playbook_results = run_playbook(
                id=self.get_fn_msg().get("workflow_instance", {}).get("workflow_instance_id"),
                private_data_dir=self.runner_dir,
                artifact_dir=self.artifact_dir,
                module_name=ansible_module.strip(' '),
                module_args=ansible_parameters,
                module_hosts=ansible_hosts)

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(playbook_results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=err)
        finally:
            self.LOG.info(f"Running cleanup_artifact_dir for {self.artifact_retention_num} previous runs")
            cleanup_artifact_dir(self.artifact_dir if self.artifact_dir else self.runner_dir,
                                 self.artifact_retention_num)
