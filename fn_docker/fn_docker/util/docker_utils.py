# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
import logging
import docker


LOG = logging.getLogger(__name__)
import os
from resilient_circuits.template_functions import render

log = logging.getLogger(__name__)


class DockerUtils:

    def __init__(self):
        self.client = None
        self.api_client = None


    def setup_docker_connection(self, options):
        """
        A function used to decide whether to connect to docker using a local or remote connection

        Depends on 2 app.config values
        A boolean determining whether to use a remote connection

        A string comprising of a remote_server_url to be connected to.

        :return: void
        """

        if options.get("docker_use_remote_conn", False):
            self.initiate_remote_docker_connection(options.get("docker_remote_url", None))
        else:
            self.initiate_local_docker_connection()

    def initiate_remote_docker_connection(self, docker_server_url):
        """
        Docker allows remote access to its API in a number of ways.
        This function takes in a parameter of a server url and attempts to establish a docker connection

        For example 'ssh://admin:pass@192.168.1.0'
        :param docker_server_url:
        :return: void
        """
        try:
            self.client = docker.DockerClient(base_url=docker_server_url)
            self.api_client = docker.APIClient(base_url=docker_server_url)
            self.client.ping()
            self.api_client.ping()
        except ConnectionError:
            LOG.debug('Error connecting to docker')
            raise ValueError("Could not setup Docker connection, is docker running ?")

    def initiate_local_docker_connection(self):
        """
        Used to connect to docker using the enviroment settings for Docker
        Generally, this means the docker connection will be local to the location of your machine.
        However you can also opt to edit the docker env settings which will change how this connects.
        :return: void
        """
        try:
            self.client = docker.from_env()
            self.api_client = docker.APIClient(base_url=os.environ.get('DOCKER_HOST', 'unix://var/run/docker.sock'))
            self.client.ping()
            self.api_client.ping()
        except ConnectionError:
            LOG.debug('Error connecting to docker')
            raise ValueError("Could not setup Docker connection, is docker running ?")

    def get_image(self, image_to_get):
        """
        Attempt to get an image.

        Takes in a
        :param image_to_get:

        which is a specific image name. Function then attempts to get the image locally.
        If the image does not exist locally this function will catch some exceptions.
        In this case, you should pull the image using docker pull <image> and then try again.
        :return: void
        """
        try:
            LOG.info("Image that will be pulled {}".format(image_to_get))
            self.client.images.get(image_to_get)
        except docker.errors.ImageNotFound:
            LOG.info('Docker image was not found, please ensure the image you want to use is on your Docker host')

        except docker.errors.NullResource:
            LOG.info('No image was passed to this function, please check your app.config')

    def get_client(self):
        return self.client

    def get_api_client(self):
        return self.api_client

    def parse_extra_kwargs(self, options):
        """
        A helper function which allows you to add extra docker run configs

        Certain args for docker run are gathered by the app.config or from the Function inputs

        In an attempt to make this as flexible as possible, you may put any number of extra kwargs to be used.
        In your app.config, prefix any extra kwargs you want to use with 'docker_extra_'.
        You should then postfix this with the actual kwarg name.

        So docker_extra_hostname becomes -> hostname

        The function will look for these extra values, parse them and attempt to use them with the docker run command.
        Take note that not all kwargs are usable this way, you may encounter an issues with certain kwargs.

        The image, command, detach and some other kwargs are not usuable with this implementation

        :param options:
        :return: dict which can be fed into the docker run command using **name_of_result, same as kwargs
        """

        return {k.replace('docker_extra_', ''): v
                for k, v in options.items()
                if 'docker_extra_' in k}

    def inspect_container(self, containerid):
        return self.api_client.inspect_container(containerid)

    def gather_image_args_and_volumes(self, helper, image_to_use, all_options, docker_extra_kwargs, escaped_args):
        """
        A helper function used to gather the command to be run aswell as format the kwargs to used on run.

        Depending on the image, there may exist the need for a specific type of volume binding.
        You have options in how you can set this value.

        You can either set it in fn_docker app.config section.
        Or if you intend to run multiple images, which each require their own separate volume binding
        you can instead configure an app.config section for each image
        where you can specify the internal and external volume primary volume bind.

        :param helper:
        :param image_to_use:
        :param all_options:
        :param docker_extra_kwargs:
        :return:
        """

        command = helper.get_image_specific_config_option(
            options=all_options.get('fn_docker_{}'.format(image_to_use.split("/", 1)[1])),
            option_name="cmd")

        output_vol = helper.get_image_specific_config_option(
            options=all_options.get('fn_docker_{}'.format(image_to_use.split("/", 1)[1])),
            option_name="primary_output_dir", optional=True)
        internal_vol = helper.get_image_specific_config_option(
            options=all_options.get('fn_docker_{}'.format(image_to_use.split("/", 1)[1])),
            option_name="primary_internal_dir", optional=True)
        vol_operation = helper.get_image_specific_config_option(
            options=all_options.get('fn_docker_' + image_to_use.split("/", 1)[1]), option_name="cmd_operation",
            optional=True)

        container_volume_bind = {output_vol: {'bind': internal_vol, 'mode': 'rw'}} if output_vol and internal_vol else None

        if docker_extra_kwargs.get('volumes', False):
            log.info("Found a Volume in Extra Kwargs. Appending to existing volume definition")

            # Split the volumes string by commas to get each volume binding
            for volume in docker_extra_kwargs.get('volumes').split(','):
                # Split the volume into each of its params
                volume_params = volume.split(':')
                # Format the volume data into a dict and update.
                container_volume_bind.update({volume_params[0]: {'bind': volume_params[1], 'mode': volume_params[2]}})

            # After we finish looping
            del docker_extra_kwargs['volumes']  # Remove the volume
        docker_extra_kwargs['volumes'] = container_volume_bind
        log.info(
            "Attempted to format volume from extra kwargs, now is type {}".format(
                type(docker_extra_kwargs['volumes'])))

        escaped_args.update({
            "internal_vol": render("{{internal_vol|%s}}" % "sh", {"internal_vol": internal_vol}),
            "operation": render("{{operation|%s}}" % "sh",
                                {"operation": vol_operation})
        })
        return render(command,escaped_args), docker_extra_kwargs

    def gather_container_stats(self, container_id):
        return self.api_client.stats(container=container_id, stream=False)





