# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Helper functions for Resilient circuits Functions supporting Cisco AMP for endpoints """

from __future__ import print_function
import logging
import re

try:
    from urllib.parse import urlparse
except:
    from urlparse import urlparse

LOG = logging.getLogger(__name__)
IP_PATTERN = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
DOMAIN_REGEX = "((?=[a-z0-9-_]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}" # AMP seems to allow underscore
# in hostnames
DOMAIN_PATTERN = re.compile(r"^\b{}\b$".format(DOMAIN_REGEX))
UUID_PATTERN = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
CLI_ID_PATTERN = re.compile(r"^[a-fA-F0-9]{20}$")
SHA256_PATTERN = re.compile(r"\b[a-fA-F0-9]{64}$")

def validate_opts(func):
    """"Check options set correctly.

    :param func: Resilient Function instance reference

     """
    if not "base_url" in func.options:
        raise Exception("Mandatory config setting 'base_url' not set.")
    if not validate_url(func.options["base_url"]):
        raise ValueError("Invalid format for config setting 'base_url'.")
    if not "api_version" in func.options:
        raise Exception("Mandatory config setting 'api_version' not set.")
    if not re.match("^v\d+$", func.options["api_version"]):
        raise ValueError("Invalid format for config setting 'api_version'.")
    if not "client_id" in func.options:
        raise Exception("Mandatory config setting 'client_id' not set.")
    if not CLI_ID_PATTERN.match(func.options["client_id"]):
        raise ValueError("Invalid format for config setting 'client_id'.")
    if not "api_token" in func.options:
        raise Exception("Mandatory config setting 'api_token' not set.")
    if not UUID_PATTERN.match(func.options["api_token"]):
        raise ValueError("Invalid format for config setting 'api_token'.")

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

def validate_params(params):
    """"Check parameter fields for Resilient Function and validate that they are in correct format.

    :param params: Dictionary of Resilient Function parameters.

     """
    if params is None:
        raise Exception("Error missing parameter 'params'")

    # Now do some validation on input parameters.
    for (k, v) in params.copy().items():
        if re.match("^(limit|offset)$", k) and v is not None and not type(v) == int:
            raise ValueError("Invalid value '{0}' for function parameter '{1}'.".format(v, k))
        if re.match("^conn_guid$", k) and v is not None and not UUID_PATTERN.match(v):
            raise ValueError("Invalid value '{0}' for function parameter '{1}'.".format(v, k))
        if re.match("^(internal_ip|external_ip)$", k) and v is not None and not IP_PATTERN.match(v):
            raise ValueError("Invalid value '{0}' for function parameter '{1}'.".format(v, k))
        if re.match("^hostname$", k) and v is not None  and not validate_domain_name(v):
            raise ValueError("Invalid value '{0}' for function parameter '{1}'.".format(v, k))

    # If any entry has "None" string change to None value.
    for k, v in params.items():
        if type(v) == str and v.lower() == 'none':
            params[k] = None

def is_none(param):
    """Test if a parameter is None value or string 'None'.

    :param param: Parameter to test
    :return: Boolen value

    """

    if param is None or (type(param) == str and param.lower() == 'none'):
        return True
    else:
        return False
