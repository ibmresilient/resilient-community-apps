# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_docker.util.selftest as selftest
import requests
from fn_docker.util.docker_utils import DockerUtils
from fn_docker.util.helper import ResDockerHelper
from resilient_lib import ResultPayload

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'docker_run_docker_container"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_docker", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_docker", {})

    @function("docker_run_docker_container")
    def _docker_run_docker_container_function(self, event, *args, **kwargs):
        """Function: A function intended to be used to create a Docker Container from an image, feed an input to the container and then return the results."""
        try:
            # Get the function parameters:
            artifact_id = kwargs.get("artifact_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            docker_image = kwargs.get("docker_image")  # text
            docker_input = kwargs.get("docker_input")  # text

            payload = ResultPayload("fn_docker", **kwargs)

            log = logging.getLogger(__name__)
            log.info("artifact_id: %s", artifact_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("docker_image: %s", docker_image)
            log.info("docker_input: %s", docker_input)

            helper = ResDockerHelper(self.options)

            docker_interface = DockerUtils()

            # Decide whether to use local connection or remote
            docker_interface.setup_docker_connection(options=self.options)

            docker_extra_kwargs = docker_interface.parse_extra_kwargs(options=self.options)

            image_to_use = helper.get_config_option("docker_image", True) or docker_image

            # Now Get the Image
            docker_interface.get_image(image_to_use)

            # Get the Client
            docker_client = docker_interface.get_client()

            # Run container using client
            container = docker_client.containers.run(
                image=image_to_use,
                command="vol.py -f /home/nonroot/memdumps/silentbanker.vmem pslist",
                detach=True,
                **docker_extra_kwargs)

            container_logs = container.logs().decode('utf-8')

            """
            Block until the container has finished its execution in some form, returns the status
            
            
            If the kwarg 'remove' was set to true in docker run, you will not be able to access the container 
            anywhere below this line, it will result in a 404 as by the time this resolves; 
            the container will be removed
            """
            container_status = container.wait()

            try:
                """
                Attempt to remove the container now we have finished.
                Will throw an exception if the container has already been removed"""
                container.remove()
            except requests.exceptions.HTTPError as e:
                yield StatusMessage("Encountered issue when trying to remove container: {} \n {}".format(str(e),
                                    "If you supplied an extra app.config value to remove the container this is fine."))

            # Produce a FunctionResult with the results using the FunctionPayload
            yield FunctionResult(payload.done(
                # If container had no errors, 0 will be returned. Use a falsey check to ensure we get 0 else False
                success=True if not container_status.get("StatusCode", 1) else False,
                content={
                    "logs": container_logs,
                    "container_status": container_status,

                }
            ))
            log.info("Complete")
        except Exception:
            yield FunctionError()

