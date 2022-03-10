# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""Template processing"""

# Jinja template functions

from __future__ import print_function
import calendar
import datetime
import jinja2
import json
import logging
import os
import pprint
import pytz
import random
import re
import sys
import time
from resilient_lib import readable_datetime

if sys.version_info.major < 3:
    from cgi import escape as html_escape
else:
    # Python 3.2 adds html.escape() and deprecates cgi.escape().
    from html import escape as html_escape

if sys.version_info.major < 3:
    from base64 import encodestring as b64encode
else:
    # Python 3.x
    from base64 import encodebytes as b64encode

if sys.version_info.major < 3:
    from urllib import quote
else:
    # Python 3.x
    from urllib.parse import quote

LOG = logging.getLogger(__name__)

def render(template, data):
    """Render data into a template, producing a string result. All the additional custom filters are available

        Inputs:
            template [str or dict]: Jinja template to use
            data [dict]: JSON data to apply to the template

        Returns:
            [str] - result from the rendering of the template
                    The template is usually a string, but can be a dict.
    """

    """
        >>> render("template {{value}}", {"value":"123"})
        u'template 123'

        >>> render({"template": "{{value}}"}, {"value":"123"})
        u'{"template": "123"}'

        You can escape values using the 'json' filter,
        or the 'url' or 'html' or 'ldap' filters.

        >>> render('{"template": {{value|json}} }', {"value":'1"23'})
        u'{"template": "1\\\\"23" }'

        >>> render('{"template": "{{value|js}}" }', {"value":'1"23'})
        u'{"template": "1\\\\"23" }'

        >>> render('{"template": {{value|ldap}} }', {"value":'1*23'})
        u'{"template": 1\\\\2a23 }'

        >>> render('shell "{{value|ps}}"', {"value":'$"foo"'})
        u'shell "`$`"foo`""'

        >>> render('shell "{{value|sh}}"', {"value":'$"foo"'})
        u'shell "\\\\$\\\\"foo\\\\""'

        >>> render('template={{value|timestamp}}', {"value":0})
        u'template=0'

        >>> render('template={{value|timestamp}}', {})
        u'template=null'

        >>> render('template={{value|timestamp}}', {"value":{"year":2015, "month":7, "day":15}})
        u'template=1436918400000'

        >>> render('template={{value|timestamp}}', {"value":datetime.datetime(2015, 7, 15)})
        u'template=1436918400000'

        >>> d = json.loads('{"attributes": \
                {"cn": ["Albert Einstein"], "createTimestamp": "2014-02-21 16:51:33+00:00", \
                 "creatorsName": "cn=admin,dc=example,dc=com", \
                 "entryCSN": ["20150720185447.990131Z#000000#000#000000"], \
                 "entryDN": "uid=einstein,dc=example,dc=com", \
                 "entryUUID": "29f6dc28-2f64-1033-898b-a53eb149a944", \
                 "hasSubordinates": false, \
                 "mail": ["einstein@ldap.forumsys.com"], \
                 "modifiersName": "cn=admin,dc=example,dc=com", \
                 "modifyTimestamp": "2015-07-20 18:54:47+00:00", \
                 "objectClass": ["inetOrgPerson", "organizationalPerson", "person", "top"], \
                 "sn": ["Einstein"], \
                 "structuralObjectClass": "inetOrgPerson", \
                 "subschemaSubentry": "cn=Subschema", \
                 "telephoneNumber": ["314-159-2653"], \
                 "uid": ["einstein"]}, \
                "dn": "uid=einstein,dc=example,dc=com"}')
        >>> render('{"description": "DN={{dn}}, mail={{attributes.mail[0]}}"}',d)
        u'{"description": "DN=uid=einstein,dc=example,dc=com, mail=einstein@ldap.forumsys.com"}'
    """

    stringtemplate = template
    if isinstance(template, dict):
        stringtemplate = json.dumps(template, sort_keys=True)

    try:
        jtemplate = environment().from_string(stringtemplate)
    except jinja2.exceptions.TemplateSyntaxError as err:
        LOG.error("Render failed: %s, with template: %s", str(err), stringtemplate)
        raise

    try:
        stringvalue = jtemplate.render(data)
    except jinja2.exceptions.TemplateError as Ex:
        LOG.error("Render failed, with data: %s", data)
        raise
    return stringvalue

