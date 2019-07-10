# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

""" Helper functions for Resilient circuits Functions supporting Symantec SEP """
from __future__ import print_function
import logging
import sys
import datetime
import tempfile
from resilient_circuits.actions_component import ResilientComponent

LOG = logging.getLogger(__name__)
CONFIG_DATA_SECTION = "fn_sep"
EP_ENGINE_STATUS_FIELDS = ["apOnOff", "avEngineOnOff", "cidsBrowserFfOnOff", "cidsBrowserIeOnOff", "cidsDrvOnOff",
                           "daOnOff", "elamOnOff", "firewallOnOff", "pepOnOff", "ptpOnOff", "tamperOnOff"]
EP_ENGINE_STATUSES = {
    0: "Disabled",
    1: "Enabled",
    2: "Not installed",
    4: "Malfunctioning",
    127: "Client not reporting"
}
READABLE_TIME_FIELDS = ["readableLastScanTime", "readableLastVirusTime", "readableLastUpdateTime"]
EP_PROP_FIELDS = ["onlineStatus", "timediffLastUpdateTime", "quarantineDesc"]
HB_DEF = 900  # Default heart-beat in seconds (15 mins)

def transform_kwargs(kwargs):
    """"Update kwargs dictionary.
    This function will perform following actions:
        - Copy kwargs to a new 'params' dict which will be used to call the apis.
        - Strip whitespaces from beginning and end of parametrs in 'kwargs' and 'params' taking into
          account lists or dicts.
        - Remove "sep_" from beginning of parameters in 'params'.
        - Convert any case insensitive "None" values to None in 'params'.
    :param kwargs: Dictionary of Resilient Function parameters.

     """
    params = {}

    # Remove  "sep_" from the kwargs key names.
    for (k, v) in kwargs.copy().items():
        v = kwargs.pop(k)

        if isinstance(k, list):
            k = [ResilientComponent.get_select_param(val) for val in v]
        elif isinstance(v, dict):
            v = v.get("name")
        kwargs[k] = v.rstrip().lstrip() if isinstance(v, str)  else v
        params[k.split('_', 1)[1]] = v.rstrip().lstrip() if isinstance(v, str) \
                                                                and v.lower().startswith("sep_") else v

    # If any entry has "None" string change to None value for params.
    for k, v in params.items():
        if isinstance(v, str) and v.lower() == 'none':
            params[k] = None

    return params


def create_attachment(rest_client, file_name, file_content, incident_id):
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
    try:
        with temp_file_obj as temp_file:
            temp_file.write(file_content)

            # Post file to Resilient
            att_report = rest_client.post_attachment("/incidents/{0}/attachments".format(incident_id),
                                                     temp_file.name, file_name,
                                                     "text/plain",
                                                     "")
            LOG.info("New attachment added to incident %s", incident_id)

    except IOError as ioerr:
        raise IOError("Unexpected IO error '{0}' for file '{1}".format(ioerr, file_name))

    except Exception as err:
        raise Exception("Exception '{0}' while trying to create attachment on incident '{1}' for file '{2}'."
                        .format(err, incident_id, file_name))

    return att_report

def generate_result_csv(rtn, sep_commandid):
    """"Generate file content for attachment from eoc scan results.

    :param rtn: Result returned from SEPM server after scan result processed.
    :param sep_commandid: Result commandid.
    :return (file_name, file_content): Return tuple of file name and  content
    """
    file_content = ""
    file_name = "EOC_scan_results_for_commandid_{0}_{1}.csv" \
        .format(sep_commandid, datetime.datetime.today().strftime('%Y%m%d%H%M%S'))
    file_content = "Computer name,Computer id,Artifact type,Artifact value,Match type,Match value\n"

    eps = rtn.get("content",[])
    for i in range(len(eps)):
        ep_name = eps[i]["computerName"]
        ep_id = eps[i]["computerId"]
        artifact_type = eps[i]["scan_result"]["artifact_type"]
        artifact_value = eps[i]["scan_result"]["artifact_value"]
        matches = eps[i]["scan_result"]["FULL_MATCHES"] if "File" in artifact_type \
            else eps[i]["scan_result"]["HASH_MATCHES"]
        for m in matches:
            if "File" in artifact_type:
                file_content += ("{0}\n".format(",".join([ep_name, ep_id, artifact_type, artifact_value,
                                                          m["hashType"], m["hashValue"]])))
            else:
                file_content += ("{0}\n".format(",".join([ep_name, ep_id, artifact_type, artifact_value,
                                                          "File path", m["value"]])))

    return(file_name, file_content)

def get_engine_status(eps, non_compliant_endpoints):
    """"Check overall status of all SEP av engines for an endpoint.
    Generate overall 'disabled_status' status of SEP av engines for an endpoint and
    update list non_compliant_endpoints if at least one installed engine disabled on an endpoint.

    :param eps: Dict with an endpoint properties.
    :param non_compliant_endpoints: List of non-compliant endpoints.
    :return disabled_status: Return disabled status, value > 0 indicated at least one disabled.
    """
    disabled_status = 0

    for i in range(len(eps)):
        ep_name = eps[i]["computerName"]
        status = 0
        for sf in EP_ENGINE_STATUS_FIELDS:
            # If engine is installed and not enabled.
            if not eps[i][sf] != 2 and not eps[i][sf]:
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

    results["eps"] = []
    eps = rtn["content"]

    for i in range(len(eps)):
        ep = {}
        ep_name = eps[i]["computerName"]
        if ep_name in non_compliant_endpoints:
            ep["computer_name"] = ep_name
            if "host integrity check passed" not in eps[i].get("quarantineDesc", "").lower():
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
                if eps[i][f] in EP_ENGINE_STATUSES:
                    ep[f] = EP_ENGINE_STATUSES[eps[i][f]]
                else:
                    ep[f] = "Unexpected status"
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

    if non_compliant_endpoints is None:
        non_compliant_endpoints = []

    if rtn is not None and rtn["content"]:
        results["total"] = len(rtn["content"])
        eps = rtn["content"]
        if eps:
            results["disabled"] = get_engine_status(eps, non_compliant_endpoints)
            for i in range(len(eps)):
                ep_name = eps[i]["computerName"]
                for f in EP_PROP_FIELDS:
                    if f == "onlineStatus" and int(eps[i][f]) == 0:
                        results["offline"] += 1
                        if not ep_name in non_compliant_endpoints:
                            non_compliant_endpoints.append(ep_name)

                    if f == "quarantineDesc" and "host integrity check passed" not in eps[i].get("quarantineDesc", "").lower():
                        results["hi_failed"] += 1
                        if not ep_name in non_compliant_endpoints:
                            non_compliant_endpoints.append(ep_name)
                    if f == "timediffLastUpdateTime":
                        if eps[i][f] > HB_DEF:
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

    if non_compliant_endpoints:
        results = add_non_compliant_ep_properties(rtn, non_compliant_endpoints, results)

    return results