# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

""" Process results from command status received form Symantec SEPM server. """
from logging import getLogger
import defusedxml.ElementTree as ET
from time import time, mktime
from datetime import datetime

LOG = getLogger(__name__)

def filter_hits(rtn, status_type):
    """ For scan commands results screen out endpoints with no hits.
    :param: Result returned from SEPM server with status updates.
    :return Result with endpoints with no hits filtered out.
    """
    # Extract content based on action type.
    if status_type == "scan":
        pattern = "MATCH"
    elif status_type == "remediation":
        pattern = "remediation_count"

    content = rtn.get("content")
    rtn["content"] = [i for i in content if "scan_result" in i and i.get("scan_result", {}).get(pattern)]
    rtn["numberOfElements"] = len(rtn.get("content"))
    rtn["totalElements"] = len(rtn.get("content"))

def parse_scan_results(xml, status_type):
    """ Parse scan eoc xml results and convert to dict.
        Example xml:
        ============
        <EOC creator="SOAR" version="1.0" id="id">
            <DataSource name="name" id="id" version="version"/>
            <ScanType>QUICK_SCAN</ScanType>
            <Threat time="" severity="" type="" category="">
                <Description>Scan eoc for suspicious hash.</Description>
                <URL></URL>
                <User></User>
                <Attacker>
                </Attacker>
                <proxy ip=""/>
                <Application></Application>
            </Threat>
            <Activity>
                <OS id="0" name="name" version="version">
                    <Process>
                    </Process>
                    <Files>
                        <File name="" action="create">
                            <Hash name="SHA256" value="8f5cae16ef5cfd3fcd9a4d6d58de14137b92a845ce00f69b64c5b04b6b712a83"/>
                            <Matched result="HASH_MATCH" value="C:\\temp\\suspicious_exe.exe" hashType="SHA256"/>
                            <Matched result="HASH_MATCH" value="C:\\Users\\Administrator\\Desktop\\suspicious_exe.exe" hashType="SHA256"/>
                            <Matched result="HASH_MATCH" value="C:\\Users\\Administrator\\Desktop\\suspicious_exe_copy.exe" hashType="SHA256"/></File>
                        <File name="" action="create">
                            <Matched result="NO_MATCH"/></File>
                        <File name="" action="create">
                            <Matched result="NO_MATCH"/></File>
                    </Files>
                    <Registry>
                    </Registry>
                    <Network/>
                </OS>
            </Activity>
        </EOC>
        Example: result
        ===============
        scan_result = {
            'match_count': 3,
            'remediation_count': 0,
            'PARTIAL_MATCHES': [],
            'HASH_MATCHES': [{'hashType': 'SHA256', 'result': 'HASH_MATCH', 'value': 'C:\\temp\\suspicious_exe.exe'},
                             {'hashType': 'SHA256', 'result': 'HASH_MATCH', 'value': 'C:\\Users\\Administrator\\Desktop\\suspicious_exe.exe'},
                             {'hashType': 'SHA256', 'result': 'HASH_MATCH', 'value': 'C:\\Users\\Administrator\\Desktop\\suspicious_exe_copy.exe'}],
            'FULL_MATCHES': [], 'artifact_value': '8f5cae16ef5cfd3fcd9a4d6d58de14137b92a845ce00f69b64c5b04b6b712a83',
            'artifact_type': 'SHA256 hash',
            'fail_remediation_count': 0,
            'MATCH': True
        }

    :param xml: Status in xml for endpoint.
    :param status_type: Scan type (scan or remediation).
    :return Scan result in a dict.
    """
    # Create empty result dict.
    scan_result = {
        "MATCH": False,
        "artifact_value": '',
        "artifact_type": '',
        "remediate_artifact_value": '',
        "FULL_MATCHES": [],
        "HASH_MATCHES": [],
        "PARTIAL_MATCHES": [],
        "match_count": 0,
        "remediation_count": 0,
        "fail_remediation_count": 0
    }
    file_seps = ['\\', '/']
    match_types = ["HASH_MATCH", "FULL_MATCH", "PARTIAL_MATCH", "NO_MATCH"]

    try:
        results = ET.fromstring(xml.encode('utf8', 'ignore'))

        for item in results.findall('Activity/OS/Files/File/Matched'):
            LOG.debug(item.attrib)
            if item.attrib.get("result", None) in match_types[-1:]: # No match
                continue
            elif status_type.lower() == "remediation" and item.attrib.get("remediation", "").lower() != "succeeded":  # Remediation not successful
                if item.attrib.get("remediation", "").lower() == "failed":
                    scan_result["fail_remediation_count"] += 1
                continue
            elif item.attrib.get("result", None) in match_types[:-1]: # Actual Match
                if status_type.lower() == "remediation":
                    for matched_file in results.findall('Activity/OS/Files/File'):
                        if not scan_result.get("remediate_artifact_value"):
                            scan_result["remediate_artifact_value"] = matched_file.attrib.get("name", None)
                            break
                scan_result["MATCH"] = True
                for match_type in match_types[:-1]:
                    if item.attrib.get("result", None) == match_type and item.attrib not in scan_result.get(match_type+'ES'):
                        # File name or path match.
                        if item.attrib.get("result", None) in match_types[1:-1]: # Full or partial match
                            for matched_file in results.findall('Activity/OS/Files/File'):
                                if not scan_result.get("artifact_value"):
                                    scan_result["artifact_value"] = matched_file.attrib.get("name", None)
                                    if any(fs in matched_file for fs in file_seps):
                                        scan_result["artifact_type"] = "File Path"
                                    else:
                                        scan_result["artifact_type"] = "File Name"
                        else:
                            # Hash match.
                            for matched_hash in results.findall('Activity/OS/Files/File/Hash'):
                                if not scan_result.get("artifact_value"):
                                    scan_result["artifact_type"] = "{} hash".format(matched_hash.attrib.get("name", None))
                                    scan_result["artifact_value"] = matched_hash.attrib.get("value", None)
                        scan_result[match_type+'ES'].append(item.attrib)
                        scan_result["match_count"] += 1
                        if "remediation" in item.attrib and item.attrib.get("remediation", None) == "SUCCEEDED":
                            scan_result["remediation_count"] += 1
                        if "remediation" in item.attrib and item.attrib.get("remediation", None) == "FAILED":
                            scan_result["fail_remediation_count"] += 1
        return scan_result

    except ET.ParseError as e:
        LOG.error("During scan result XML processing, Got exception type: %s, msg: %s", e.__repr__(), e.message)
        raise e

