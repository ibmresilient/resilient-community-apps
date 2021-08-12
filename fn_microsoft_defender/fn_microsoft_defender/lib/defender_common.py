# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import calendar
import logging
import time
from msal import ConfidentialClientApplication
from resilient_lib import RequestsCommon, IntegrationError
from simplejson.errors import JSONDecodeError

PACKAGE_NAME = "fn_microsoft_defender"
INDICATOR_URL = "api/indicators"
MACHINES_URL = "api/machines"
MACHINE_ACTIONS_URL = "api/machineactions"
PACKAGE_URI = "GetPackageUri"
FILES_URL = "api/files/{}/machines"
MACHINES_FILTER = {
     "filter_by_name": "startswith(computerDnsName,'{}')"
}
ALERTS_URL = "api/alerts"

AUTH_URL = "https://login.microsoftonline.com/{tenant_id}" # /v2.0  https://login.microsoftonline.com/82319d65-80f7-431f-8ee7-57bae5b231c2/oauth2/token
RESOURCE_URI = "https://api.securitycenter.windows.com"
DEFENDER_SCOPE = [
    "https://securitycenter.onmicrosoft.com/windowsatpservice/.default"
]

LOG = logging.getLogger(__name__)

class DefenderAPI():
    """[class to manage authentication and API calls to Defender ATP]
    """
    def __init__(self, tenant_id, client_id, app_secret, opts, options, rc=None):
        """build the connection class for Defender ATP

        Args:
            tenant_id ([type]): [description]
            client_id ([type]): [description]
            app_secret ([type]): [description]
            opts ([dict]): [description]
            options ([dict]): [description]
            rc ([object]): RequestCommon if passed in
        """
        self.api_url = options.get("api_url")
        if rc:
            self.rc = rc
        else:
            self.rc = RequestsCommon(opts, options)

        authority = AUTH_URL.format(tenant_id=tenant_id)
        self.access_token = None
        self.app = ConfidentialClientApplication(
            client_id,
            authority=authority,
            client_credential=app_secret,
            proxies=self.rc.get_proxies(),
            timeout=self.rc.get_timeout()
        )

    def defender_authenticate(self, app_scope=DEFENDER_SCOPE):
        """[authenticate to defender and get the access token]

        Args:
            app_scope ([str], optional): [scope of authentication]. Defaults to DEFENDER_SCOPE.

        Raises:
            IntegrationError: [if authentication errors occur]

        Returns:
            [str]: [access token]
        """
        result = self.app.acquire_token_silent(app_scope, account=None)

        if not result:
            result = self.app.acquire_token_for_client(scopes=app_scope)

        if "access_token" in result:
            self.access_token = result['access_token']
            return True

        msg = u"Unable to authenticate to MS Azure: Error: {}\nDescription: {}\nCorrelation_id: {}"\
                .format(result.get("error"), result.get("error_description"), result.get("correlation_id"))
        raise IntegrationError(msg)

    def make_header(self, content_type="application/json"):
        """build headers needed for API calls. It will include the Defender access token

        Args:
            content_type (str, optional): Defaults to "application/json".

        Returns:
            [dict]: [api headers to use]
        """
        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        if content_type:
            headers['Content-Type'] = content_type

        return headers

    def call(self, url_endpoint, payload=None, oper="GET", content_type="application/json"):
        """make the API call to Defender

        Args:
            url_endpoint ([type]): [description]
            payload ([dict], optional): [payload to send]. Defaults to None.
            oper (str, optional): ["GET", "POST", "DELETE"]. Defaults to "GET".
            content_type (str, optional): [value for content_type]. Defaults to "application/json".

        Returns:
            [json]: [returned API payload]
        """
        self.defender_authenticate()
        url = "/".join([self.api_url, url_endpoint])
        headers = self.make_header(content_type)

        if oper in ["POST", "PATCH"]:
            result, status = self.rc.execute_call_v2(oper, url, json=payload, headers=headers, callback=callback_response)
        else:
            result, status = self.rc.execute_call_v2(oper, url, params=payload, headers=headers, callback=callback_response)

        reason = None
        if not status:
            reason = result['error'].get('message')

        return result, status, reason

    def wait_for_action(self, url, iter=10, wait=30):
        """[summary]

        Args:
            url ([type]): [description]
            iter (int, optional): [description]. Defaults to 10.
            wait (int, optional): [description]. Defaults to 30.
        """
        for _ in range(0, iter):
            time.sleep(wait)
            result, status, reason = self.call(url, oper="GET")
            if not status or (status and result.get('status') != 'Pending'):
                break

        return result, status, reason


def callback_response(response):
    """call back routine to review HTTP status code

    Args:
        response ([requests Response]): [object returned from Requests API call]

    Returns:
        [json]: [payload from API call]
        [bool]: True is call was successful
    """
    status = bool(response.status_code <= 300)

    try:
        result = response.json()
    except JSONDecodeError:
        if status:
            result = {}
        else:
            result = {
                "error": {
                    "code": response.status_code,
                    "message": str(response.status_code)
                }
            }

    return result, status

def convert_date(value):
    """convert UTC formatted timestamp to epoch value

    Args:
        value ([str]): [UTC formatted timestamp]

    Returns:
        [number]: [Epoch value]
    """
    if not value:
        return value

    # Defender can return 7 millisecond characters which time.strptime cannot parse
    # strip milliseconds as 7 characters cannot be parsed by %f
    utc_time = time.strptime(value[:value.rfind('.')], "%Y-%m-%dT%H:%M:%S")
    return calendar.timegm(utc_time)*1000

def make_filter_url(url, filter_template, value):
    """[make an api call using odata filters]

    Args:
        url ([str]): [base url]
        filter_template ([str]): [filter template]
        value ([str]): [substitution value]
    Return:
        update url ([str])
    """
    if filter_template in MACHINES_FILTER:
        return "?$filter=".join([url, MACHINES_FILTER[filter_template].format(value)])
    else:
        raise ValueError("{} is invalid filter template name".format(filter_template))
