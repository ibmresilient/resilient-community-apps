# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
from calendar import timegm
from logging import getLogger
from rapidjson import loads, PM_TRAILING_COMMAS, JSONDecodeError
from re import sub, compile, findall
from os import path
from time import strptime
from resilient_circuits.template_functions import environment, render

LOG = getLogger(__name__)

DUPLICATE_COMMAS = compile(r',(\s*,)+')
LEADING_COMMAS = compile(r'\[\s*,')

SANITIZE_URL = compile(r"[\[\]\"']") # Remove square brackets and quotes

class JinjaEnvironment():
    def __init__(self):
        # Add the timestamp-parse function to the global JINJA environment
        env = environment()
        env.globals.update({
            "resilient_datetimeformat": jinja_resilient_datetimeformat,
            "soar_datetimeformat": jinja_resilient_datetimeformat,
            "resilient_substitute": jinja_resilient_substitute,
            "soar_substitute": jinja_resilient_substitute,
            "regex_sub": jinja_regex_sub,
            "sanitize_url": jinja_sanitize_url
            })
        env.filters.update({
            "resilient_datetimeformat": jinja_resilient_datetimeformat,
            "soar_datetimeformat": jinja_resilient_datetimeformat,
            "resilient_substitute": jinja_resilient_substitute,
            "soar_substitute": jinja_resilient_substitute,
            "regex_sub": jinja_regex_sub,
            "sanitize_url": jinja_sanitize_url
            })

    def make_payload_from_template(self, template_override, default_template, payload):
        """Convert a payload into a new format based on a specified template
        Args:
            template_override ([str]): /path/to/template.jinja
            default_template ([str]): /path/to/template.jinja
            payload ([dict]): Data to convert
        Returns:
            [dict]: Converted payload
        """
        template_data = self.get_template(template_override, default_template)

        # Render the template.
        rendered_payload = render_json(template_data, payload)
        LOG.debug(rendered_payload)

        return rendered_payload

    def get_template(self, specified_template, default_template):
        """Return the contents of a jinja template, either from the default or a customer specified
            custom path
        Args:
            specified_template ([str]): Customer specified template path
            default_template ([str]): Default template location
        Returns:
            [str]: Contents of template
        """
        if specified_template:
            if not (path.exists(specified_template) and path.isfile(specified_template)):
                LOG.error("Template file: %s doesn't exist, using default template",
                        specified_template)
                specified_template = None

        if not specified_template:
            # Using default template
            specified_template = path.join(
                                    path.dirname(path.realpath(__file__)),
                                    default_template)

        LOG.debug("Incident template file: %s", specified_template)
        with open(specified_template, "r") as definition:
            return definition.read()

def jinja_regex_sub(value, repl, pattern):
    """Custom filter to run the regex substitute function

    :param pattern: Pattern to execute. Can be a compiled patter or string
    :type pattern: Union[Patter, str]
    :param repl: Replacement for found characters
    :type repl: str
    :param value: String to perform substitutes
    :type value: str
    :return: Transformed string
    :rtype: str
    """
    if isinstance(pattern, str):
        return sub(pattern, repl, value)

    return pattern.sub(repl, value)

def jinja_sanitize_url(value):
    """Custom filter just for URL sanitization

    :param value: URL to sanitize
    :type value: str
    :return: Cleaned URL
    :rtype: URL
    """
    return jinja_regex_sub(value, "", SANITIZE_URL)

def jinja_resilient_datetimeformat(value, date_format="%Y-%m-%dT%H:%M:%S"):
    """Custom jinja filter to convert UTC dates to epoch format
    Args:
        value ([str]): jinja provided field value
        date_format (str, optional): Conversion format. Defaults to "%Y-%m-%dT%H:%M:%S".
    Returns:
        [int]: epoch value of datetime, in milliseconds
    """
    if not value:
        return value

    utc_time = strptime(value[:value.rfind('.')], date_format)
    return timegm(utc_time)*1000

def jinja_resilient_substitute(value, json_str):
    """jinja custom filter to replace values based on a lookup dictionary
    Args:
        value ([str]): Original value
        json_str ([str]): String encoded json lookup values
    Returns:
        [str]: Replacement value or original value if no replacement found
    """
    replace_dict = loads(json_str)
    if value in replace_dict:
        return replace_dict[value]

    # Use a default value if specific match is missing
    if 'DEFAULT' in replace_dict:
        return replace_dict['DEFAULT']

    return value

def render_json(template, data):
    """Render data into a template, producing a JSON result
       Also clean up any "really bad" control characters to avoid failure

       >>> d = {"value": "the" + chr(10) + "new" + chr(10) + "thing"}
       >>> render_json('{"result":"{{value}}"}', d)
       {'result': 'the new thing'}

       >>> d = {"value": "the" + chr(1) + "new" + chr(9) + "thing"}
       >>> render_json('{"result":"{{value}}"}', d)
       {'result': 'the new thing'}
    """
    result = render(template, data)
    for n in range(1, 32):
        result = result.replace(chr(n), " ")

    # Remove duplicate/unnecessary commas
    result = DUPLICATE_COMMAS.sub(',', result)
    result = LEADING_COMMAS.sub('[', result)

    # Continue to parse the json, attempting to look for escape characters to fix
    attempt_counter = 0
    value = {}
    while attempt_counter < 500:
        try:
            value = loads(result, parse_mode=PM_TRAILING_COMMAS)
            break # Parsing worked -> exit loop
        except JSONDecodeError as e:
            # Parse error at offset 6946: Invalid escape character in string.
            if "Invalid escape character" in str(e):
                offset = int(findall(r'offset (\d+)', str(e))[0])
                if result[offset] != '\\':
                    raise e
                # Position of unescaped '\' before that
                result = result[:offset] + r'\\' + result[offset+1:]
            else:
                LOG.error(result)
                raise e
            attempt_counter += 1
    return value
