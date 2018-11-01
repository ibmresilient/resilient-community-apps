# -- coding: utf-8 --
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

import datetime
from bs4 import BeautifulSoup
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

    s = BeautifulSoup(unescape(htmlFragment), "html.parser")

    return ' '.join(s.strings)


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


def readable_datetime(timestamp, milliseconds=True, rtn_format='%Y-%m-%d %H:%M:%S'):
    """
    convert an epoch timestamp to a string using a format
    :param timestamp:
    :param milliseconds: True = epoch in
    :param rtn_format: format of resulant string
    :return: string representation of timestamp
    """
    if milliseconds:
        ts = int(timestamp/1000)
    else:
        ts = timestamp

    return datetime.datetime.utcfromtimestamp(ts).strftime(rtn_format)
