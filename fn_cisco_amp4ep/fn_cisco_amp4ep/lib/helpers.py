# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Helper functions for Resilient circuits Functions supporting Cisco AMP for endpoints """

from __future__ import print_function
import logging
import re
from sys import version_info

try:
    from urllib.parse import urlparse
except:
    from urlparse import urlparse

LOG = logging.getLogger(__name__)
IP_PATTERN = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
DOMAIN_REGEX = "((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}((\.)(xn--)?" \
               "([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,}))*"
# in hostnames
DOMAIN_PATTERN = re.compile(r"^\b{}\b$".format(DOMAIN_REGEX), re.IGNORECASE)
UUID_PATTERN = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
CLI_ID_PATTERN = re.compile(r"^[a-fA-F0-9]{20}$")
SHA256_PATTERN = re.compile(r"\b[a-fA-F0-9]{64}$")
AMP_LIMIT_MAX = 1000

def validate_opts(func):
    """"Check options set correctly.

    :param func: Resilient Function instance reference

     """
    if not "base_url" in func.options:
        raise Exception("Mandatory config setting 'base_url' not set.")
    if func.options["base_url"] is None or not validate_url(func.options["base_url"]):
        raise ValueError("Invalid format for config setting 'base_url'.")
    if not "api_version" in func.options:
        raise Exception("Mandatory config setting 'api_version' not set.")
    if func.options["api_version"] is None or not re.match("^v\d+$", func.options["api_version"]):
        raise ValueError("Invalid format for config setting 'api_version'.")
    if not "client_id" in func.options:
        raise Exception("Mandatory config setting 'client_id' not set.")
    if func.options["client_id"] is None or not CLI_ID_PATTERN.match(func.options["client_id"]):
        raise ValueError("Invalid format for config setting 'client_id'.")
    if not "api_token" in func.options:
        raise Exception("Mandatory config setting 'api_token' not set.")
    if func.options["api_token"] is None or not UUID_PATTERN.match(func.options["api_token"]):
        raise ValueError("Invalid format for config setting 'api_token'.")
    if not "max_retries" in func.options:
        raise Exception("Mandatory config setting 'max_retries' not set.")
    if func.options["max_retries"] is None or not validate_is_int(func.options["max_retries"]):
        raise ValueError("Invalid format for config setting 'max_retries'.")
    if "query_limit" in func.options and func.options["query_limit"] is not None and not \
            validate_is_int(func.options["query_limit"]):
            raise ValueError("Invalid format for config setting 'query_limit'.")

def validate_url(url):
    """"Validate url string in a valid format and can be parsed ok.

    :param url: url parameter value
    :return : boolean

    """
    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc]):
            return True
        else:
            return False
    except:
        return False

def validate_domain_name(domain_or_hostname):
    """"Validate domain string(s) are in a valid format.

    :param domain_or_hostname: Domain or hostname parameter value
    :return : boolean

     """

    for d in re.split('\s+|,', domain_or_hostname):
        if not DOMAIN_PATTERN.match(d):
            return False
    return True

def validate_is_int(val):
    """"Validate value is in a valid int format.

    :param val: Value to test
    :return : boolean

     """

    try:
        int(val)
        return True
    except ValueError:
        return False

def validate_is_event_type(event_types):
    """"Validate domain string(s) are in a valid format.

    :param event_types: Ent type or types parameter value
    :return : boolean

     """

    for et in re.split('\s+|,', event_types):
        if not validate_is_int(et):
            return False
    return True

def validate_params(params):
    """"Check parameter fields for Resilient Function and validate that they are in correct format.

    :param params: Dictionary of Resilient Function parameters.

     """
    if params is None:
        raise Exception("Error missing parameter 'params'")

    # Now do some validation on input parameters.
    for (k, v) in params.copy().items():
        if re.match("^(limit|offset|start_date)$", k) and v is not None and not type(v) == int:
            raise_value_error(v, k)
        if re.match("^conn_guid|group_guid|file_list_guid$", k) and v is not None and not UUID_PATTERN.match(v):
            raise_value_error(v, k)
        if re.match("^(internal_ip|external_ip)$", k) and v is not None and not IP_PATTERN.match(v):
            raise_value_error(v, k)
        if re.match("^hostname$", k) and v is not None  and not validate_domain_name(v):
            raise_value_error(v, k)
        if re.match("^detection_sha256|application_sha256|file_sha256$", k) and v is not None and not SHA256_PATTERN.match(v):
            raise_value_error(v, k)
        if re.match("^event_type$", k) and v is not None and not validate_is_event_type(v):
            raise_value_error(v, k)
        if re.match("^q|scd_name$", k) and v is not None and v == '':
            raise_value_error(v, k, "Invalid or empty value")


    # If any entry has "None" string change to None value.
    for k, v in params.items():
        if type(v) == str and v.lower() == 'none':
            params[k] = None

def raise_value_error(v, k, msg=None):
    if msg is None:
        msg = "Invalid value"
    if version_info.major == 2:
        raise ValueError("{2} '{0}' for function parameter '{1}'.".format(v.encode('utf-8'), k, msg))
    else:
        raise ValueError("{2} '{0}' for function parameter '{1}'.".format(v, k, msg))

def is_none(param):
    """Test if a parameter is None value or string 'None'.

    :param param: Parameter to test
    :return: Boolen value

    """

    if param is None or (type(param) == str and param.lower() == 'none'):
        return True
    else:
        return False
