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

EP_ENGINE_STATUS_FIELDS = ["apOnOff", "avEngineOnOff", "cidsBrowserFfOnOff", "cidsBrowserIeOnOff", "cidsDrvOnOff",
                            "daOnOff", "elamOnOff", "firewallOnOff", "pepOnOff", "ptpOnOff", "tamperOnOff"]
READABLE_TIME_FIELDS = ["readableLastScanTime", "readableLastVirusTime", "readableLastUpdateTime"]

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

def get_engine_status(eps, non_compliant_endpoints):
    global EP_ENGINE_STATUS_FIELDS

    disabled_status = 0

    for i in range(len(eps)):
        ep_name = eps[i]["computerName"]
        status = 0
        for sf in EP_ENGINE_STATUS_FIELDS:
            if not eps[i][sf]:
                if not ep_name in non_compliant_endpoints:
                    non_compliant_endpoints.append(ep_name)
                    status = 1
                break
        if status:
            disabled_status += 1

    return disabled_status

def add_non_compliant_ep_properties(rtn, non_compliant_endpoints, results):
    """"Add properties to results dict for non-compliant endpoints.

    :param rtn: Result returned from SEPM server after scan result processed.
    :param non_compliant_endpoints: List of non-compliant endpoint names.
    :param results: Copy of results dict.
    :return results: Return updated results dict.
    """
    global EP_ENGINE_STATUS_FIELDS, READABLE_TIME_FIELDS
    results["eps"] = []
    eps = rtn["content"]

    for i in range(len(eps)):
        ep = {}
        ep_name = eps[i]["computerName"]
        if ep_name in non_compliant_endpoints:
            ep["computer_name"] = ep_name
            if ( eps[i]["quarantineDesc"].find("Host Integrity check passed") == -1):
                ep["host_integrity_check"] = "Failed"
            else:
                ep["host_integrity_check"] = "Passed"
            if  eps[i]["onlineStatus"]:
                ep["onlineStatus"] = "Online"
            else:
                ep["onlineStatus"] = "Offline"
            for f in READABLE_TIME_FIELDS:
                ep[f] = eps[i][f]
            for f in EP_ENGINE_STATUS_FIELDS:
                if eps[i][f]:
                    ep[f] = "On"
                else:
                    ep[f] = "Off"
        if ep:
            results["eps"].append(ep)

    return results

def get_endpoints_status(rtn, non_compliant_endpoints=None):
    """"Get enpoint basic endpoint status .

    :param rtn: Result returned from SEPM server after scan result processed.
    :param non_compliant_endpoints: List of non-compliant endpoint names.
    :param results: Copy of results dict.
    :return results: Return updated results dict.
    """
    results = {
        "total": 0,
        "non_compliant": 0,
        "offline": 0,
        "hi_failed": 0,
        "up_to_date": 0,
        "out_of_date": 0,
        "disabled": 0
    }
    hb_def = 900  # Default heart-beat in seconds (15 mins)
    data_tbl_fields = ["total", "offline", "timediffLastUpdateTime", "quarantineDesc"]

    if non_compliant_endpoints is None:
        non_compliant_endpoints = []

    if rtn is not None and len(rtn["content"]) > 0:
        results["total"] = len(rtn["content"])
        eps = rtn["content"]
        if len(eps) > 0:
            results["disabled"] = get_engine_status(eps, non_compliant_endpoints)
            for i in range(len(eps)):
                ep_name = eps[i]["computerName"]
                for f in data_tbl_fields:
                    if f == "onlineStatus" and not eps[i][f]:
                        results["offline"] += 1
                        if not ep_name in non_compliant_endpoints:
                            non_compliant_endpoints.append(ep_name)
                    if f == "quarantineDesc" and (eps[i][f].find("Host Integrity check passed") == -1):
                        results["hi_failed"] += 1
                        if not ep_name in non_compliant_endpoints:
                            non_compliant_endpoints.append(ep_name)
                    if f == "timediffLastUpdateTime":
                        if eps[i][f] > hb_def:
                            results["out_of_date"] += 1
                            if not ep_name in non_compliant_endpoints:
                                non_compliant_endpoints.append(ep_name)
                        else:
                            results["up_to_date"] += 1
        results["non_compliant"] = len(non_compliant_endpoints)

    return results

def get_endpoints_status_details(rtn):
    """"Get endpoint detailed status for non-compliante endpoints.

    :param rtn: Result returned from SEPM server after scan result processed.
    :return results: Return updated results dict.
    """
    non_compliant_endpoints = []

    results = get_endpoints_status(rtn, non_compliant_endpoints)

    if len(non_compliant_endpoints) > 0:
        results = add_non_compliant_ep_properties(rtn, non_compliant_endpoints, results)

    return results