def get_overall_progress(rtn, sep_scan_timeout=None, scan_date=None):
    """ Calculate overall progress of a command.

    The command states are as follows:

        0 = Initial / Not received
        1 = Received (by the client(s))
        2 = In progress
        3 = Completed
        4 = Rejected
        5 = Canceled
        6 = Error

    :param rtn: Result returned from SEPM server.
    :return Return overall command state.
    """
    state_map = {
        0: "Waiting/Not received",
        1: "Received",
        2: "In progress",
        3: "Completed",
        4: "Rejected",
        5: "Canceled",
        6: "Error"
    }
    overall_state = "Completed"
    timeout_state = "Timeout"

    if scan_date and sep_scan_timeout:
        scan_time = int(mktime(datetime.strptime(scan_date, "%Y-%m-%d %H:%M:%S").timetuple()))
        now_time = int(time())
        time_since_scan = now_time - scan_time

    if not rtn.get("content", []):
        # When the scan command initially launched the content dict is typically empty.
        overall_state = state_map[0]
    else:
        for i in range(len(rtn.get("content", []))):
            if rtn.get("content", [])[i].get("stateId") in state_map.keys():
                # Set the overall progress based on the stateID
                overall_state = state_map[rtn.get("content", [])[i].get("stateId")]
                break

    # Set the overall command state across multiple endpoints.
    rtn["overall_command_state"] = overall_state
    # Reset the overall command state if all endpoints have not responded within 'sep_scan_timeout' period.
    if overall_state != "Completed" and sep_scan_timeout and scan_date:
        if sep_scan_timeout and time_since_scan >= int(sep_scan_timeout):
            rtn["overall_command_state"] = timeout_state

    return overall_state

def process_results(rtn, options, status_type, scan_date):
    """"Process command status for types 'scan, ''upload', 'remediation, 'quarantine'.

    :param rtn: Result return from SEPM server.
    :return Result with command status results updates.
    """

    # If all endpoints have completed scan then process results
    # Set top level counters to 0 value.
    # total_match_count = Total artifact matches across target endpoints.
    # total_match_ep_count = Total number of target endpoints with matched artifacts.
    # total_remediation_count = Total artifacts remediated across target endpoints.
    # total_remediation_ep_count = Total number of target endpoints with remediated artifacts.
    # total_ep_count = Total endpoint count for the command.
    # total_not_completed = Total endpoints which have not completed command.
    # total_fail_remediation_count = Total remediation failures.
    # scan_artifact_value = The originating artifact value for eoc scan.
    # remediate_artifact_value = The originating artifact value for remediate scan.
    sep_scan_timeout = options.get("sep_scan_timeout", None)
    rtn["total_match_count"] = rtn["total_match_ep_count"] = rtn["total_remediation_count"] \
        = rtn["total_fail_remediation_count"] = rtn["total_remediation_ep_count"] = 0
    rtn["total_not_completed"] = 0
    rtn["total_ep_count"] = len(rtn.get("content"))
    rtn["scan_artifact_value"] = ''
    rtn["remediate_artifact_value"] = ''
    get_overall_progress(rtn, sep_scan_timeout, scan_date)

    for i in range(len(rtn.get("content"))):
        if rtn.get("content", [])[i].get("stateId") == 3:
            if status_type.lower() in ["scan", "remediation"]:
                rtn["content"][i]["scan_result"] = parse_scan_results(rtn.get("content", [])[i].get("resultInXML"), status_type)
                # Reset total count.
                rtn["total_match_count"] += rtn.get("content", [])[i].get("scan_result", {}).get("match_count")
                rtn["total_remediation_count"] += rtn.get("content", [])[i].get("scan_result", {}).get("remediation_count")
                rtn["total_fail_remediation_count"] += rtn.get("content", [])[i].get("scan_result", {}).get("fail_remediation_count")
                if rtn.get("content", [])[i].get("scan_result", {}).get("match_count") > 0:
                    rtn["total_match_ep_count"] += 1
                    if not rtn.get("scan_artifact_value"):
                        rtn["scan_artifact_value"] = rtn.get("content", [])[i].get("scan_result", {}).get("artifact_value")
                if rtn.get("content", [])[i].get("scan_result", {}).get("remediation_count") > 0:
                    rtn["total_remediation_ep_count"] += 1
                    if not rtn.get("remediate_artifact_value"):
                        rtn["remediate_artifact_value"] = rtn.get("content", [])[i].get("scan_result", {}).get("remediate_artifact_value")
        else:
            # Increment if endpoint status ne 3
            rtn["total_not_completed"] += 1

    return rtn
