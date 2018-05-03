# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
import collections
import datetime
import html2text
import re
from six import string_types
try:
    import HTMLParser as htmlparser
except:
    import html.parser as htmlparser

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
        return htmlparser.unescape(data)
    except:
        return data


def validate_fields(fieldList, kwargs):
    """
    ensure required fields are present. Throw ValueError if not
    :param fieldList:
    :param kwargs:
    :return: no return
    """
    for field in fieldList:
        if field not in kwargs or kwargs.get(field) == '':
            raise ValueError('Required field is missing or empty: '+field)

def build_timestamp(ts, format="%Y-%m-%dT%H:%M:%SZ"):
    """ create a timestamp. ts is in milliseconds """
    return datetime.datetime.utcfromtimestamp(ts/1000).strftime(format)