# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Helper functions for Resilient circuits Functions supporting Bigfix integration """

from __future__ import print_function
import logging
import re
import os
import json
import tempfile

LOG = logging.getLogger(__name__)

def validate_opts(func):
    """"Check options set correctly.

    :param func: Resilient Function instance reference

     """
    if not "bigfix_url" in func.options:
        raise Exception("Mandatory config setting 'bigfix_url' not set.")
    if not "bigfix_port" in func.options:
        raise Exception("Mandatory config setting 'bigfix_port' not set.")
    if not "bigfix_user" in func.options:
        raise Exception("Mandatory config setting 'bigfix_url' not set.")
    if not "bigfix_pass" in func.options:
        raise Exception("Mandatory config setting 'bigfix_pass' not set.")
    if not "hunt_results_limit" in func.options:
        raise Exception("Mandatory config setting 'hunt_results_limit' not set.")


def validate_params(params, func_name):
    """"Check parameter fields for Resilient Function and validate that they are in correct format.

    :param params: Dictionary of Resilient Function parameters.
    :param func_name: Resilient Function name.
     """
    if params is None:
        raise Exception("Error missing parameter 'params'")

    # Do some validation on input parameters.
    if func_name == "fn_bigfix_artifact":
        for (k, v) in params.copy().items():
            if re.match("^(artifact_id|artifact_value|artifact_type)$", k) and is_none(v):
                raise ValueError("Required parameter '{}' not set.".format(k))
            if re.match("^(incident_id|bigfix_incident_plan_status)$", k) and is_none(v):
                raise ValueError("Required parameter '{}' not set.".format(k))
            if re.match("^artifact_type$", k) and v == "Registry Key":
                if is_none(params["artifact_properties_name"]):
                    raise ValueError("Required parameter '{}' not set.".format("artifact_properties_name"))
                if is_none(params["artifact_properties_value"]):
                    raise ValueError("Required parameter '{}' not set.".format("artifact_properties_value"))

    elif func_name == "fn_bigfix_remediation":
        for (k, v) in params.copy().items():
            if re.match("^(artifact_value|artifact_type)$", k) and is_none(v):
                raise ValueError("Required parameter '{}' not set.".format(k))
            if re.match("^incident_id$", k) and is_none(v):
                raise ValueError("Required parameter '{}' not set.".format(k))
            if re.match("^asset_id$", k) and is_none(v):
                raise ValueError("Required parameter '{}' not set.".format(k))

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

def create_attachment(rest_client, file_name, file_content, params):
    """"Add file as Resilient incident attachment.

    :param rest_client: Resilient Rest client
    :param file_name: Name of file to add as attachment
    :param file_content: Content of file to add as attachment
    :param params: Resilient Function parameters (dict)
    :return att_report: Return result (dict) of Resilient post attachment request
    """

    # Create the temporary file save results in json format.
    with tempfile.NamedTemporaryFile('w+b', bufsize=0, delete=False) as temp_file:
        json.dump(file_content, temp_file)
        temp_file.close()
        try:
            # Post file to Resilient
            att_report = rest_client.post_attachment("/incidents/{0}/attachments".format(params["incident_id"]),
                                                     temp_file.name,
                                                     file_name,
                                                     "text/plain",
                                                     "")
            LOG.info("New attachment added to incident %s", params["incident_id"])
        except Exception as err:
            raise err
        finally:
            os.unlink(temp_file.name)

    return att_report
