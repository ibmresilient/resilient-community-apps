# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import (
    ResilientComponent,
    function,
    handler,
    StatusMessage,
    FunctionResult,
    FunctionError,
)
from resilient_lib import ResultPayload
from fn_ansible.lib.ansible_api import run_playbook, cleanup_artifact_dir

SECTION_HDR = "fn_ansible"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_ansible"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self._init_function(opts)


    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self._init_function(opts)

    def _init_function(self, opts):
        self.options = opts.get(SECTION_HDR, {})
        self.runner_dir = self.options.get("runner_dir")
        self.artifact_dir = self.options.get("artifact_dir")
        self.artifact_rentention_num = int(self.options.get("artifact_retention_num", 0))

        if not self.runner_dir:
            raise ValueError("Specify the runner_dir in app.config")

    @function("fn_ansible")
    def _fn_ansible_function(self, event, *args, **kwargs):
        """Function: Ansible is simple IT engine for automation, it is designed for manage many systems, rather than just one at a time."""
        try:
            # Get the function parameters:
            ansible_playbook = kwargs.get("ansible_playbook_name")  # text
            ansible_parameters = kwargs.get("ansible_parameters")  # text

            log = logging.getLogger(__name__)
            log.info(u"playbook_name: %s", ansible_playbook)
            log.info(u"ansible_parameters: %s", ansible_parameters)

            # use the workflow_id to identify the ansible process
            workflow_id = event.message['workflow_instance']['workflow_instance_id']

            result = ResultPayload(SECTION_HDR, **kwargs)

            # Prepare playbook vars
            extra_vars = {}
            if ansible_parameters:
                for item in ansible_parameters.split(u";"):
                    if len(item.strip(u' ')) > 0:
                        k, v = item.split(u"=")
                        extra_vars[k.strip(u' ')] = v.strip(u' ')

            # prepare playbook arg
            playbook_extension = ansible_playbook.split(u".")[-1]
            if playbook_extension != "yml":
                ansible_playbook = u"{}.yml".format(ansible_playbook.strip(u' '))

            playbook_results = run_playbook(
                id=workflow_id,
                private_data_dir=self.runner_dir,
                artifact_dir=self.artifact_dir,
                playbook_name=ansible_playbook,
                playbook_args=extra_vars
            )

            result_payload = result.done(True, playbook_results)

            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload)
        except Exception:
            yield FunctionError()
        finally:
            log.info("Running cleanup_artifact_dir for {} previous runs".format(self.artifact_rentention_num))
            cleanup_artifact_dir(self.artifact_dir if self.artifact_dir else self.runner_dir,
                                 self.artifact_rentention_num)


    @function("fn_ansible_module")
    def _fn_ansible_module_function(self, event, *args, **kwargs):
        """Function: Ansible is simple IT engine for automation, it is designed for manage many systems, rather than just one at a time."""
        try:
            # Get the function parameters:
            ansible_module = kwargs.get("ansible_module")  # text
            ansible_parameters = kwargs.get("ansible_parameters")  # text
            ansible_hosts = kwargs.get("ansible_hosts") # text

            log = logging.getLogger(__name__)
            log.info(u"playbook_name: %s", ansible_module.strip(u' '))
            log.info(u"ansible_parameters: %s", ansible_parameters)

            workflow_id = event.message['workflow_instance']['workflow_instance_id']

            result = ResultPayload(SECTION_HDR, **kwargs)

            playbook_results = run_playbook(
                id=workflow_id,
                private_data_dir=self.runner_dir,
                artifact_dir=self.artifact_dir,
                module_name=ansible_module.strip(u' '),
                module_args=ansible_parameters,
                module_hosts=ansible_hosts
            )

            result_payload = result.done(True, playbook_results)

            # Produce a FunctionResult with the results
            yield FunctionResult(result_payload)
        except Exception:
            yield FunctionError()
        finally:
            log.info("Running cleanup_artifact_dir for {} previous runs".format(self.artifact_rentention_num))
            cleanup_artifact_dir(self.artifact_dir if self.artifact_dir else self.runner_dir,
                                 self.artifact_rentention_num)
