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

INDICATOR_URL = "api/indicators"
MACHINES_URL = "api/machines"
FILES_URL = "api/files/{}/machines"
ALERTS_URL = "api/alerts"

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

## TODO
new_result = {
  "value": [
    {
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "name": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "type": "Microsoft.SecurityInsights/incidents",
      "etag": "\"0300bf09-0000-0000-0000-5c37296e0000\"",
      "properties": {
        "lastModifiedTimeUtc": "2019-01-01T13:15:30Z",
        "createdTimeUtc": "2019-01-01T13:15:30Z",
        "lastActivityTimeUtc": "2019-01-01T13:05:30Z",
        "firstActivityTimeUtc": "2019-01-01T13:00:30Z",
        "description": "This is a demo incident",
        "title": "My incident",
        "owner": {
          "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
          "email": "john.doe@contoso.com",
          "userPrincipalName": "john@contoso.com",
          "assignedTo": "john doe"
        },
        "severity": "Informational",
        "classification": "FalsePositive",
        "classificationComment": "Not a malicious activity",
        "classificationReason": "IncorrectAlertLogic",
        "status": "New",
        "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5",
        "incidentNumber": 3177,
        "labels": [],
        "relatedAnalyticRuleIds": [
          "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/fab3d2d4-747f-46a7-8ef0-9c0be8112bf7",
          "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/8deb8303-e94d-46ff-96e0-5fd94b33df1a"
        ],
        "additionalData": {
          "alertsCount": 0,
          "bookmarksCount": 0,
          "commentsCount": 3,
          "alertProductNames": [],
          "tactics": [
            "Persistence"
          ]
        }
      }
    }
  ]
}

update_result = {
  "value": [
    {
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "name": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "type": "Microsoft.SecurityInsights/incidents",
      "etag": "\"0300bf09-0000-0000-0000-5c37296e0000\"",
      "properties": {
        "lastModifiedTimeUtc": "2019-01-01T13:15:30Z",
        "createdTimeUtc": "2019-01-01T13:15:30Z",
        "lastActivityTimeUtc": "2019-01-01T13:05:30Z",
        "firstActivityTimeUtc": "2019-01-01T13:00:30Z",
        "description": "This is a demo incident",
        "title": "My incident",
        "owner": {
          "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
          "email": "john.doe@contoso.com",
          "userPrincipalName": "john@contoso.com",
          "assignedTo": "john doe"
        },
        "severity": "Medium",
        "classification": "FalseNegative",
        "classificationComment": "Not a malicious activity",
        "classificationReason": "IncorrectAlertLogic",
        "status": "Active",
        "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5",
        "incidentNumber": 3177,
        "labels": [],
        "relatedAnalyticRuleIds": [
          "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/fab3d2d4-747f-46a7-8ef0-9c0be8112bf7",
          "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/8deb8303-e94d-46ff-96e0-5fd94b33df1a"
        ],
        "additionalData": {
          "alertsCount": 0,
          "bookmarksCount": 0,
          "commentsCount": 3,
          "alertProductNames": [],
          "tactics": [
            "Persistence"
          ]
        }
      }
    }
  ]
}

