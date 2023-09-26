# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

from logging import getLogger
from json import loads, decoder
from urllib.parse import urljoin
from resilient_lib import RequestsCommon, validate_fields, IntegrationError

PACKAGE_NAME = "fn_mcafee_epo"
SIXTY_SECONDS = 60 # Default timeout
LOG = getLogger()

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

def clear(rest_client, table_name, incident_id):
    """
    Clear data in given table on SOAR
    :param res_rest_client: SOAR rest client connection
    :param table_name: API access name of the table to clear
    :param incident_id: SOAR ID for the incident
    :return: None
    """
    try:
        rest_client.delete(f"/incidents/{incident_id}/table_data/{table_name}/row_data?handle_format=names")
        LOG.info(f"Data in table {table_name} in incident {incident_id} has been cleared")

    except Exception as err_msg:
        LOG.error(f"Failed to clear table: {table_name} error: {err_msg}")
        raise IntegrationError(f"Error while clearing table: {table_name}")

class Client:
    """Class to make ePo API calls"""
    def __init__(self, url, username, password, trust_cert, opts, options):
        self.url = url
        self.username = username
        self.password = password
        self.trust_cert = trust_cert
        self.rc = RequestsCommon(opts, options)
        self.timeout = self.rc.get_timeout()
        if not self.timeout or self.timeout < SIXTY_SECONDS:
            self.timeout = SIXTY_SECONDS

    def request(self, command_name, params):
        """
        Make the call to ePO, returning results as json formatted
        :param command_name: Name of the command
        :param params: ePO command params
        :return: Response of request to the server
        """
        params_ext = params.copy() if params else {}
        params_ext.setdefault(':output', 'json')

        request_params = {
            "params": params_ext,
            "auth": (self.username, self.password),
            "verify": False if self.trust_cert.lower() == "false" else True,
            "timeout": self.timeout
        }
        url = urljoin(self.url, f'remote/{command_name}')

        # Make request
        r = self.rc.execute_call_v2("get", url, **request_params)

        if r.status_code >= 300 or not r.text.startswith('OK'):
            raise IntegrationError(f"Failed: {r.text}")

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
