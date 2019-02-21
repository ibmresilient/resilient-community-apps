# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_docker
"""

import logging
from fn_docker.util.docker_utils import DockerUtils


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_docker", {})
    try:
        docker_interface = DockerUtils()

        # Decide whether to use local connection or remote
        docker_interface.setup_docker_connection(options=options)
    except Exception:
        return {"state": "failed", "reason": "Could not establish a connection to a docker daemon"}
    else:  # If no exceptions raised
        return {"state": "success"}