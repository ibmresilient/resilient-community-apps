# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import tempfile
import os
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_docker.util.selftest as selftest
import requests
from resilient_circuits.actions_component import Actions
from fn_docker.util.docker_utils import DockerUtils
from fn_docker.util.helper import ResDockerHelper
from resilient_lib import ResultPayload
import resilient_lib as resilient_lib
from resilient_circuits.template_functions import render


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'docker_run_docker_container"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.org_id = Actions(opts=opts).org_id
        print("Org ID is {}".format(self.org_id))

        self.options = opts.get("fn_docker", {})
        self.all_options = {k:v for k,v in opts.items() if 'fn_docker' in k}
        self.host_config = (opts.get("host"), opts.get("org"))
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
            docker_image = self.get_select_param(kwargs.get("docker_image"))  # select, values: "volatility", "nsrl", "plaso", "bloodhound"
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
            image_to_use = helper.get_config_option("docker_image", True) or docker_image

            # Prepare the args which will be rendered into the app.config cmd
            escaped_args = {
                "docker_input": render(u"{{docker_input|%s}}" % "sh", kwargs),
            }

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
                    options=self.all_options.get('fn_docker_{}'.format(image_to_use)),
                    option_name="primary_output_dir", optional=True)

                yield StatusMessage("Writing attachment to bind folder")

                # Convert to named temp file
                with tempfile.NamedTemporaryFile(delete=False, prefix='.docker_integration_input_',
                                                 suffix=attachment_name, dir=output_vol) as temp_file:
                    try:
                        temp_file.write(attachment_input)
                        temp_file.close()
                    finally:
                        attachment_file_name = os.path.split(temp_file.name)[1]
                        # Add a attachment_input arg to be rendered into the cmd command
                        escaped_args.update({
                            "attachment_input": render("{{attachment_input|%s}}" % "sh",
                                                       {"attachment_input": attachment_file_name}),
                        })
                        yield StatusMessage("Added this as an Attachment Input: {}".format(attachment_file_name))

            else:
                # We are not dealing with an attachment
                log.debug("Working with an artifact")

            docker_interface = DockerUtils()

            # Decide whether to use local connection or remote
            docker_interface.setup_docker_connection(options=self.options)
            docker_extra_kwargs = dict()

            # Ensure the specified image is an approved one
            if image_to_use not in helper.get_config_option("docker_approved_images").split(","):
                raise ValueError("Image is not in list of approved images. Review your app.config")

            image_fullname = None
            # Gather the command to send to the image and format docker_extra_kwargs for any image specific volumes
            command, docker_extra_kwargs, image_fullname = docker_interface.gather_image_args_and_volumes(
                helper, image_to_use, self.all_options, escaped_args)

            log.info("Command: {} \n Volume Bind: {}".format(command, docker_extra_kwargs.get('volumes', "No Volumes")))
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

            except requests.exceptions.HTTPError as e:
                yield StatusMessage("Encountered issue when trying to remove container: {} \n {}".format(str(e),
                                    "If you supplied an extra app.config value to remove the container this is expected."))

            # Setup tempfile
            with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as temp_upload_file:
                try:
                    # Write and close tempfile
                    temp_upload_file.write(container_logs.decode('utf-8'))
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
                                                            filename="{}{}".format("logs-from-",container_id), mimetype='text/plain')



                finally:
                    os.unlink(temp_upload_file.name)

            result = payload.done(
                # If container had no errors, 0 will be returned. Use a falsey check to ensure we get 0 else False
                success=True if not container_status.get("StatusCode", 1) else False,
                content={
                    "logs": container_logs.decode('utf-8'),
                    "container_exit_status": container_status,
                    "container_stats": container_stats,
                    "container_id": container_id,
                    "res_links": {
                        "input_attachment": '<a href="{}"> Input</a>'.format(helper.prepare_attachment_link(
                            host=self.host_config[0],org_id=self.org_id,
                            attachment_id=attachment_id, incident_id=incident_id,
                            task_id=task_id)),
                        "res_object": helper.prepare_res_link(host=self.host_config[0], incident_id=incident_id, task_id=task_id)
                    }

                }
            )
            import pprint
            pprint.pprint(result)
            from datetime import datetime
            dt_obj = datetime.strptime(result["metrics"]["timestamp"],
                                       '%Y-%m-%d %H:%M:%S')
            millisec = dt_obj.timestamp()

            result["metrics"]["timestamp_epoch"] = int(millisec * 1000)


            #helper.add_row(incident_id=incident_id, apiname="docker_integration_invocations",client=self.rest_client(), time=result["metrics"]["timestamp_epoch"], id=container_id, link=result["content"]["res_links"]["input_attachment"])
            import pprint
            pprint.pprint(result)
            # Produce a FunctionResult with the results using the FunctionPayload
            yield FunctionResult(result)
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





