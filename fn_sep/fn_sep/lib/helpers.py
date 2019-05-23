# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

""" Helper functions for Resilient circuits Functions supporting Symantec SEP """

from __future__ import print_function
import logging
import re
import os
import sys
import datetime
import tempfile
from resilient_circuits.actions_component import ResilientComponent

LOG = logging.getLogger(__name__)


def transform_kwargs(kwargs):
    """"Update kwargs dictionary.

    :param kwargs: Dictionary of Resilient Function parameters.

     """
    params = {}

    # Remove  "sep_" from the kwargs key names.
    for (k, v) in kwargs.copy().items():
            v = kwargs.pop(k)

            if isinstance(k, list):
                k =  [ResilientComponent.get_select_param(val) for val in v]
            elif isinstance(v, dict):
                v =  v.get("name")
            kwargs[k] = v.rstrip().lstrip() if isinstance(v, str)  else v
            params[re.split('_', k, 1)[1]] = v.rstrip().lstrip() if isinstance(v, str)  else v

    # If any entry has "None" string change to None value.
    for k, v in kwargs.items():
        if type(v) == str and v.lower() == 'none':
            params[k] = None

    return params

def validate_fields(field_list, kwargs):
    """
    ensure required fields are present. Throw ValueError if not
    :param field_list:
    :param kwargs:
    :return: no return
    """
    for field in field_list:
        if field not in kwargs or kwargs.get(field) == '':
            raise ValueError('Required field is missing or empty: '+field)

def create_attachment(rest_client, file_name, file_content, params):
    """"Add file as Resilient incident attachment.

    :param rest_client: Resilient Rest client
    :param file_name: Name of file to add as attachment
    :param file_content: Content of file to add as attachment
    :param params: Resilient Function parameters (dict)
    :return att_report: Return result (dict) of Resilient post attachment request
    """

    if sys.version_info.major == 3:
        temp_file_obj = tempfile.NamedTemporaryFile('w', delete=False, encoding="utf8")
    else:
        temp_file_obj = tempfile.NamedTemporaryFile('w+b', delete=False)

    # Create the temporary file save results in json format.
    with temp_file_obj as temp_file:
        temp_file.write(file_content)
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

def generate_result_cvs(rtn, sep_commandid):
    """"Generate file content for attachment from eoc scan results.

    :param rtn: Result returned from SEPM server after scan result processed.
    :param sep_commandid: Result commandid.
    :return (file_name, file_content): Return tuple of file name and  content
    """
    file_content = ""
    file_name = "EOC_scan_results_for_commandid_{0}_{1}.csv" \
        .format(sep_commandid, datetime.datetime.today().strftime('%Y%m%d'))
    file_content = "Computer name,Computer id,Artifact type,Artifact value,Match type,Match value\n"

    eps = rtn["content"]
    for i in range(len(eps)):
        ep_name = eps[i]["computerName"]
        ep_id = eps[i]["computerId"]
        artifact_type = eps[i]["scan_result"]["artifact_type"]
        artifact_value = eps[i]["scan_result"]["artifact_value"]
        matches = eps[i]["scan_result"]["FULL_MATCHES"] if "File" in artifact_type \
            else eps[i]["scan_result"]["HASH_MATCHES"]
        for m in matches:
            if "File" in artifact_type:
                file_content += "{0},{1},{2},{3},{4},{5}\n"\
                    .format(ep_name, ep_id, artifact_type, artifact_value, m["hashType"],m["hashValue"])
            else:
                file_content += "{0},{1},{2},{3},{4},{5}\n"\
                    .format(ep_name, ep_id, artifact_type, artifact_value, "File path", m["value"])
                pass

    return(file_name, file_content)