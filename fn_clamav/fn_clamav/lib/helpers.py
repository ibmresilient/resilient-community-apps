# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Helper functions for Resilient circuits Functions supporting ClamAV """

from __future__ import print_function
import re
import base64

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

def validate_params(params):
    """"Check parameter fields for Resilient Function that they exist and validate that are non None
        they are in correct format.

    :param params: Dictionary of Resilient Function parameters.
    :param kwargs:
    :return: no return

    """
    for (k, v) in params.copy().items():
        if re.match("^incident_id$", k) and (v == '' or is_none(v)):
            raise ValueError("Required parameter '{}' is missing or empty.".format(k))
        if re.match("^(incident_id|artifact_id|task_id|attachment_id)$", k) and v is not None and not validate_is_int(v):
            raise ValueError("Invalid value for function parameter '{}'.".format(k))

def is_none(param):
    """Test if a parameter is None value or string 'None'.

    :param param: Parameter to test
    :return: Boolen value

    """

    if param is None or (type(param) == str and param.lower() == 'none'):
        return True
    else:
        return False

def get_file_attachment(res_client, incident_id, artifact_id=None, task_id=None, attachment_id=None):
    """
    call the Resilient REST API to get the attachment or artifact data
    :param res_client: required for communication back to resilient
    :param incident_id: required
    :param artifact_id: optional
    :param task_id: optional
    :param attachment_id: optional
    :return: byte string of attachment
    """

    if incident_id and artifact_id:
        data_uri = "/incidents/{}/artifacts/{}/contents".format(incident_id, artifact_id)
        metadata_uri = "/incidents/{}/artifacts/{}".format(incident_id, artifact_id)
    elif attachment_id:
        if task_id:
            data_uri = "/tasks/{}/attachments/{}/contents".format(task_id, attachment_id)
            metadata_uri = "/tasks/{}/attachments/{}".format(task_id, attachment_id)
        elif incident_id:
            data_uri = "/incidents/{}/attachments/{}/contents".format(incident_id, attachment_id)
            metadata_uri = "/incidents/{}/attachments/{}".format(incident_id, attachment_id)
        else:
            raise ValueError("task_id or incident_id must be specified with attachment")
    else:
        raise ValueError("artifact or attachment or incident id must be specified")

    # Get the data
    metadata = res_client.get(metadata_uri)
    data = res_client.get_content(data_uri)

    if attachment_id:
        results = {
            "filename": metadata["name"],
            "content": data
        }
    else:
        results = {
            "filename": metadata["value"],
            "content": data
        }

    return results