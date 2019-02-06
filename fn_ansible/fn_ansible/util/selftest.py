# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-ansible
"""

import logging
from fn_ansible.lib.ansible_api import run_playbook

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_ansible", {})
    playbook_path = "/home/sudip/ansible-playbooks/playbook_encrypted.yml",
    playbook_become_user = options.get("playbook_become_user")
    playbook_become_method = options.get("playbook_become_method")
    control_machine_username = options.get("control_machine_username")
    control_machine_password = options.get("control_machine_password")
    vault_password_file = options.get("vault_password_file")
    
    results = run_playbook( hosts_path="localhost,", 
                                    user_name=control_machine_username, 
                                    root_password=control_machine_password, 
                                    playbook_path=playbook_path, 
                                    playbook_extra_vars={},
                                    playbook_become_method=playbook_become_method,
                                    playbook_become_user=playbook_become_user,
                                    vault_password_file=vault_password_file,
                                    connection_type="local")
    
    state = "failure"
    if(results["localhost"]["ok"] == 1):
        state = "success"
    return {"state": state}