close_result = {
  "value": [
    {
      "id": "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "name": "73e01a99-5cd7-4139-a149-9f2736ff2ab5",
      "type": "Microsoft.SecurityInsights/incidents",
      "etag": "\"0300bf09-0000-0000-0000-5c37296e0000\"",
      "properties": {
        "lastModifiedTimeUtc": "2019-01-01T13:15:30Z",
        "createdTimeUtc": "2019-01-01T13:15:30Z",
        "lastActivityTimeUtc": "2019-01-01T13:05:30Z",
        "firstActivityTimeUtc": "2019-01-01T13:00:30Z",
        "description": "This is a demo incident",
        "title": "My incident",
        "owner": {
          "objectId": "2046feea-040d-4a46-9e2b-91c2941bfa70",
          "email": "john.doe@contoso.com",
          "userPrincipalName": "john@contoso.com",
          "assignedTo": "john doe"
        },
        "severity": "Low",
        "classification": "FalsePositive",
        "classificationComment": "Not a malicious activity",
        "classificationReason": "IncorrectAlertLogic",
        "status": "Closed",
        "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/73e01a99-5cd7-4139-a149-9f2736ff2ab5",
        "incidentNumber": 3177,
        "labels": [],
        "relatedAnalyticRuleIds": [
          "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/fab3d2d4-747f-46a7-8ef0-9c0be8112bf7",
          "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/8deb8303-e94d-46ff-96e0-5fd94b33df1a"
        ],
        "additionalData": {
          "alertsCount": 0,
          "bookmarksCount": 0,
          "commentsCount": 3,
          "alertProductNames": [],
          "tactics": [
            "Persistence"
          ]
        }
      }
    }
  ]
}

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

        # TODO
        self.test_counter = 0
        self.test_payloads = [new_result, update_result, close_result]
        # TODO

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
            "$filters": self._make_createdate_filter(last_poller_datetime)
        }

        result, status, reason = self._call(url, payload=payload)

        #### $filters appears not to be working. do a second pass on the incident data
        if status:
            result = self._filter_by_last_modified_date(result, last_poller_datetime)

        ## TODO
        #status = True
        #result = self.test_payloads[self.test_counter]
        #self.test_counter += 1
        ## TODO
        LOG.debug("%s:%s:%s", status, reason, result)
        return result, status, reason

    def _filter_by_last_modified_date(self, result, poller_last_modified_date, field="lastModifiedTimeUtc", \
                                      date_format="%Y-%m-%dT%H:%M:%S"):
        """this logic is unnecessary of the $filters capability is workin in the query API call.
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
                    LOG.debug("Allowing incident:%s %s", inc['properties']['incidentNumber'],
                              incident_last_modified_date.isoformat())
                else:
                    LOG.debug("Filtering incident:%s %s", inc['properties']['incidentNumber'],
                              incident_last_modified_date.isoformat())

            except ValueError as err:
                LOG.error(str(err))

        return { "value": filtered }

    def get_incident_alerts(self, profile_data, sentinel_incident_id):
        """Query for alerts associated with a sentinel incident

        Args:
            profile_name ([str]): [profile name with incident access parameters]
            sentinel_incident_id ([str]): [sentinel incident id]

        Returns:
            [dict]: [alert list from API call]
        """
        #
        """
        mock_result = {
            "value": [
                {
                    "id": "/subscriptions/##SUBSCRIPTIONID##/resourceGroups/jn-sentineltest/providers/Microsoft.OperationalInsights/workspaces/cybtgmu6sxcvk/providers/Microsoft.SecurityInsights/Incidents/ad7cb03c-37c8-4f98-a34a-c76951b8683e/relations/ad7cb03c-37c8-4f98-a34a-c76951b8683e_fe3ca9f0-0765-b792-cd03-d3aa100571d8",
                    "name": "ad7cb03c-37c8-4f98-a34a-c76951b8683e_fe3ca9f0-0765-b792-cd03-d3aa100571d8",
                    "type": "Microsoft.SecurityInsights/Incidents/relations",
                    "properties": {
                        "relatedResourceId": "/subscriptions/a7be6876-1523-4cd2-b50c-75c5d041da61/resourceGroups/jn-sentineltest/providers/Microsoft.OperationalInsights/workspaces/cybtgmu6sxcvk/providers/Microsoft.SecurityInsights/entities/fe3ca9f0-0765-b792-cd03-d3aa100571d8",
                        "relatedResourceName": "fe3ca9f0-0765-b792-cd03-d3aa100571d8",
                        "relatedResourceType": "Microsoft.SecurityInsights/entities",
                        "relatedResourceKind": "SecurityAlert"
                    }
                },
                {
                    "id": "/subscriptions/##SUBSCRIPTIONID##/resourceGroups/jn-sentineltest/providers/Microsoft.OperationalInsights/workspaces/cybtgmu6sxcvk/providers/Microsoft.SecurityInsights/Incidents/ad7cb03c-37c8-4f98-a34a-c76951b8683e/relations/ad7cb03c-37c8-4f98-a34a-c76951b8683e_fe3ca9f0-0765-b792-cd03-d3aa100571d8",
                    "name": "ad7cb03c-37c8-4f98-a34a-c76951b8683e_fe3ca9f0-0765-b792-cd03-d3aa100571d9",
                    "type": "Microsoft.SecurityInsights/Incidents/relations",
                    "properties": {
                        "relatedResourceId": "/subscriptions/a7be6876-1523-4cd2-b50c-75c5d041da61/resourceGroups/jn-sentineltest/providers/Microsoft.OperationalInsights/workspaces/cybtgmu6sxcvk/providers/Microsoft.SecurityInsights/entities/fe3ca9f0-0765-b792-cd03-d3aa100571d8",
                        "relatedResourceName": "fe3ca9f0-0765-b792-cd03-d3aa100571d8",
                        "relatedResourceType": "Microsoft.SecurityInsights/entities",
                        "relatedResourceKind": "SecurityAlert"
                    }
                }
            ]
        }

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
        """
        relations_url = "/".join([INCIDENTS_URL, str(sentinel_incident_id),
                                  RELATIONS_URL])

        url = self._get_base_payload(profile_data['subscription_id'],
                                     profile_data['resource_groupname'],
                                     profile_data['workspace_name'],
                                     extra_url=relations_url,
                                     api_version=PREVIEW_API_VERSION)

        result, status, reason = self._call(url)

        ## TODO
        #status = True
        #result = mock_result
        ## TODO

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
        mock_result = {
  "value": {
    "entities": [
      {
        "id": "/subscriptions/##SUBSCRIPTIONID##/resourceGroups/jn-sentineltest/providers/Microsoft.OperationalInsights/workspaces/cybtgmu6sxcvk/providers/Microsoft.SecurityInsights/entities/2e269cb7-3810-1601-eaa5-c8c3f3665898",
        "name": "2e269cb7-3810-1601-eaa5-c8c3f3665898",
        "type": "Microsoft.SecurityInsights/entities",
        "kind": "Ip",
        "properties": {
          "address": "83.84.75.154",
          "friendlyName": "83.84.75.154"
        }
      },
      {
        "id": "/subscriptions/##SUBSCRIPTIONID##/resourceGroups/jn-sentineltest/providers/Microsoft.OperationalInsights/workspaces/cybtgmu6sxcvk/providers/Microsoft.SecurityInsights/entities/0862214e-677f-cd12-bd65-d27628097200",
        "name": "0862214e-677f-cd12-bd65-d27628097200",
        "type": "Microsoft.SecurityInsights/entities",
        "kind": "Account",
        "properties": {
          "accountName": "jeroen",
          "upnSuffix": "niesen.nl",
          "isDomainJoined": True,
          "friendlyName": "jeroen"
        },
      },
      {
        "id": "/subscriptions/##SUBSCRIPTIONID##/resourceGroups/jn-sentineltest/providers/Microsoft.OperationalInsights/workspaces/cybtgmu6sxcvk/providers/Microsoft.SecurityInsights/entities/2e269cb7-3810-1601-eaa5-c8c3f3665898",
        "name": "2e269cb7-3810-1601-eaa5-c8c3f3665800",
        "type": "Microsoft.SecurityInsights/entities",
        "kind": "FileHash",
        "properties": {
          "address": "12345678901234567890123456789012",
          "friendlyName": "12345678901234567890123456789012"
        }
      }
    ],
    "edges": [
    ]
  },
  "metaData": {
    "aggregations": [
      {
        "entityKind": "Ip",
        "count": 1
      },
      {
        "entityKind": "Account",
        "count": 1
      }
    ]
  }
}

        url = "{}{}/expand?{}".format(self.base_url, alert_url, PREVIEW_API_VERSION)

        result, status, reason = self._call(url, payload=ENTITY_BODY, oper="POST")
        LOG.debug("%s:%s:%s", status, reason, result)

        ## TODO
        #status = True
        #result = mock_result
        ## TODO

        # convert entity types to artifact types, adding 'resilient_artifact_type' property
        if status:
            for entity in result['value']['entities']:
                entity['resilient_artifact_type'] = convert_entity_type(entity['kind'],
                                                            entity['properties']['friendlyName'])

        return result, status, reason

    def _make_createdate_filter(self, last_poller_datetime):
        """build the $filters parameter to find incidents by last poller run datetime

        Args:
            last_poller_datetime ([datetime]): [last poller time]

        Returns:
            [str]: [$filter string to use]
        """
        last_poller_datetime_iso = last_poller_datetime.isoformat()

        # remove milliseconds
        return "lastModifiedTimeUtc ge {lookback_date}"\
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
                "message": note
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

def get_sentinel_incident_id(sentinel_incident):
    if not sentinel_incident:
        return None

    return sentinel_incident['name']

def make_uuid():
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