def render_json(template, data):
    """Render data into a template, producing a JSON result
       Also clean up any "really bad" control characters to avoid failure.

        Args:
            template [str or dict]: Jinja template to use
            data [dict]: JSON data to apply to the template

        Returns:
            [dict] - JSON entresult from the rendering of the template
    """

    """
       >>> d = {"value": "the" + chr(10) + "new" + chr(10) + "thing"}
       >>> render_json('{"result":"{{value}}"}', d)
       {u'result': u'the new thing'}

       >>> d = {"value": "the" + chr(1) + "new" + chr(9) + "thing"}
       >>> render_json('{"result":"{{value}}"}', d)
       {u'result': u'the new thing'}
    """
    result = render(template, data)
    result = _remove_ctl_chars(result)
    return _convert_to_json(result)

def _remove_ctl_chars(result):
    # Replace any control characters with spaces
    for n in range(1, 32):
        result = result.replace(chr(n), " ")
    return result

def _convert_to_json(result):
    try:
        return json.loads(result)
    except:
        LOG.error("invalid json result: %s", result)
        raise

def make_payload_from_template(template_override, default_template, payload, return_json=True):
    """Convert a payload into a newformat based on a specified template

    Args:
        template_override ([str]): [/path/to/customer/supplied/template.jinja]
        default_template ([str]): [/path/to/template.jinja]
        payload ([dict]): [data to convert]
        return_json ([bool]): [True if results should be returned as JSON]

    Returns:
        [dict/str]: [result of rendered template]
    """
    template_data = _get_template(template_override, default_template)

    # Render the template.
    if return_json:
        rendered_payload = render_json(template_data, payload)
    else:
        rendered_payload = render(template_data, payload)
        rendered_payload = _remove_ctl_chars(rendered_payload)
    LOG.debug(rendered_payload)

    return rendered_payload

def _get_template(specified_template, default_template):
    """Return the contents of a jinja template, either from the default location or from a customer specified
        custom path

    Args:
        specified_template ([str]): [customer specified template path]
        default_template ([str]): [default template path]

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

    LOG.debug(u"template file used: %s", template_file_path)
    with open(template_file_path, "r", encoding='utf-8') as definition:
        return definition.read()

# C U S T O M   J I N J A   F I L T E R S
def soar_datetimeformat(value, date_format="%Y-%m-%dT%H:%M:%S", split_at=None):
    """Custom jinja filter to convert UTC dates to epoch format

    Args:
        value ([str]): [jinja provided field value]
        date_format (str, optional): [conversion format]. Defaults to "%Y-%m-%dT%H:%M:%S".
        split_at (str, optional): [character to split the date field to scope the date field.]
            examples: split_at='.' to remove milliseconds for "2021-10-22T20:53:53.913Z",
                      split_at='+' tp remove tz information "2021-10-22T20:53:53+00:00",
    Returns:
        [int]: [epoch value of datetime, in milliseconds]
    """
    if not value:
        return value

    if split_at:
        utc_time = time.strptime(value[:value.rfind(split_at)], date_format)
    else:
        utc_time = time.strptime(value, date_format)
    return calendar.timegm(utc_time)*1000

def soar_substitute(value, json_str):
    """Jinja custom filter to replace values based on a lookup dictionary

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

def soar_splitpart(value, index, split_chars=' - '):
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

def soar_trimlist(org_list):
    """[trim whitespace from elements in a list]

    Args:
        list ([type]): [description]
    Returns:
        [list]: [list with elements trimmed of whitespace]
    """
    if not isinstance(org_list, list):
        return org_list
    return [element.strip() for element in org_list]

