# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_ansible
"""

import logging
import time
from fn_ansible.lib.ansible_api import run_playbook

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

ANSIBLE_PING = "ping"
ANSIBLE_HOST = "localhost"


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_ansible", {})

    runner_dir = app_configs.get("runner_dir")
    artifact_dir = app_configs.get("artifact_dir")

    try:
        selftest_results = run_playbook(
            id=time.time(),
            private_data_dir=runner_dir,
            artifact_dir=artifact_dir,
            module_name=ANSIBLE_PING,
            module_args=None,
            module_hosts=ANSIBLE_HOST
        )

        if selftest_results['localhost'].get('summary') == "successful":
            return {
                "state": "success"
            }
        else:
            return {
                "state": "failure",
                "reason": "returned summary: {}".format(selftest_results['localhost'].get('summary'))
            }

    except Exception as err:
        return {
            "state": "failure",
            "reason": str(err)
        }
