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
PINPOINT_FEEDBACK_URL = "/api/{api_version}/update_pinpoint_session_resolution"

# URL prefix to refer back to your console for a specific alert, event, etc.
LINKBACK_URL = "{base_url}/search-results?{id_type}={id}&type=session"

# E N D P O I N T S

class AppCommon():
    def __init__(self, package_name: str, app_configs: dict) -> None:
        """
        Initialize the parameters needed to communicate to the endpoint solution

        :param rc: object to resilient_lib.requests_common for making API calls
        :type rc: ``resilient_lib.RequestsCommon``
        :param package_name: name of the package to be created
        :type package_name: str
        :param app_configs: app.config parameters in order to authenticate and access the endpoint
        :type app_configs: dict
        """
        self.package_name = package_name

        # required configs
        self.api_token = app_configs.get("api_token")
        self.endpoint_url = app_configs.get("endpoint_url")
        self.api_version = app_configs.get("api_version")
        self.base_url = urljoin(self.endpoint_url, "-api/api/{version}".format(version=self.api_version))
        self.verify = _get_verify_ssl(app_configs)

        self.header = self._make_header(self.api_token)
        self.rc = RequestsCommon()

    def _get_uri(self, cmd: str) -> str:
        """
        Build API url

        :param cmd: portion of API: alerts, endpoints, policies
        :type cmd: str
        :return: complete URL
        :rtype: str
        """
        return urljoin(self.base_url, cmd.format(api_version=self.api_version))

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

    def make_linkback_url(self, id: str, id_type: str, linkback_url : str = LINKBACK_URL) -> str:
        """
        Create a url to link back to the endpoint entity

        :param id: A PUID or the Device ID of the session in Trusteer
        :type id: str
        :param id_type: 'puid' or 'device_id' indicating the type of id's to link back to in Trusteer
        :type id: str
        :param linkback_url: _description_, defaults to LINKBACK_URL
        :type linkback_url: str|int, optional
        :return: completed url for linkback
        :rtype: str
        """
        return linkback_url.format(base_url=self.endpoint_url, id_type=id_type, id=id)

    def update_classification(self, session_id: str, application_id: str, feedback: str, fraud_mo: str) -> dict:
        """_summary_

        Args:
            classification (str): The new resolution value for the record. 
            The possible values are:
                confirmed_fraud - You confirm that the session was fraudulent whether Pinpoint generated an alert or not.
                confirmed_legitimate - Pinpoint generated an alert and you confirm that the session is not fraudulent.
                undetermined - Pinpoint generated an alert and you are not able to determine whether the session was fraudulent.
                pending_confirmation - Default, waiting for your classification.

            fraud_mo (str): fraud_mo
                (Optional) If you set feedback to confirmed_fraud and confirm that the session was fraudulent, 
                            you can also set the specific type of fraud that occurred. If you are not sure of the type of 
                            fraud, do not set the fraud_mo field.

                account_takeover - An attempt was made to access the account using stolen credentials from the fraudster device.
                remote_access_tool - An attempt was made to access the account using a device that is suspected to be remotely controlled by another device.
                first_party - The account owner is attempting to commit fraud.
                social_engineering - The account owner is the victim of a social-engineering attack.
                stolen_device - An attempt was made to access the account from a stolen device.
                mule_account - The account is a mule account that is used by fraudsters

        Returns:
            dict: _description_
        """
        # URL: https://orgname-api.trusteer.com/api/v1/update_pinpoint_session_resolution
        url = self._get_uri(PINPOINT_FEEDBACK_URL)
        data = {
            "app_id": application_id,
            "customer_session_id": session_id,
            "feedback": feedback,
            "api_key": self.api_token
        }
        # If confirmed fraud, set fraud_mo if it is specified
        if fraud_mo and feedback == "confirmed_fraud":
            data["fraud_mo"] = fraud_mo

        response = self.rc.execute("POST",
                                   url=url,
                                   json=data,
                                   headers=self.header,
                                   verify=self.verify)
        response_json = response.json()

        return response_json

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