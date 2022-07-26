# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

from json import loads, decoder
from urllib.parse import urljoin
from resilient_lib import RequestsCommon, validate_fields, IntegrationError

PACKAGE_NAME = "fn_mcafee_epo"

def init_client(opts, options):
    validate_fields(["epo_url", "epo_username",
                    "epo_password", "epo_trust_cert"], options)
    return Client(
        options.get("epo_url"),
        options.get("epo_username"),
        options.get("epo_password"),
        options.get("epo_trust_cert"),
        opts,
        options
    )

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
        self.timeout = options.get("timeout", 60)

    def request(self, command_name, params):
        """
        Make the call to ePO, returning results as json formatted
        :param command_name:
        :param params: ePO command params
        :param timeout: Default timeout is 30 seconds
        :return:
        """
        params_ext = params.copy() if params else {}
        params_ext.setdefault(':output', 'json')

        request_params = {
            "params": params_ext,
            "auth": (self.username, self.password),
            "verify": False if self.trust_cert.lower() == "false" else True
        }
        url = urljoin(self.url, 'remote/{}'.format(command_name))

        # Make request
        r = self.rc.execute_call_v2("get", url, **request_params, timeout=self.timeout)

        if r.status_code >= 300 or not r.text.startswith('OK'):
            raise IntegrationError("find tags failed: {}".format(r.text))

        # Convert result to true json
        try:
            result = loads(b_to_s(r.text).replace("OK:", ""))
        except decoder.JSONDecodeError:
            result = {}

        return result

def b_to_s(value):
    try:
        return value.decode()
    except Exception:
        return value

def get_list(tags):
    tag_list = [tags]
    try:
        tag_list = loads(tags.replace("'", '"').replace('u"', '"'))
    except Exception:
        pass

    return tag_list
