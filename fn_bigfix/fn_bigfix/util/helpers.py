# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
""" Helper functions for SOAR Functions supporting Bigfix integration """

from __future__ import print_function
from os import unlink
from logging import getLogger
from tempfile import NamedTemporaryFile

LOG = getLogger(__name__)
PACKAGE_NAME = "fn_bigfix"

def validate_opts(func):
    """"Check options set correctly.
    :param func: SOAR Function instance reference
     """
    if "bigfix_url" not in func.options or func.options["bigfix_url"]:
        raise ValueError("Mandatory config setting 'bigfix_url' not set.")
    if "bigfix_port" not in func.options or func.options["bigfix_port"]:
        raise ValueError("Mandatory config setting 'bigfix_port' not set.")
    if "bigfix_user" not in func.options or func.options["bigfix_user"]:
        raise ValueError("Mandatory config setting 'bigfix_user' not set.")
    if "bigfix_pass" not in func.options or func.options["bigfix_pass"]:
        raise ValueError("Mandatory config setting 'bigfix_pass' not set.")
    if "bigfix_hunt_results_limit" not in func.options or func.options["bigfix_hunt_results_limit"]:
        raise ValueError(
            "Mandatory config setting 'bigfix_hunt_results_limit' not set.")
    if "bigfix_polling_interval" not in func.options or func.options["bigfix_polling_interval"]:
        raise ValueError(
            "Mandatory config setting 'bigfix_polling_interval' not set.")
    if "bigfix_polling_timeout" not in func.options or func.options["bigfix_polling_timeout"]:
        raise ValueError(
            "Mandatory config setting 'bigfix_polling_timeout' not set.")
    if "bigfix_endpoints_wait" not in func.options or func.options["bigfix_endpoints_wait"]:
        raise ValueError(
            "Mandatory config setting 'bigfix_endpoints_wait' not set.")

def create_attachment(rest_client, file_name, file_content, params):
    """"Add file as SOAR incident attachment.
    :param rest_client: SOAR Rest client
    :param file_name: Name of file to add as attachment
    :param file_content: Content of file to add as attachment
    :param params: SOAR Function parameters (dict)
    :return att_report: Return result (dict) of SOAR post attachment request
    """

    temp_file_obj = NamedTemporaryFile('w', delete=False, encoding="utf8")

    # Create the temporary file save results in json format.
    with temp_file_obj as temp_file:
        temp_file.write(file_content)
        temp_file.flush()
        try:
            # Post file to SOAR
            att_report = rest_client.post_attachment("/incidents/{}/attachments".format(params["incident_id"]),
                                                     temp_file.name,
                                                     file_name,
                                                     "text/plain",
                                                     "")
            LOG.info("New attachment added to incident {}".format(
                params["incident_id"]))
        except Exception as err:
            raise err
        finally:
            unlink(temp_file.name)

    return att_report
