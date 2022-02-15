#
import logging
from urllib.parse import urljoin
from resilient_lib import str_to_bool, readable_datetime

LOG = logging.getLogger(__name__)

HEADER = { 'Content-Type': 'application/json' }

class EndPointCommon():
    def __init__(self, rc, options):
        self.api_key = options['api_key']
        self.api_secret = options['api_secret']
        self.reaqta_url = options['reaqta_url']
        self.api_version = options['api_version']
        self.rc = rc
        self.verify = str_to_bool(options.get("cafile", "false"))

    def authenticate(self, headers):
        params = {
            "secret": self.api_secret,
            "id": self.api_key
        }

        auth_url = self._get_uri('authenticate')

        response = self.rc.execute("POST", auth_url, json=params, headers=headers, verify=self.verify)
        return response.json()['token']

    def get_entities_since_ts(self, query_field_name, timestamp, **kwargs):
        query = {
            query_field_name: readable_datetime(timestamp)
        }

        # add any additional query parameters
        if kwargs:
            for k,v in kwargs:
                query[k] = v

        self.token = self.authenticate(HEADER)
        self.header = self._make_header(self.token)
        response = self.rc.execute("GET", self._get_uri("alerts"), params=query, headers=self.header, verify=self.verify)
        # "result":[],"nextPage":"","remainingItems":0}
        return response.json()

    def get_next_entities(self, next_url):
        response = self.rc.execute("GET", next_url, headers=self.header, verify=self.verify)
        # "result":[],"nextPage":"","remainingItems":0}
        return response.json()

    def _get_uri(self, cmd):
        return urljoin(urljoin(self.reaqta_url, self.api_version), cmd)

    def _make_header(self, token):
        header = HEADER.copy()
        header['Authorization'] = "Bearer {}".format(token)

        return header

    def make_linkback_url(self, template_uri, entity_id):
        """Create a url to link back to the endpoint alert, case, etc.

        Args:
            template (str): portion of url to join with base url
            entity_id (str/int): id representing the alert, case, etc.

        Returns:
            str: completed url for linkback
        """
        return urljoin(self.reaqta_url, template_uri.format(entity_id))
