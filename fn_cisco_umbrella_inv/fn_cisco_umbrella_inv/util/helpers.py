# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Helper functions for Resilient circuits Functions supporting Cisco Umbrella Investigate """

from __future__ import print_function
import logging
import datetime
import re
import urllib
from urlparse import urlparse

LOG = logging.getLogger(__name__)
IP_PATTERN = re.compile(r"^(\d{1,3}\.){3}\d{1,3}$")
DOMAIN_REGEX = "((?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}"
DOMAIN_PATTERN = re.compile(r"^\b{}\b$".format(DOMAIN_REGEX))
EMAIl_PATTERN = re.compile(r"(^[a-zA-Z0-9_.+-]+@{}$)".format(DOMAIN_REGEX))
UUID_PATTERN = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
TIMEDELTA_PATTERN =  re.compile(r"^-*(\d+)(seconds|minutes|hours|days|weeks)$")
MD5_PATTERN = re.compile(r"^[a-fA-F0-9]{32}$")
SHA1_PATTERN = re.compile(r"\b[a-fA-F0-9]{40}$")
SHA256_PATTERN = re.compile(r"\b[a-fA-F0-9]{64}$")

def init_env(func):
    """"Initialize function environment.
    Delete instance attributes which may be retained value from previous execution of a Resilient Function.

    :param func: Resilient Function instance reference

     """
    for v in ["_params", "_res", "_domain", "_domains", "_ipaddr", "_regex", "_asn",
                "_emails", "_nameservers"]:
        if hasattr(func, v):
            delattr(func, v)

def validate_opts(func):
    """"Check options set correctly.

    :param func: Resilient Function instance reference

     """
    if not "api_token" in func.options:
        raise Exception("Mandatory config setting 'api_token' not set.")
    if not "api_token" in func.options:
        raise Exception("Mandatory config setting 'api_token' not set.")
    if not UUID_PATTERN.match(func.options["api_token"]):
        raise ValueError("Invalid format for config setting 'api_token'.")
    if not "base_url" in func.options:
        raise Exception("Mandatory config setting 'base_url' not set.")
    if not validate_url(func.options["base_url"]):
        raise ValueError("Invalid format for config setting 'base_url'.")


