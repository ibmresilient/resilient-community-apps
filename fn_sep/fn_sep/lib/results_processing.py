# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

""" Process results from command status received form Symantec SEPM server. """
from __future__ import print_function
import logging
import xml.etree.ElementTree as ET
import time
from datetime import datetime

LOG = logging.getLogger(__name__)

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

    content = rtn["content"]
    rtn["content"] = [i for i in content if "scan_result" in i and i["scan_result"][pattern]]
    rtn["numberOfElements"] = len(rtn["content"])
    rtn["totalElements"] = len(rtn["content"])


def parse_scan_results(xml, status_type):
    """ Parse scan eoc xml results and convert to dict.
        Example xml:
        ============
        <EOC creator="Resilient" version="1.0" id="id">
            <DataSource name="name" id="id" version="version"/>
            <ScanType>QUICK_SCAN</ScanType>
            <Threat time="" severity="" type="" category="">
                <Description>Scan eoc for for suspicious hash.</Description>
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
            test = match_types[-1:]
            if item.attrib["result"] in match_types[-1:]: # No match
                continue
            elif status_type.lower() == "remediation" and item.attrib["remediation"].lower() != "succeeded":  # Remediation not successful
                if item.attrib["remediation"].lower() == "failed":
                    scan_result["fail_remediation_count"] += 1
                continue
            elif item.attrib["result"] in match_types[:-1]: # Actual Match
                if status_type.lower() == "remediation":
                    for matched_file in results.findall('Activity/OS/Files/File'):
                        if not scan_result["remediate_artifact_value"]:
                            scan_result["remediate_artifact_value"] = matched_file.attrib["name"]
                            break
                scan_result["MATCH"] = True
                for match_type in match_types[:-1]:
                    if item.attrib["result"] == match_type and not item.attrib in scan_result[match_type+'ES']:
                        # File name or path match.
                        if item.attrib["result"] in match_types[1:-1]: # Full or partial match
                            for matched_file in results.findall('Activity/OS/Files/File'):
                                if not scan_result["artifact_value"]:
                                    scan_result["artifact_value"] = matched_file.attrib["name"]
                                    if any(fs in matched_file for fs in file_seps):
                                        scan_result["artifact_type"] = "File Path"
                                    else:
                                        scan_result["artifact_type"] = "File Name"
                        else:
                            # Hash match.
                            for matched_hash in results.findall('Activity/OS/Files/File/Hash'):
                                if not scan_result["artifact_value"]:
                                    scan_result["artifact_type"] = "{} hash".format(matched_hash.attrib["name"])
                                    scan_result["artifact_value"] = matched_hash.attrib["value"]
                        scan_result[match_type+'ES'].append(item.attrib)
                        scan_result["match_count"] += 1
                        if "remediation" in  item.attrib and item.attrib["remediation"] == "SUCCEEDED":
                            scan_result["remediation_count"] += 1
                        if "remediation" in  item.attrib and item.attrib["remediation"] == "FAILED":
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
    overall_state = "Completed"
    timeout_state = "Timeout"
    in_progress_states = {
        0: "Waiting/Not received",
        1: "Received",
        2: "In progress"
    }

    if scan_date is not None and sep_scan_timeout:
        scan_time = int(time.mktime(datetime.strptime(scan_date, "%Y-%m-%d %H:%M:%S").timetuple()))
        now_time = int(time.time())
        time_since_scan = now_time - scan_time

    if not rtn["content"]:
        # When the scan command initially launched the content dict is typically empty.
        overall_state = in_progress_states[0]
    else:
        for i in range(len(rtn["content"])):
            if rtn["content"][i]["stateId"] in in_progress_states.keys():
                # If any of the endpoint statuses is still in any of the non-completed states reset overall
                # scan status to "In progress".
                overall_state = in_progress_states[2]
                break

    # Set the overall command state across multiple endpoints.
    rtn["overall_command_state"] = overall_state
    # Reset the overall command state if all endpoints have not responded within 'sep_scan_timeout' period.
    if overall_state != "Completed" and sep_scan_timeout is not None and scan_date is not None:
        if sep_scan_timeout is not None and time_since_scan >= int(sep_scan_timeout):
            rtn["overall_command_state"] = timeout_state

    return overall_state


def process_results(rtn, options, status_type, scan_date):
    """"Process command status for types 'scan, ''upload', 'remediation, 'quarantine'.

    :param rtn: Result return from SEPM server.
    :return Result with command status results updates.
    """

    # If all endpoints have completed scan then process results
    # Set top level counters to 0 value.
    # total_match_count =  Total artifact matches across target endpoints.
    # total_match_ep_count =  Total number of target endpoints with matched artifacts.
    # total_remediation_count =  Total artifacts remediated across target endpoints.
    # total_remediation_ep_count =  Total number of target endpoints with remediated artifacts.
    # total_ep_count = Total endpoint count for the command.
    # total_not_completed = Total endpoints which have not completed command.
    # total_fail_remediation_count = Total remediation failures.
    # scan_artifact_value = The originating artifact value for eoc scan.
    # remediate_artifact_value = The originating artifact value for remediate scan.
    sep_scan_timeout = options.get("sep_scan_timeout", None)
    rtn["total_match_count"] = rtn["total_match_ep_count"] = rtn["total_remediation_count"] \
        = rtn["total_fail_remediation_count"] = rtn["total_remediation_ep_count"] = 0
    rtn["total_not_completed"] = 0
    rtn["total_ep_count"] = len(rtn["content"])
    rtn["scan_artifact_value"] = ''
    rtn["remediate_artifact_value"] = ''
    get_overall_progress(rtn, sep_scan_timeout, scan_date)

    for i in range(len(rtn["content"])):
        if rtn["content"][i]["stateId"] == 3:
            if status_type.lower() in ["scan", "remediation"]:
                rtn["content"][i]["scan_result"] = parse_scan_results(rtn["content"][i]["resultInXML"], status_type)
                # Reset total count.
                rtn["total_match_count"] += rtn["content"][i]["scan_result"]["match_count"]
                rtn["total_remediation_count"] += rtn["content"][i]["scan_result"]["remediation_count"]
                rtn["total_fail_remediation_count"] += rtn["content"][i]["scan_result"]["fail_remediation_count"]
                if rtn["content"][i]["scan_result"]["match_count"] > 0:
                    rtn["total_match_ep_count"] += 1
                    if not rtn["scan_artifact_value"]:
                        rtn["scan_artifact_value"] = rtn["content"][i]["scan_result"]["artifact_value"]
                if rtn["content"][i]["scan_result"]["remediation_count"] > 0:
                    rtn["total_remediation_ep_count"] += 1
                    if not rtn["remediate_artifact_value"]:
                        rtn["remediate_artifact_value"] = rtn["content"][i]["scan_result"]["remediate_artifact_value"]
        else:
            # Increment if endpoint status ne 3
            rtn["total_not_completed"] += 1

    if status_type.lower() in ["scan", "remediation"]:
        filter_hits(rtn, status_type)

    return rtn