def js_filter(val):
    """Jinja2 filter function 'js' produces JSONified string of the value, without surrounding quotes"""
    if val is None or isinstance(val, jinja2.Undefined):
        return "null"
    js = json_filter(val)
    return js[1:-1]

def json_filter(val, indent=0):
    """Jinja2 filter function 'json' produces JSONified string of the value"""
    if val is None or isinstance(val, jinja2.Undefined):
        return "null"
    return json.dumps(val, indent=indent, sort_keys=True)

def html_filter(val):
    """Jinja2 filter function 'html' produces HTML-encoded string of the value"""
    if isinstance(val, jinja2.Undefined):
        return "[undefined]"
    return html_escape(val)

def url_filter(val):
    """Jinja2 filter function 'url' produces URL-encoded string of the value"""
    if isinstance(val, jinja2.Undefined):
        return "[undefined]"
    return quote(str(val))

def idna_filter(val):
    """Jinja2 filter function 'idna' encodes the value per RFC 3490"""
    if isinstance(val, jinja2.Undefined):
        return "[undefined]"
    return val.encode("idna").decode("utf-8")

def punycode_filter(val):
    """Jinja2 filter function 'punycode' encodes the value per RFC 3492"""
    if isinstance(val, jinja2.Undefined):
        return "[undefined]"
    return val.encode("punycode").decode("utf-8")

def ldap_filter(val):
    """Jinja2 filter function 'ldap' produces LDAP-encoded string of the value"""
    if isinstance(val, jinja2.Undefined):
        return "[undefined]"
    escaped = []
    for char in str(val):
        if char < '0' or char > 'z' or char in "\\*()":
            char = "\\%02x" % ord(char)
        escaped.append(char)
    return ''.join(escaped)

def ps_filter(val):
    """Jinja2 filter function 'ps' escapes for use in a PowerShell commandline"""
    if isinstance(val, jinja2.Undefined):
        return "[undefined]"
    escaped = []
    for char in str(val):
        if char in "`$#'\"":
            char = "`" + char
        elif char == '\0':
            char = "`0"
        elif char == '\a':
            char = "`a"
        elif char == '\b':
            char = "`b"
        elif char == '\f':
            char = "`f"
        elif char == '\n':
            char = "`n"
        elif char == '\r':
            char = "`r"
        elif char == '\t':
            char = "`t"
        elif char == '\v':
            char = "`v"
        escaped.append(char)
    return ''.join(escaped)

def sh_filter(val):
    """Jinja2 filter function 'sh' escapes for use in a Unix shell commandline"""
    if isinstance(val, jinja2.Undefined):
        return "[undefined]"
    escaped = []
    for char in str(val):
        if char in "$#\"":
            char = "\\" + char
        elif ord(char) < 32 or ord(char) > 126:
            char = "\\%03o" % ord(char)
        escaped.append(char)
    return ''.join(escaped)

def pretty_filter(val, indent=2):
    """Jinja2 filter function 'pretty' produces pretty-printed string of the value"""
    if isinstance(val, jinja2.Undefined):
        return "[undefined]"

    def nice_repr(obj, context, maxlevels, level):
        if sys.version_info.major < 3:
            typ = type(obj)
            if typ is unicode:
                obj = obj.encode("utf-8")
        return pprint._safe_repr(obj, context, maxlevels, level)

    printer = pprint.PrettyPrinter(indent=indent)
    printer.format = nice_repr
    return printer.pformat(val)

def iso8601(val):
    """Assuming val is an epoch milliseconds timestamp, produce ISO8601 datetime"""
    dt = datetime.datetime.utcfromtimestamp(int(int(val)/1000))
    return pytz.UTC.localize(dt).isoformat()

