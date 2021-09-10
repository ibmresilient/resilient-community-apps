# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

import calendar
import datetime
import logging
import time
import uuid
from resilient_lib import RequestsCommon, IntegrationError
from simplejson.errors import JSONDecodeError
from fn_microsoft_sentinel.lib.constants import FROM_SOAR_COMMENT_HDR

INDICATOR_URL = "api/indicators"
MACHINES_URL = "api/machines"
FILES_URL = "api/files/{}/machines"
ALERTS_URL = "incidents/{}/alerts"

DEFAULT_POLLER_LOOBACK_MINUTES = 120

API_VERSION = "api-version=2020-01-01"
PREVIEW_API_VERSION = "api-version=2019-01-01-preview"
SUBSCRIPTION_URL = "/subscriptions/{subscription_id}/resourceGroups/{resource_groupname}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/providers/Microsoft.SecurityInsights"
INCIDENTS_URL = "incidents"
COMMENTS_URL = "comments"
RELATIONS_URL = "relations"
ENTITY_BODY = {
    "expansionId": "98b974fd-cc64-48b8-9bd0-3a209f5b944b",
}

AUTH_URL = "https://login.microsoftonline.com/{}/oauth2/token"
RESOURCE_URI = "https://management.core.windows.net"

AUTH_SCOPE = [ None ]

# convert entity types to resilient artifact types
ENTITY_TYPE_LOOKUP = {
    "account": "User Account",
    "host": "System Name",
    "ip": "IP Address",
    "malware": "Malware Family/Variant",
    "file": "File Name",
    "process": "Process Name",
    "cloudapplication": "String",
    "dns": "DNS Name",
    "azure resource": "Service",
    "filehash": {
        "(SHA1)": "Malware SHA-1 Hash",
        "(SHA256)": "Malware SHA-256 Hash",
        "(MD5)": "Malware MD5 Hash",
        "default": "Malware Sample Fuzzy Hash"
    },
    "registry key": "Registry Key",
    "registry value": "Registry Key",
    "security group": "String",
    "url": "URL",
    "iot device": "DNS Name",
    "mailbox": "String",
    "mail cluster": "String",
    "mail message": "Email Body",
    "submission mail": "Email Body"
}

LOG = logging.getLogger(__name__)

