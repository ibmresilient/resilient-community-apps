# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
from resilient_lib import validate_fields
from fn_scheduler.components import SECTION_SCHEDULER


def get_incident(rest_client, incident_id):
    """
    api call to get a resilient incident
    :param rest_client:
    :param incident_id:
    :return: incident in json format
    """
    url = "/incidents/{}".format(incident_id)
    resp = rest_client.get(url)

    return resp

def get_rule_by_name(rest_client, pb_name):
    """
    api call to get a resilient rule
    :param rest_client: object to make API calls back to SOAR
    :param pb_name: either a rule name or playbook name (can be pb_name)
    :return: rule in json format
    """
    rules = get_rules(rest_client)

    # try rules
    for rule in rules['entities']:
        if rule['name'].lower() == pb_name.lower():
            if not rule['enabled']:
                raise AttributeError(u"Rule '{}' is disabled".format(pb_name))

            return (rule['id'], rule["object_type"])

    # try playbooks
    playbooks = get_playbooks(rest_client)

    for playbook in playbooks['data']:
        if playbook['name'] == pb_name.lower() or playbook['display_name'].lower() == pb_name.lower():
            if playbook['status'] != 'enabled':
                raise AttributeError(u"Playbook '{}' is disabled".format(pb_name))

            return (playbook['id'], playbook["object_type"])

    return (None, None)

def get_rule_by_id(rest_client, pb_id):
    """
    api call to get a SOAR rule/playbook by id and ensure that it is still enabled
    :param rest_client: object to make API calls back to SOAR
    :param pb_id: rule or playbook id
    :return: True is id is a playbook, false if a rule.
    :raises AttributeError if the rule/playbook disabled
    :raises KeyError if the id is not found
    """
    rules = get_rules(rest_client)

    for rule in rules['entities']:
        if rule['id'] == pb_id:
            if rule['enabled']:
                return False
            else:
                raise AttributeError("Rule id '{}' is disabled".format(pb_id))

    # try playbooks
    playbooks = get_playbooks(rest_client)

    for playbook in playbooks['data']:
        if playbook['id'] == pb_id:
            if playbook['status'] == 'enabled':
                return True
            else:
                raise AttributeError(u"Playbook id '{}' is disabled".format(pb_id))

    raise KeyError("Rule/Playbook id '{}' is not found".format(pb_id))

def get_rules(rest_client):
    """
    api call to get all rules for the SOAR organization
    :param rest_client:
    :return: json formatted rule list
    """
    url = "/actions"

    return rest_client.get(url)

def get_playbooks(rest_client):
    """
    api call to get all playbooks for the SOAR organization
    :param rest_client:
    :return: json formatted rule list
    """
    url = "/playbooks/query_paged"

    payload = {
        "sorts": [
            {
                "field_name": "display_name",
                "type": "asc"
            }
        ]
    }

    return rest_client.post(url, payload)

def add_comment(rest_client, incident_id, comment):
    """
    api call to add a comment to an incident
    :param rest_client:
    :param incident_id:
    :param comment:
    :return: json formatted response
    """
    url = "/incidents/{}/comments".format(incident_id)
    payload = {
        "text": {
            "format": "text",
            "content": comment
        }
    }

    return rest_client.post(url, payload)

def lookup_object_type(rest_client, type_id):
    """
    convert a resilient object_type_id into a label for use in api call for rule invocation
    :param type: internal number of object
    :return: object name or ValueError if not found
    """
    lookup = ['', 'tasks', 'notes', 'milestones', 'artifacts', 'attachments', None, 'organizations']

    if type_id <= len(lookup):
        if lookup[type_id] is not None:
            return lookup[type_id]
    else:
        # check to see if a datatable
        url = "/types/{}".format(type_id)
        resp = rest_client.get(url)

        if resp['type_id'] == 8:
            return "table_data"

    raise ValueError("Rule type not supported")

def validate_app_config(options):
    """
    ensure app.config settings are in place
    :param options:
    :return: True if success, otherwise ValueError
    """
    validate_fields(["thread_max", "timezone"], options)
    if not options.get("db_url", options.get("datastore_dir", False)):
        raise ValueError("Specify either [{}] db_url or datastore_dir".format(SECTION_SCHEDULER))
    return True