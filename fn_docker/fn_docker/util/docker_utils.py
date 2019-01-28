# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
import logging
import docker


LOG = logging.getLogger(__name__)
import os

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
            self.api_client = docker.APIClient(base_url=os.environ.get('DOCKER_HOST', 'unix://var/run/docker.sock'))
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
                if 'docker_extra' in k}

    def inspect_container(self, containerid):
        return self.api_client.inspect_container(containerid)