def timestamp(val):
    """Try convert non-timestamp values to a timestamp

       >>> timestamp({"year": 2018, "month": 8, "day": 1, "timezoneID": "CET"})
       1533078000000

       >>> timestamp(jinja2.Undefined())
       'null'

       >>> timestamp("now") > 1530000000000
       True

       >>> timestamp("now") > 2000000000000 # 2033
       False
    """
    if isinstance(val, dict):
        y = val.get("year", 1970)
        m = val.get("month", 1)
        d = val.get("day", 1)
        h = val.get("hour", 0)
        n = val.get("minute", 0)
        s = val.get("second", 0)
        u = val.get("milliSecond", 0)
        z = pytz.timezone(val.get("timezoneID", "UTC"))
        dt = datetime.datetime(y, m, d, h, n, s, u, z)
        return int(calendar.timegm(dt.utctimetuple()) * 1000)
    if isinstance(val, jinja2.Undefined):
        return "null"
    if isinstance(val, datetime.datetime):
        return int(calendar.timegm(val.utctimetuple()) * 1000)
    if val == "now":
        return int(calendar.timegm(datetime.datetime.now().utctimetuple()) * 1000)
    return val

def uniq(val, key=None):
    """Produce the unique list.  If val is a dict, produce unique of key values.

       >>> sorted(uniq([1,2,3,2]))
       [1, 2, 3]

       >>> sorted(uniq([ {"a":1}, {"a":2}, {"a":3}, {"a":2}]))
       [{'a': 1}, {'a': 2}, {'a': 3}]

       >>> sorted(uniq([ {"a":1}, {"a":2}, {"a":3}, {"a":2}, Exception()], "a"))
       [{'a': 1}, {'a': 2}, {'a': 3}, Exception()]
    """
    if not isinstance(val, list):
        return val
    if key is None:
        try:
            return list(set(val))
        except TypeError:
            pass
    keys = []
    values = []
    for value in val:
        try:
            thiskey = value[key]
        except:
            thiskey = repr(value)
        if thiskey not in keys:
            keys.append(thiskey)
            values.append(value)
    return values

def sample_filter(val, count=None):
    """Return a random sample from a list"""
    if count is None:
        # Return a single value
        try:
            return random.sample(list(val), 1)[0]
        except ValueError:
            return None
    else:
        # Return a list
        try:
            return random.sample(list(val), count)
        except ValueError:
            return []

def camel_filter(val):
    """Return CamelCase

       >>> camel_filter("a#bc_def")
       'ABcDef'
    """
    titlecase = val.title()
    return re.sub(r"[\W^_]", "", titlecase)

def base64_filter(val, indent=2):
    """Jinja2 filter function 'base64' breaks text into fixed-width blocks"""
    if isinstance(val, jinja2.Undefined):
        return ""
    s = json.dumps(val).encode("utf-8")
    return b64encode(s).decode("utf-8")


JINJA_FILTERS = {
    "json": json_filter,
    "js": js_filter,
    "html": html_filter,
    "url": url_filter,
    "idna": idna_filter,
    "punycode": punycode_filter,
    "ldap": ldap_filter,
    "ps": ps_filter,
    "sh": sh_filter,
    "pretty": pretty_filter,
    "timestamp": timestamp,
    "iso8601": iso8601,
    "uniq": uniq,
    "sample": sample_filter,
    "camel": camel_filter,
    "base64": base64_filter,
    "soar_datetimeformat": soar_datetimeformat,
    "soar_display_datetimeformat": readable_datetime,
    "soar_substitute": soar_substitute,
    "soar_splitpart": soar_splitpart,
    "soar_trimlist": soar_trimlist
}

# Maintain one global Environment
_ENV = jinja2.Environment(autoescape=jinja2.select_autoescape(default_for_string=False))
_ENV.globals.update(JINJA_FILTERS)
_ENV.filters.update(JINJA_FILTERS)

def environment():
    """ Return the jinja environment. This environment can be expanded upon to add additional custom filters:
        Ex:
            addl_custom_filters = {
                "filter_name": method_name
            }
            env = environment()
            env.globals.update(addl_custom_filters)
            env.filters.update(addl_custom_filters)

    """
    return _ENV
