# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import future        # pip install future
import builtins      # pip install future
import past          # pip install future
import six           # pip install six
from past.builtins import basestring, unicode
import tldextract
import logging
import time
import traceback
from ipwhois import IPWhois, exceptions
from datetime import datetime, date

ip_from_domain = None

def time_str():
    today = date.fromtimestamp(time.time())
    timestamp = time.strftime('%H:%M:%S')
    timenow = "{1} on {0}".format(today, timestamp)
    return timenow


def check_input_ip(query):
    """This function checks if the input is an IP, URL or DNS

    Arguments:
        query {string} -- Artifact.value

    Returns:
        {bool, str} -- True or False, registered domain
    """
    input_is_ip = True
    ext = tldextract.extract(query)
    if ext.registered_domain:
        input_is_ip = False
    return input_is_ip, ext.registered_domain

# Gather registry information
def get_whois_registry_info(ip_input):
    """Gather registry information
    Arguments:
        ip_input {string} -- Artifact.value
    Returns:
        {object} -- Contains all registry information
    """

    internet_protocol_address_object = IPWhois(ip_input,allow_permutations=True)
    try:
        whois_response = internet_protocol_address_object.lookup_whois()
        if internet_protocol_address_object.dns_zone:
            whois_response["dns_zone"] = internet_protocol_address_object.dns_zone
        return whois_response
    except exceptions.ASNRegistryError as e:
        logging.error(traceback.format_exc())

def get_rdap_registry_info(ip_input, rdap_depth):
    """Gathers registry info in RDAP protocol

    Arguments:
        ip_input {string} -- Artifact.value
        rdap_depth {int} -- 0,1 or 2

    Returns:
        {object} -- Registry info, RDAP Protocol
    """

    internet_protocol_address_object = IPWhois(ip_input,allow_permutations=True)
    try:
        rdap_response = internet_protocol_address_object.lookup_rdap(rdap_depth)
        if internet_protocol_address_object.dns_zone:
            rdap_response["dns_zone"] = internet_protocol_address_object.dns_zone
        return rdap_response
    except exceptions.ASNRegistryError as e:
        logging.error(traceback.format_exc())

def check_response(response,payload_object):
    if response:
        response["display_content"] = dict_to_json_str(response)
        results = payload_object.done(True, response)
    else:
        results = payload_object.done(False, response)
    return results

def dict_to_json_str(d):
  """Function that converts a dictionary into a JSON string.
     Supports types: basestring, bool, int and nested dicts.
     Does not support lists.
     If the value is None, it sets it to False."""

  json_entry = u'"{0}":{1}'
  json_entry_str = u'"{0}":"{1}"'
  entries = [] 

  for entry in d:
    key = entry
    value = d[entry]

    if value is None:
      value = False

    if isinstance(value, list):
      dummy = {}

    if isinstance(value, basestring):
      value = value.replace(u'"', u'\\"')
      entries.append(json_entry_str.format(unicode(key), unicode(value)))
      
    elif isinstance(value, unicode):
      entries.append(json_entry.format(unicode(key), unicode(value)))
    
    elif isinstance(value, bool):
      value = 'true' if value == True else 'false'
      entries.append(json_entry.format(key, value))

    elif isinstance(value, int):
      entries.append(json_entry.format(unicode(key), value))

    elif isinstance(value, dict):
      entries.append(json_entry.format(key, dict_to_json_str(value)))

    else:
      dummy = {}

  return u'{0} {1} {2}'.format(u'{', ','.join(entries), u'}')


