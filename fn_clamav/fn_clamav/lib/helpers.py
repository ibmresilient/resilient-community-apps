# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Helper functions for Resilient circuits Functions supporting ClamAV """

from __future__ import print_function
import re

# Hostname or domain pattern.
DOMAIN_REGEX = "((?!-))(xn--)?[a-z0-9][a-z0-9-_]{0,61}[a-z0-9]{0,1}((\.)(xn--)?" \
               "([a-z0-9\-]{1,61}|[a-z0-9-]{1,30}\.[a-z]{2,}))*"
DOMAIN_PATTERN = re.compile(r"^\b{}\b$".format(DOMAIN_REGEX), re.IGNORECASE)

def validate_opts(func):
    """"Check options set correctly.

    :param func: Resilient Function instance reference

     """
    if not "host" in func.options:
        raise Exception("Mandatory config setting 'host' not set.")
    if func.options["host"] is None or not validate_domain_name(func.options["host"]):
        raise ValueError("Invalid format for config setting 'host'.")
    if not "port" in func.options:
        raise Exception("Mandatory config setting 'port' not set.")
    if func.options["host"] is None or not validate_is_int(func.options["port"]):
        raise ValueError("Invalid format for config setting 'port'.")
    if not "timeout" in func.options:
        raise Exception("Mandatory config setting 'timeout' not set.")
    if func.options["timeout"] is None or not validate_is_int(func.options["timeout"]):
        raise ValueError("Invalid format for config setting 'timeout'.")

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

def validate_domain_name(domain_or_hostname):
    """"Validate domain string(s) are in a valid format.

    :param domain_or_hostname: Domain or hostname parameter value
    :return : boolean

     """

    for d in re.split('\s+|,', domain_or_hostname):
        if not DOMAIN_PATTERN.match(d):
            return False
    return True

def validate_params(fieldList, kwargs):
    """"Check parameter fields for Resilient Function that they exist and validate that are non None
        they are in correct format.

    :param fieldList:
    :param kwargs:
    :return: no return

    """
    for f in fieldList:
        if f not in kwargs or kwargs.get(f) == '' or is_none(kwargs[f]) :
            raise ValueError('Required field is missing or empty: '+f)

def is_none(param):
    """Test if a parameter is None value or string 'None'.

    :param param: Parameter to test
    :return: Boolen value

    """

    if param is None or (type(param) == str and param.lower() == 'none'):
        return True
    else:
        return False