def validate_url(url):
    """"Validate url string in a valid format and can be parsed ok.

    :param regex: url paramter value
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

def validate_regex(regex):
    """"Validate regex string in a valid format and can be parsed ok.

    :param regex: Regex parameter value
    :return : boolean

    """
    try:
        re.compile(regex)
        valid_regex = True
    except re.error:
        LOG.debug("regex: %s", regex)
        valid_regex = False
    return valid_regex

def validate_domains(doms):
    """"Validate domain string(s) are in a valid format.

    :param doms: Domain(s) parameter value
    :return : boolean

     """

    for d in re.split('\s+|,', doms):
        if not DOMAIN_PATTERN.match(d):
            return False
    return True

def validate_emails(emails):
    """"Validate email string(s) are a valid format.

    :param emails: Email(s) parameter value
    :return : boolean

     """

    for d in re.split('\s+|,', emails):
        if not EMAIl_PATTERN.match(d):
            return False
    return True

def validate_params(func):
    """"Check parameter fields for Resilient Function and validate that they are in correct format.

    :param func: Resilient Function instance reference.

     """
    if not hasattr(func, "_params") or func._params is None:
        raise Exception("Cisco Umbrella investigate query requires parameters dictionary to be set")

    # If any entry has "None" string change to None value.
    for k, v in func._params.items():
        if type(v) == str and v.lower() == 'none':
            func._params[k] = None

    # Now do some validation on input parameters.
    for (k, v) in func._params.items():
        if re.match("^resource$", k) and v is not None:
            if not IP_PATTERN.match(v) and not validate_url(v) \
                and not validate_domains(v):
                raise ValueError("Invalid value for function parameter 'resource'.")
        if re.match("^resource", k) and IP_PATTERN.match(v):
            if "resource_type" in func._params and func._params["resource_type"] != "ip_address":
                raise ValueError("Invalid value for function parameter 'resource', should be type 'ip_address'.")
        if re.match("^resource", k) and validate_domains(v):
            if "resource_type" in func._params and func._params["resource_type"] != "domain_name":
                raise ValueError("Invalid value for function parameter 'resource', should be type 'domain_name'.")
        if re.match("^resource", k) and validate_url(v):
            if "resource_type" in func._params and func._params["resource_type"] != "url":
                raise ValueError("Invalid value for function parameter 'resource', should be type 'url'.")
        # Domain name and name server should be in similar format use same validator.
        if re.match("^(domain|nameservers)", k) and v is not None and not validate_domains(v):
            raise ValueError("Invalid value for function parameter '{}'.".format(k))
        if re.match("^emails$", k) and v is not None and not validate_emails(v):
            raise ValueError("Invalid value for function parameter '{}'.".format(k))
        if re.match("^ipaddr$", k) and v is not None and not IP_PATTERN.match(v):
            raise ValueError("Invalid value for function parameter 'ipaddr'.")
        if re.match("^regex$", k) and v is not None and not validate_regex(v):
            raise ValueError("Invalid value for function parameter 'regex'.")
        if re.match("^asn$", k) and v is not None and not type(v) == int:
            raise ValueError("Invalid value for function parameter 'asn'.")
        if re.match("^(limit|start_epoch|stop_epoch)$", k) and v is not None and not type(v) == int:
            raise ValueError("Invalid value for function parameter '{}'.".format(k))
        if re.match("^(start_relative|stop_relative)$", k) and v is not None and not (TIMEDELTA_PATTERN.match(v) or \
            re.match("^Now$", v, re.IGNORECASE)):
            raise ValueError("Invalid value for function parameter '{}'. ".format(k))
        if re.match("^(start|stop)", k) and v is None:
            func._params.pop(k)
            # The regex pattern re.split('_', k)[0] splits [start|stop]_[epoch|relative] on '_' and selects 1st value
        elif re.match("^(start|stop)", k) and v is not None and re.split('_', k)[0] not in func._params:
            func._params[re.split('_', k)[0]] = func._params.pop(k)
        elif re.match("^(start|stop)", k) and v is not None and re.split('_', k)[0] in func._params:
            raise ValueError("Duplicate parameter {} since the parameter {} already set.".format(k, re.split('_', k)[0]))
        if re.match("^(showlabels|include_category)", k) and v is not None and not type(v) == bool:
            raise ValueError("Invalid value for function parameter '{}'".format(k))
        if re.match("^hash$", k) and v is not None:
            if not MD5_PATTERN.match(v) and not SHA1_PATTERN.match(v) \
                and not SHA256_PATTERN.match(v):
                raise ValueError("Invalid value for function parameter 'hash'.")

def set_attribs(func, attrib_name, val):
    """"Setup string or list attribute for the Resilient Function for types:

        domain or domains,
        email or emails,
        nameserver or nameservers

    :param params: Resilient Function instance reference
    :param attrib_name: Attribute name
    :param val: Value for attribute to be processed.

    """
    if (re.search('[\s+|,]', val)):
        # Assume multiple domains will be a list
        # Split on white spaces or commas e.g '"domain1.com" "domain2.com"' or '"domain1.com","domain2.com"'
        setattr(func, "_"+attrib_name, re.split('\s+|,', val))
        #func._domains = re.split('\s+|,', val)
    else:
        # Assume single domain  will be a string
        #func._domain = str(val)
        setattr(func, "_"+attrib_name, str(val))

def process_params(func):
    """"Process Resilient Function parameter fields doing any necessary transformations.

    :param params: Resilient Function instance reference

    """
    for (k, v) in func._params.items():
        if (re.match("^resource$", k)) and v is not None:
            if IP_PATTERN.match(v):
                # Assume "resource" param is an ip address.
                func._res = str(v)
            elif validate_url(v):
                # Assume "resource" param is a url.
                    func._res = urllib.quote_plus(v)
            elif validate_domains(v):
                # Assume "resource" param is a domain.
                func._res = str(v)
        if (re.match("^(domain|nameservers|emails)", k)) and v is not None:
            set_attribs(func, k, v)
        if (re.match("^ipaddr$", k)) and v is not None:
            func._ipaddr = str(v)
        if (re.match("^regex$", k)) and v is not None:
            func._regex = str(v)
        if (re.match("^asn$", k)) and v is not None:
            func._asn = str(v)
        if (re.match("^hash$", k)) and v is not None:
            func._hash = str(v)
        if re.match("^(start|stop)$", k) and v is not None:
            if type(v) == int:
                func._params[k] = datetime.datetime.fromtimestamp(v / 1e3)
            else:
                if re.match("^Now$", v, re.IGNORECASE):
                    func._params[k] = datetime.datetime.now()
                else:
                    # Split value using regex e.g. -30days, m splits as m.group(1) = -30, m.group(2) = days
                    m = TIMEDELTA_PATTERN.search(v)
                    func._params[k] = datetime.timedelta(**{str(m.group(2)): int(m.group(1))})

def omit_params(params, omit_list):
    """"Filter out 'omit_list' list of parameters from the 'params' dict keys.

    :param params: Resilient Function parameters dictionary
    :param omit_list: List of parameter keys to remove
    :return: Updated parameter dictionary

    """
    if params is None:
        raise Exception("Error missing parameter 'params'")
    if omit_list is None:
        raise Exception("Error missing parameter 'omit_set'")
    if not isinstance(omit_list, str) and not isinstance(omit_list, list):
        raise ValueError("omit_list argument must be a string or list")
    params = {k: v for (k, v) in params.iteritems() if not k in omit_list}
    return params

def is_none(param):
    """Test if a parameter is None value or string 'None'.

    :param param: Parameter to test
    :return: Boolen value

    """

    if param is None or (type(param) == str and param.lower() == 'none'):
        return True
    else:
        return False