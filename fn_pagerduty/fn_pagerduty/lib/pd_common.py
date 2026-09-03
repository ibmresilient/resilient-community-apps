# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
from logging import getLogger
from json import dumps
from pdpyras import APISession, PDClientError
from datetime import datetime, timedelta

PRIORITIES = 'priorities'
ESCALATION_POLICIES = 'escalation_policies'
SERVICES = 'services'
INCIDENT_FRAGMENT = 'incidents'
SINCE = 'since='
UPDATE_FRAGMENT = '/'.join((INCIDENT_FRAGMENT, '{}'))
NOTE_FRAGMENT = '/'.join((UPDATE_FRAGMENT, 'notes'))
PACKAGE_NAME = "pagerduty"
SIX_MONTHS_IN_WEEKS = 26

LOG = getLogger(__name__)

class PDClient(object):

    def __init__(self, appDict: dict):
        self.pdClient = APISession(appDict.get('api_token'),
                                   name=appDict.get('resilient_client'),
                                   default_from=appDict.get('from_email'))
        self.appDict = appDict
    
    def PDsession(self):
        """
        Return PagerDuty APISession
        Used by the poller
        """
        return self.pdClient
    
    def find_element_by_name(self, element, name):
        """
        Find the internal id for a PagerDuty element (policy, service, priority, etc.)
        :param appDict:
        :param element: escalation_policies, service, priority, etc.
        :param name:
        :return: id of policy or None
        """
        try:
            rtn_element = self.pdClient.find(element, name.strip().lower())
            LOG.debug(rtn_element)
            return rtn_element.get('id') if rtn_element else None
        except PDClientError as err:
            LOG.error(str(err))

    def create_incident(self):
        """
        Logic to create a PagerDuty incident
        :param appDict:
        :return: the json string from the PD API
        """
        return self.pdClient.post(
            INCIDENT_FRAGMENT,
            build_incident_payload(self.appDict)
        ).json()

    def create_service(self):
        """
        Logic to create a PagerDuty service
        :param appDict:
        :return: the json string from the PD API
        """
        return self.pdClient.post(
            SERVICES,
            build_service_payload(self.appDict)
        ).json()
    
    def update_incidents(self, payload):
        """
        Update multiple PagerDuty incidents at once
        :param payload (dict): Payload of incident updates
        :return (dict): json response from PagerDuty
        """
        return self.pdClient.put(
            INCIDENT_FRAGMENT,
            dumps(payload)
        ).json()

    def update_incident(self, incident_id, status, priority, resolution, severity):
        """
        Update an incident. Used to raise the severity or to close the Incident
        :param incident_id:
        :param status:
        :param priority:
        :param resolution:
        :return: the json string from the PD API
        """
        return self.pdClient.put(
            UPDATE_FRAGMENT.format(incident_id),
            build_update_payload(self.appDict, status, priority, resolution, severity)
        ).json()

    def create_note(self, incident_id: str, note: str):
        """
        Create a PagerDuty note
        :param incident_id:
        :param note:
        :return: the json string from the PD API
        """
        return self.pdClient.post(
            NOTE_FRAGMENT.format(incident_id),
            build_note_payload(note)
        ).json()

    def list_incident_notes(self, incident_id: str):
        """
        List notes that are on the PagerDuty incident
        Args:
            incident_id (str): PagerDuty incident id
        """
        return self.pdClient.get(NOTE_FRAGMENT.format(incident_id)).json()

    def list_incidents(self, timestamp: str=None, statuses: list=[], time_zone: str="UTC",
                    service_ids: list=[], urgencies: str=None, user_ids: list=[], team_ids: list=[]):
        """
        List incidents that match given filters
        :param appDict: (dict) Settings from the app.config
        :param timestamp: (str) A string of an integer time, example 1713375533.059529
        :param statuses: (list) A list of PagerDuty incident statuses to filter for. Allowed values are triggered, acknowledged, and resolved.
        :param time_zone: (str) Time zone string to use. Example: UTC
        :param service_ids: (list) A list of PagerDuty service ids to filter for.
        :param urgencies: (str) The PagerDuty urgency to filter for. Allowed values are high and low.
        :param user_ids: (list) A list of PagerDuty user ids to filter for.
        :param team_ids: (list) A list of PagerDuty team ids to filter for.
        :return: the json string from the PD API
        """    
        params = {"time_zone": time_zone} # Filters to use when querying PagerDuty incidents
        if timestamp:
            since_date = datetime.fromtimestamp(int(timestamp))
            if since_date < datetime.now() - timedelta(weeks=SIX_MONTHS_IN_WEEKS):
                raise ValueError("The maximum range is 6 months")
            else:
                params["since"] = since_date.isoformat()

        if statuses: # Allowed values are triggered, acknowledged, and resolved
            params["statuses[]"] = statuses
        if service_ids:
            params["service_ids[]"] = service_ids
        if urgencies and urgencies.lower() in ["high", "low"]: # Allowed values are high and low
            params["urgencies[]"] = urgencies
        if user_ids:
            params["user_ids[]"] = user_ids
        if team_ids:
            params["team_ids[]"] = team_ids
        # Make call to PagerDuty to return incidents that match the given filters.
        return self.pdClient.get(INCIDENT_FRAGMENT, params=params).json()

    def list_services(self):
        """
        List all the services
        :param appDict:
        :return: the json string from the PD API
        """
        return self.pdClient.get(SERVICES).json()

