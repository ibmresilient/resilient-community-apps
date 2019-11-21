# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import io
import re
import six
from resilient_lib import RequestsCommon, validate_fields, str_to_bool, write_file_attachment

TOWER_API_BASE = "api/v2"
SECTION_HDR = "fn_ansible_tower"

LIST_URL = 'job_templates/'

JSON_HEADERS = {
    "Content-Type": "application/json"
}

def get_job_template_by_name(opts, options, filter_by_name):
    """
    get job templates, optionally based on template name
    :param opts: app.config file
    :param options: app.config section just for this integration
    :param filter_by_name: name of template to search for
    :return: found template or None
    """
    basic_auth, cafile = get_common_request_items(options)

    rc = RequestsCommon(opts, options)

    next_url = "/".join((TOWER_API_BASE, LIST_URL))
    while next_url:
        url = "/".join((options.get('url'), next_url)).replace("//api", "/api")
        results = rc.execute_call_v2("get", url, proxies=rc.get_proxies(), auth=basic_auth,
                                     verify=cafile)
        json_results = results.json()

        if filter_by_name:
            for template in json_results['results']:
                if template['name'].lower() == filter_by_name.strip().lower():
                    return template

        # get next paged set of results
        next_url = json_results['next']

    return None

def get_job_template_by_project(opts, options, filter_by_project):
    """
    get job templates, optionally based on project name
    :param opts: app.config file
    :param options: app.config section just for this integration
    :param filter_by_project: name of project to search for
    :return: list of templates by project
    """
    url = "/".join((options.get('url'), TOWER_API_BASE, LIST_URL))
    basic_auth, cafile = get_common_request_items(options)

    rc = RequestsCommon(opts, options)

    next_url = "/".join((TOWER_API_BASE, LIST_URL))
    result_templates = []
    while next_url:
        url = "/".join((options.get('url'), next_url)).replace("//api", "/api")
        results = rc.execute_call_v2("get", url, proxies=rc.get_proxies(), auth=basic_auth,
                                     verify=cafile)
        json_results = results.json()

        if filter_by_project:
            result_templates.extend([template for template in json_results['results']
                                     if template['summary_fields']['project']['name'].lower() == filter_by_project.lower()])
        else:
            result_templates.extend(json_results['results'])

        # get next paged set of results
        next_url = json_results['next']

    return result_templates

def make_extra_vars(arguments):
    """
    convert from name=value;name=value into dictionary
    :param arguments:
    :return: dictionary of name/value pairs
    """
    extra_vars = {}
    if arguments:
        for item in arguments.split(u";"):
            if item.strip(u' '):
                k, v = item.split(u"=")
                extra_vars[k.strip(u' ')] = v.strip(u' ')

    return extra_vars

def get_common_request_items(options):
    """
    return basic auth and cafile information
    :return: basic_auth and cafile
    """
    validate_fields(("username", "password"), options)
    basic_auth = (options['username'], options['password'])
    cafile = str_to_bool(options.get("cafile")) if options.get("cafile", "False").lower() in ("true", "false") else True

    return basic_auth, cafile

def save_as_attachment(res_client, incident_id, results):
    """
    save an attachment to the incident with the job results
    :param res_client:
    :param incident_id:
    :param results: payload to parse
    :return: None
    """
    finished = results['summary']['finished'].replace('T', ' ') if results['summary']['finished'] else None
    note = u"Job Id: {}\nStatus: {}\nTemplate Name: {}\nFinished: {}".format(results['summary']['id'], results['summary']['status'],
                                                                             results['summary']['name'], finished)
    note = note + u"\n".join(event.get("stdout") for event in results['events']['results'])
    note = re.sub(r'[\x00-\x7f]\[[0-9;]*m', r'', note) # remove color hilighting

    if six.PY2:
        file_handle = io.BytesIO(note.encode('utf-8'))
    else:
        file_handle = io.StringIO(note)

    file_name = u"{}_{}.txt".format(results['summary']['name'].replace(" ", "_"), results['summary']['id'])
    write_file_attachment(res_client, file_name, file_handle, incident_id)
