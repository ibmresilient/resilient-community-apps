# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
import docker
import logging
import os
import hashlib
import base64
import tempfile
import shutil
from requests.exceptions import ConnectionError
from .errors import IntegrationError

LOG = logging.getLogger(__name__)
THUG_IMAGE = 'honeynet/thug:latest'


class DockerClientError(Exception):
    def __init__(self):
        super(DockerClientError, self).__init__('Docker is not installed or started')


class ThugUtils:
    def __init__(self, opts):
        self.thug_dir = get_config_option(opts, 'thug_dir')

    def run_thug(self, client, args, url):
        try:
            # Create temporary directory to store thug output
            output_dir = tempfile.mkdtemp(dir=self.thug_dir)

            # Specify an output directory for thug results in docker
            thug_log_dir = '/{}'.format(md5(url))

            # Create command
            command = 'python /opt/thug/src/thug.py -FZM -n {} {} {}'.format(thug_log_dir, args, url)

            # Mount output_dir to thug_log_dir and run thug, remove container when thug is done running
            thug_logs = {output_dir: {'bind': thug_log_dir, 'mode': 'rw'}}
            thug_container = client.containers.run('honeynet/thug', volumes=thug_logs, command=command, detach=True)
            status = thug_container.wait()
            thug_container.remove()

            # Get output directory
            wanted_analysis_path = os.path.join(output_dir, 'analysis')

            # test for files. If missing, the analysis failed
            graph_file = os.path.join(wanted_analysis_path, 'graph.svg')
            if not os.path.isfile(graph_file):
                raise IntegrationError("Analysis failed. Check iput parameters")

            # Get files results from thug in the analysis directory and convert to base64
            graph_path = os.path.join(wanted_analysis_path, 'graph.svg')
            with open(graph_path, "rb") as f:
                data = f.read()
                thug_graph_svg_b64 = base64.b64encode(data)

            json_path = os.path.join(wanted_analysis_path, 'json', 'analysis.json')
            with open(json_path, "rb") as f:
                report_json = f.read()
            maec11_path = os.path.join(wanted_analysis_path, 'maec11', 'analysis.xml')
            with open(maec11_path, "rb") as f:
                data = f.read()
                maec11_b64 = base64.b64encode(data)
        finally:
            try:
                # Remove the temporary directory and its contents
                shutil.rmtree(output_dir)
            except UnboundLocalError:
                LOG.debug('Failed to create temporary directory, check filepath in config file')

        results = {
            'url': url,
            'report_json': report_json.decode("utf-8"),
            'graph_svg': thug_graph_svg_b64.decode("utf-8"),
            'report_xml': maec11_b64.decode("utf-8"),
            'exit_status': status[u'StatusCode'],
            'error': status[u'Error']
        }
        return results


def get_thug_client():
    """Setup a connection to docker and pull thug image if not pulled"""

    # Get connection to docker
    try:
        client = docker.from_env()
        client.ping()
    except ConnectionError:
        LOG.debug('Error connecting to docker')
        raise DockerClientError()

    # Get thug image
    try:
        client.images.get(THUG_IMAGE)
    except docker.errors.ImageNotFound:
        LOG.info('Docker image was not found, pulling image')
        client.images.pull(THUG_IMAGE)

    return client


def md5(my_val):
    """Creates an MD5 from given value"""
    m_val = hashlib.md5()
    m_val.update(my_val.encode('utf-8'))
    return m_val.hexdigest()


def get_config_option(options, option_name):
    """If the specified option is in options, return it. If it isn't raise an error"""
    option = options.get(option_name)

    if option is None:
        err = "'{}' is mandatory and not set in the app.config file. This option must be set to run this function"
        raise ValueError(err.format(option_name))
    else:
        return option