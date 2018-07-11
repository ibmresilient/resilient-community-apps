# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import logging
import json
import os
import datetime
import calendar
from os.path import join, pardir
from resilient_circuits.template_functions import environment
import resilient_circuits.template_functions as template_functions


log = logging.getLogger(__name__)


def verify_config(opts):
    config_opts = opts.get("fn_mcafee_opendxl")
    if config_opts is None:
        log.error("There is no [fn_mcafee_opendxl] section in the config file,"
                  "please set that by running resilient-circuits config -u")
        raise ValueError("[fn_mcafee_opendxl] section is not set in the config file")

    config_client = config_opts.get("dxlclient_config")
    topic_listener_on = config_opts.get("topic_listener_on")
    custom_template_dir = config_opts.get("custom_template_dir")

    if config_client is None:
        log.error("dxlclient_config is not set. You must set this path to run this service")
        raise ValueError("dxlclient_config is not set. You must set this path to run this service")

    if topic_listener_on is None:
        log.error("topic_listener_on is not set. You must set this value to run this service")
        raise ValueError("topic_listener_on is not set. You must set this value to run this service")

    config = {
        "config_client": config_client,
        "topic_listener_on": topic_listener_on,
        "custom_template_dir": custom_template_dir,
        "opts": opts
    }

    return config


def create_incident(resilient_client, payload):
    uri = "/incidents"
    payload_dict = json.loads(payload)
    log.info("Creating incident with payload: {}".format(json.dumps(payload_dict)))
    log.debug("Payload: {}".format(payload))

    response = resilient_client.post(uri=uri, payload=payload_dict)
    return response


def add_methods_to_global():
    # Add ds_to_millis to global env so it can be used in filters
    ds_filter = {
        "ds_to_millis": ds_to_millis,
        "get_incident_type": get_incident_type
    }
    env = environment()
    env.globals.update(ds_filter)


# Converts string datetime to milliseconds epoch
def ds_to_millis(val):
    """Assuming val is a string datetime, e.g. '2017-05-17T17:07:59.114Z' (UTC), convert to milliseconds epoch"""
    if not val:
        return val
    try:
        if len(val) != 24:
            raise ValueError("Invalid timestamp length %s" % val)
        ts = val[:23]
        ts_format = "%Y-%m-%dT%H:%M:%S.%f"
        dt = datetime.datetime.strptime(ts, ts_format)
        return calendar.timegm(dt.utctimetuple()) * 1000
    except Exception as e:
        log.exception("%s Not in expected timestamp format YYYY-MM-DDTHH:MM:SS.mmmZ", val)
        return None


# Returns Incident Type if there is one to return
def get_incident_type(category):
    log.debug("Category is {}".format(category))

    incident_type_lookup = {
        "Malware detected": "Malware"
    }
    incident_type = incident_type_lookup.get(category)

    if incident_type is not None:
        return incident_type
    else:
        return ""


def map_values(template_file, message_dict):
    with open(template_file, 'r') as template:

        log.debug("Message in dict form: {}".format(message_dict))

        incident_template = template.read()
        incident_data = template_functions.render(incident_template, message_dict)

        return incident_data


def _merge_two_dicts(a, b):
    c = a.copy()
    c.update(b)  # modifies c with b's keys and values
    return c


def _get_topic_from_file_name(f):
    file_no_extention = f.split('.')[0]
    topic = file_no_extention.replace('_', '/')

    return topic


def _get_jinja_files(dir):
    # return [f for f in os.listdir(dir) if f.endswith(".jinja2") or f.endswith(".jinja")]
    dict = {}
    for f in os.listdir(dir):
        if f.endswith(".jinja2") or f.endswith(".jinja"):
            dict[f] = join(dir, f)  # dictionary with key=filename and values=path to file
    return dict


def _get_template_files(overrides_dir=None):
    # Get custom templates
    custom_templates = []
    if overrides_dir:
        custom_templates = _get_jinja_files(overrides_dir)

    # Get default templates
    current_path = os.path.dirname(os.path.realpath(__file__))
    default_dir = join(current_path, pardir, "data/templates")
    default_templates = _get_jinja_files(default_dir)

    return _merge_two_dicts(default_templates, custom_templates)


def get_topic_template_dict(overrides_dir=None):
    template_files = _get_template_files(overrides_dir)

    topic_template_dict = {}

    # Python 2.x solution
    try:
        for k, v in template_files.iteritems():
            topic = _get_topic_from_file_name(k)
            topic_template_dict[topic] = v

    # Python 3.6 solution
    except AttributeError:
        for k, v in template_files.items():
            topic = _get_topic_from_file_name(k)
            topic_template_dict[topic] = v

    return topic_template_dict
