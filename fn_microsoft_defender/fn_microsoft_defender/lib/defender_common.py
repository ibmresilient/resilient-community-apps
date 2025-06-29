# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

from calendar import timegm
from logging import getLogger
from time import strptime, sleep
from msal import ConfidentialClientApplication
from resilient_lib import RequestsCommon, IntegrationError, str_to_bool
from simplejson.errors import JSONDecodeError

PACKAGE_NAME = "fn_microsoft_defender"

INCIDENTS_URL = "api/incidents"
INDICATOR_URL = "api/indicators"
MACHINES_URL = "api/machines"
MACHINE_ACTIONS_URL = "api/machineactions"
MACHINE_RECOMMENDATIONS_URL = "api/machines/{}/vulnerabilities"
PACKAGE_URI = "GetPackageUri"
FILES_URL = "api/files/{}"
FILES_URL_BY_MACHINE = "/".join([FILES_URL, "machines"])
MACHINES_FILTER = {
     "filter_by_name": "startswith(computerDnsName,'{}')",
     "filter_by_id": "id+eq+'{}'"
}
ALERTS_URL = "api/alerts"
EXPAND_PARAMS = {"$expand": "evidence"}
EXPAND_PARAMS_URL = "$expand=evidence"

# Extra parameters possible in sentinel section for requests calls
REQUEST_PARAMS = {
    'verify': str_to_bool,
    'cert': str
}

# Authentication
AUTH_URL = "https://login.microsoftonline.com/{tenant_id}" # /v2.0  https://login.microsoftonline.com/82319d65-80f7-431f-8ee7-57bae5b231c2/oauth2/token
RESOURCE_URI = "https://api.security.microsoft.com"
# "offline_access https://security.microsoft.com/mtp/.default"
DEFENDER_SCOPE = ["offline_access https://api.securitycenter.windows.com/.default"]
DEFENDER_INCIDENT_SCOPE = ["offline_access https://security.microsoft.com/mtp/.default"]
"""
"offline_access https://graph.microsoft.com/mtp/.default",
"offline_access https://api.securitycenter.windows.com/.default",
"offline_access https://securitycenter.onmicrosoft.com/windowsatpservice/.default"
"""

DEFENDER_AUTH_URL = "https://login.windows.net/{tenant_id}/oauth2/token"

DEFAULT_DEFENDER_CLOSE_INCIDENT_TEMPLATE = "data/defender_close_incident_template.jinja"
DEFAULT_DEFENDER_UPDATE_INCIDENT_TEMPLATE = "data/defender_update_incident_template.jinja"
DEFAULT_DEFENDER_UPDATE_ALERT_TEMPLATE = "data/defender_update_alert_template.jinja"

DEFAULT_INCIDENT_CREATION_TEMPLATE = "data/incident_creation_template.jinja"
DEFAULT_INCIDENT_UPDATE_TEMPLATE = "data/incident_update_template.jinja"
DEFAULT_INCIDENT_CLOSE_TEMPLATE = "data/incident_close_template.jinja"

log = getLogger(__name__)

