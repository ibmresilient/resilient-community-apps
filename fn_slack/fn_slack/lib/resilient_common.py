# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import collections
import html
import html2text
import re
from six import string_types

INCIDENT_FRAGMENT = '#incidents'

def build_incident_url(url, incidentId):
    """
    build the url to link to an resilient incident
    :param url: base url
    :param incidentId:
    :return: full url
    """
    return '/'.join([url, INCIDENT_FRAGMENT, str(incidentId)])

def build_resilient_url(host, port):
    """
    build basic url to resilient instance
    :param host: host name
    :param port: port
    :return: base url
    """
    return "https://{0}:{1}".format(host, port)

def clean_html(htmlFragment):
    """
    Resilient textarea fields return html fragments. This routine will remove the html and insert any code within <div></div>
    with a linefeed
    :param htmlFragment:
    :return: cleaned up code
    """

    if not htmlFragment or not isinstance(htmlFragment, string_types):
        return htmlFragment

    return html2text.html2text(unescape(htmlFragment))


def unescape(data):
    """ Return unescaped data such as &gt; -> >, &quot -> ', etc. """
    try:
        return html.unescape(data)
    except:
        return data

def update_with_result(message, result):
    """Update the dict 'message', applying the values in 'result'
        recursively (unlike dict.update() which is shallow).
        >>> update_with_result({"a": 1, "b": "B"}, {"b": 2})
        {'a': 1, 'b': 2}
        >>> update_with_result({"properties": {"a": 1}}, {"properties": {"b": 2}})
        {'properties': {'a': 1, 'b': 2}}
        >>> update_with_result({'values': None}, {'properties': {'b': 2}})
        {'values': None, 'properties': {'b': 2}}
        >>> update_with_result({"properties": "string"}, {"properties": {"b": 2}})
        {'properties': {'b': 2}}
    """
    # LOG.info("Message: %s", message)
    # LOG.info("Result: %s", result)
    for k, v in result.items():
        if isinstance(message, collections.Mapping):
            if isinstance(v, collections.Mapping):
                r = update_with_result(message.get(k, {}), v)
                message[k] = r
            else:
                message[k] = result[k]
        else:
            message = {k: result[k]}

    return message


def validateFields(fieldList, kwargs):
    """
    ensure required fields are present. Throw ValueError if not
    :param fieldList:
    :param kwargs:
    :return: no return
    """
    for field in fieldList:
        if field not in kwargs or kwargs.get(field) == '':
            raise ValueError('Required field is missing or empty: '+field)

def groom(field_data):
    """ remove whitespae -- this is needed to load json strings"""
    return re.sub(r"\s+", " ", field_data)