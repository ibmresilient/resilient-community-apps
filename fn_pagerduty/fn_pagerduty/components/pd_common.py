# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import json
from fn_pagerduty.lib.requests_common import execute_call

PRIORITIES_FRAGMENT = 'priorities'
ESCALATION_FRAGMENT = 'escalation_policies'
SERVICE_FRAGMENT    = 'services'
INCIDENT_FRAGMENT   = 'incidents'
UPDATE_FRAGMENT     = '/'.join((INCIDENT_FRAGMENT, '{}'))
NOTE_FRAGMENT       = '/'.join((UPDATE_FRAGMENT, 'notes'))

HEADERS = { 'Accept': 'application/vnd.pagerduty+json;version=2',
            'Content-Type': 'application/json',
            'Authorization': 'Token token={}',
            'From': '{}'
          }

PD_BASE_URL = 'https://api.pagerduty.com'

def find_escalation_policy_by_name(log, appDict, name):
    """
    find the internal id for an escalation polocu
    :param log:
    :param appDict:
    :param name:
    :return: id of policy or None
    """
    headers = _build_header(appDict['api_token'], appDict['from_email'])

    # build url
    url = '/'.join((PD_BASE_URL, ESCALATION_FRAGMENT))

    resp = execute_call(log, 'get', url, None, None, None, True, headers, None)
    return _compareName(resp, 'escalation_policies', name.strip().lower())


def find_service_by_name(log, appDict, name):
    """
    return the service Id for a service
    :param log:
    :param appDict:
    :param name:
    :return: service Id or None
    """
    headers = _build_header(appDict['api_token'], appDict['from_email'])

    # build url
    url = '/'.join((PD_BASE_URL, SERVICE_FRAGMENT))

    resp = execute_call(log, 'get', url, None, None, None, True, headers, None)
    return _compareName(resp, 'services', name.strip().lower())


def find_priority_by_name(log, appDict, name):
    """
    Find the policy Id for a policy
    :param log:
    :param appDict:
    :param name:
    :return: policy Id or None
    """
    headers = _build_header(appDict['api_token'], appDict['from_email'])

    # build url
    url = '/'.join((PD_BASE_URL, PRIORITIES_FRAGMENT))

    # trap the possibility that priorities are disabled
    try:
        resp = execute_call(log, 'get', url, None, None, None, True, headers, None)
        return _compareName(resp, 'priorities', name.strip().lower())
    except:
        return None

def create_incident(log, appDict):
    """
    logic to create a pagerduty incident
    :param log:
    :param appDict:
    :return: the json string from the PD API
    """
    headers = _build_header(appDict['api_token'], appDict['from_email'])

    payload = build_incident_payload(appDict)

    # build url
    url = '/'.join((PD_BASE_URL, INCIDENT_FRAGMENT))
    resp = execute_call(log, 'post', url, None, None, payload, True, headers, None)
    return resp

def update_incident(log, appDict, incident_id, status, priority, resolution, callback):
    """
    update an incident. Used to raise the severity or to close the Incident
    :param log:
    :param appDict:
    :param incident_id:
    :param status:
    :param priority:
    :param resolution:
    :param callback: a callback method used to parse errors
    :return: the json string from the PD API
    """
    headers = _build_header(appDict['api_token'], appDict['from_email'])

    payload = build_update_payload(appDict, status, priority, resolution)

    # build url
    url = '/'.join((PD_BASE_URL, UPDATE_FRAGMENT))
    url = url.format(incident_id)
    resp = execute_call(log, 'put', url, None, None, payload, True, headers, callback)
    return resp


def create_note(log, appDict, incident_id, note, callback):
    """
    Create a PagerDuty note
    :param log:
    :param appDict:
    :param incident_id:
    :param note:
    :return: the json string from the PD API
    """
    headers = _build_header(appDict['api_token'], appDict['from_email'])

    payload = build_note_payload(note)

    # build url
    url = '/'.join((PD_BASE_URL, NOTE_FRAGMENT))
    url = url.format(incident_id)

    resp = execute_call(log, 'post', url, None, None, payload, True, headers, callback)
    return resp


def _compareName(resp, respName, compareName):
    """
    Search a list of objects (services, policies, priortities, etc.) and return the id for the search name
    :param resp:
    :param respName:
    :param compareName:
    :return: id found or None
    """
    for item in resp[respName]:
        if item['name'].lower() == compareName:
            return item['id']

    return None

def _build_header(api_token, from_email):
    """
    build the header needed for API calls
    :param api_token:
    :return: https headers
    """
    headers = HEADERS.copy()
    headers['Authorization'] = headers['Authorization'].format(api_token)
    headers['From'] = headers['From'].format(from_email)

    return headers

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
        payload['incident']['body'] = { 'type': 'incident_body',
                                        'details': appDict['description'] }

    if appDict.get('incident_key'):
        payload['incident']['incident_key'] = appDict['incident_key']

    if appDict.get('service'):
        # find the service
        serviceId = find_service_by_name(None, appDict, appDict['service'])
        if serviceId:
            payload['incident']['service'] = {
                "type": "service_reference",
                "id": serviceId
            }

    if appDict.get('escalation_policy'):
        # find the escalation policy
        escalationId = find_escalation_policy_by_name(None, appDict, appDict['escalation_policy'])
        if escalationId:
            payload['incident']['escalation_policy'] = {
                "type": "escalation_policy_reference",
                "id": escalationId
            }

    if appDict.get('priority'):
        # find the escalation policy
        priorityId = find_priority_by_name(None, appDict, appDict['priority'])
        if priorityId:
            payload['incident']['priority'] = {
                "type": "priority_reference",
                "id": priorityId
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
        priorityId = find_priority_by_name(None, appDict, priority)
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