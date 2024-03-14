# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import json
import logging
import traceback

API_VERSION = "/api/v1"

class InvalidCredentials(Exception):
    """Raise when user has entered wrong password or username"""
    pass

class PasswordChangeRequired(Exception):
    """Raise when the user's password needs to be changed"""
    pass

class StaxxUnreachable(Exception):
    """Raised when the API cannot make contact with the Staxx appliance"""
    pass

JSON_HEADERS =  {'Content-type': 'application/json', 'Accept': 'text/plain'}

class StaxxClient:
    def __init__(self, host, username, password, request_common):
        self.host = host
        self.username = username
        self.password = password
        self.request_common = request_common
        self.token = self.__public_login__(username, password)
        self.log = logging.getLogger(__name__)

    def __make_post__(self, url, **kwargs):
        headers = JSON_HEADERS.copy()
        headers.update(kwargs.get("headers",{}))
        url = self.make_url(url)
        if "params" in kwargs:
            return self.request_common.execute_call_v2("post",
                                                       url,
                                                       params=kwargs.get("params"),
                                                       headers=headers
                                                       )
        try:
            return self.request_common.execute_call_v2("post",
                                                       url,
                                                       data=kwargs.get("payload", {}),
                                                       headers=headers,
                                                       verify=False
                                                       )
        except Exception as e:
            traceback.format_exception(e)
            raise StaxxUnreachable("Staxx appliance is down or is taking too long to respond")


    def __make_get__(self, url, **params):
        url = self.host + url
        r = self.session.get(url, params=params)
        if 'json' in r.headers.get('content-type'):
            return r.json()
        else:
            return r.text

    def __public_login__(self, username, password):
        payload = {"username": username, "password": password}
        response_json = self.__make_post__(payload=json.dumps(payload),url="/login").json()
        try:
            return response_json['token_id']
        except Exception as e:
            raise InvalidCredentials("The credentials are incorrect")

    def import_staxx_intel(self, **kwargs):
        """
        :param kwargs: tlp - RED,WHITE,AMBER...etc
                    severity - low,medium....etc
                    threat_type - phish,malware..etc
                    auto_approve - yes/no
                    confidence - 0-100
                    tags - comma separated list
                    intel_str - indicators
        :return:
        """
        url = self.make_url("/import_intel")
        data = {k:kwargs[k] for k in kwargs if k!="file"}
        data["token"] = self.token
        payload={"import_params":json.dumps(data)}

        self.log.debug(payload)

        resp = self.request_common.execute_call_v2("post",
                                                   url,
                                                   data=payload,
                                                   verify=False
                                                   )
        resp_json = resp.text
        return resp_json

    def query(self, query=None, size=10):
        url = self.make_url("/intelligence")

        # build the entire query string
        payload = {
            "token": self.token,
            "size": size,
            "type": "json",
            "query": query
        }

        self.log.debug(payload)

        resp = self.request_common.execute_call_v2("post",
                                                   url,
                                                   data=json.dumps(payload),
                                                   verify=False,
                                                   headers=JSON_HEADERS
                                                   )

        resp_json = resp.json()
        return resp_json

    def make_url(self, endpoint):
        return "{}{}{}".format(self.host, API_VERSION, endpoint)
