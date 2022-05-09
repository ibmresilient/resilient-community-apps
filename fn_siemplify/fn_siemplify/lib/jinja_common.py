# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import calendar
import logging
import json
import os
import time
from json.decoder import JSONDecodeError
from resilient_circuits.template_functions import render, environment
from resilient_lib import readable_datetime

LOG = logging.getLogger(__name__)

class JinjaEnvironment():
    def __init__(self):
        # Add the timestamp-parse function to the global JINJA environment
        env = environment()
        env.globals.update({
            "resilient_datetimeformat": jinja_resilient_datetimeformat,
            "resilient_display_datetimeformat": readable_datetime,
            "resilient_substitute": jinja_resilient_substitute,
            "resilient_splitpart": jinja_resilient_splitpart,
            "resilient_trimlist": jinja_resilient_trimlist
            })
        env.filters.update({
            "resilient_datetimeformat": jinja_resilient_datetimeformat,
            "resilient_display_datetimeformat": readable_datetime,
            "resilient_substitute": jinja_resilient_substitute,
            "resilient_splitpart": jinja_resilient_splitpart,
            "resilient_trimlist": jinja_resilient_trimlist
            })

    def make_payload_from_template(self, template_override, default_template, payload):
        """convert a payload into a newformat based on a specified template

        Args:
            template_override ([str]): [/path/to/template.jinja]
            default_template ([str]): [/path/to/template.jinja]
            payload ([dict]): [data to convert]

        Returns:
            [dict]: [converted payload]
        """
        template_data = self.get_template(template_override, default_template)

        # Render the template.
        try:
            rendered_payload = render(template_data, payload)
            LOG.debug(rendered_payload)
            rendered_payload = json.loads(rendered_payload)

        except JSONDecodeError as err:
            LOG.error("Template error: %s. data: %s", str(err), payload)
            raise err

        LOG.debug(rendered_payload)

        return rendered_payload

    def get_template(self, specified_template, default_template):
        """return the contents of a jinja template, either from the default or a customer specified
            custom path

        Args:
            specified_template ([str]): [customer specified template path]
            default_template ([str]): [default template location]

        Returns:
            [str]: [contents of template]
        """
        template_file_path = specified_template
        if template_file_path:
            if not (os.path.exists(template_file_path) and os.path.isfile(template_file_path)):
                LOG.error(u"Template file: %s doesn't exist, using default template",
                        template_file_path)
                template_file_path = None

        if not template_file_path:
            # using default template
            template_file_path = os.path.join(
                                    os.path.dirname(os.path.realpath(__file__)),
                                    default_template
                                )

        LOG.debug(u"Incident template file: %s", template_file_path)
        with open(template_file_path, "r") as definition:
            return definition.read()

def jinja_resilient_datetimeformat(value, date_format="%Y-%m-%dT%H:%M:%S.000Z"):
    """custom jinja filter to convert UTC dates to epoch format

    Args:
        value ([str]): [jinja provided field value]
        date_format (str, optional): [conversion format]. Defaults to "%Y-%m-%dT%H:%M:%S.000Z".

    Returns:
        [int]: [epoch value of datetime, in milliseconds]
    """
    if not value:
        return value

    utc_time = time.strptime(value[:value.rfind('.')], date_format)
    return calendar.timegm(utc_time)*1000

def jinja_resilient_substitute(value, json_str):
    """jinja custom filter to replace values based on a lookup dictionary

    Args:
        value ([str]): [original value]
        json_str ([str]): [string encoded json lookup values]

    Returns:
        [str]: [replacement value or original value if no replacement found]
    """
    replace_dict = json.loads(json_str)
    if value in replace_dict:
        return replace_dict[value]

    # use a default value if specific match is missing
    if 'DEFAULT' in replace_dict:
        return replace_dict['DEFAULT']

    return value

def jinja_resilient_splitpart(value, index, split_chars=' - '):
    """[split a string and return the index]

    Args:
        value ([str]): [string to split]
        index ([int]): [index to return]
        split_chars (str, optional): [split characters]. Defaults to ' - '.

    Returns:
        [str]: [index of string. if index is out of bounds, the original string is returned]
    """
    splits = value.split(split_chars)
    if len(splits) > index:
        return splits[index]

    return value

def jinja_resilient_trimlist(org_list):
    """[trim whitespace from elements in a list]

    Args:
        list ([type]): [description]
    Returns:
        [list]: [list with elements trimmed of whitespace]
    """
    if not isinstance(org_list, list):
        return org_list
    return [element.strip() for element in org_list]
