# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2019. All Rights Reserved.

import logging
import json
import os
import jinja2
from requests.auth import HTTPBasicAuth
from six import string_types
from requests.exceptions import HTTPError
from resilient_lib.components.integration_errors import IntegrationError
from pkg_resources import Requirement, resource_filename
from resilient_circuits import template_functions
try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

log = logging.getLogger(__name__)
PROOFPOINT_TAP_404_ERROR = "404 Client Error"


def get_threat_list(rc, options, lastupdate, bundle):
    base_url = options['base_url']
    username = options['username']
    password = options['password']
    basic_auth = HTTPBasicAuth(username, password)
    url = '{0}/siem/all?format=JSON'.format(base_url)  # /v2/siem/all Fetch events for all clicks and messages relating to known threats within the specified time period

    if isinstance(lastupdate, string_types):
        url += '&sinceTime={}'.format(lastupdate)
    else:
        if lastupdate is None:
            # first run, fetch for time span equivalent to polling interval
            lastupdate = int(options['polling_interval']) * 60
        url += '&sinceSeconds={}'.format(lastupdate)

    res = rc.execute_call_v2('get', url, auth=basic_auth, verify=bundle, proxies=rc.get_proxies())

    # Debug logging
    log.debug("Response content: {}".format(res.content))
    return res.json()


def custom_response_err_msg(response):
    """
    Custom handler for response handling.
    :param response:
    :return: response
    """
    try:
        # Raise error is bad status code is returned
        response.raise_for_status()

        # Return requests.Response object
        return response

    except Exception as err:
        msg = str(err)

        if isinstance(err, HTTPError) and response.status_code == 404:
            msg = "{} - {}".format(PROOFPOINT_TAP_404_ERROR, response.text)

        log and log.error(msg)
        raise IntegrationError(msg)


def filter_reports(aggregate_forensics, malicious_flag, temp_file, options, default_path):
    """
    Filter Reports based on malicious_flag.
    :param aggregate_forensics:
    :param malicious_flag:
    :param temp_file:
    :param options
    :param default_path
    :return: filtered_reports
    """
    filtered_reports = []
    reports = aggregate_forensics.get('reports', [])
    for report in reports:
        count = 1
        # array of text output of forensic evidence data (filtered based on malicious_flag)
        # and rendered with jinja template
        forensic_evidence = []
        for forensic in report.get('forensics', []):

            if not forensic:
                # no object
                continue
            if malicious_flag is True and forensic.get('malicious') is False:
                # Filter - If malicious_flag is True we're only interested in malicious forensic evidence
                continue
            if malicious_flag is False and forensic.get('malicious') is True:
                # Filter - If malicious_flag is False we're only interested in not malicious forensic evidence
                continue

            # Render the forensics evidence that hasn't been filtered
            log.debug('Forensic evidence found {}'.format(json.dumps(forensic, indent=2)))
            try:
                # Get template file path
                template_path = _get_template_file_path(options, default_path)
                # Convert data to a txt output using a jinja template.
                forensics_txt_data = _map_values(template_path, forensic)
                # add forensics_txt_data to forensic_evidence list
                forensic_evidence.append(forensics_txt_data)
            except jinja2.exceptions.TemplateSyntaxError:
                log.info('Forensics template is not set correctly in config file')

        if forensic_evidence:
            # append the report to the filtered_reports list
            filtered_reports.append(report)
            # Write in a temp file
            report_note = u"""\n\nReport {} generated on '{}':\n- Name '{}'\n- Scope '{}'\n- Type '{}'\n- Id '{}'\n- Evidence Objects: \n{}""".format(
                count,
                aggregate_forensics.get('generated'),
                report.get('name'),
                report.get('scope'),
                report.get('type'),
                report.get('id'),
                '\n\n'.join(forensic_evidence))

            temp_file.write(report_note.encode('utf-8'))
        count += 1

    return filtered_reports


def _get_template_file_path(options, default_path):
    """
    Get template file path.
    :return:
    """
    forensics_path = options.get("forensics_template", default_path)
    if forensics_path and not os.path.exists(forensics_path):
        log.warning(u"Template file '%s' not found.", forensics_path)
        forensics_path = None
    if not forensics_path:
        # Use the template file installed by this package
        forensics_path = resource_filename(Requirement("fn-proofpoint_tap"),
                                           "fn_proofpoint_tap/data/templates/pp_threat_forensics.jinja")
    if not os.path.exists(forensics_path):
        raise Exception(u"Template file '{}' not found".format(forensics_path))

    return forensics_path


def _map_values(template_file, message_dict):
    """
    Map values from jinja template.
    :param template_file:
    :param message_dict:
    :return: output_data
    """
    with open(template_file, 'r') as template:
        log.debug("Message in dict format: %s", message_dict)
        template = template.read()
        output_data = template_functions.render(template, message_dict)
        return output_data


def create_attachment(res_client, file_name, temp_file, incident_id, content_type):
    """
    Create a new attachment by calling resilient REST API
    :param res_client:
    :param file_name:
    :param temp_file:
    :param incident_id:
    :param content_type:
    :return:
    """
    attachment_uri = "/incidents/{}/attachments".format(incident_id)

    new_attachment = res_client.post_attachment(attachment_uri,
                                                temp_file.name,
                                                filename=file_name,
                                                mimetype=content_type)
    return new_attachment