def build_incident_payload(appDict):
    """
    build the JSON payload to create an incident
    :param appDict:
    :return: json
    """
    client = PDClient(appDict)
    payload = { 
        'incident': {
            'type': 'incident',
            'title': appDict.get("title")
        }
    }

    # optional parts
    if appDict.get('description'):
        payload['incident']['body'] = {
            'type': 'incident_body',
            'details': appDict.get('description')
        }

    if appDict.get('incident_key'):
        payload['incident']['incident_key'] = appDict.get('incident_key')

    if appDict.get('service'):
        # find the service
        serviceId = client.find_element_by_name(SERVICES, appDict.get('service'))
        if serviceId:
            payload['incident']['service'] = {
                "type": "service_reference",
                "id": serviceId
            }

    if appDict.get('escalation_policy'):
        # find the escalation policy
        escalationId = client.find_element_by_name(ESCALATION_POLICIES, appDict.get('escalation_policy'))
        if escalationId:
            payload['incident']['escalation_policy'] = {
                "type": "escalation_policy_reference",
                "id": escalationId
            }

    if appDict.get('priority'):
        # find the escalation policy
        priorityId = client.find_element_by_name(PRIORITIES, appDict.get('priority'))
        if priorityId:
            payload['incident']['priority'] = {
                "type": "priority_reference",
                "id": priorityId
            }

    LOG.debug(payload)
    return dumps(payload)

def build_service_payload(appDict):
    """
    Build the JSON payload to create a service
    :param appDict:
    :return: json
    """
    payload = {
        'service':  {
            'type': 'service',
            'name': appDict.get("title")
        }
    }

    # optional parts
    if appDict.get('description'):
        payload['service']['description'] = appDict.get('description')
        
    if appDict.get('escalation_policy'):
        # find the escalation policy
        escalationId = PDClient(appDict).find_element_by_name(ESCALATION_POLICIES, appDict.get('escalation_policy'))
        if escalationId:
            payload['service']['escalation_policy'] = {
                "type": "escalation_policy_reference",
                "id": escalationId
            }

    LOG.debug(payload)
    return dumps(payload)

def build_update_payload(appDict, status, priority, resolution, severity = None):
    """
    Build the JSON payload to update an incident
    :param appDict:
    :param status:
    :param priority:
    :param resolution:
    :param severity:
    :return: JSON payload
    """
    payload= {
        "incident": {
            "type": "incident_reference"
        }
    }

    if status:
        payload['incident']['status'] = status
    
    if severity and severity.lower() in ['low', 'high']:
        payload['incident']['urgency'] = severity.lower()

    if priority:
        # find the escalation policy
        priorityId = PDClient(appDict).find_element_by_name(PRIORITIES, priority)
        if priorityId:
            payload['incident']['priority'] = {
                "type": "priority_reference",
                "id": priorityId
            }

    if resolution:
        payload['incident']['resolution'] = resolution

    LOG.debug(payload)
    return dumps(payload)

def build_note_payload(note):
    """
    build the JSON to create a Note
    :param note:
    :return: JSON payload
    """
    payload = {
        "note": {
            "content": note
        }
    }

    LOG.debug(payload)
    return dumps(payload)
