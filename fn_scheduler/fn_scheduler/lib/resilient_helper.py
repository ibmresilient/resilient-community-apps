# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

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

def get_rule_by_name(rest_client, rule_name):
    """
    api call to get a resilient rule
    :param rest_client:
    :param rule_name:
    :return: rule in json format
    """
    rules = get_rules(rest_client)

    for rule in rules['entities']:
        if rule['name'].lower() == rule_name.lower():
            if not rule['enabled']:
                raise AttributeError(u"Rule '{}' is disabled".format(rule_name))

            return (rule['id'], rule["object_type"])

    return (None, None)

def get_rule_by_id(rest_client, rule_id):
    """
    api call to get a resilient rule by id and ensure the rule is still enabled
    :param incident_id:
    :param rule_id:
    :return: True if rule is enabled for an incident or AttributeError
    """
    rules = get_rules(rest_client)

    for rule in rules['entities']:
        if rule['id'] == rule_id:
            if rule['enabled']:
                return True
            else:
                raise AttributeError("Rule is disabled")

    raise KeyError("Rule id {} is not found".format(rule_id))

def get_rules(rest_client):
    """
    api call to get all rules for the resilient organization
    :param rest_client:
    :return: json formatted rule list
    """
    url = "/actions"

    return rest_client.get(url)

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