class SentinelAPI():
    """[class to manage authentication and API calls to Sentinel]
    """
    def __init__(self, tenant_id, client_id, app_secret, opts, options):
        """build the connection class for Sentinel

        Args:
            tenant_id ([type]): [description]
            client_id ([type]): [description]
            app_secret ([type]): [description]
            opts ([type]): [description]
            options ([type]): [description]
        """
        self.polling_lookback = int(options.get("polling_lookback", DEFAULT_POLLER_LOOBACK_MINUTES))
        self.base_url = options.get("azure_url")
        self.rc = RequestsCommon(opts, options)
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.app_secret = app_secret

        self.access_token = None

    def _authenticate(self, app_scope=AUTH_SCOPE):
        """[authenticate to azure and get the access token]

        Args:
            app_scope ([str], optional): [scope of authentication]. Defaults to AUTH_SCOPE.

        Raises:
            IntegrationError: [if authentication errors occur]

        Returns:
            [str]: [access token]

        Raises:
            IntegrationError: [description]

        Returns:
            [type]: [description]
        """
        authenticate_url = AUTH_URL.format(self.tenant_id)
        post_data = {
            "client_id": self.client_id,
            "resource": "https://management.azure.com/",
            "scope": ["https://graph.microsoft.com/.default"],
            "client_secret": self.app_secret,
            "grant_type": "client_credentials"
        }
        result = self.rc.execute_call_v2("POST", authenticate_url, data=post_data)
        result_json = result.json()

        if "access_token" in result_json:
            self.access_token = result_json['access_token']
            return True

        msg = u"Unable to authenticate to MS Azure: Error: {}\nDescription: {}\nCorrelation_id: {}"\
                .format(result_json.get("error"), result_json.get("error_description"), result_json.get("correlation_id"))
        raise IntegrationError(msg)


    def _make_header(self, content_type="application/json"):
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

    def _call(self, url_endpoint, payload=None, oper="GET", content_type="application/json"):
        """make the API call to Defender

        Args:
            url_endpoint ([type]): [description]
            payload ([dict], optional): [payload to send]. Defaults to None.
            oper (str, optional): ["GET", "POST", "DELETE"]. Defaults to "GET".
            content_type (str, optional): [value for content_type]. Defaults to "application/json".

        Returns:
            [json]: [returned API payload]
        """
        self._authenticate()
        headers = self._make_header(content_type)

        try:
            if oper in ["PUT", "POST", "PATCH"]:
                result, status = self.rc.execute_call_v2(oper, url_endpoint, json=payload, headers=headers, callback=callback_response)
            else:
                result, status = self.rc.execute_call_v2(oper, url_endpoint, params=payload, headers=headers, callback=callback_response)
        except Exception as err:
            LOG.error(str(err))
            status = False
            result = {
                "error": {
                    "code": 999,
                    "message": str(err)
                }
            }

        reason = None
        if not status:
            reason = result['error'].get('message')

        return result, status, reason

    def query_incidents(self, profile_data):
        """Query Sentinel for all incidents created within the last polling window. If first time,
              then use a lookback value.

        Args:
            profile_data ([dict]): [profile to query incidents]

        Returns:
            result [dict]: API results
            status [bool]: True if API call was successful
            reason [str]: Reason of error when status=False
        """
        url = self._get_base_payload(profile_data['subscription_id'],
                                     profile_data['resource_groupname'],
                                     profile_data['workspace_name'],
                                     extra_url=INCIDENTS_URL)

        # build filter information
        last_poller_datetime = self._get_last_poller_date(profile_data)
        payload = {
            "$filter": self._make_createdate_filter(last_poller_datetime)
        }

        result, status, reason = self._call(url, payload=payload)

        #### $filters appears not to be working. do a second pass on the incident data
        if status:
            result = self._filter_by_last_modified_date(result, last_poller_datetime)

        LOG.debug("%s:%s:%s", status, reason, result)
        return result, status, reason

    def query_next_incidents(self, profile_data, nextlink):
        """[get the next set of incident data]

        Args:
            profile_data ([dickt]): [app settings for this profile]
            nextlink ([str]): [url]

        Returns:
            result [dict]: API results
            status [bool]: True if API call was successful
            reason [str]: Reason of error when status=False
        """
        last_poller_datetime = self._get_last_poller_date(profile_data)

        result, status, reason = self._call(nextlink)
        if status:
            result = self._filter_by_last_modified_date(result, last_poller_datetime)

        LOG.debug("%s:%s:%s", status, reason, result)
        return result, status, reason


    def _filter_by_last_modified_date(self, result, poller_last_modified_date, field="lastModifiedTimeUtc", \
                                      date_format="%Y-%m-%dT%H:%M:%S"):
        """this logic is unnecessary of the $filter capability is workin in the query API call.
             loop through all incidents results and reapply the logic to filter the list based on
             the last poller window time.

        Args:
            result ([dict]): [api result from query API]
            poller_last_modified_date ([datetime]): [datetime of last poller run]
            field (str, optional): [field to check for last poller time]. Defaults to "lastModifiedTimeUtc".

        Returns:
            [dict]: [filtered out incident list]
        """

        # loop through all incidents and filter out older incidents outside poller window
        filtered = []
        for inc in result['value']:
            try:
                str_date = inc['properties'][field]
                incident_last_modified_date = datetime.datetime.strptime(str_date[:str_date.rfind('.')], date_format)
                if incident_last_modified_date >= poller_last_modified_date:
                    filtered.append(inc)
                    LOG.debug("Allowing incident:%s %s", inc['name'],
                              incident_last_modified_date.isoformat())
                else:
                    LOG.debug("Filtering incident:%s %s", inc['name'],
                              incident_last_modified_date.isoformat())

            except ValueError as err:
                LOG.error(str(err))

        return { "value": filtered, "nextLink": result.get("nextLink") }

    def get_incident_entities(self, profile_data, sentinel_incident_id):
        """Query for entities associated with a sentinel incident

        Args:
            profile_name ([str]): [profile name with incident access parameters]
            sentinel_incident_id ([str]): [sentinel incident id]

        Returns:
            [dict]: [entity list from API call]
        """

        relations_url = "/".join([INCIDENTS_URL, str(sentinel_incident_id),
                                  RELATIONS_URL])

        url = self._get_base_payload(profile_data['subscription_id'],
                                     profile_data['resource_groupname'],
                                     profile_data['workspace_name'],
                                     extra_url=relations_url,
                                     api_version=PREVIEW_API_VERSION)

        result, status, reason = self._call(url)

        LOG.debug("%s:%s:%s", status, reason, result)
        return result, status, reason

    def get_incident_alerts(self, profile_data, sentinel_incident_id):
        """Query for alerts associated with a sentinel incident

        Args:
            profile_name ([str]): [profile name with incident access parameters]
            sentinel_incident_id ([str]): [sentinel incident id]
            max_alerts: number of alerts to return (in descending order) or all if set to None

        Returns:
            [dict]: [alert list from API call]
        """

        alerts_url = ALERTS_URL.format(str(sentinel_incident_id))

        url = self._get_base_payload(profile_data['subscription_id'],
                                     profile_data['resource_groupname'],
                                     profile_data['workspace_name'],
                                     extra_url=alerts_url,
                                     api_version=PREVIEW_API_VERSION)

        result, status, reason = self._call(url, oper="POST")

        # limit the number of alerts returned
        if profile_data.get('max_alerts'):
            result['value'] = result['value'][:int(profile_data.get('max_alerts'))]

        # build epoch values for time stamps
        for alert in result['value']:
            alert['properties']['timeGenerated_ms'] = convert_date(alert['properties']['timeGenerated'])

        LOG.debug("%s:%s:%s", status, reason, result)
        return result, status, reason

    def get_incident_alert_entities(self, alert_url):

        # https://management.azure.com" + $workspaceId + "/providers/Microsoft.SecurityInsights/incidents?/incidents/$incidentId/relations?api-version=2020-01-01"
        """
        {
            "id": "/subscriptions/67d6179d-a99d-4aad-8c11-4d3ff2e12249/resourceGroups/azsec-corporate-rg/providers/Microsoft.OperationalInsights/workspaces/azsec-shared-workspace/providers/Microsoft.SecurityInsights/Incidents/52668a53-85df-4bc2-90fe-c94ed40adc69/relations/52668a53-85af-4cc1-00fe-c94ed40adc69_63ad2c2a-555f-6714-e989-328faa684c1d",
            "name": "52668a53-85af-4cc1-00fe-c94ed40adc69_63ad2c2a-555f-6714-e989-328faa684c1d",
            "type": "Microsoft.SecurityInsights/Incidents/relations",
            "properties": {
                "relatedResourceId": "/subscriptions/67d6179d-a99d-4aad-8c11-4d3ff2e12249/resourceGroups/azsec-corporate-rg/providers/Microsoft.OperationalInsights/workspaces/azsec-shared-workspace/providers/Microsoft.SecurityInsights/entities/63ad2c2a-555f-6714-e989-328faa684c1d",
                "relatedResourceName": "63ad2c2a-555f-6714-e989-328faa684c1d",
                "relatedResourceType": "Microsoft.SecurityInsights/entities",
                "relatedResourceKind": "SecurityAlert"
            }
        }
        >> relatedResourceName
        In the above API response the “relatedResourceName” (which is actually an ID) is important. This value is required in the next API call:
        POST https://management.azure.com/subscriptions/##SUBSCRIPTIONID##/resourceGroups/##RESOURCEGROUP##/providers/Microsoft.OperationalInsights/workspaces/{2}/providers/Microsoft.SecurityInsights/entities/##RelatedResourceName##/expand?api-version=2019-01-01-preview
        The following HTTP-body should be used:
        {
        "expansionId": "98b974fd-cc64-48b8-9bd0-3a209f5b944b",
        }
        The return of this API call will be:

        """

        url = "{}{}/expand?{}".format(self.base_url, alert_url, PREVIEW_API_VERSION)

        result, status, reason = self._call(url, payload=ENTITY_BODY, oper="POST")
        LOG.debug("%s:%s:%s", status, reason, result)

        # convert entity types to artifact types, adding 'resilient_artifact_type' property
        if status:
            for entity in result['value']['entities']:
                artifact_type, artifact_value = convert_entity_type(entity['kind'],
                                                                    entity['properties'].get('friendlyName', 'Unknown'))
                entity['resilient_artifact_type']  = artifact_type
                entity['resilient_artifact_value']  = artifact_value

        return result, status, reason

    def _make_createdate_filter(self, last_poller_datetime):
        """build the $filter parameter to find incidents by last poller run datetime

        Args:
            last_poller_datetime ([datetime]): [last poller time]

        Returns:
            [str]: [$filter string to use]
        """
        last_poller_datetime_iso = last_poller_datetime.isoformat()

        # remove milliseconds
        return "properties/lastModifiedTimeUtc ge {lookback_date}Z"\
                    .format(lookback_date=last_poller_datetime_iso[:last_poller_datetime_iso.rfind('.')])

    def _get_last_poller_date(self, profile_data):
        """get the last poller datetime based on a profile. If first time, use the lookback
             parameter to calculate it from the current datetime.

        Args:
            profile_data ([str]): profile to get last poller runtime

        Returns:
            [datetime]: [datetime to use for last poller run time]
        """
        if profile_data.get('last_poller_time'):
            last_poller_datetime = profile_data['last_poller_time']
            LOG.debug("last_poller_time: %s", last_poller_datetime.isoformat())
        else:
            # use lookback value
            last_poller_datetime = datetime.datetime.utcnow() - datetime.timedelta(minutes=self.polling_lookback)

        return last_poller_datetime

    def create_update_incident(self, profile_data, sentinel_incident_id, incident_payload):
        """create or update a Sentinel incident based on a resilient incident.

        Args:
            profile_name ([str]): [profile to use for creating the incident]
            sentinel_incident_id ([str]): [sentinel incident id or None for creating a new one]
            incident_payload ([dict]): [dictionary of sentinel incident data]

        Returns:
            result [dict]: API results
            status [bool]: True if API call was successful
            reason [str]: Reason of error when status=False
        """
        if sentinel_incident_id is None:
            sentinel_incident_id = make_uuid()

        incident_url = "/".join([INCIDENTS_URL, sentinel_incident_id])

        url = self._get_base_payload(profile_data['subscription_id'],
                                     profile_data['resource_groupname'],
                                     profile_data['workspace_name'],
                                     extra_url=incident_url)

        result, status, reason = self._call(url, payload=incident_payload, oper="PUT")

        LOG.debug("%s:%s:%s", status, reason, result)
        return result, status, reason

    def get_incident_comments(self, profile_data, sentinel_incident_id):
        """Get all comments for a Sentinel incident

        Args:
            profile_name ([str]): [profile for incident]
            sentinel_incident_id ([str]): [sentinel incident id]

        Returns:
            result [dict]: API results
            status [bool]: True if API call was successful
            reason [str]: Reason of error when status=False
        """
        comments_url = "/".join([INCIDENTS_URL, str(sentinel_incident_id), COMMENTS_URL])

        url = self._get_base_payload(profile_data['subscription_id'],
                                     profile_data['resource_groupname'],
                                     profile_data['workspace_name'],
                                     extra_url=comments_url)

        result, status, reason = self._call(url)

        LOG.debug("%s:%s:%s", status, reason, result)
        return result, status, reason

    def create_comment(self, profile_data, sentinel_incident_id, note):
        """create a sentinel incident comment

        Args:
            sentinel_incident_id ([str]): [sentinel incident id]
            profile_name ([str]): [profile to use for the incident]
            note ([str]): [note to sync]

        Returns:
            result [dict]: API results
            status [bool]: True if API call was successful
            reason [str]: Reason of error when status=False
        """
        comment_url = "/".join([INCIDENTS_URL, sentinel_incident_id, COMMENTS_URL, make_uuid()])

        url = self._get_base_payload(profile_data['subscription_id'],
                                     profile_data['resource_groupname'],
                                     profile_data['workspace_name'],
                                     extra_url=comment_url)

        payload = {
            "properties": {
                "message": "{}:\n{}".format(FROM_SOAR_COMMENT_HDR, note)
            }
        }

        result, status, reason = self._call(url, payload=payload, oper="PUT")

        LOG.debug("%s:%s:%s", status, reason, result)
        return result, status, reason

    def get_comments(self, profile_data, sentinel_incident_id):
        """get all comments for sentinel incident

        Args:
            profile_name ([str]): [profile to use for the incident]
            sentinel_incident_id ([str]): [sentinel incident id]

        Returns:
            result [dict]: API results
            status [bool]: True if API call was successful
            reason [str]: Reason of error when status=False
        """
        comment_url = "/".join([INCIDENTS_URL, sentinel_incident_id, COMMENTS_URL])

        url = self._get_base_payload(profile_data['subscription_id'],
                                     profile_data['resource_groupname'],
                                     profile_data['workspace_name'],
                                     extra_url=comment_url)

        result, status, reason = self._call(url)

        LOG.debug("%s:%s:%s", status, reason, result)
        return result, status, reason

    def _get_base_payload(self, subscription_id, resource_groupname, workspace_name,
                          extra_url=None, api_version=API_VERSION):
        """build the URL needed for sentinel incident access

        Args:
            subscription_id ([str]): [description]
            resource_groupname ([str]): [description]
            workspace_name ([type]): [description]
            extra_url ([str], optional): [additional url information to append]. Defaults to None.
            api_version ([str], optional): [API version to use]. Defaults to API_VERSION.

        Returns:
            [type]: [description]
        """
        # build url
        url = "{}{}".format(self.base_url,
                            SUBSCRIPTION_URL.format(subscription_id=subscription_id,
                                                    resource_groupname=resource_groupname,
                                                    workspace_name=workspace_name
                                                   )
                           )

        if extra_url:
            url = '/'.join([url, extra_url])

        url = "?".join([url, api_version])

        return url

