# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Helper functions for Resilient circuits Functions supporting Cisco Umbrella Investigate """

from __future__ import print_function
import logging
import datetime
import re
import os
import json

try:
    from urllib.parse import urlparse, quote_plus
except:
    from urlparse import urlparse
    from urllib import quote_plus

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

def validate_opts(func):
    """"Check options set correctly.

    :param func: Resilient Function instance reference

     """
    if not "api_token" in func.options:
        raise Exception("Mandatory config setting 'api_token' not set.")
    if not UUID_PATTERN.match(func.options["api_token"]):
        raise ValueError("Invalid format for config setting 'api_token'.")
    if not "base_url" in func.options:
        raise Exception("Mandatory config setting 'base_url' not set.")
    if not validate_url(func.options["base_url"]):
        raise ValueError("Invalid format for config setting 'base_url'.")
    if not "results_limit" in func.options:
        raise Exception("Mandatory config setting 'results_limit' not set.")
    if not validate_is_int(func.options["results_limit"]):
        raise ValueError("Invalid value for config setting 'results_limit'.")

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

def validate_params(params):
    """"Check parameter fields for Resilient Function and validate that they are in correct format.

    :param params: Dictionary of Resilient Function parameters.

     """
    if params is None:
        raise Exception("Error missing parameter 'params'")

    # If any entry has "None" string change to None value.
    for k, v in params.items():
        if type(v) == str and v.lower() == 'none':
            params[k] = None

    # Now do some validation on input parameters.
    for (k, v) in params.copy().items():
        if re.match("^resource$", k) and v is not None:
            if not IP_PATTERN.match(v) and not validate_url(v) \
                and not validate_domains(v) and not validate_emails(v) \
                    and not validate_is_int(v):
                raise ValueError("Invalid value for function parameter 'resource'.")
        # Domain name and name server should be in similar format use same validator.
        if re.match("^domain", k) and v is not None and not validate_domains(v):
            raise ValueError("Invalid value for function parameter '{}'.".format(k))
        if re.match("^ipaddr$", k) and v is not None and not IP_PATTERN.match(v):
            raise ValueError("Invalid value for function parameter 'ipaddr'.")
        if re.match("^regex$", k) and v is not None and not validate_regex(v):
            raise ValueError("Invalid value for function parameter 'regex'.")
        if re.match("^(limit|start_epoch|stop_epoch)$", k) and v is not None and not type(v) == int:
            raise ValueError("Invalid value for function parameter '{}'.".format(k))
        if re.match("^(start_relative|stop_relative)$", k) and v is not None and not (TIMEDELTA_PATTERN.match(v) or \
            re.match("^Now$", v, re.IGNORECASE)):
            raise ValueError("Invalid value for function parameter '{}'. ".format(k))
        if re.match("^(start|stop)", k) and v is None:
            params.pop(k)
            # The regex pattern re.split('_', k)[0] splits [start|stop]_[epoch|relative] on '_' and selects 1st value
        elif re.match("^(start|stop)", k) and v is not None and re.split('_', k)[0] not in params:
            params[re.split('_', k)[0]] = params.pop(k)
        elif re.match("^(start|stop)", k) and v is not None and re.split('_', k)[0] in params:
            raise ValueError("Duplicate parameter {} since the parameter {} already set.".format(k, re.split('_', k)[0]))
        if re.match("^(showlabels|include_category)", k) and v is not None and not type(v) == bool:
            raise ValueError("Invalid value for function parameter '{}'".format(k))
        if re.match("^hash$", k) and v is not None:
            if not MD5_PATTERN.match(v) and not SHA1_PATTERN.match(v) \
                and not SHA256_PATTERN.match(v):
                raise ValueError("Invalid value for function parameter 'hash'.")

def set_result(process_result, key_name, val):
    """"Setup string or list attribute for the Resilient Function for types:

        domain or domains,
        email or emails,
        nameserver or nameservers

    :param process_result: Processing result dict.
    :param key_name: Parameter Key name
    :param val: Value for parameter to be processed.

    """
    if (re.search('[\s+|,]', val)):
        # Assume multiple domains will be a list
        # Split on white spaces or commas e.g '"domain1.com" "domain2.com"' or '"domain1.com","domain2.com"'
        process_result["_"+key_name] = re.split('\s+|,', val)
    else:
        # Assume single domain  will be a string
        process_result["_"+key_name] = str(val)

def process_params(params, process_result):
    """"Process Resilient Function parameter fields doing any necessary transformations.

    :param params: Dictionary of Resilient Function parameters.
    :param process_result: Processing result dict.

     """
    if params is None:
        raise Exception("Error missing parameter 'params'")

    for (k, v) in params.items():
        if (re.match("^resource$", k)) and v is not None:
            if IP_PATTERN.match(v) or validate_domains(v) or validate_emails(v) \
                    or validate_is_int(v):
                # Assume "resource" param is a domain name, nameserver, ip address, email address or asn.
                process_result["_res"] = str(v)
                if IP_PATTERN.match(v):
                    process_result["_res_type"] = "ip_address"
                elif validate_domains(v):
                    process_result["_res_type"] = "domain_name"
                elif validate_emails(v):
                    process_result["_res_type"] = "email_address"
                elif validate_is_int(v):
                    process_result["_res_type"] = "as_number"
            elif validate_url(v):
                # Assume "resource" param is a url.
                process_result["_res"] = quote_plus(v)
                process_result["_res_type"] = "url"
        if (re.match("^domain", k)) and v is not None:
            set_result(process_result, k, v)
        if (re.match("^ipaddr$", k)) and v is not None:
            process_result["_ipaddr"] = str(v)
        if (re.match("^regex$", k)) and v is not None:
            process_result["_regex"] = str(v)
        if (re.match("^hash$", k)) and v is not None:
            process_result["_hash"] = str(v)
        if re.match("^(start|stop)$", k) and v is not None:
            if type(v) == int:
                params[k] = datetime.datetime.fromtimestamp(v / 1e3)
            else:
                if re.match("^Now$", v, re.IGNORECASE):
                    params[k] = datetime.datetime.now()
                else:
                    # Split value using regex e.g. -30days, m splits as m.group(1) = -30, m.group(2) = days
                    m = TIMEDELTA_PATTERN.search(v)
                    params[k] = datetime.timedelta(**{str(m.group(2)): int(m.group(1))})

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
    params = {k: v for (k, v) in params.items() if not k in omit_list}
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

def create_attachment(func_ref, func_name, artifact_value, params, rtn, query_execution_time):
    """"Create an attachment and post to Resilient platform.

    :param func_ref: Resilient Function instance reference
    :param func_name: Resilient Function name
    :param artifact_value: Resilient artifact value
    :param params: Resilient Function parameters dictionary
    :param rtn: Result returned from external source
    :param query_execution_time: External time of query
    :return att_report: Updated attachment report dictionary

    """
    file_name = func_name + " [{0}: {1}].txt" \
        .format(params['artifact_type'], artifact_value)

    try:
        rest_client = func_ref.rest_client()

        # Create the temporary file save results in json format.
        with open(file_name, 'w') as outfile:
            json.dump(rtn, outfile)

        # Post file to Resilient
        att_report = rest_client.post_attachment("/incidents/{0}/attachments".format(params["incident_id"]),
                                                      file_name,
                                                      file_name,
                                                      "text/plain",
                                                      "")
        LOG.info("New attachment added to incident %s", params["incident_id"])

        # Delete the temporary file.
        os.remove(file_name)

    except Exception as ex:
        LOG.error(ex)
        raise ex

    return att_report
