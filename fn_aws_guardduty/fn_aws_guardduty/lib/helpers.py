# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Helpers for AWS GuardDuty """
import json
import os
import io
import re
import datetime as dt
import time
import fnmatch
import logging
from fn_aws_guardduty.util import const
from pkg_resources import resource_filename, Requirement

LOG = logging.getLogger(__name__)
PACKAGE = "fn-aws-guardduty"
PATH_TO_TEMPLATES = "fn_aws_guardduty/data/templates/"


class IQuery(dict):
    """Class to create a query for existing findings from AWS GuardDuty in Resilient.

    # Default query example:
        {"filters":[{
              "conditions":
                  [{"field_name":"plan_status", "method":"equals", "value":"A"},
                   {"field_name":"properties.aws_guardduty_finding_id", "method":"equals",
                    "value":"b8baffd3f900972453b724a4147cba6f"},
                   {"field_name":"properties.aws_guardduty_region", "method":"equals", "value":"us-west-2"}]}
          ],
          "sorts":[
            {"field_name":"create_date", "type":"desc"}
          ]
        }
    Alternate query example:
        {"filters":[{
            "conditions":
                [{"field_name":"plan_status", "method":"equals", "value":"A"},
                 {"field_name":"properties.aws_guardduty_finding_id", "method":"has_a_value"},
                 {"field_name":"properties.aws_guardduty_region", "method":"has_a_value"}]}
         ]}
        }
    """
    def __init__(self, paged=False):
        super(IQuery, self).__init__()
        # Add default condition.
        self["filters"] = [{
            "conditions": [
                {
                    "field_name": "plan_status",
                    "method": "equals",
                    "value": 'A'
                }
            ]
        }]
        # If a paged query.
        if paged:
            self["start"] = 0
            self["length"] = const.INC_PAGE_SIZE

    def add_conditions(self, gd_obj=None, fields=None):
        """
        Update query for conditions for GuardDuty finding fields.

        :param gd_obj: Object with GuardDuty properties e.g finding payload dict.
        :param fields: String or List of GuardDuty finding field name(s)
        """
        if isinstance(fields, list):
            for f in fields:
                (res_prop, path) = map_property(f)
                self["filters"][0]["conditions"].append({
                    "field_name": "properties.{}".format(res_prop),
                    "method": "equals",
                    "value": gd_obj.get(path, {}).get(f) if path else gd_obj.get(f)
                })

            self["sorts"] = [{
                "field_name": "create_date",
                "type": "desc"
            }]
        elif isinstance(fields, str):
            (res_prop, _) = map_property(fields)
            self["filters"][0]["conditions"].append({
                "field_name": "properties.{}".format(res_prop),
                "method": "equals",
                "value": gd_obj
            })

    def add_alt_conditions(self, fields=None):
        """
        Update query for alternate conditions for GuardDuty finding fields.

        :param fields: String or List of GuardDuty finding field name(s)
        """
        if isinstance(fields, list):
            for f in fields:
                (res_prop, _) = map_property(f)
                self["filters"][0]["conditions"].append({
                    "field_name": "properties.{}".format(res_prop),
                    "method": "has_a_value"
                })
        elif isinstance(fields, str):
            (res_prop, _) = map_property(fields)
            self["filters"][0]["conditions"].append({
                "field_name": "properties.{}".format(res_prop),
                "method": "has_a_value"
            })

class FCrit(dict):
    """Class to create criteria for querying findings on AWS GuardDuty.

    # Example criterion:

    """
    def __init__(self):
        super(FCrit, self).__init__()
        # Add default empty criterion.
        self["Criterion"] = {}

    def set_severity(self, severity_threshold):
        """
        Set severity criterion for GuardDuty findings.

        :param severity_threshold: GuardDuty severity threshold
        """
        self["Criterion"].update({
            'severity': {'Gte': severity_threshold}
        })

    def set_update(self, update_epoch):
        """
        Set updated criteria for GuardDuty findings.

        :param update_epoch: Epoch value in millisecs
        """
        self["Criterion"].update({
            "updatedAt": {"Gte": int(update_epoch)}
        })

    def set_archived(self, value="false"):
        """
        Set archived  filter for GuardDuty findings.

        :param value: String value should be "true" or "false"
        """
        self["Criterion"].update({
            "service.archived": {"Eq":[value]}
        })

def is_regex(regex_str):
    """"Test if sting is a correctly formed regular expression.

    :param regex_str: Regular expression string.
    :return: Boolean.
    """
    try:
        re.compile(regex_str)
        return True
    except re.error:
        return False

