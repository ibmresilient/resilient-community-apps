# -*- coding: utf-8 -*-


from __future__ import print_function
import logging
import datetime
import re
import urllib
from urlparse import urlparse

IP_PATTERN = re.compile(r"(\d{1,3}\.){3}\d{1,3}")
DOMAIN_PATTERN = re.compile(r"\b((?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}\b")
UUID_PATTERN = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
TIMEDELTA_PATTERN =  re.compile(r"^(-\d+)(second|minutes|hours|days|weeks)$")

def validate_opts(func):
    """"Check options set correctly.

    :param func: Resilient Function instance reference

     """
    if not "api_token" in func.options:
        raise Exception("Mandatory config setting 'api_token' not set.")
    if not UUID_PATTERN.match(func.options["api_token"]):
        raise ValueError("Invalid format for config setting 'api_token'")

def validate_url(url):
    """"Validate url string in a valid format and can be parsed ok.

    :param regex: url paramter value

    """
    parsedurl = urlparse(url)
    if parsedurl.scheme is not None and parsedurl.scheme is not None and parsedurl.path is not None:
        return True
    else:
        return False

def validate_regex(regex):
    """"Validate regex string in a valid format and can be parsed ok.

    :param regex: Regex parameter value

    """
    try:
        re.compile(regex)
        valid_regex = True
    except re.error:
        valid_regex = False
    return valid_regex

def validate_domains(dom):
    """"Validate domain string in a valid format.

    :param dom: Domain parameter value

     """

    for d in re.split('\s+|,', dom):
        if not DOMAIN_PATTERN.match(d):
            return False
    return True

def validate_params(func):
    """"Check parameter fields for Resilient Function and validate that they are in correct format.

    :param func: Resilient Function instance reference.

     """
    if func._params is None:
        raise Exception("Cisco Umbrella investigate query requires parameters dictionary to be set")
    for (k, v) in func._params.items():
        if re.match("^resource", k) and v is not None:
            if not IP_PATTERN.match(v) and not validate_url(v) \
                and not validate_domains(v):
                raise ValueError("Invalid value for function parameter 'resource' .")
        if re.match("^domain", k) and v is not None and not validate_domains(v):
            raise ValueError("Invalid value for function parameter '{}'".format(k))
        if re.match("^ipaddr$", k) and v is not None and not IP_PATTERN.match(v):
            raise ValueError("Invalid value for function parameter 'ipaddr' .")
        if re.match("^regex$", k) and v is not None and not validate_regex(v):
            raise ValueError("Invalid value for function parameter 'regex' .")
        if re.match("^(limit|start_epoch|stop_epoch)$", k) and v is not None and not type(v) == int:
            raise ValueError("Invalid value for function parameter 'limit'.".format(k))
        if re.match("^(start_relative|stop_relative)$", k) and v is not None and not TIMEDELTA_PATTERN.match(v):
            raise ValueError("Invalid value for function parameter '{}' . ".format(k))
        if re.match("^(start|stop)", k) and v is None:
            func._params.pop(k)
            # The regex pattern re.split('_', k)[0] splits [start|stop]_[epoch|relative] on '_' and selects 1st value
        elif re.match("^(start|stop)", k) and v is not None and re.split('_', k)[0] not in func._params:
            func._params[re.split('_', k)[0]] = func._params.pop(k)
        elif re.match("^(start|stop)", k) and v is not None and re.split('_', k)[0] in func._params:
            raise ValueError("Duplicate parameter {} since the parameter {} already set.".format(k, re.split('_', k)[0]))
        if re.match("^(showlabels|include_category)", k) and v is not None and not type(v) == bool:
            raise ValueError("Invalid value for function parameter '{}'".format(k))

def set_domains(func, doms):
    """"Setup the domain or domains attribute from the Resilient Function.

    :param params: Resilient Function instance reference
    :param dom: domains or domain parameter value

    """
    if (re.search('[\s+|,]', doms)):
        # Assume multiple domains will be a list
        # Split on white spaces or commas e.g '"domain1.com" "domain2.com"' or '"domain1.com","domain2.com"'
        func._domains = re.split('\s+|,', doms)
    else:
        # Assume single domain  will be a string
        func._domain = str(doms)

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
            if (re.match("^domain", k)) and v is not None:
                set_domains(func, v)
            if (re.match("^ipaddr$", k)) and v is not None:
                func._ipaddr = str(v)
            if (re.match("^regex$", k)) and v is not None:
                func._regex = str(v)
            if re.match("^(start|stop)$", k) and v is not None:
                if type(v) == int:
                    func._params[k] = datetime.datetime.fromtimestamp(v / 1e3)
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
