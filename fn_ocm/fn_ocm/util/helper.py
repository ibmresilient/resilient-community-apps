# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
# Helper file

from json import dumps
from resilient_lib import IntegrationError
PACKAGE_NAME = "fn_ocm"

def custom_callback(response):
    # custom callback function to handle error codes between 405 and 500
    if response.status_code > 409 and response.status_code < 500:
        # raise ValueError which will be retried
        raise ValueError("retry me")
    elif response.status_code <= 400:
        return response.json()
    elif response.status_code == 409:
        return {"level": "error", "description": response.text}
    else:
        return {"level": "error", "description": response.reason}

class ocm_client():
    def __init__(self, base_url, api_key_name, api_key_pass, rc):
        self.base_url = base_url
        self.basicAuth = (api_key_name, api_key_pass)
        self.rc = rc

    def execute_call(self, method: str, uri: str, data: dict={}, **args):
        """Make an API call to On Call Manager

        Args:
            uri (str): The URI path to call.
            method (str): The request method to make. Defaults to "GET".
            data (dict, optional): Payload to send with API call. Defaults to {}.
        """
        header = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }
        return self.rc.execute(method, f"{self.base_url}{uri}", data=dumps(data), auth=self.basicAuth, headers=header, callback=custom_callback, **args)

    def create_event(self, soar_inc_link:str, ocm_resource_name:str, summary:str, severity:str, statusOrThreshold:str=None, eventType:str=None, resource_type:str=None, resource_sourceId:str=None,
                     resource_service:str=None, resource_cluster:str=None, resource_displayName:str=None, resource_component:str=None, resource_location:str=None,
                     resource_application:str=None, resource_controller:str=None, resource_hostname:str=None, resource_ipaddress:str=None, resource_port:str=None,
                     resource_interface:str=None, resource_correlationKey:str=None, resource_accessScope:str=None, priority:int=None, deduplicationkey:str=None, details:dict=None,
                     resolution:bool=False, expiryTime:int=None):
        """Creates an event in On Call Manager. The event that is created automatically creates an incident in On Call Manager.

        Args:
            soar_inc_link (str, required): The URL back to the SOAR incident.
            ocm_resource_name (str, required): The name of the resource causing the event. Identifies the primary resource that the event is affecting.
            summary (str, required): Contains text which describes the event condition.
            severity (str, required): The severity of the event.
            statusOrThreshold (str, optional): The status or the threshold causing the event. E.g. Down, 95%, Unavailable
            eventType (str, optional): Description of the type of the event. E.g. Utilization, System status, Threshold breach
            resource_type (str, optional): The type of the resource causing the event. Should be used to identify the primary resource that the event is affecting. The value of the type field can be one of the defined key types for resources, eg Application, Server, Service, Cluster. Or it can be a user defined value. If a defined value is used, then the event processing may make use of it during processing.
            resource_sourceId (str, optional): The id the resource is known by in the source system
            resource_service (str, optional): The service that caused the event
            resource_cluster (str, optional): The cluster that caused the event
            resource_displayName (str, optional): The display name for the resource
            resource_component (str, optional): The component that caused the event
            resource_location (str, optional): Where the event is being reported from
            resource_application (str, optional): The application that caused the event
            resource_controller (str, optional): The controller that caused the event
            resource_hostname (str, optional): The fully qualified hostname
            resource_ipaddress (str, optional): The IP address of the device
            resource_port (str, optional): The port reporting the issue
            resource_interface (str, optional): The interface reporting the issue
            resource_correlationKey (str, optional): This is the key used to determine if event records presented to the system should be correlated to the same incident. If present, it prevents construction of a corelation key, if not present the corelation will be constructed from the resource.
            resource_accessScope (str, optional): The project or namespace the resource is part of
            priority (int, optional): The integer priority of the event
            deduplicationkey (str, optional): This is the key used to determine if two instances of an event record presented to the system de-duplicate. If present prevents construction of identifier for de-duplication. If not present the Identifier will be constructed from the resource and type fields.
            details (dict, optional): Additional properties for the event, key,value value may be string or integer
            resolution (bool, optional): True if this is a resolution event. Defaults to False.
            expiryTime (int, optional): The number of seconds after which the event will be cleared, if there have been no further occurrence
        """
        # Build payload
        payload = {
            "resource": {"name": ocm_resource_name},
            "summary": summary,
            "severity": severity,
            "type": {},
            "urls": [# Add link back to the SOAR incident
                {
                    "url": soar_inc_link,
                    "description": "Link to the SOAR incident."
                }
            ]
        }
        if statusOrThreshold: # Add type property if given
            payload["type"]["statusOrThreshold"] = statusOrThreshold
        if eventType: # Add type property if given
            payload["type"]["eventType"] = eventType
        # Dictionary of event resource property names and given value.
        resources = {"type": resource_type, "sourceID": resource_sourceId, "service": resource_service, "cluster": resource_cluster, "displayName": resource_displayName,
                     "component": resource_component, "location": resource_location, "application": resource_application, "controller": resource_controller, "hostname": resource_hostname,
                     "ipaddress": resource_ipaddress, "port": resource_port, "interface": resource_interface, "correlationKey": resource_correlationKey, "accessScope": resource_accessScope}
        for key, value in resources.items(): # Loop through resource property inputs and add the ones with values to the payload
            if value: # Check if a value was given
                payload["resource"][key] = value # Add the property to the resource dict in the payload
        if priority: # Add int priority if given
            payload["priority"] = priority
        if deduplicationkey: # Add deduplicationkey if value given
            payload["deduplicationkey"] = deduplicationkey
        if details: # Add details if value given
            payload["details"] = details
        if resolution is not None: # Add boolean value if given
            payload["resolution"] = resolution
        if expiryTime: # Add expiryTime if given
            payload["expiryTime"] = expiryTime

        return self.execute_call("POST", f"events/v1", data=payload)

    def query_incidents(self, starttime:str=None, endtime:str=None, incident_filter:str=None, event_combiner:str="and", event_filter_1:str=None, event_filter_2:str=None, event_filter_3:str=None, event_filter_4:str=None, event_filter_5:str=None):
        """Query incidents for a given period of time based on properties of the incident or properties of the events correlated to the incidents. By default, incidents created in the last 7 days will be retrieved and filtered. A start time and end time can be provided to define the time range, but the range is limited to a 30 day period. The query also has a limit of 500 incidents being returned for any query.
Incidents can be requested by incident properties, like incident priority and incident state. You can also set 1 or more event filters that set conditions on events that must be correlated to an incident for it to be included in the query results. You can filter only on incident properties, only on properties of the correlated events, or a combination of the two.

        Args:
            starttime (str, optional): Beginning UTC timestamp (YYYY-MM-DDTHH:mm:SS.sssZ) for range of incidents to query - will default to system configured value of 7 days ago. This time is compared to the "created" time of an incident to determine if the incident should be included. Example values: 2017-09-12T08:00:00.000Z, 2017-09-12T08:00, 2017-09-12
            endtime (str, optional): Ending UTC timestamp (YYYY-MM-DDTHH:mm:SS.sssZ) for range of incidents to query - - will default to current time. This time is compared to the "created" time of an incident to determine if the incident should be included. Example values: 2017-09-14T17:00:00.000Z, 2017-09-14T17:00, 2017-09-14
            incident_filter (str, optional): A condition filter that specifies expression matches for incident properties. Examples: 'lastChanged > "2017-08-01"', 'priority == 5 OR priority == 4'
            event_combiner (str, optional): Set to "and" or "or" to indicate how the event filters should be combined when filtering by event content. The default is to combine the event filters using the "and" operator, meaning all event filters must be satisfied by any returned incident. Use "or" if only one of the event filters must be satisfied. Available values: and, or
            event_filter_1 (str, optional): A condition filter that specifies expression matches for the properties of a single event on the incident. Examples: severity >= "minor"
            event_filter_2 (str, optional): A condition filter that specifies expression matches for the properties of a single event on the incident. Examples: summary starts with "Failure" and resource.application == "payroll"
            event_filter_3 (str, optional): A condition filter that specifies expression matches for the properties of a single event on the incident. Examples: type.eventType == 'a1' or type.eventType == 'a2' or type.eventType == 'a3'
            event_filter_4 (str, optional): A condition filter that specifies expression matches for the properties of a single event on the incident. Examples: summary starts with "Failure"
            event_filter_5 (str, optional): A condition filter that specifies expression matches for the properties of a single event on the incident. Examples: type.eventType == 'a2'
        """
        # Make API call to query for incidents
        return self.execute_call("GET", f"incidentquery/v1",
                                 params={"starttime": starttime, "endtime": endtime, "incident_filter": incident_filter,
                                         "event_combiner": event_combiner, "event_filter_1": event_filter_1, "event_filter_2": event_filter_2,
                                         "event_filter_3": event_filter_3, "event_filter_4": event_filter_4, "event_filter_5": event_filter_5})

    def get_incident(self, incident_id:str):
        """Get incident on the default queue.

        Args:
            incident_id (str): Incident ID
        """
        # Make API call to get an incident
        return self.execute_call("GET", f"incidentquery/v1/{incident_id}")

    def list_incidents(self, owner:str=None, team:str=None, limit:int=9999, start:int=1, eventsummary:bool=False, includecounts:bool=False, stream:bool=False):
        """List incidents in a team, owner, or default queue. Specify only owner to get a personal queue. Specify only team for a team queue. Omit owner and team to fetch incidents that are on the default queue.

        Args:
            owner (str, optional): Fetch only incidents on the queue associated with this owner. This parameter takes precedence over team.
            team (str, optional): Fetch only incidents on the queue associated with this team. Ignored if owner is specified.
            limit (int, optional): Limit the returned matching incidents to the first N incidents starting with _start index. Defaults to 9999.
            start (int, optional): Return the matching incidents starting from the specified 1 based index. Defaults to 1.
            eventsummary (bool, optional): Include the event summary for each matching incident. Defaults to False.
            includecounts (bool, optional): Include the event type and resource property counts for each matching incident. Defaults to False.
            stream (bool, optional): Stream the results. Defaults to False.

        Returns:
            list: List of incidents.
        """
        # Build the uri
        uri = f'incimgmt/v1?_start={start}&_limit={limit}&eventsummary={str(eventsummary).lower()}&includecounts={str(includecounts).lower()}&stream={str(stream).lower()}'
        if owner: # If owner given add to query
            uri += f"&owner={owner}"
        elif team: # If team is given add to query
            uri += f"&team={team}"
        # Make API call to list incidents
        return self.execute_call("GET", uri)

    def create_comment(self, incident_id: str, comment: str, author: str):
        """Creates a comment on the incident

        Args:
            incident_id (str): ID of the On Call Manager incident.
            comment (str): Comment to add to the incident.
            author (str): The user creating the comment.
        """
        return self.execute_call("POST", f"incimgmt/v1/{incident_id}/comment", {"comment":comment, "author":author})

    def list_incident_policies(self, expand:bool=False):
        """List the summary information for all policies within a subscription.

        Args:
            expand (bool, optional): Includes detail information with each policy. Defaults to False.

        Returns:
            list: List of incident policies.
        """
        return self.execute_call("GET", f"incidentPolicies/v1?expand={str(expand).lower()}")

    def update_incident(self, incident_id:str, state:str="resolved", resolutionCode:str="", owner:str=None, team:str=None, matchedPolicies:list=None, eventsummary:bool=False, includecounts:bool=False):
        """Updates the header properties of an incident, like state, owner, and team. Set the owner to move the incident to a personal queue associated with the owner. Set the team, but not the owner, to put the incident on the team queue. Incidents with no team or owner set are on the default queue. Set the owner and/or team to a single dash(-) to clear the values and move the incident back to the default queue.

        Args:
            incident_id (str): On Call Manager incident ID.
            state (str): State to be set for the incident. Values are unassigned, assignedToTeam, assignedToIndividual, inProgress, onHold, resolved, closed. Defaults to "resolved".
            resolutionCode (str, optional): Reason for incident being moved to the resolved state. Only allowed when state is also specified with a value of resolved or closed. Values are "" or rejected. Defaults to "".
            owner (str, optional): Owner to be assigned to the incident. This puts the incident on the personal queue for the owner. Use a single dash(-) to clear the owner value, which moves the incident to the team queue, if team is set, or the default queue.
            team (str, optional): Team to be set as responsible for the incident. This puts the incident on the team queue, but only if the owner is not set. Use a single dash(-) to clear the team value, which moves the incident to the default queue, assuming owner is not set.
            matchedPolicies (list, optional): List of policy ids that have been matched to the incident.
            eventsummary (bool, optional): Include the event summary for each matching incident. Defaults to False.
            includecounts (bool, optional): Include the event type and resource property counts for each matching incident. Defaults to False.
        """
        # Build payload for API call
        payload = {"state": state}
        # If owner given then team must also be given
        if owner and team:
            payload["owner"] = owner
            payload["team"] = team
            # If incident state is unassigned or assignedToTeam, then change it to assignedToIndividual.
            if state in ["unassigned", "assignedToTeam"]:
                payload["state"] = "assignedToIndividual"
        elif owner: # Fail if just owner given
            raise IntegrationError("When assigning an owner to the incident a group must also be given.")
        elif team: # Check if just team given
            payload["team"] = team
            # If state is unassigned or assignedToIndividual, then change it to assignedToTeam.
            if state in ["unassigned", "assignedToIndividual"]:
                payload["state"] = "assignedToTeam"

        # Add resolutionCode if state is either resolved or closed.
        if state in ["resolved", "closed"]:
            payload["resolutionCode"] = resolutionCode if resolutionCode else ""
        if owner: # Add owner if one given. If - given then remove the owner.
            payload["owner"] = owner
        if team: # Add team if one given. If - given then remove the team.
            payload["team"] = team
        if matchedPolicies: # Add list of matched policies to the incident if given.
            payload["matchedPolicies"] = matchedPolicies
        return self.execute_call("POST", f"incimgmt/v1/{incident_id}?eventsummary={str(eventsummary).lower()}&includecounts={str(includecounts).lower()}", data=payload)

    def get_event(self, eventid:str, deduplicationKey:str):
        """Get event details.

        Args:
            eventid (str): Event ID
            deduplicationKey (str): deduplicationKey of the event.
        """
        return self.execute_call("GET", f"events/v1?eventid={eventid}&deduplicationKey={deduplicationKey}")
