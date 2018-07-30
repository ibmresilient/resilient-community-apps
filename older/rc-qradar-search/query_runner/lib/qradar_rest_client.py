"""# A simple REST client for QRadar SIEM and Ariel"""
import urllib
import ssl
import logging
try:
    from urllib.parse import urlencode
except:
    # Python2
    from urllib import urlencode
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

LOG = logging.getLogger(__name__)

# For details of the QRadar API, see:
# <https://github.com/ibm-security-intelligence/api-samples/blob/master/qradar_api_guide.pdf>

EVENT_FIELDS = ["*"]

# The default set of fields we want from an offense
ID_ONLY = ["id"]


class TLSHttpAdapter(HTTPAdapter):
    """Adapter that ensures that we use best-available TLS version."""
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       assert_hostname=False,
                                       ssl_version=ssl.PROTOCOL_SSLv23)


class SimpleHTTPException(Exception):
    """Exception for HTTP errors."""
    def __init__(self, response):
        """
        Args:
          response - the Response object from the get/put/etc.
        """
        if isinstance(response, str):
            text = response
            status = 500
        else:
            text = response.text
            status = response.status_code

        LOG.error("SimpleHTTPException %s", status)
        self.response = response


def _raise_if_error(response):
    """raise error for failed GET request"""
    if response.status_code != 200:
        raise SimpleHTTPException(response)


def _raise_if_posterror(response):
    """raise error for failed POST request"""
    if response.status_code not in [200, 201]:
        LOG.error(response.text)
        raise SimpleHTTPException(response)


class QRadarClient(object):
    """A simple REST client class for QRadar"""

    def __init__(self, base_url, auth_token, version='7.0', verify=True):

        self.base_url = base_url
        self.verify = verify

        # Set up the security credentials.
        self.auth = {'SEC': auth_token}

        self.headers = {'Accept': 'application/json'}
        if version:
            self.headers['Version'] = version
        self.headers.update(self.auth)

        self.session = requests.Session()
        # self.session.mount('https://', TLSHttpAdapter())

    # Generic REST calls

    def get(self, uri, headers=None, params=None):
        """Generic GET"""
        if headers is None:
            header = self.headers
        else:
            header = self.headers.copy()
            header.update(headers)
        url = "{0}/api/{1}".format(self.base_url, uri)
        LOG.info("GET %s", url)
        response = self.session.get(url, headers=header, verify=self.verify, params=params)
        _raise_if_error(response)
        return response.json()

    def post(self, uri, headers=None, params=None):
        """Generic POST"""
        if headers is None:
            header = self.headers
        else:
            header = self.headers.copy()
            header.update(headers)
        url = "{0}/api/{1}".format(self.base_url, uri)
        if params:
            url = url + '?' +self.encode_params(params)
        LOG.info("POST %s", url)
        response = self.session.post(url, headers=header, verify=self.verify)
        _raise_if_posterror(response)
        return response.json()

    def delete(self, uri, headers=None, params=None):
        """Generic DELETE"""
        if headers is None:
            header = self.headers
        else:
            header = self.headers.copy()
            header.update(headers)
        url = "{0}/api/{1}".format(self.base_url, uri)
        response = self.session.delete(url, headers=header, verify=self.verify, params=params)
        return response

    def get_search_status(self, search_id):
        """ Retrieve ariel search status """
        url = "ariel/searches/{0}".format(search_id)
        search_status = self.get(url)
        if search_status:
            LOG.info("Search '%s' progress: '%s' status: '%s'",
                     search_id,
                     search_status["progress"],
                     search_status["status"])
        return search_status

    @staticmethod
    def encode_params(params):
        """ encode params for use in QRadar URL """
        encoded_params = urlencode(params)
        encoded_params = encoded_params.replace('+', '%20').replace(r'%28', '(').replace(r'%29', ')').replace(r'%27', "'").replace(r'%2A', '*')
        LOG.debug(str(params) + "\n" + encoded_params)
        return encoded_params
