# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

from calendar import timegm
from datetime import datetime, timedelta
from logging import getLogger
from time import strptime
from uuid import uuid1

from resilient_lib import IntegrationError, RequestsCommon
from simplejson.errors import JSONDecodeError

from fn_microsoft_sentinel.lib.constants import FROM_SOAR_COMMENT_HDR

ALERTS_URL = "incidents/{}/alerts"
DEFAULT_POLLER_LOOKBACK_MINUTES = 120
API_VERSION = "api-version=2023-11-01-preview"
SUBSCRIPTION_URL = "/subscriptions/{subscription_id}/resourceGroups/{resource_groupname}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/providers/Microsoft.SecurityInsights"
INCIDENTS_URL = "incidents"
COMMENTS_URL = "comments"
RELATIONS_URL = "relations"
ENTITY_BODY = {"expansionId": "98b974fd-cc64-48b8-9bd0-3a209f5b944b",}
AUTH_URL = "https://login.microsoftonline.com/{}/oauth2/token"
RESOURCE_URI = "https://management.core.windows.net"
AUTH_SCOPE = [ None ]

# Convert entity types to SOAR artifact types
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

# Extra parameters possible in sentinel section for requests calls
REQUEST_PARAMS = {
    'verify': lambda val: False if val and val.lower() in ['false', 'no', 'off', '0'] else val,
    'cert': str
}

LOG = getLogger(__name__)

