# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

""" Process results from command status received form Symantec SEPM server. """

from __future__ import print_function
import logging
import xml.etree.ElementTree as ET

LOG = logging.getLogger(__name__)


def filter_hits(rtn):
    """ For scan commands results screen out endpoints with no hits.


    :param: Result returned from SEPM server with status updates.
    :return Result with endpoints with no hits filtered out.

    """
    # Extract events based on filter(s)
    content = rtn["content"]
    rtn["content"] = [i for i in content if i["scan_result"]["MATCH"]]
    rtn["numberOfElements"] = len(rtn["content"])
    rtn["totalElements"] = len(rtn["content"])


def parse_scan_results(xml):
    """"Parse scan eoc xml results and convert to dict.

    :param xml: Status in xml for endpoint.
    :return Scan result in a dict.
    """
    # Create empty result dict.
    scan_result = {
        "MATCH": False,
        "FULL_MATCHES": [],
        "HASH_MATCHES": [],
        "match_count": 0,
        "remediation_count": 0,
    }

    try:
        results = ET.fromstring(xml.encode('utf8', 'ignore'))

        for item in results.findall('Activity/OS/Files/File/Matched'):
            LOG.debug(item.attrib)
            if item.attrib["result"] == "NO_MATCH":
                continue
            elif item.attrib["result"] in ["FULL_MATCH", "HASH_MATCH"]:
                scan_result["MATCH"] = True
                if item.attrib["result"] == "FULL_MATCH" and not item.attrib in scan_result["FULL_MATCHES"]:
                    scan_result["FULL_MATCHES"].append(item.attrib)
                    scan_result["match_count"] += 1
                    if "remediation" in  item.attrib and item.attrib["remediation"] == "SUCCEEDED":
                        scan_result["remediation_count"] += 1
                elif item.attrib["result"] == "HASH_MATCH" and not item.attrib in scan_result["HASH_MATCHES"]:
                    scan_result["HASH_MATCHES"].append(item.attrib)
                    scan_result["match_count"] += 1
                    if "remediation" in  item.attrib and item.attrib["remediation"] == "SUCCEEDED":
                        scan_result["remediation_count"] += 1
        return scan_result

    except ET.ParseError as e:
        LOG.error("There was an error trying to process scan result XML.", e.__repr__(), e.message)
        raise e

def get_overall_progress(rtn):
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

    inprogress_state_ids = [0, 1, 2]
    overall_state = "Processed"
    in_prog_state = "In progress"

    for i in range(len(rtn["content"])):
        if rtn["content"][i]["stateId"] in inprogress_state_ids:
            # If any of the endpoint statuses is still in an in-progress state, reset overall
            # scan status to "In progress".
            overall_state = in_prog_state
            break
    # Set the overall command state across multiple endpoints.
    rtn["overall_command_state"] = overall_state
    return overall_state


def process_results(rtn, status_type):
    """"Process command status for types 'scan, ''upload', 'remediation, 'quarantine'.

    :param rtn: Result return from SEPM server.
    :return Result with command status results updates.
    """

    # If all endpoints have completed scan then process results
    rtn["total_match_count"] = rtn["total_remediation_count"] = 0

    if get_overall_progress(rtn) == "Processed":

        for i in range(len(rtn["content"])):
            rtn["content"][i]["command_status_id"] = rtn["content"][i]["stateId"]
            if status_type.lower() in ["scan", "remediation"]:
                rtn["content"][i]["scan_result"] = parse_scan_results(rtn["content"][i]["resultInXML"])
                # Reset total count.
                rtn["total_match_count"] += rtn["content"][i]["scan_result"]["match_count"]
                rtn["total_remediation_count"] += rtn["content"][i]["scan_result"]["remediation_count"]

        if status_type.lower() == "scan":
            filter_hits(rtn)

    return rtn