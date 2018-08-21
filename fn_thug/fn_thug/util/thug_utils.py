import docker
import logging
import os
import hashlib
from requests.exceptions import ConnectionError
import base64
import tempfile
import shutil

LOG = logging.getLogger(__name__)
DIR = '/Users/Keenan.Mach@ibm.com/logs'

class DockerClientError(Exception):
    def __init__(self):
        super(DockerClientError, self).__init__('Docker is not installed or started')


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


def run_thug(client, args, url):
    try:
        # Create command
        command = 'python /opt/thug/src/thug.py {} {}'.format(args, url)

        DIR = tempfile.mkdtemp(dir='/tmp')

        thug_logs = {DIR: {'bind': '/logs', 'mode': 'rw'}}
        thug_container = client.containers.run('honeynet/thug', volumes=thug_logs, command=command, detach=True)
        # thug_container = client.containers.run('honeynet/thug', command, detach=True)
        thug_container.wait()
        thug_container.remove()
        art_val_md5 = md5(url)

        site_analysis_dir = os.path.join(DIR, art_val_md5)
        all_analysis_dir = os.listdir(site_analysis_dir)
        wanted_analysis_dir = all_analysis_dir[-1]
        wanted_analysis_path = os.path.join(DIR, art_val_md5, wanted_analysis_dir, 'analysis')

        graph_path = os.path.join(wanted_analysis_path, 'graph.svg')
        with open(graph_path, "rb") as f:
            data = f.read()
            thug_png_b64 = base64.b64encode(data)
            print('png: ' + thug_png_b64)

        json_path = os.path.join(wanted_analysis_path, 'json', 'analysis.json')
        with open(json_path, "rb") as f:
            data = f.read()
            thug_report_b64 = base64.b64encode(data)
            print('report: ' + thug_report_b64)
    except Exception as e:
        LOG.debug('An error occurred while running thug. This is most likely an issue with a temporary directory not'
                  'being able to be mounted into docker')
        raise e
    finally:
        shutil.rmtree(DIR)


def md5(my_val):
    """ Creates an MD5 from given value"""
    m_val = hashlib.md5()
    m_val.update(my_val)
    return m_val.hexdigest()