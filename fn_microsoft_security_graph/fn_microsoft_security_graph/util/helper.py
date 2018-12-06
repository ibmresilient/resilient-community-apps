# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import requests
import logging
from cachetools import TTLCache


log = logging.getLogger(__name__)


class MicrosoftGraphHelper:
    def __init__(self, tenant_id, client_id, client_secret):
        self.__cache = TTLCache(maxsize=1, ttl=55*60)  # Set to expire after 55 minutes so it is always fresh

        self.__tenant_id = tenant_id
        self.__client_id = client_id,
        self.__client_secret = client_secret
        self.__get_cache('microsoft_security_graph_access_token')

    def __set_cache(self, d):
        try:
            for k, v in d.iteritems():
                self.__cache.update([(k, v)])
        except AttributeError:
            for k, v in d.items():
                self.__cache.update([(k, v)])

    def __get_cache(self, key):
        if key not in self.__cache:
            self.__set_cache({key: self.__refresh_access_token()})
        return self.__cache.get(key)

    def __refresh_access_token(self):
        token_url = 'https://login.microsoftonline.com/{}/oauth2/v2.0/token'.format(self.__tenant_id)
        post_data = {
            "client_id": self.__client_id,
            "scope": ["https://graph.microsoft.com/.default"],
            "client_secret": self.__client_secret,
            "grant_type": "client_credentials"
        }
        r = requests.post(token_url, data=post_data)
        json = r.json()
        return json.get("access_token")

    def check_status_code(self, response):
        if 200 <= response.status_code <= 299:
            return True
        # Access token has expired, request a new one
        elif response.status_code == 401:
            log.debug(response.content)
            access_token = self.__refresh_access_token()
            self.__set_cache({"microsoft_security_graph_access_token": access_token})
            return False
        else:
            raise ValueError("Invalid response from Microsoft Security Graph")

    def microsoft_graph_request(self, method, url, headers, json=None):
        r = None
        for i in list(range(2)):
            if method == "GET":
                r = requests.get(url, headers=headers)
            elif method == "PATCH":
                r = requests.patch(url, headers=headers, json=json)
            else:
                raise ValueError("{} not implemented.".format(method))

            if self.check_status_code(r):
                break
            # If it fails a second time, something more serious is wrong, ie: creds, query, etc.
            elif i == 1:
                log.info(r.content)
                return False
        return r

    def get_access_token(self):
        return self.__get_cache("microsoft_security_graph_access_token")

    def clear_cache(self):
        self.__cache.clear()