def get_lastrun_unix_epoch(lookback_interval):
    """
    Get Unix epoch in miliseconds since last run.

    :param lookback_interval: Interval in minutes(int) or a datetime object.
    :return: Unix epoch in miliseconds.
    """
    now = dt.datetime.now()
    if isinstance(lookback_interval, int):
        past = now - dt.timedelta(minutes=lookback_interval)
    else:
        past = lookback_interval

    return  (time.mktime(past.timetuple()) + past.microsecond / 1e6) * 1000.0

def get_data_at_path(data, path):
    """
    Get data starting at path.

     All findings data will not have the same contents. Iterate over elements
     (int or string) in a path list to determine if they match a path in the json data.
     Path elements can have Unix shell-style wildcards.
     e.g.["Service", "Action", "*Action", "LocalIpDetails"] will match data starting
     at
      {'Service': {'Action': {'NetworkConnectionAction': {'LocalIpDetails':

    :param data: Finding Json Data to search for path.
    :param path: List of path elements to key in the data.
    :return: Tuple of Boolean indicating a path match and data starting at path.
    """
    for ele in path:
        ele_match = False
        if isinstance(data, list) and isinstance(ele, int) and ele < len(data):
            data = data[ele]
            ele_match = True
        elif isinstance(data, dict) and not isinstance(ele, int):
            if not isinstance(ele, int):
                for data_ele, item in data.items():
                    # Do a Unix shell-style wildcard match
                    if fnmatch.fnmatch(data_ele, ele):
                        data = item
                        ele_match = True

        # If any elem in path doesn't exist in data exit loop.
        if not ele_match:
            break

    return(ele_match, data)

def search_json(data, key, path=None, level=0):
    """
    Search finding json recursively for key, return all matching values + list of path
     elements to key.

    :param data: Finding Json Data to search in.
    :param key: Key to search for in finding.
    :param path: List of path elements to key in the data.
    :param level: Level of recursion.
    :return: Tuple of matched values and list of path elements in json data.
    """
    values = []
    if path is None:
        path = []
    new_path = []

    if level==0 and path:
        # Running at top level and path has a value.
        ele_match = False
        (ele_match, data) = get_data_at_path(data, path)
        if not ele_match:
            return {"msg": "Path not found", "path": "{}".format(path)}

    if isinstance(data, dict):
        for k, v in data.items():
            new_path = path[:]
            if isinstance(v, (dict, list)):
                new_path.append(k)
                items = search_json(v, key, path=new_path, level=level+1)
                for item in items:
                    if isinstance(item, tuple):
                        values.append(item)
                    else:
                        values.append((item, new_path))
            elif k == key:
                if new_path:
                    values.append((v, new_path))
                else:
                    # Empty 'new_path' so top level property add at beginning of list.
                    values[:0] = [(v, new_path)]
    elif isinstance(data, list):
        new_path = path[:]
        for i, item_outer in enumerate(data):
            new_path.append(i)
            items = search_json(item_outer, key, path=new_path, level=level+1)
            for item in items:
                if isinstance(item, tuple):
                    values.append(item)
                else:
                    values.append((item, new_path))
    return values

def map_property(gd_prop):
    """
    Map GuardDuty property field to corresponding Resilient value.
    Return a path variable if GuardDuty property not at top-level

    :param gd_prop: GuardDuty property value.
    :return : Tuple of Resilient property value and path
    """
    path = None
    res_prop = None
    try:
        prop = const.CUSTOM_FIELDS_MAP[gd_prop]
        if isinstance(const.CUSTOM_FIELDS_MAP[gd_prop], dict):
            # Get the Resilient incident property value.
            res_prop = list(prop.keys())[0]
            # Get path to property in finding json
            path = list(prop.values())[0]["path"]
        else:
            res_prop = prop
    except KeyError:
        raise KeyError("Unsupported finding property: {}.".format(gd_prop))

    return (res_prop, path)


def load_template(filename, override_template_file=None):
    """ Load contents of template file return as json.

    :param filename: Template file.
    :param override_template_file: Options user defined template path.
    :return : Return contents of file as json.
    """
    file_contents = None
    template_file = None
    override_file_exists = False

    if override_template_file:
        # Check user defined template file exists.
        if os.path.exists(override_template_file):
            override_file_exists = True
            template_file = override_template_file
            LOG.debug("Using user defined template file %s", override_template_file)

    if not override_file_exists:
        # Use the default template file.
        template_file = resource_filename(Requirement(PACKAGE),
                                          PATH_TO_TEMPLATES + filename)
        if not os.path.exists(template_file):
            raise Exception("Template file '{}' not found".format(template_file))

        LOG.debug("Using package defined template file %s", template_file)

    LOG.debug("Attempting to use template file %s", template_file)

    with io.open(template_file, mode="rt", encoding="utf-8") as load_file:
        file_contents = json.load(load_file)

    return file_contents
