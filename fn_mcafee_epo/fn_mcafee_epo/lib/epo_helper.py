# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import json
import sys
if sys.version_info.major < 3:
    from urlparse import urljoin
else:
    from urllib.parse import urljoin
from resilient_lib import  RequestsCommon, validate_fields, IntegrationError


def init_client(opts, options):
    validate_fields(["epo_url", "epo_username", "epo_password", "epo_trust_cert"], options)
    url = options.get("epo_url")
    username = options.get("epo_username")
    password = options.get("epo_password")
    cert_trust = options.get("epo_trust_cert")
    return Client(url, username, password, cert_trust, opts, options)

class Client:
    """
    class to make ePo API calls
    """

    def __init__(self, url, username, password, trust_cert, opts, options):
        self.url = url
        self.username = username
        self.password = password
        self.trust_cert = trust_cert
        self.rc = RequestsCommon(opts, options)

    def request(self, command_name, params):
        """
        make the call to ePO, returning results as json formatted
        :param command_name:
        :param params: ePO command params
        :return:
        """
        params_ext = params.copy() if params else {}
        params_ext.setdefault(':output', 'json')

        request_params = {
            "params": params_ext,
            "auth": (self.username, self.password),
            "verify": False if self.trust_cert == "false" else True
        }
        url = urljoin(self.url, 'remote/{}'.format(command_name))

        # Make request
        r = self.rc.execute_call_v2("get", url, **request_params)

        status_code = r.status_code
        if status_code >= 300 or not r.text.startswith('OK'):
            raise IntegrationError("find tags failed: {}".format(r.text))

        # convert result to true json
        try:
            result = json.loads(b_to_s(r.text).replace("OK:", ""))
        except json.decoder.JSONDecodeError:
            result = {}

        return result

def b_to_s(value):
    try:
        return value.decode()
    except:
        return value

def get_list(tags):
    tag_list = [tags]
    try:
        tag_list = json.loads(tags.replace("'", '"').replace('u"', '"'))
    except:
        pass

    return tag_list
