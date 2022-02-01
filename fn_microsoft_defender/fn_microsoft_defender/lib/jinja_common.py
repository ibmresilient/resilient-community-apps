# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
import calendar
import logging
import rapidjson
import re
import os
import time
from resilient_circuits.template_functions import environment, render

LOG = logging.getLogger(__name__)

DUPLICATE_COMMAS = re.compile(r',\s*,')
class JinjaEnvironment():
    def __init__(self):
        # Add the timestamp-parse function to the global JINJA environment
        env = environment()
        env.globals.update({
            "resilient_datetimeformat": jinja_resilient_datetimeformat,
            "resilient_substitute": jinja_resilient_substitute
            })
        env.filters.update({
            "resilient_datetimeformat": jinja_resilient_datetimeformat,
            "resilient_substitute": jinja_resilient_substitute
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
        rendered_payload = render_json(template_data, payload)
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

def jinja_resilient_datetimeformat(value, date_format="%Y-%m-%dT%H:%M:%S"):
    """custom jinja filter to convert UTC dates to epoch format
    Args:
        value ([str]): [jinja provided field value]
        date_format (str, optional): [conversion format]. Defaults to "%Y-%m-%dT%H:%M:%S".
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
    replace_dict = rapidjson.loads(json_str)
    if value in replace_dict:
        return replace_dict[value]

    # use a default value if specific match is missing
    if 'DEFAULT' in replace_dict:
        return replace_dict['DEFAULT']

    return value

def render_json(template, data):
    """Render data into a template, producing a JSON result
       Also clean up any "really bad" control characters to avoid failure.

       >>> d = {"value": "the" + chr(10) + "new" + chr(10) + "thing"}
       >>> render_json('{"result":"{{value}}"}', d)
       {u'result': u'the new thing'}

       >>> d = {"value": "the" + chr(1) + "new" + chr(9) + "thing"}
       >>> render_json('{"result":"{{value}}"}', d)
       {u'result': u'the new thing'}
    """
    result = render(template, data)
    for n in range(1, 32):
        result = result.replace(chr(n), " ")

    # remove duplicate commas
    result = DUPLICATE_COMMAS.sub(',', result)

    # continue to parse the json, attempting to look for escape characters to fix
    attempt_counter = 0
    value = {}
    while attempt_counter < 500:
        try:
            value = rapidjson.loads(result, parse_mode=rapidjson.PM_TRAILING_COMMAS)
            break                    # parsing worked -> exit loop
        except rapidjson.JSONDecodeError as e:
            # Parse error at offset 6946: Invalid escape character in string.
            if "Invalid escape character" in str(e):
                offset = int(re.findall(r'offset (\d+)', str(e))[0])
                if result[offset] != '\\':
                    raise e
                # position of unescaped '\' before that
                result = result[:offset] + r'\\' + result[offset+1:]
            else:
                raise e
            attempt_counter += 1
    return value
