# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

""" This module intends to provide a high level API 
for Ansible's core level modules and their functionalities.
"""

import ansible_runner
import logging
import os
import sys
import traceback

if sys.version_info[0] >= 3:
    import html as HTMLParser
    h = HTMLParser
else:
    from HTMLParser import HTMLParser
    h = HTMLParser()

log = logging.getLogger(__name__)


def run_playbook(
        id=None,
        private_data_dir=None,
        artifact_dir=None,
        playbook_name=None,
        playbook_args=None,
        module_name=None,
        module_args=None,
        module_hosts=None
    ):
    """This function is responsible for running a playbook
    and returns the results of the queries that the playbook
    contains.
    """

    result = {}
    try:
        if playbook_name:
            log.info(u"Running playbook '{}' with ID {}".format(playbook_name, id))
            r = ansible_runner.run(ident=id,
                                   private_data_dir=private_data_dir,
                                   artifact_dir=artifact_dir,
                                   playbook=playbook_name,
                                   extravars=playbook_args
                                   )
        elif module_name:
            log.info(u"Running module '{}' with ID {}".format(module_name, id))
            r = ansible_runner.run(ident=id,
                                   private_data_dir=private_data_dir,
                                   artifact_dir=artifact_dir,
                                   module=module_name,
                                   module_args=module_args,
                                   host_pattern=module_hosts
                                   )

        for host in r.events:
            log.debug(host)
            if sys.version_info[0] >= 3:
                detail = bytes(host.get('stdout', ''), 'utf-8').decode('unicode_escape')
            else:
                detail = host.get('stdout', '').decode('string_escape')

            if host.get('event', '').startswith('runner_on'):
                # look for json results
                if host['event_data'].get("res"):
                    detail = host['event_data'].get("res")

                result[host['event_data']['host']] = \
                    { 'summary': r.status,
                       'detail': detail
                    }
            elif host.get('event', '') in ('verbose', 'error'):
                result[host['runner_ident']] = \
                    { 'summary': r.status,
                       'detail': detail
                    }

        return result

    except Exception as original_exception:
        raise ValueError(original_exception)


def cleanup_artifact_dir(path, num):
    # navigate to directory for artifacts
    artifacts_path = os.path.join(path, 'artifacts')
    ansible_runner.utils.cleanup_artifact_dir(artifacts_path, num_keep=num)