class SentinelAPI():
    """ class to manage authentication and API calls to Sentinel """
    def __init__(self, opts, options):
        """
        Build the connection class for Sentinel
        :param opts (Dict): All of the configurations in the app.config
        :param options (Dict): function_section parameters
        """
        self.polling_lookback = int(options.get("polling_lookback", DEFAULT_POLLER_LOOKBACK_MINUTES))
        self.base_url = options.get("azure_url")
        self.rc = RequestsCommon(opts, options)
        self.tenant_id = options.get("tenant_id")
        self.client_id = options.get("client_id")
        self.app_secret = options.get("app_secret")
        self.kwargs = self.get_requests_kwargs(REQUEST_PARAMS, options)
        LOG.debug(f"kwargs: {self.kwargs}")

        self.api_version = API_VERSION
        # If api_version is given in the app.config
        if options.get("api_version"):
            self.api_version = f"api-version={options.get('api_version')}"

        self.access_token = None

    def get_requests_kwargs(self, params_list, options):
        """
        Create dictionary of addl parameters to send to the requests call
        :param params_list [dict]: parameters to include if specified in [function_section]
        :param options [dict]: function_section parameters
        :return [dict]: returned values, with any conversion is necessary
        """
        return { k:opr(options[k]) for k, opr in params_list.items() if k in options }

    def _authenticate(self, app_scope=AUTH_SCOPE):
        """
        Authenticate to azure and get the access token
        :param app_scope ([str], optional): scope of authentication. Defaults to AUTH_SCOPE.
        :raises IntegrationError: if authentication errors occur
        :return [str]: access token
        """
        authenticate_url = AUTH_URL.format(self.tenant_id)
        post_data = {
            "client_id": self.client_id,
            "resource": "https://management.azure.com/",
            "scope": ["https://graph.microsoft.com/.default"],
            "client_secret": self.app_secret,
            "grant_type": "client_credentials"
        }
        result = self.rc.execute("POST", authenticate_url, data=post_data, **self.kwargs)
        result_json = result.json()

        if "access_token" in result_json:
            self.access_token = result_json['access_token']
            return True

        msg = "Unable to authenticate to MS Azure: Error: {}\nDescription: {}\nCorrelation_id: {}"\
            .format(result_json.get("error"), result_json.get("error_description"), result_json.get("correlation_id"))
        raise IntegrationError(msg)

    def _make_header(self, content_type="application/json"):
        """
        Build headers needed for API calls. It will include the Defender access token.
        :param content_type (str, optional): Defaults to "application/json".
        :return [dict]: api headers to use
        """
        headers = {'Authorization': f'Bearer {self.access_token}'}
        if content_type:
            headers['Content-Type'] = content_type

        return headers

    def _call(self, url_endpoint, payload=None, oper="GET", content_type="application/json"):
        """
        Make the API call to Defender
        :param url_endpoint [str]: Endpoint url
        :param payload ([dict], optional): Payload to send. Defaults to None.
        :param oper (str, optional): "GET", "POST", "DELETE". Defaults to "GET".
        :param content_type (str, optional): Value for content_type. Defaults to "application/json".
        :return [json]: Returned API payload
        """
        self._authenticate()
        headers = self._make_header(content_type)

        try:
            if oper in ["PUT", "POST", "PATCH"]:
                result, status = self.rc.execute(oper, url_endpoint, json=payload, headers=headers,
                    callback=callback_response,
                    **self.kwargs
                )
            else:
                result, status = self.rc.execute(oper, url_endpoint, params=payload, headers=headers,
                    callback=callback_response,
                    **self.kwargs
                )
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
        """
        Query Sentinel for all incidents created within the last polling window. If first time,
        then use a lookback value.
        :param profile_data [dict]: Profile to query incidents
        :return result [dict]: API results
        :return status [bool]: True if API call was successful
        :return reason [str]: Reason of error when status=False
        """
        url = self._get_base_payload(profile_data['subscription_id'],
            profile_data['resource_groupname'],
            profile_data['workspace_name'],
            extra_url=INCIDENTS_URL,
            api_version=self.api_version
        )

        # Build filter information
        last_poller_datetime = self._get_last_poller_date(profile_data)
        payload = {"$filter": self._make_createdate_filter(last_poller_datetime)}

        result, status, reason = self._call(url, payload=payload)

        #### $filters appears not to be working. do a second pass on the incident data
        if status:
            result = self._filter_by_last_modified_date(result, last_poller_datetime)

        LOG.debug(f"{status}:{reason}:{result}")
        return result, status, reason

    def query_next_incidents(self, profile_data, nextlink):
        """
        Get the next set of incident data
        :param profile_data ([dict]): app settings for this profile
        :param nextlink [str]: url
        :return result [dict]: API results
        :return status [bool]: True if API call was successful
        :return reason [str]: Reason of error when status=False
        """
        last_poller_datetime = self._get_last_poller_date(profile_data)

        result, status, reason = self._call(nextlink)
        if status:
            result = self._filter_by_last_modified_date(result, last_poller_datetime)

        LOG.debug(f"{status}:{reason}:{result}")
        return result, status, reason

    def _filter_by_last_modified_date(self, result, poller_last_modified_date, field="lastModifiedTimeUtc",
            date_format="%Y-%m-%dT%H:%M:%S"):
        """
        This logic is unnecessary of the $filter capability is working in the query API call.
        Loop through all incidents results and reapply the logic to filter the list based on
        the last poller window time.
        :param result [dict]: api result from query API
        :param poller_last_modified_date [datetime]: datetime of last poller run
        :param field (str, optional): Field to check for last poller time. Defaults to "lastModifiedTimeUtc".
        :return [dict]: Filtered out incident list
        """
        # Loop through all incidents and filter out older incidents outside poller window
        filtered = []
        for inc in result['value']:
            try:
                str_date = inc['properties'][field]
                incident_last_modified_date = datetime.strptime(str_date[:str_date.rfind('.')], date_format)
                if incident_last_modified_date >= poller_last_modified_date:
                    filtered.append(inc)
                    LOG.debug(f"Allowing incident:{inc['name']} {incident_last_modified_date.isoformat()}")
                else:
                    LOG.debug(f"Filtering incident:{inc['name']} {incident_last_modified_date.isoformat()}")

            except ValueError as err:
                LOG.error(str(err))

        return { "value": filtered, "nextLink": result.get("nextLink") }

    def get_incident_entities(self, profile_data, sentinel_incident_id):
        """
        Query for entities associated with a sentinel incident
        :param profile_name [str]: Profile name with incident access parameters
        :param sentinel_incident_id [str]: Sentinel incident id
        :return [dict]: Entity list from API call
        """
        relations_url = "/".join([INCIDENTS_URL, str(sentinel_incident_id), RELATIONS_URL])

        url = self._get_base_payload(profile_data['subscription_id'],
            profile_data['resource_groupname'],
            profile_data['workspace_name'],
            extra_url=relations_url,
            api_version=self.api_version
        )

        result, status, reason = self._call(url)

        LOG.debug(f"{status}:{reason}:{result}")
        return result, status, reason

    def get_incident_alerts(self, profile_data, sentinel_incident_id):
        """
        Query for alerts associated with a sentinel incident
        :param profile_name [str]: Profile name with incident access parameters
        :param sentinel_incident_id [str]: Sentinel incident id
        :param max_alerts (int): number of alerts to return (in descending order) or all if set to None
        :return [dict]: Alert list from API call
        """
        alerts_url = ALERTS_URL.format(str(sentinel_incident_id))

        url = self._get_base_payload(profile_data.get('subscription_id'),
            profile_data.get('resource_groupname'),
            profile_data.get('workspace_name'),
            extra_url=alerts_url,
            api_version=self.api_version
        )

        result, status, reason = self._call(url, oper="POST")

        # Limit the number of alerts returned
        if profile_data.get('max_alerts'):
            result['value'] = result['value'][:int(profile_data.get('max_alerts'))]

        # Build epoch values for time stamps
        for alert in result['value']:
            alert['properties']['timeGenerated_ms'] = convert_date(alert['properties']['timeGenerated'])

        LOG.debug(f"{status}:{reason}:{result}")
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
        url = f"{self.base_url}{alert_url}/expand?{self.api_version}"

        result, status, reason = self._call(url, payload=ENTITY_BODY, oper="POST")
        LOG.debug(f"{status}:{reason}:{result}")

        # Convert entity types to artifact types, adding 'soar_artifact_type' property
        if status:
            for entity in result['value']['entities']:
                if entity['properties'].get('friendlyName'):
                    artifact_type, artifact_value = convert_entity_type(entity['kind'],
                        entity['properties']['friendlyName']
                    )
                    entity['resilient_artifact_type'] = artifact_type
                    entity['resilient_artifact_value'] = artifact_value

        return result, status, reason

    def _make_createdate_filter(self, last_poller_datetime):
        """
        Build the $filter parameter to find incidents by last poller run datetime
        :param last_poller_datetime ([datetime]): Last poller time
        :return [str]: $filter string to use
        """
        last_poller_datetime_iso = last_poller_datetime.isoformat()

        # Remove milliseconds
        return "properties/lastModifiedTimeUtc ge {lookback_date}Z"\
                    .format(lookback_date=last_poller_datetime_iso[:last_poller_datetime_iso.rfind('.')])

    def _get_last_poller_date(self, profile_data):
        """
        Get the last poller datetime based on a profile. If first time, use the lookback
        parameter to calculate it from the current datetime.
        :param profile_data [str]: Profile to get last poller runtime
        :return [datetime]: Datetime to use for last poller run time
        """
        if profile_data.get('last_poller_time'):
            last_poller_datetime = profile_data['last_poller_time']
            LOG.debug(f"last_poller_time: {last_poller_datetime.isoformat()}")
        else:
            # Use lookback value
            last_poller_datetime = datetime.utcnow() - timedelta(minutes=self.polling_lookback)

        return last_poller_datetime

    def create_update_incident(self, profile_data, sentinel_incident_id, incident_payload):
        """
        Create or update a Sentinel incident based on a SOAR incident.
        :param profile_name [str]: Profile to use for creating the incident
        :param sentinel_incident_id [str]: Sentinel incident id or None for creating a new one
        :param incident_payload [dict]: Dictionary of sentinel incident data
        :return result [dict]: API results
        :return status [bool]: True if API call was successful
        :return reason [str]: Reason of error when status=False
        """
        if not sentinel_incident_id:
            sentinel_incident_id = make_uuid()

        incident_url = "/".join([INCIDENTS_URL, sentinel_incident_id])

        url = self._get_base_payload(profile_data['subscription_id'],
            profile_data['resource_groupname'],
            profile_data['workspace_name'],
            extra_url=incident_url,
            api_version=self.api_version
        )

        result, status, reason = self._call(url, payload=incident_payload, oper="PUT")

        LOG.debug(f"{status}:{reason}:{result}")
        return result, status, reason

    def get_incident_comments(self, profile_data, sentinel_incident_id):
        """
        Get all comments for a Sentinel incident
        :param profile_name [str]: Profile for incident
        :param sentinel_incident_id [str]: Sentinel incident id
        :return result [dict]: API results
        :return status [bool]: True if API call was successful
        :return reason [str]: Reason of error when status=False
        """
        comments_url = "/".join([INCIDENTS_URL, str(sentinel_incident_id), COMMENTS_URL])

        url = self._get_base_payload(profile_data['subscription_id'],
            profile_data['resource_groupname'],
            profile_data['workspace_name'],
            extra_url=comments_url,
            api_version=self.api_version
        )

        result, status, reason = self._call(url)

        LOG.debug(f"{status}:{reason}:{result}")
        return result, status, reason

    def create_comment(self, profile_data, sentinel_incident_id, note):
        """
        Create a sentinel incident comment
        :param sentinel_incident_id [str]: Sentinel incident id
        :param profile_name [str]: Profile to use for the incident
        :param note [str]: Note to sync
        :return result [dict]: API results
        :return status [bool]: True if API call was successful
        :return reason [str]: Reason of error when status=False
        """
        comment_url = "/".join([INCIDENTS_URL, sentinel_incident_id, COMMENTS_URL, make_uuid()])

        url = self._get_base_payload(profile_data['subscription_id'],
            profile_data['resource_groupname'],
            profile_data['workspace_name'],
            extra_url=comment_url,
            api_version=self.api_version
        )

        payload = {
            "properties": {
                "message": f"{FROM_SOAR_COMMENT_HDR}:\n{note}"
            }
        }

        result, status, reason = self._call(url, payload=payload, oper="PUT")

        LOG.debug(f"{status}:{reason}:{result}")
        return result, status, reason

    def get_comments(self, profile_data, sentinel_incident_id):
        """
        Get all comments for sentinel incident
        :param profile_name [str]: Profile to use for the incident
        :param sentinel_incident_id [str]: Sentinel incident id
        :return result [dict]: API results
        :return status [bool]: True if API call was successful
        :return reason [str]: Reason of error when status=False
        """
        comment_url = "/".join([INCIDENTS_URL, sentinel_incident_id, COMMENTS_URL])

        url = self._get_base_payload(profile_data['subscription_id'],
            profile_data['resource_groupname'],
            profile_data['workspace_name'],
            extra_url=comment_url,
            api_version=self.api_version
        )

        result, status, reason = self._call(url)

        LOG.debug(f"{status}:{reason}:{result}")
        return result, status, reason

    def _get_base_payload(self, subscription_id, resource_groupname, workspace_name,
                          extra_url=None, api_version=API_VERSION):
        """
        Build the URL needed for sentinel incident access
        :param subscription_id [str]: Sentinel subscription ID
        :param resource_groupname [str]: Sentinel resource group name
        :param workspace_name [str]: Sentinel workspace name
        :param extra_url ([str], optional): Additional url information to append. Defaults to None.
        :param api_version ([str], optional): API version to use. Defaults to API_VERSION.
        :return [str]: Url
        """
        # Build url
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
    :param sentinel_incident: Dictionary of the Sentinel incident fields
    :return [str]: sentinel_incident_id or None if not found
    """
    if not sentinel_incident:
        return None, None

    return sentinel_incident['name'], sentinel_incident['properties']['incidentNumber']

def make_uuid():
    """
    :return [str]: Created uuid
    """
    return str(uuid1())

def callback_response(response):
    """
    Call back routine to review HTTP status code
    :param response ([requests Response]): Object returned from Requests API call
    :return [json]: Payload from API call
    :return [bool]: True is call was successful
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
    """
    Convert UTC formatted timestamp to epoch value
    :param value [str]: UTC formatted timestamp
    :return [number]: Epoch value
    """
    if not value:
        return value

    # Sentinel can return 7 millisecond characters which time.strptime cannot parse
    # strip milliseconds as 7 characters cannot be parsed by %f
    utc_time = strptime(value[:value.rfind('.')], date_format)
    return timegm(utc_time)*1000

def convert_entity_type(entity_type, entity_value):
    """
    Convert entity information to artifacts. A lookup table on entity types is used
    :param entity_type [str]: Type of the entity
    :param entity_value [str]: Entity value used in part or whole as an artifact value
        sha-1 - 40(MD5)
        md5 - 32(SHA1)
        sha-256 - 64(SHA256)
    :return: artifact_type, artifact_value
    """
    soar_artifact_type = ENTITY_TYPE_LOOKUP.get(entity_type.lower(), "String")
    if isinstance(soar_artifact_type, dict):
        # Find the specific type of entity
        for label in soar_artifact_type.keys():
            if label in entity_value:
                # Return just the hash value without the label
                return soar_artifact_type[label], entity_value.replace(label, "")

        return soar_artifact_type["default"], entity_value

    # If the artifact type is URL and the entity_value does not start with either https:// or http://, then change
    # soar_artifact_type to equal URI Path. SOAR artifact types of URL have to start with either http:// or https://.
    if soar_artifact_type == "URL" and not entity_value.startswith("https://", "http://"):
        soar_artifact_type = "URI Path"

    return soar_artifact_type, entity_value