class DefenderAPI():
    """class to manage authentication and API calls to Defender ATP"""
    def __init__(self, tenant_id, client_id, app_secret, opts, options, scope=DEFENDER_SCOPE, rc=None):
        """build the connection class for Defender ATP

        Args:
            tenant_id ([type]): description
            client_id ([type]): description
            app_secret ([type]): description
            opts ([dict]): description
            options ([dict]): description
            scope (list): scope to use for API calls
            rc ([object]): RequestCommon if passed in
        """
        self.api_url = options.get("api_url")
        self.rc = rc if rc else RequestsCommon(opts, options)

        self.scope = scope
        authority = AUTH_URL.format(tenant_id=tenant_id)
        self.access_token = None
        self.kwargs = self.get_requests_kwargs(REQUEST_PARAMS, options)
        self.app = ConfidentialClientApplication(
            client_id,
            authority=authority,
            client_credential=app_secret,
            proxies=self.rc.get_proxies(),
            timeout=self.rc.get_timeout(),
            **self.kwargs
        )

    def get_requests_kwargs(self, params_list, options):
        """Create dictionary of addl parameters to send to the requests call

        Args:
            params_list ([dict]): Parameters to include if specificized in [function_section]
            options ([dict]): function_section parameters

        Returns:
            [dict]: returned values, with any conversion is necessary
        """
        return { k:opr(options[k]) for k, opr in params_list.items() if k in options }

    def defender_authenticate(self):
        """Authenticate to defender and get the access token

        Args:
            app_scope ([str], optional): Scope of authentication]. Defaults to DEFENDER_SCOPE.

        Raises:
            IntegrationError: If authentication errors occur

        Returns:
            [str]: access token
        """
        result = self.app.acquire_token_silent(self.scope, account=None)

        if not result:
            result = self.app.acquire_token_for_client(scopes=self.scope)

        if "access_token" in result:
            self.access_token = result['access_token']
            return True

        raise IntegrationError(f'Unable to authenticate to MS Azure: Error: {result.get("error")}\nDescription: \
            {result.get("error_description")}\nCorrelation_id: {result.get("correlation_id")}')

    def make_header(self, content_type="application/json"):
        """Build headers needed for API calls. It will include the Defender access token

        Args:
            content_type (str, optional): Defaults to "application/json".

        Returns:
            [dict]: api headers to use
        """
        headers = {'Authorization': 'Bearer ' + self.access_token}
        if content_type:
            headers['Content-Type'] = content_type

        return headers

    def call(self, url_endpoint, payload=None, oper="GET", content_type="application/json"):
        """Make the API call to Defender

        Args:
            url_endpoint ([type]): description
            payload ([dict], optional): [payload to send]. Defaults to None.
            oper (str, optional): ["GET", "POST", "DELETE"]. Defaults to "GET".
            content_type (str, optional): [value for content_type]. Defaults to "application/json".

        Returns:
            [json]: returned API payload
        """
        self.defender_authenticate()
        url = "/".join([self.api_url, url_endpoint])
        headers = self.make_header(content_type)

        if oper in ["POST", "PATCH"]:
            result, status = self.rc.execute(oper, url, json=payload, headers=headers, callback=callback_response, **self.kwargs)
        else:
            result, status = self.rc.execute(oper, url, params=payload, headers=headers, callback=callback_response, **self.kwargs)

        reason = None
        if not status:
            reason = result['error'].get('message')

        return result, status, reason

    def query_incidents(self, last_poller_datetime):
        """Query Defender for all incidents created within the last polling window. If first time,
              then use a lookback value.
        Args:
            last_poller_datetime ([number]): epoch value of last time poller ran
        Returns:
            result [dict]: API results
            status [bool]: True if API call was successful
            reason [str]: Reason of error when status=False
        """
        # Build filter information
        result, status, reason = self.call(INCIDENTS_URL,
            payload={"$filter": self._make_createdate_filter(last_poller_datetime)})

        return result, status, reason

    def query_alerts(self, last_poller_datetime):
        """Query Defender for all alerts created within the last polling window. If first time,
              then use a lookback value.
        Args:
            last_poller_datetime ([number]): [epoch value of last time poller ran]
        Returns:
            result [dict]: API results
            status [bool]: True if API call was successful
            reason [str]: Reason of error when status=False
        """
        # Build filter information
        result, status, reason = self.call(
            ALERTS_URL,
            payload={
                "$filter": self._make_createdate_filter(last_poller_datetime),
                **EXPAND_PARAMS
            }
        )

        return result, status, reason

    def _make_createdate_filter(self, last_poller_datetime):
        """Build the $filter parameter to find alerts by last poller run datetime
        Args:
            last_poller_datetime ([datetime]): last poller time
        Returns:
            [str]: $filter string to use
        """
        last_poller_datetime_iso = last_poller_datetime.isoformat()

        # Remove milliseconds
        return "lastUpdateTime ge {lookback_date}Z"\
                    .format(lookback_date=last_poller_datetime_iso[:last_poller_datetime_iso.rfind('.')])

    def wait_for_action(self, url, iter=10, wait=30):
        """Wait for an action

        Args:
            url ([type]):
            iter (int, optional): Defaults to 10.
            wait (int, optional): Defaults to 30.
        """
        for _ in range(0, iter):
            sleep(wait)
            result, status, reason = self.call(url, oper="GET")
            if not status or (status and result.get('status') != 'Pending'):
                break

        return result, status, reason

def callback_response(response):
    """Call back routine to review HTTP status code

    Args:
        response ([requests Response]): Object returned from Requests API call

    Returns:
        [json]: Payload from API call
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
    """Convert UTC formatted timestamp to epoch value

    Args:
        value ([str]): UTC formatted timestamp

    Returns:
        [number]: Epoch value
    """
    if not value:
        return value

    # Defender can return 7 millisecond characters which time.strptime cannot parse
    # strip milliseconds as 7 characters cannot be parsed by %f
    return timegm(strptime(value[:value.rfind('.')], "%Y-%m-%dT%H:%M:%S"))*1000

def make_filter_url(url, filter_template, value):
    """Make an api call using odata filters

    Args:
        url ([str]): Base url
        filter_template ([str]): Filter template
        value ([str]): Substitution value
    Return:
        update url ([str])
    """
    if filter_template in MACHINES_FILTER:
        return "?$filter=".join([url, MACHINES_FILTER[filter_template].format(value)])

    raise ValueError(f"{filter_template} is invalid filter template name")
