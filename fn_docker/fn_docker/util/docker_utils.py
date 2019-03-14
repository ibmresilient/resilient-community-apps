# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
import logging
import os
import docker
from resilient_circuits.template_functions import render
import resilient_lib
from requests.exceptions import ConnectionError
LOG = logging.getLogger(__name__)

CONFIGSECTIONPREFIX = 'docker_'  # A constant prefix used for an images app.config section.

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

        if resilient_lib.str_to_bool(options.get("docker_use_remote_conn", "False")):
            LOG.debug("Use Remote Connection config set to true.")
            LOG.debug("Docker Remote URL provided %s", options.get("docker_remote_url", None))
            if 'ssh://' not in options.get("docker_remote_url", "No URL Provided") \
                    and 'tcp://' not in options.get("docker_remote_url", "No URL Provided"):
                raise ValueError("docker_remote_url does not appear to be configured correctly. Current value {}".format(options.get("docker_remote_url", None)))
            self.initiate_remote_docker_connection(options.get("docker_remote_url"))
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
            LOG.debug("The DockerClient version is {}".format(self.client.version()['Version']))
            self.client.ping()
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
            raise ValueError('Docker image was not found, please ensure the image you want to use is on your Docker host')

        except docker.errors.NullResource:
            LOG.info('No image was passed to this function, please check your app.config')


    def get_client(self):
        """
        An OOP method to get a handle on a Docker client
        :return:
        """
        return self.client

    def get_api_client(self):
        """
        An OOP method to get a handle on a Docker API client
        :return:
        """
        return self.api_client

    @staticmethod
    def parse_extra_kwargs(options):
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
        """
        A helper function which is used to return some low-level information about a container

        :param containerid:
        :return:
        """
        return self.api_client.inspect_container(containerid)

    def gather_image_args_and_volumes(self, helper, image_to_use, all_options, escaped_args, docker_operation=None):
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
        :param escaped_args:
        :return:
        """
        LOG.debug(all_options.get('{}{}'.format(CONFIGSECTIONPREFIX, image_to_use)))
        command = helper.get_image_specific_config_option(
            options=all_options.get('{}{}'.format(CONFIGSECTIONPREFIX, image_to_use)),
            option_name="cmd")

        output_vol = helper.get_image_specific_config_option(
            options=all_options.get('{}{}'.format(CONFIGSECTIONPREFIX, image_to_use)),
            option_name="primary_source_dir", optional=True)
        internal_vol = helper.get_image_specific_config_option(
            options=all_options.get('{}{}'.format(CONFIGSECTIONPREFIX, image_to_use)),
            option_name="primary_dest_dir", optional=True)
        docker_config_operation = helper.get_image_specific_config_option(
            options=all_options.get('{}{}'.format(CONFIGSECTIONPREFIX, image_to_use)), option_name="cmd_operation",
            optional=True)

        approved_operations = helper.get_image_specific_config_option(
            options=all_options.get('{}{}'.format(CONFIGSECTIONPREFIX, image_to_use)), option_name="{}_approved_operations".format(image_to_use),
            optional=True)

        image_fullname = helper.get_image_specific_config_option(
            options=all_options.get('{}{}'.format(CONFIGSECTIONPREFIX, image_to_use)), option_name="docker_image",
            optional=True)

        docker_extra_kwargs = self.parse_extra_kwargs(options=all_options.get('{}{}'.format(CONFIGSECTIONPREFIX, image_to_use)))

        container_volume_bind = {output_vol: {'bind': internal_vol, 'mode': 'rw'}} if output_vol and internal_vol else dict()

        if docker_extra_kwargs.get('volumes', False):
            LOG.debug("Found a Volume in Extra Kwargs. Appending to existing volume definition")

            # Split the volumes string by commas to get each volume binding
            for volume in docker_extra_kwargs.get('volumes').split(','):

                # Split the volume into each of its params
                volume_params = volume.split(':')

                if volume == docker_extra_kwargs.get('volumes').split(',')[0] and not internal_vol:
                    internal_vol = volume_params[1]
                # Format the volume data into a dict and update.
                container_volume_bind.update({volume_params[0]: {'bind': volume_params[1], 'mode': volume_params[2]}})

            # After we finish looping
            del docker_extra_kwargs['volumes']  # Remove the volume
        docker_extra_kwargs['volumes'] = container_volume_bind

        # If config is not set at all for approved operations, all operations are approved
        # Ensure the operation that will be done is an approved one
        # An operation set as a function field will take priority over one set as a app.config to enable multiple workflows with different operations
        operation = docker_operation or docker_config_operation
        if approved_operations and operation not in approved_operations:
            raise ValueError(u"Operation is not found in the list of approved operations. Review your app.config and add {} to the approved_operations for the {} image to fix this. ".format(operation, image_to_use))
        escaped_args.update({
            "internal_vol": render("{{internal_vol|%s}}" % "sh", {"internal_vol": internal_vol}),
            "operation": render("{{operation|%s}}" % "sh",
                                {"operation": operation})
        })
        return render(command, escaped_args), docker_extra_kwargs, image_fullname, operation

    def gather_container_stats(self, container_id):
        """
        Used to gather the execution stats for a Docker Container by its ID
        :param container_id:
        :return:
        """
        return self.api_client.stats(container=container_id, stream=False)
