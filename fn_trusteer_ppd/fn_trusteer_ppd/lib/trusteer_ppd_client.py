# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
import os
from base64 import b64encode
import logging
from urllib.parse import urljoin

from resilient_lib import RequestsCommon, validate_fields, IntegrationError


LOG = logging.getLogger(__name__)

PACKAGE_NAME = "fn_trusteer_ppd"

# Trusteer REST API header
HEADER = { 'Content-Type': 'application/json' }

# URL prefix to refer back to your console for a specific alert, event, etc.
ENDPOINT_URL = "https://{customer_name}.trusteer.com"
REST_API_BASE_URL = "https://{customer_name}-api.trusteer.com"
PINPOINT_FEEDBACK_URL = "/api/{api_version}/update_pinpoint_session_resolution"
LINKBACK_URL = "{base_url}/search-results?{id_type}={id}"

# E N D P O I N T S

class TrusteerPPDClient():
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
        validate_fields(["api_token", "api_version", "customer_name", "client_auth_cert", "client_auth_key"],
                         app_configs)
        self.rc = rc
        self.package_name = package_name

        # required configs
        self.api_token = app_configs.get("api_token")
        self.api_version = app_configs.get("api_version")
        self.customer_name = app_configs.get("customer_name")

        # Make sure the client auth cert and key files are there.
        self.client_auth_key = app_configs.get("client_auth_key")
        self.client_auth_cert = app_configs.get("client_auth_cert")
        if not os.path.isfile(self.client_auth_cert):
            raise IntegrationError("No Trusteer client_auth_cert file found.")
        if not os.path.isfile(self.client_auth_key):
            raise IntegrationError("No Trusteer client_auth_key file found.")

        self.endpoint_url = ENDPOINT_URL.format(customer_name=self.customer_name)
        self.rest_api_base_url = REST_API_BASE_URL.format(customer_name=self.customer_name)
        self.headers = HEADER

    def _get_uri(self, cmd: str) -> str:
        """
        Build API url

        :param cmd: portion of API: alerts, endpoints, policies
        :type cmd: str
        :return: complete URL
        :rtype: str
        """
        return urljoin(self.rest_api_base_url, cmd.format(api_version=self.api_version))


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
        # Get Trusteer Pinpoint REST API URL for feedback
        url = self._get_uri(PINPOINT_FEEDBACK_URL)
        data = {
            "api_key": self.api_token,
            "app_id": application_id,
            "customer_session_id": session_id,
            "feedback": feedback
        }
        # If session is confirmed fraud then also set the fraud mo if specified
        if fraud_mo and feedback == "confirmed_fraud":
            data["fraud_mo"] = fraud_mo

        response = self.rc.execute("POST",
                                   url=url,
                                   json=data,
                                   headers=self.headers)
        response_json = response.json()

        return response_json
