# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import tempfile
import os
import time
import requests

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_circuits.template_functions import render

import resilient_lib
from resilient_lib import ResultPayload

from fn_docker.util.docker_utils import DockerUtils
from fn_docker.util.helper import ResDockerHelper


DOCKERATTACHMENTPREFIX = '.docker_integration_input_'
CONFIGSECTIONPREFIX = 'docker_'  # A constant prefix used for an images app.config section.


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'docker_run_docker_container"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_docker", {})
        self.all_options = {k: v for k, v in opts.items() if CONFIGSECTIONPREFIX in k}
        self.host_config = (opts.get("host"), opts.get("org"))

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
            docker_image = self.get_select_param(kwargs.get("docker_image"))  # select, values: "volatility", "nsrl", "plaso", "bloodhound"
            docker_input = kwargs.get("docker_input")  # text
            docker_operation = kwargs.get("docker_operation")  # text
            docker_artifact_type = kwargs.get("docker_artifact_type")
            attachment_name = None  # Initialise attachment name as none

            payload = ResultPayload("fn_docker", **kwargs)

            log = logging.getLogger(__name__)
            log.info("artifact_id: %s", artifact_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("docker_image: %s", docker_image)
            log.info("docker_input: %s", docker_input)
            log.info("docker_artifact_type: %s", docker_artifact_type)
            log.info("docker_operation: %s", docker_operation)

            helper = ResDockerHelper(self.options)
            image_to_use = helper.get_config_option("docker_image", True) or docker_image

            # Prepare the args which will be rendered into the app.config cmd
            escaped_args = {
                "docker_input": render(u"{{docker_input|%s}}" % "sh", kwargs),
            }
            attachment_file_name = None  # Initialise filename as None to avoid reference errors
            # Check whether we are dealing with an attachment or artifact
            if (artifact_id or attachment_id or task_id) and docker_input is None:
                log.debug("Working with an attachment")

                yield StatusMessage("Input appears to be an attachment, attempting to parse.")
                # Get the files data
                attachment_input = resilient_lib.get_file_attachment(
                    incident_id=incident_id, artifact_id=artifact_id,
                    attachment_id=attachment_id, task_id=task_id, res_client=self.rest_client())

                # Get the files name
                attachment_name = resilient_lib.get_file_attachment_name(
                    incident_id=incident_id, artifact_id=artifact_id,
                    attachment_id=attachment_id, task_id=task_id, res_client=self.rest_client())
                # Get the external directory in which to save the file
                output_vol = helper.get_image_specific_config_option(
                    options=self.all_options.get('{}{}'.format(CONFIGSECTIONPREFIX, image_to_use)),
                    option_name="primary_source_dir", optional=True)

                yield StatusMessage("Writing attachment to bind folder")

                if os.path.isdir(output_vol):
                    # Convert to named temp file
                    with tempfile.NamedTemporaryFile(delete=False, prefix=DOCKERATTACHMENTPREFIX,
                                                     dir=output_vol) as temp_file:
                        try:
                            temp_file.write(attachment_input)
                            temp_file.close()

                        finally:
                            attachment_file_name = os.path.split(temp_file.name)[1]
                            # Add a attachment_input arg to be rendered into the cmd command
                            escaped_args.update({
                                "attachment_input": render("{{attachment_input|%s}}" % "sh",
                                                           {u"attachment_input": attachment_file_name}),
                            })
                            yield StatusMessage(u"Added this as an Attachment Input: {}".format(attachment_file_name))
                else:
                    errMsg = u"""Could not write file to directory, does the directory {0} exist? If not create it with mkdir {0}""".format(output_vol)
                    raise FunctionError(errMsg)
            else:
                # We are not dealing with an attachment
                log.debug("Working with an artifact")

            docker_interface = DockerUtils()

            # Decide whether to use local connection or remote
            docker_interface.setup_docker_connection(options=self.options)

            # Ensure the specified image is an approved one
            if image_to_use not in helper.get_config_option("docker_approved_images").split(","):
                raise ValueError("Image is not in list of approved images. Review your app.config")

            # Gather the command to send to the image and format docker_extra_kwargs for any image specific volumes
            command, docker_extra_kwargs, image_fullname, docker_operation = docker_interface.gather_image_args_and_volumes(
                helper, image_to_use, self.all_options, escaped_args, docker_operation)

            log.info("Command: %s \n Volume Bind: %s", (command, docker_extra_kwargs.get('volumes', "No Volumes")))
            # Now Get the Image
            docker_interface.get_image(image_fullname)
            # Get the Client
            docker_client = docker_interface.get_client()

            yield StatusMessage("Now starting container with input")

            # Run container using client
            container = docker_client.containers.run(
                image=image_fullname,
                command=render(command, escaped_args),
                detach=True,  # Detach from container
                remove=False,  # Remove set to false as will be removed manually after gathering info
                **docker_extra_kwargs)

            container_stats = docker_interface.gather_container_stats(container_id=container.id)
            container_id = container.id
            # Gather the logs as they happen, until the container finishes.
            container_logs = container.logs(follow=True)

            yield StatusMessage("Container has finished and logs gathered")

            try:
                """
                Attempt to remove the container now we have finished.
                Will throw an exception if the container has already been removed"""

                container_status = container.wait()
                container.remove()

            except requests.exceptions.HTTPError as request_exception:
                yield StatusMessage(u"""Encountered issue when trying to remove container: {} \n {}""".format(
                    request_exception,
                    u"""If you supplied an extra app.config value to remove the container this is expected."""))

            timestamp_epoch = int(time.time() * 1000)
            # Setup tempfile
            with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as temp_upload_file:
                try:
                    new_attachment_name = helper.format_result_attachment_name(image_to_use, container_id)

                    # Write and close tempfile
                    temp_upload_file.write(helper.format_output_attachment_body(container_id,
                                                                                docker_operation,
                                                                                attachment_file_name,
                                                                                docker_artifact_type,
                                                                                docker_input,
                                                                                container_logs.decode('utf-8'),
                                                                                timestamp_epoch))
                    temp_upload_file.close()

                    #  Access Resilient API
                    client = self.rest_client()

                    # Create POST uri
                    # ..for a task, if task_id is defined
                    if task_id:
                        attachment_uri = '/tasks/{}/attachments'.format(task_id)
                    # ...else for an attachment
                    else:
                        attachment_uri = '/incidents/{}/attachments'.format(incident_id)

                    # POST the new attachment
                    new_attachment = client.post_attachment(attachment_uri, temp_upload_file.name,
                                                            filename=new_attachment_name, mimetype='text/plain')

                finally:
                    os.unlink(temp_upload_file.name)

            results = payload.done(
                # If container had no errors, 0 will be returned. Use a falsey check to ensure we get 0 else False
                success=bool(container_status.get("StatusCode", 1)),
                content={
                    "logs": container_logs.decode('utf-8'),
                    "container_exit_status": container_status,
                    "container_stats": container_stats,
                    "container_id": container_id,
                    "res_links": {
                        "res_object": helper.prepare_res_link(host=self.host_config[0], incident_id=incident_id, task_id=task_id)
                    },
                    "attachment_name": attachment_name or None,
                }
            )
            results["metrics"]["timestamp_epoch"] = timestamp_epoch

            # Update the docker_operation input to ensure we have captured the operation done, if any
            results["inputs"]["docker_operation"] = docker_operation
            # Produce a FunctionResult with the results using the FunctionPayload
            yield FunctionResult(results)
            log.debug("RESULTS: %s", results)
            log.info("Complete")
        except Exception:
            yield FunctionError()
        finally:
            try:
                os.unlink(temp_file.name)
            except NameError:
                log.debug("Error when trying to unlink file.")
            else:
                log.debug("Successfully cleaned up file")
