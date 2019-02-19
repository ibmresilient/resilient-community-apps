# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from subprocess import PIPE, Popen
import logging
import os
import chardet
import json
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_ansible.lib.ansible_api import run_playbook


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_ansible"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ansible", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ansible", {})

    @function("fn_ansible")
    def _fn_ansible_function(self, event, *args, **kwargs):
        """Function: Ansible is simple IT engine for automation, it is designed for manage many systems, rather than just one at a time."""
        try:
            # Get the function parameters:
            playbook_name = kwargs.get("ansible_playbook_name") # text
            ansible_parameters = kwargs.get("ansible_parameters") # text

            log = logging.getLogger(__name__)
            log.info("playbook_name: %s", playbook_name)
            log.info("ansible_parameters: %s", ansible_parameters)


            user_name = self.options.get("user_name")
            playbook_dir = self.options.get("playbook_dir")
            hosts_path = self.options.get("hosts_path")
            root_password = self.options.get("root_password")
            playbook_become_method = self.options.get("playbook_become_method")
            playbook_become_user = self.options.get("playbook_become_user")
            vault_password_file = self.options.get("vault_password_file")
            connection_type = self.options.get("connection_type")
            
            # Prepare playbook vars
            extra_vars = {}
            if ansible_parameters:
                for item in ansible_parameters.split(","):
                    # removing whitespaces around comma(,) and = character
                    for pair in [[" ,", ","], [", ", ","], [" =", "="], ["= ", "="]]:
                        item = item.replace(pair[0], pair[1])
                    k, v = item.split("=")
                    extra_vars[k] = v

            # prepare playbook arg
            playbook_extention = playbook_name.split('.')[len(playbook_name.split('.'))-1]
            if(playbook_extention != "yml"):
                playbook_name = "{}.yml".format(playbook_name)
            # check for playbook's availability in the dir
            os.chdir(playbook_dir)
            if playbook_name in os.listdir(playbook_dir):
                target_playbook = '/'.join((playbook_dir, playbook_name)), # As per ansible convention a trailing ',' given
            else:
                raise ValueError("Target playbook not present in following path: '%s'" %playbook_dir)
            
            results = run_playbook( hosts_path=hosts_path, 
                                    user_name=user_name, 
                                    root_password=root_password, 
                                    playbook_path=target_playbook, 
                                    playbook_extra_vars=extra_vars,
                                    playbook_become_method=playbook_become_method,
                                    playbook_become_user=playbook_become_user,
                                    vault_password_file=vault_password_file,
                                    connection_type=connection_type)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()