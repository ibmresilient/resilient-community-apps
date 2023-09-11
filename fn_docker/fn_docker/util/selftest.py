# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_docker
"""

import logging
from fn_docker.util.docker_utils import DockerUtils


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_docker", {})
    if not options:
        log.debug("Config Options gathered appear to be empty, review your app.config")

    if options.get("docker_approved_images", None) is None:
        log.debug("Could not gather approved images list. While you could still make a valid connection to Docker, "
                  "without this list, you will not be able to run any containers with the integration.")
        return {"state": "failed", "reason": "Could not establish a connection to a docker daemon"}
    log.debug("These are the images specified as approved to create containers from: %s", options.get("docker_approved_images", None))
    try:
        if not options.get("docker_use_remote_conn", True):
            log.debug("Remote connection will be used for Docker as docker_use_remote_conn is %s",options.get("docker_use_remote_conn"))
        else:
            log.debug("Local connection will be used for Docker")

        log.debug("Attempting to make connection to Docker daemon and ping it")
        docker_interface = DockerUtils()

        # Decide whether to use local connection or remote
        docker_interface.setup_docker_connection(options=options)

    except Exception as e:
        log.debug("Encounted an exception when establishing Docker connection. Exception message: %s", e)
        return {"state": "failed", "reason": "Could not establish a connection to a docker daemon"}
    else:  # If no exceptions raised
        return {"state": "success"}