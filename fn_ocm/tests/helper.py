# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Unit tests helper functions
PACKAGE_NAME = "fn_ocm"

def get_mock_config_data():
    return """[fn_ocm]
ocm_url = https://oncallmanager.ibm.com/api/
ocm_api_key_name = xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/qactalrirsin
ocm_api_key_pass = aaaa22222jjjj+H+vNeeeeeIyKx8rZXs"""

def get_event_return(): # Mock return of get event function
    return {
      "deduplicationKey": "abc",
      "instanceUuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "firstOccurrence": "2025-07-08T15:37:31.545Z",
      "lastOccurrence": "2025-07-08T15:37:31.545Z",
      "postTime": "2025-07-08T15:37:31.570Z",
      "resource": {
        "name": "Something failed",
        "type": "Unknown"
      },
      "accessScopes": [],
      "summary": "failure somewhere",
      "severity": 3,
      "severity10": 40,
      "maxSeverity10Seen": 40,
      "urls": [
        {
          "url": "https://example.com",
          "description": "Link to the SOAR incident."
        }
      ],
      "type": {
        "statusOrThreshold": "> 1 minute"
      },
      "eventSource": "Event API",
      "eventState": "open",
      "xInYSuppressed": False,
      "incidentUuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "suppressed": False,
      "eventid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }

def get_incident_return(): # Mock return of get incident function
    return {
      "state": "unassigned",
      "summary": "Name: Something failed",
      "description": "Name: Something failed",
      "owner": "-",
      "team": "-",
      "closedOwner": "-",
      "closedTeam": "-",
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "displayId": "0000-34m1",
      "createdTime": "2025-07-08T15:37:31.545Z",
      "lastChanged": "2025-07-08T15:37:33.436Z",
      "firstInProgressTime": "-",
      "resolvedTime": "-",
      "eventSummary": {
        "events": 1,
        "severities": [
          {
            "severity": 3,
            "count": 1
          }
        ],
        "severities10": [
          {
            "severity": 40,
            "count": 1
          }
        ],
        "maxSeverities10Seen": [
          {
            "severity": 40,
            "count": 1
          }
        ],
        "openSeverities10": [
          {
            "severity": 40,
            "count": 1
          }
        ]
      },
      "priority": 2,
      "escalated": False,
      "wasEscalated": False,
      "correlationDetails": {
        "name": "Something failed"
      },
      "accessScopes": []
    }

def create_event_return(): # Mock return of create event function
    return {
        "deduplicationKey": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "eventid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }

def query_incidents_return(): # Mock return of query incident function
  return [
    {
      "state": "unassigned",
      "summary": "Application: SAMPLE - Online Sales",
      "description": "Application: SAMPLE - Online Sales",
      "owner": "-",
      "team": "-",
      "closedOwner": "-",
      "closedTeam": "-",
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "displayId": "0000-32m1",
      "createdTime": "2025-07-08T15:00:37.538Z",
      "lastChanged": "2025-07-08T15:00:49.937Z",
      "firstInProgressTime": "-",
      "resolvedTime": "-",
      "priority": 2,
      "escalated": False,
      "wasEscalated": False,
      "correlationDetails": {
        "application": "SAMPLE - Online Sales"
      },
      "accessScopes": [],
      "incidentURL": "https://oncallmanager.ibm.com/api/incidentquery/v1/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "eventsURL": "https://oncallmanager.ibm.com/api/incidentquery/v1/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events",
      "timelineURL": "https://oncallmanager.ibm.com/api/incidentquery/v1/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/timeline"
    },
    {
      "state": "unassigned",
      "summary": "Application: SAMPLE - Online Banking",
      "description": "Application: SAMPLE - Online Banking",
      "owner": "-",
      "team": "-",
      "closedOwner": "-",
      "closedTeam": "-",
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "displayId": "0000-31m1",
      "createdTime": "2025-07-08T15:00:30.658Z",
      "lastChanged": "2025-07-08T15:00:54.943Z",
      "firstInProgressTime": "-",
      "resolvedTime": "-",
      "priority": 2,
      "escalated": False,
      "wasEscalated": False,
      "correlationDetails": {
        "application": "SAMPLE - Online Banking"
      },
      "accessScopes": [],
      "incidentURL": "https://oncallmanager.ibm.com/api/incidentquery/v1/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "eventsURL": "https://oncallmanager.ibm.com/api/incidentquery/v1/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/events",
      "timelineURL": "https://oncallmanager.ibm.com/api/incidentquery/v1/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/timeline"
    }
  ]

def list_incidents_return(): # Mock return of list incident function
    return [
    {
      "state": "unassigned",
      "summary": "Cluster: SAMPLE - Pipeline Project",
      "description": "Cluster: SAMPLE - Pipeline Project",
      "owner": "-",
      "team": "-",
      "closedOwner": "-",
      "closedTeam": "-",
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "displayId": "0000-20m1",
      "createdTime": "2025-05-23T14:29:03.698Z",
      "lastChanged": "2025-05-23T14:29:10.258Z",
      "firstInProgressTime": "-",
      "resolvedTime": "-",
      "priority": 2,
      "escalated": False,
      "wasEscalated": False,
      "correlationDetails": {
        "cluster": "SAMPLE - Pipeline Project"
      },
      "accessScopes": []
    },
    {
      "state": "unassigned",
      "summary": "Application: SAMPLE - Online Sales",
      "description": "Application: SAMPLE - Online Sales",
      "owner": "-",
      "team": "-",
      "closedOwner": "-",
      "closedTeam": "-",
      "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "displayId": "0000-19m1",
      "createdTime": "2025-05-23T14:29:00.871Z",
      "lastChanged": "2025-05-23T14:29:14.512Z",
      "firstInProgressTime": "-",
      "resolvedTime": "-",
      "priority": 2,
      "escalated": False,
      "wasEscalated": False,
      "correlationDetails": {
        "application": "SAMPLE - Online Sales"
      },
      "accessScopes": []
    }
  ]

def update_incident_return(): # Mock return of update incident function
    return {
    "state": "assignedToTeam",
    "summary": "Cluster: SAMPLE - Pipeline Project",
    "description": "Cluster: SAMPLE - Pipeline Project",
    "owner": "-",
    "team": "test_1",
    "closedOwner": "-",
    "closedTeam": "-",
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "displayId": "0000-20m1",
    "createdTime": "2025-05-23T14:29:03.698Z",
    "lastChanged": "2025-05-23T15:27:13.602Z",
    "firstInProgressTime": "-",
    "resolvedTime": "-",
    "eventTypeCounts": [
      {
        "eventType": "Build Status",
        "count": 3
      }
    ],
    "resourcePropertyCounts": [
      {
        "propertyName": "cluster",
        "propertyValue": "SAMPLE - Pipeline Project",
        "count": 3
      },
      {
        "propertyName": "hostname",
        "propertyValue": "buildbox",
        "count": 3
      },
      {
        "propertyName": "name",
        "propertyValue": "SAMPLE - Pipeline Project",
        "count": 3
      },
      {
        "propertyName": "type",
        "propertyValue": "Pipeline",
        "count": 3
      }
    ],
    "priority": 2,
    "escalated": False,
    "wasEscalated": False,
    "correlationDetails": {
      "cluster": "SAMPLE - Pipeline Project"
    },
    "accessScopes": [],
    "assignedBy": "MANUAL"
  }

def create_comment(self, incident_id: str, comment: str, author: str):
    return {}

def update_incident(self, incident_id:str, state:str="resolved", resolutionCode:str="", owner:str=None, team:str=None, matchedPolicies:list=None, eventsummary:bool=False, includecounts:bool=False):
    return update_incident_return()

def create_event(self, soar_inc_link:str, ocm_resource_name:str, summary:str, severity:str, statusOrThreshold:str=None, eventType:str=None, resource_type:str=None, resource_sourceId:str=None,
                resource_service:str=None, resource_cluster:str=None, resource_displayName:str=None, resource_component:str=None, resource_location:str=None,
                resource_application:str=None, resource_controller:str=None, resource_hostname:str=None, resource_ipaddress:str=None, resource_port:str=None,
                resource_interface:str=None, resource_correlationKey:str=None, resource_accessScope:str=None, priority:int=None, deduplicationkey:str=None, details:dict=None,
                resolution:bool=False, expiryTime:int=None):
    return create_event_return()

def list_incidents(self, owner:str=None, team:str=None, limit:int=9999, start:int=1, eventsummary:bool=False, includecounts:bool=False, stream:bool=False):
    return list_incidents_return()

def query_incidents(self, starttime:str=None, endtime:str=None, incident_filter:str=None, event_combiner:str="and", event_filter_1:str=None, event_filter_2:str=None, event_filter_3:str=None, event_filter_4:str=None, event_filter_5:str=None):
    return query_incidents_return()

def get_incident(self, incident_id:str):
    return get_incident_return()

def get_event(self, eventid:str, deduplicationKey:str):
    return get_event_return()