def get_sentinel_incident_ids(sentinel_incident):
    """
    Returns:
        [str]: [sentinel_indident_id or None if not found]
    """
    if not sentinel_incident:
        return None

    return sentinel_incident['name'], sentinel_incident['properties']['incidentNumber']

def make_uuid():
    """
    Returns:
        [str]: [created uuid]
    """
    return str(uuid.uuid1())


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

def convert_date(value, date_format="%Y-%m-%dT%H:%M:%S"):
    """convert UTC formatted timestamp to epoch value

    Args:
        value ([str]): [UTC formatted timestamp]

    Returns:
        [number]: [Epoch value]
    """
    if not value:
        return value

    # Sentinel can return 7 millisecond characters which time.strptime cannot parse
    # strip milliseconds as 7 characters cannot be parsed by %f
    utc_time = time.strptime(value[:value.rfind('.')], date_format)
    return calendar.timegm(utc_time)*1000


def convert_entity_type(entity_type, entity_value):
    """[convert entity information to artifacts. A lookup table on entity types is used]

    Args:
        entity_type ([str]): [description]
        entity_value ([str]): [entity value used in part or whole as an artifact value]

        sha-1 - 40(MD5)
        md5 - 32(SHA1)
        sha-256 - 64(SHA256)

    Returns:
        artifact_type, artifact_value
    """

    resilient_artifact_type = ENTITY_TYPE_LOOKUP.get(entity_type.lower(), "String")
    if isinstance(resilient_artifact_type, dict):
        new_value = None
        for label in resilient_artifact_type:
            if label in entity_value:
                new_value = entity_value.replace(label, "")
                return resilient_artifact_type[label], entity_value.replace(label, "")

        if not new_value:
            return resilient_artifact_type["default"], entity_value

    return resilient_artifact_type, entity_value
