import docker
import logging
import os
import hashlib
from requests.exceptions import ConnectionError
import base64
import tempfile
import shutil

LOG = logging.getLogger(__name__)


class DockerClientError(Exception):
    def __init__(self):
        super(DockerClientError, self).__init__('Docker is not installed or started')


class thug_utils:
    def __init__(self, opts):
        self.thug_dir = get_config_option(opts, 'thug_dir')

    def run_thug(self, client, args, url):
        try:
            # Create temporary directory to store thug output
            output_dir = tempfile.mkdtemp(dir=self.thug_dir)

            # Specify an output directory for thug results in docker
            thug_log_dir = '/{}'.format(md5(url))

            # Create command
            command = 'python /opt/thug/src/thug.py -n {} {} {}'.format(thug_log_dir, args, url)

            # Mount output_dir to thug_log_dir and run thug, remove container when thug is done running
            thug_logs = {output_dir: {'bind': thug_log_dir, 'mode': 'rw'}}
            thug_container = client.containers.run('honeynet/thug', volumes=thug_logs, command=command, detach=True)
            thug_container.wait()
            thug_container.remove()

            # Get output directory
            wanted_analysis_path = os.path.join(output_dir, 'analysis')

            # Get files outputted from thug in the analysis directory and convert to base64
            graph_path = os.path.join(wanted_analysis_path, 'graph.svg')
            with open(graph_path, "rb") as f:
                data = f.read()
                thug_graph_svg_b64 = base64.b64encode(data)

            json_path = os.path.join(wanted_analysis_path, 'json', 'analysis.json')
            with open(json_path, "rb") as f:
                data = f.read()
                thug_report_b64 = base64.b64encode(data)
        except Exception as e:
            LOG.debug('An error occurred while running thug. This is most likely an issue with a temporary directory '
                      'not being able to be mounted into docker or an issue with the specified arguments')
            raise e
        finally:
            try:
                # Remove the temporary directory and its contents
                shutil.rmtree(output_dir)
            except UnboundLocalError:
                LOG.debug('Failed to create temporary directory, check filepath in config file')

        results = {
            'report_json': thug_report_b64,
            'graph_svg': thug_graph_svg_b64
        }

        return results


def get_thug_client():
    """Setup a connection to docker and pull thug image if not pulled"""

    # Get connection to docker
    try:
        client = docker.from_env()
        client.ping()
    except (ConnectionError):
        LOG.debug('Error connecting to docker')
        raise DockerClientError()

    # Get thug image
    try:
        client.images.get('honeynet/thug:latest')
    except docker.errors.ImageNotFound:
        LOG.info('Docker image was not found, pulling image')
        client.images.pull('honeynet/thug:latest')

    return client


def md5(my_val):
    """ Creates an MD5 from given value"""
    m_val = hashlib.md5()
    m_val.update(my_val)
    return m_val.hexdigest()


def get_config_option(options, option_name):
    """If the specified option is in options, return it. If it isn't raise an error"""
    option = options.get(option_name)

    if option is None:
        err = "'{}' is mandatory and not set in the app.config file. This option must be set to run this function"
        raise ValueError(err.format(option_name))
    else:
        return option


thug_utils = thug_utils({'thug_dir': '/tmp'})
args = '-FZM'
print(thug_utils.run_thug(get_thug_client(), args, 'https://google.com'))