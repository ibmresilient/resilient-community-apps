# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""
This module intends to provide a high level API
for Ansible's core level modules and their functionalities.
"""

from ansible_runner import run, utils
from functools import wraps
from logging import getLogger
from os import path
from shutil import copytree
from tempfile import TemporaryDirectory

PACKAGE_NAME = "fn_ansible"

log = getLogger(__name__)

def private_dir(func):
    """
    Make a private, writable copy of the ansible directory of hosts, secrets, yml playbooks per each invocation
    :return: temporary directory used
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        with TemporaryDirectory() as fp:
            new_dir = path.join(fp, "private")
            copytree(kwargs.get('private_data_dir'), new_dir)
            kwargs['private_data_dir'] = new_dir
            return func(*args, **kwargs)

    return wrapper

@private_dir
def run_playbook(
        id=None,
        private_data_dir=None,
        artifact_dir=None,
        playbook_name=None,
        playbook_args=None,
        module_name=None,
        module_args=None,
        module_hosts=None,
        **kwargs
    ):
    """ This function is responsible for running a playbook and returns the results of the queries that the playbook contains. """

    result = {}
    try:
        if playbook_name:
            log.info("Running playbook '%s' with ID %s", playbook_name, id)
            run_resp = run(ident=id,
                private_data_dir=private_data_dir,
                artifact_dir=artifact_dir,
                playbook=playbook_name,
                extravars=playbook_args,
                **kwargs)
        elif module_name:
            log.info("Running module '%s' with ID %s", module_name, id)
            run_resp = run(ident=id,
                private_data_dir=private_data_dir,
                artifact_dir=artifact_dir,
                module=module_name,
                module_args=module_args,
                host_pattern=module_hosts,
                **kwargs)

        for host in run_resp.events:
            log.debug(host)
            detail = bytes(host.get('stdout', ''), 'utf-8').decode('unicode_escape')

            if host.get('event', '').startswith('runner_on'):
                # look for json results
                if host.get('event_data', {}).get("res"):
                    detail = host.get('event_data', {}).get("res")

                result[host.get('event_data', {}).get('host')] = {
                    'summary': run_resp.status,
                    'detail': detail
                }
            elif host.get('event', '') in ('verbose', 'error'):
                result[host.get('runner_ident')] = {
                    'summary': run_resp.status,
                    'detail': detail
                }

        return result

    except Exception as original_exception:
        raise ValueError(original_exception)

def cleanup_artifact_dir(path, num):
    # navigate to directory for artifacts
    artifacts_path = path.join('artifacts')
    utils.cleanup_artifact_dir(artifacts_path, num_keep=num)
