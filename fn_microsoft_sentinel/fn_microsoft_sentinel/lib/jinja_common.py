# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
from calendar import timegm
from json import loads
from logging import getLogger
from os.path import dirname, exists, isfile, join, realpath
from time import strptime

from resilient_circuits.template_functions import environment, render_json

LOG = getLogger(__name__)

class JinjaEnvironment():
    def __init__(self):
        # Add the timestamp-parse function to the global JINJA environment
        env = environment()
        env.globals.update({
            "soar_datetimeformat": jinja_resilient_datetimeformat,
            "soar_substitute": jinja_resilient_substitute,
            "soar_splitpart": jinja_resilient_splitpart
            })
        env.filters.update({
            "soar_datetimeformat": jinja_resilient_datetimeformat,
            "soar_substitute": jinja_resilient_substitute,
            "soar_splitpart": jinja_resilient_splitpart
            })

    def make_payload_from_template(self, template_override, default_template, payload):
        """
        Convert a payload into a newformat based on a specified template
        :param template_override [str]: /path/to/template.jinja
        :param default_template [str]: /path/to/template.jinja
        :param payload [dict]: data to convert
        :return [dict]: converted payload
        """
        template_data = self.get_template(template_override, default_template)

        # Render the template.
        rendered_payload = render_json(template_data, payload)
        LOG.debug(rendered_payload)

        return rendered_payload

    def get_template(self, specified_template, default_template):
        """
        Return the contents of a jinja template, either from the default or a customer specified
        custom path.
        :param specified_template [str]: customer specified template path
        :param default_template [str]: default template location
        :return [str]: contents of template
        """
        template_file_path = specified_template
        if template_file_path:
            if not (exists(template_file_path) and isfile(template_file_path)):
                LOG.error(f"Template file: {template_file_path} doesn't exist, using default template")
                template_file_path = None

        if not template_file_path:
            # Using default template
            template_file_path = join(
                dirname(realpath(__file__)),
                default_template
            )

        LOG.debug(f"Incident template file: {template_file_path}")
        with open(template_file_path, "r") as definition:
            return definition.read()

def jinja_resilient_datetimeformat(value, date_format="%Y-%m-%dT%H:%M:%S"):
    """
    Custom jinja filter to convert UTC dates to epoch format
    :param value [str]: jinja provided field value
    :param date_format (str, optional): conversion format. Defaults to "%Y-%m-%dT%H:%M:%S".
    :return [int]: epoch value of datetime, in milliseconds
    """
    if not value:
        return value

    utc_time = strptime(value[:value.rfind('.')], date_format)
    return timegm(utc_time)*1000

def jinja_resilient_substitute(value, json_str):
    """
    jinja custom filter to replace values based on a lookup dictionary
    :param value [str]: original value
    :param json_str [str]: string encoded json lookup values
    :return [str]: replacement value or original value if no replacement found
    """
    replace_dict = loads(json_str)
    if value in replace_dict:
        return replace_dict[value]

    # Use a default value if specific match is missing
    if 'DEFAULT' in replace_dict:
        return replace_dict['DEFAULT']

    return value

def jinja_resilient_splitpart (value, index, split_chars=' - '):
    """
    Split a string and return the index
    :param value [str]: string to split
    :param index [int]: index to return
    :param split_chars (str, optional): split characters. Defaults to ' - '.
    :return [str]: index of string. if index is out of bounds, the original string is returned
    """
    splits = value.split(split_chars)
    if len(splits) > index:
        return splits[index]
    else:
        return value
