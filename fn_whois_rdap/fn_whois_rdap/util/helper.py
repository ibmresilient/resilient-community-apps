# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use


import socket
from past.builtins import basestring, unicode
import tldextract
import logging
import time
import traceback
from ipwhois import IPWhois, exceptions
from datetime import datetime, date
from urllib import request

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

def check_registered_domain(registered_domain):
    real_domain = False
    try:
        socket.getaddrinfo(registered_domain, None)[-1][4][0]
        real_domain = True
        return real_domain
    except socket.gaierror as socket_error:
        logging.error(traceback.format_exc())
        return real_domain

# Gather registry information
def get_whois_registry_info(ip_input, proxies=None):
    """Gather registry information
    Arguments:
        ip_input {string} -- Artifact.value
    Returns:
        {object} -- Contains all registry information
    """
    try:
        proxy_opener = make_proxy_opener(proxies) if proxies else None

        internet_protocol_address_object = IPWhois(ip_input,allow_permutations=True, proxy_opener=proxy_opener)
        try:
            whois_response = internet_protocol_address_object.lookup_whois()
            if internet_protocol_address_object.dns_zone:
                whois_response["dns_zone"] = internet_protocol_address_object.dns_zone
            return whois_response
        except exceptions.ASNRegistryError as e:
            logging.error(traceback.format_exc())
    except:
        logging.error(traceback.format_exc())

def get_rdap_registry_info(ip_input, rdap_depth, proxies=None):
    """Gathers registry info in RDAP protocol

    Arguments:
        ip_input {string} -- Artifact.value
        rdap_depth {int} -- 0,1 or 2

    Returns:
        {object} -- Registry info, RDAP Protocol
    """
    try:
        proxy_opener = make_proxy_opener(proxies) if proxies else None
        internet_protocol_address_object = IPWhois(ip_input,allow_permutations=True, proxy_opener=proxy_opener)
        try:
            rdap_response = internet_protocol_address_object.lookup_rdap(rdap_depth)
            if internet_protocol_address_object.dns_zone:
                rdap_response["dns_zone"] = internet_protocol_address_object.dns_zone
            return rdap_response
        except exceptions.ASNRegistryError as e:
            logging.error(traceback.format_exc())
    except:
        logging.error(traceback.format_exc())

def make_proxy_opener(proxies):
    handler = request.ProxyHandler({
        'http': 'http://192.168.0.1:80/',
        'https': 'https://192.168.0.1:443/'
    })
    return request.build_opener(handler)

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


