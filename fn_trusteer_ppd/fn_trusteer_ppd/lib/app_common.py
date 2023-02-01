# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

from base64 import b64encode
import logging
from urllib.parse import urljoin

from resilient_lib import str_to_bool, eval_mapping, RequestsCommon


LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_trusteer_ppd"

# Trusteer REST API header
HEADER = { 'Content-Type': 'application/json' }

# URL prefix to refer back to your console for a specific alert, event, etc.
LINKBACK_URL = "{organization_name}/targets/{target_id}"

# E N D P O I N T S

class AppCommon():
    def __init__(self, rc: RequestsCommon, package_name: str, app_configs: dict) -> None:
        """
        Initialize the parameters needed to communicate to the endpoint solution

        :param rc: object to resilient_lib.requests_common for making API calls
        :type rc: ``resilient_lib.RequestsCommon``
        :param package_name: name of the package to be created
        :type package_name: str
        :param app_configs: app.config parameters in order to authenticate and access the endpoint
        :type app_configs: dict
        """
        self.rc = rc
        self.package_name = package_name

        # required configs
        self.api_token = app_configs.get("api_token")
        self.endpoint_url = app_configs.get("endpoint_url")
        self.api_version = app_configs.get("api_version")
        self.organization_name = app_configs.get("organization_name")
        self.verify = _get_verify_ssl(app_configs)
        self.polling_filters = eval_mapping(app_configs.get('polling_filters', ''), wrapper='[{}]')

        self.header = self._make_header(self.api_token)

    def _get_uri(self, cmd: str) -> str:
        """
        Build API url

        :param cmd: portion of API: alerts, endpoints, policies
        :type cmd: str
        :return: complete URL
        :rtype: str
        """
        return urljoin(self.endpoint_url, cmd.format(api_version=self.api_version))

    def _make_header(self, token: str) -> dict:
        """Build API header using authorization token

        :param token: authorization token
        :type token: str
        :return: complete header
        :rtype: dict
        """

        header = HEADER.copy()
        # modify to represent how to build the header
        header['Authorization'] = f"Bearer {token}"

        return header

    def make_linkback_url(self, account_id: str, linkback_url : str = LINKBACK_URL) -> str:
        """
        Create a url to link back to the endpoint entity

        :param account_id: id representing the account in Trusteer
        :type account_id: str
        :param linkback_url: _description_, defaults to LINKBACK_URL
        :type linkback_url: str|int, optional
        :return: completed url for linkback
        :rtype: str
        """
        return urljoin(self.endpoint_url, linkback_url.format(organization_name=self.organization_name, 
                                                              account_id=account_id))

def _get_verify_ssl(app_configs: dict):
    """
    Get ``verify`` parameter from app config.
    Value can be set in the [fn_my_app] section

    :param opts: All of the app.config file as a dict
    :type opts: dict
    :param app_options: App specific configs
    :type app_options: dict
    :return: Value to set ``requests.request.verify`` to. Either a path or a boolean. Defaults to ``True``
    :rtype: bool|str(path)
    """
    # start checking the app specific settings
    verify = app_configs.get("verify")

    # because verify can be either a boolean or a path,
    # we need to check if it is a string with a boolean 
    # value first then, and only then, we convert it to a bool
    # NOTE: that this will then only support "true" or "false"
    # (case-insensitive) rather than the normal "true", "yes", etc...
    if isinstance(verify, str) and verify.lower() in ["false", "true"]:
        verify = str_to_bool(verify)

    return verify