# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
import logging
import json
from pdpyras import APISession, PDClientError
from datetime import datetime, timedelta

PRIORITIES = 'priorities'
ESCALATION_POLICIES = 'escalation_policies'
SERVICES = 'services'
INCIDENT_FRAGMENT = 'incidents'
SINCE = 'since='
UPDATE_FRAGMENT = '/'.join((INCIDENT_FRAGMENT, '{}'))
NOTE_FRAGMENT = '/'.join((UPDATE_FRAGMENT, 'notes'))
PACKAGE_NAME = "fn_pagerduty"

LOG = logging.getLogger(__name__)

def find_element_by_name(appDict, element, name):
    """
    find the internal id for a pagerduty element (policy, service, priority, etc.)
    :param appDict:
    :param element: escalation_policies, service, priority, etc.
    :param name:
    :return: id of policy or None
    """

    session = APISession(appDict['api_token'])
    try:
        rtn_element = session.find(element, name.strip().lower())
        LOG.debug(rtn_element)
        return rtn_element['id'] if rtn_element else None
    except PDClientError as err:
        LOG.error(str(err))

    return None

def create_incident(appDict):
    """
    logic to create a pagerduty incident
    :param appDict:
    :return: the json string from the PD API
    """

    payload = build_incident_payload(appDict)
    LOG.debug(payload)

    # build url
    session = APISession(appDict['api_token'], name=appDict['resilient_client'], default_from=appDict['from_email'])
    resp = session.post(INCIDENT_FRAGMENT, payload)
    return resp.json()

def create_service(appDict):
    """
    logic to create a pagerduty service
    :param appDict:
    :return: the json string from the PD API
    """

    payload = build_service_payload(appDict)
    LOG.debug(payload)

    # build url
    session = APISession(
        appDict['api_token'], name=appDict['resilient_client'])
    resp = session.post(SERVICES, payload)
    return resp.json()

def update_incident(appDict, incident_id, status, priority, resolution):
    """
    update an incident. Used to raise the severity or to close the Incident
    :param appDict:
    :param incident_id:
    :param status:
    :param priority:
    :param resolution:
    :return: the json string from the PD API
    """
    payload = build_update_payload(appDict, status, priority, resolution)

    # build url
    url = UPDATE_FRAGMENT.format(incident_id)
    session = APISession(appDict['api_token'], name=appDict['resilient_client'], default_from=appDict['from_email'])
    resp = session.put(url, payload)
    return resp.json()


def create_note(appDict, incident_id, note):
    """
    Create a PagerDuty note
    :param appDict:
    :param incident_id:
    :param note:
    :return: the json string from the PD API
    """
    payload = build_note_payload(note)

    # build url
    url = NOTE_FRAGMENT.format(incident_id)

    session = APISession(appDict['api_token'], name=appDict['resilient_client'], default_from=appDict['from_email'])
    resp = session.post(url, payload)
    return resp.json()


def list_incidents(appDict, timestamp):
    """
    List all the incidents
    :param appDict:
    :return: the json string from the PD API
    """    
    
    session = APISession(appDict['api_token'])
    if timestamp:
        timestamp_seconds =int(str(timestamp)[:-3])
        since_date = datetime.fromtimestamp(timestamp_seconds)
        since_date_str = since_date.strftime("%Y-%m-%d")
        six_months_ago = datetime.now() - timedelta(days=6*30)
        
        if since_date < six_months_ago:
            raise ValueError("The maximum range is 6 months")
        else:
            resp = session.get(INCIDENT_FRAGMENT + "?" + SINCE + since_date_str)
    else:
        resp = session.get(INCIDENT_FRAGMENT)
    return resp.json()


def list_services(appDict):
    """
    List all the services
    :param appDict:
    :return: the json string from the PD API
    """
    session = APISession(appDict['api_token'])
    resp = session.get(SERVICES)
    return resp.json()

def build_incident_payload(appDict):
    """
    build the JSON payload to create an incident
    :param appDict:
    :return: json
    """
    payload = { 'incident':
                {
                    'type': 'incident',
                    'title': appDict['title']
                }
              }

    # optional parts
    if appDict['description']:
        payload['incident']['body'] = {
            'type': 'incident_body',
            'details': appDict['description']
        }

    if appDict.get('incident_key'):
        payload['incident']['incident_key'] = appDict['incident_key']

    if appDict.get('service'):
        # find the service
        serviceId = find_element_by_name(appDict, SERVICES, appDict['service'])
        if serviceId:
            payload['incident']['service'] = {
                "type": "service_reference",
                "id": serviceId
            }

    if appDict.get('escalation_policy'):
        # find the escalation policy
        escalationId = find_element_by_name(appDict, ESCALATION_POLICIES, appDict['escalation_policy'])
        if escalationId:
            payload['incident']['escalation_policy'] = {
                "type": "escalation_policy_reference",
                "id": escalationId
            }

    if appDict.get('priority'):
        # find the escalation policy
        priorityId = find_element_by_name(appDict, PRIORITIES, appDict['priority'])
        if priorityId:
            payload['incident']['priority'] = {
                "type": "priority_reference",
                "id": priorityId
            }

    return json.dumps(payload)


def build_service_payload(appDict):
    """
    build the JSON payload to create a service
    :param appDict:
    :return: json
    """
    payload = {'service':
               {
                   'type': 'service',
                   'name': appDict['title']
               }
               }
    
    # optional parts
    if appDict['description']:
        payload['service']['description'] = appDict['description']
        
    if appDict.get('escalation_policy'):
        # find the escalation policy
        escalationId = find_element_by_name(
            appDict, ESCALATION_POLICIES, appDict['escalation_policy'])
        if escalationId:
            payload['service']['escalation_policy'] = {
                "type": "escalation_policy_reference",
                "id": escalationId
            }
            
    return json.dumps(payload)

def build_update_payload(appDict, status, priority, resolution):
    """
    build the JSON payload to update an incident
    :param appDict:
    :param status:
    :param priority:
    :param resolution:
    :return: JSON payload
    """
    payload= {
        "incident": {
            "type": "incident_reference"
        }
    }

    if status:
        payload['incident']['status'] = status

    if priority:
        # find the escalation policy
        priorityId = find_element_by_name(appDict, PRIORITIES, priority)
        if priorityId:
            payload['incident']['priority'] = {
                "type": "priority_reference",
                "id": priorityId
            }

    if resolution:
        payload['incident']['resolution'] = resolution

    return json.dumps(payload)


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

    return json.dumps(payload)