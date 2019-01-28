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
        self.all_options = {k:v for k,v in opts.items() if 'fn_docker' in k}
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

            if image_to_use not in helper.get_config_option("docker_image", True).split(","):
                raise ValueError("Image is not in list of approved images. Review your app.config")

            # Acquire any specific configs for this image
            command = helper.get_image_specific_config_option(options=self.all_options.get('fn_docker_volatility', {}), option_name="cmd")

            output_vol = helper.get_image_specific_config_option(options=self.all_options.get('fn_docker_'+image_to_use.split("/", 1)[1]), option_name="output_dir")

            internal_vol = helper.get_image_specific_config_option(options=self.all_options.get('fn_docker_'+image_to_use.split("/", 1)[1]), option_name="vol_internal_dir")

            vol_operation = helper.get_image_specific_config_option(options=self.all_options.get('fn_docker_'+image_to_use.split("/", 1)[1]), option_name="volcmd")

            container_volume_bind = {output_vol: {'bind': internal_vol, 'mode': 'rw'}}

            if docker_extra_kwargs.get('volumes', False):
                log.info("Found a Volume in Extra Kwargs. Appending to existing volume definition")

                for volume in docker_extra_kwargs.get('volumes').split(','):

                    extra_volume = volume.split(':')

                    container_volume_bind.update(
                        helper.merge_two_dicts(
                            container_volume_bind,
                            {extra_volume[0]: {'bind': extra_volume[1], 'mode': extra_volume[2]}}))

                # After we finish looping
                del docker_extra_kwargs['volumes']  # Remove the volume to prevent multiple keyword error
                log.info("Attempted to delete volume from extra kwargs, now returns {}".format('volumes' in docker_extra_kwargs))

            actual_command = command.format(internal_vol, vol_operation)
            log.info("Command {} \n Volume Bind {}".format(actual_command, container_volume_bind))
            # Now Get the Image
            docker_interface.get_image(image_to_use)

            # Get the Client
            docker_client = docker_interface.get_client()
            yield StatusMessage("Now starting container with input")
            # Run container using client
            container = docker_client.containers.run(
                image=image_to_use,
                command=actual_command,
                detach=True,  # Detach from container
                volumes=container_volume_bind,
                remove=False,  # Remove set to false as will be removed manually after gathering info
                **docker_extra_kwargs)

            container_logs = container.logs(follow=True)
            log.info(container_logs)
            yield StatusMessage("Container has finished and logs gathered")
            """
            Block until the container has finished its execution in some form, returns the status
            
            
            If the kwarg 'remove' was set to true in docker run, you will not be able to access the container 
            anywhere below this line, it will result in a 404 as by the time this resolves; 
            the container will be removed
            """
            print(docker_interface.inspect_container(container.id))

            try:
                """
                Attempt to remove the container now we have finished.
                Will throw an exception if the container has already been removed"""

                container_status = container.wait()
                container_stats_gen = container.stats()

                """
                import itertools
                container_stats = None
                container_stats_gen = container.stats()
                for line in container_stats_gen:
                    print(line)
                print(container_stats)
                
                """
                container.remove()

            except requests.exceptions.HTTPError as e:
                yield StatusMessage("Encountered issue when trying to remove container: {} \n {}".format(str(e),
                                    "If you supplied an extra app.config value to remove the container this is fine."))

            # Produce a FunctionResult with the results using the FunctionPayload
            yield FunctionResult(payload.done(
                # If container had no errors, 0 will be returned. Use a falsey check to ensure we get 0 else False
                success=True if not container_status.get("StatusCode", 1) else False,
                content={
                    "logs": container_logs.decode('utf-8'),
                    "container_exit_status": container_status,
                    "container_stats": container_stats

                }
            ))
            log.info("Complete")
        except Exception:
            yield FunctionError()

