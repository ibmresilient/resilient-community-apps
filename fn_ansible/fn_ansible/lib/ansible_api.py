# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor


def run_playbook(playbook_path, hosts_path, user_name, root_password, playbook_extra_vars):
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=hosts_path)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    if playbook_extra_vars:
        variable_manager.extra_vars = playbook_extra_vars

    # Todo - Scope for vault password
    passwords={'become_pass': root_password}

    Options = namedtuple('Options',
                        ['connection',
                        'remote_user',
                        'ask_sudo_pass',
                        'verbosity',
                        'ack_pass',
                        'module_path',
                        'forks',
                        'become',
                        'become_method',
                        'become_user',
                        'check',
                        'listhosts',
                        'listtasks',
                        'listtags',
                        'syntax',
                        'sudo_user',
                        'sudo',
                        'diff'])
    options = Options(connection='smart',
                        remote_user=user_name,
                        ack_pass=None,
                        sudo_user=None,
                        forks=5,
                        sudo=None,
                        ask_sudo_pass=False,
                        verbosity=5,
                        module_path=None,
                        become=True,
                        become_method='sudo',
                        become_user='root',
                        check=False,
                        diff=False,
                        listhosts=None,
                        listtasks=None,
                        listtags=None,
                        syntax=None)

    playbook = PlaybookExecutor(playbooks=playbook_path,inventory=inventory,
                variable_manager=variable_manager,
                loader=loader,options=options,passwords=passwords)
    playbook.run()
    stats = playbook._tqm._stats
    hosts = sorted(stats.processed.keys())
    for h in hosts:
        result = {h: stats.summarize(h)}
    
    return result
