# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_ansible.lib.ansible_api import run_playbook, cleanup_artifact_dir, PACKAGE_NAME
from os.path import splitext

FN_NAME = "fn_ansible"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_ansible'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        validate_fields(["runner_dir", "artifact_dir"], self.options)

        self.runner_dir = self.options.get("runner_dir")
        self.artifact_dir = self.options.get("artifact_dir")
        self.artifact_retention_num = int(self.options.get("artifact_retention_num", 0))

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Ansible is simple IT engine for automation, it is designed for manage many systems, rather than just one at a time.
        Inputs:
            -   fn_inputs.ansible_parameters
            -   fn_inputs.ansible_playbook_name
        """
        try:
            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            # Validate required inputs
            validate_fields(["ansible_playbook_name"], fn_inputs)

            # Get the function parameters:
            ansible_playbook = getattr(fn_inputs, "ansible_playbook_name", None)  # text
            ansible_parameters = getattr(fn_inputs, "ansible_parameters", None)  # text

            self.LOG.info("Ansible Playbook Name: %s", ansible_playbook)
            self.LOG.info("Ansible Parameters: %s", ansible_parameters)

            # Prepare playbook vars
            # convert name=value;name=value syntax to a dictionary
            extra_vars = None
            if ansible_parameters:
                extra_vars = {item.split('=')[0].strip():item.split('=')[1].strip()
                            for item in ansible_parameters.split(';')
                            if len(item.strip()) > 0}

            # prepare playbook arg
            _playbook_name, playbook_extension = splitext(ansible_playbook)
            if playbook_extension != "yml":
                ansible_playbook = f"{ansible_playbook.strip(' ')}.yml"

            playbook_results = run_playbook(
                id=self.get_fn_msg().get("workflow_instance", {}).get("workflow_instance_id"),
                private_data_dir=self.runner_dir,
                artifact_dir=self.artifact_dir,
                playbook_name=ansible_playbook,
                playbook_args=extra_vars
            )

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            yield FunctionResult(playbook_results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=err)
        finally:
            self.LOG.info(f"Running cleanup_artifact_dir for {self.artifact_retention_num} previous runs")
            cleanup_artifact_dir(self.artifact_dir if self.artifact_dir else self.runner_dir,
                                 self.artifact_retention_num)
