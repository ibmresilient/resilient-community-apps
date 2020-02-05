# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Helper functions for Resilient circuits Functions supporting Symantec SEP """
from __future__ import print_function
import logging
import re
from resilient_circuits.actions_component import ResilientComponent

LOG = logging.getLogger(__name__)
CONFIG_DATA_SECTION = "fn_aws_iam"
PARAM_PREFIX = CONFIG_DATA_SECTION.split('_', 1)[1]+'_'
MANDATORY_CONFIG_PARAMS = ["aws_iam_access_key_id", "aws_iam_secret_access_key"]

def transform_kwargs(kwargs):
    """"Update kwargs dictionary.
    This function will perform following actions:
        - Copy kwargs to a new 'params' dict which will be used to call the apis.
        - Strip whitespaces from beginning and end of parameters in 'kwargs' and 'params' taking into
          account lists or dicts.
        - Remove common prefix 'aws_iam_' from beginning of keys in 'params'.
        - Convert keys in 'params' to "PascalCase" as used for AWS IAM api parameters.
        - Convert any case insensitive "None" values to None in 'params'.

    :param kwargs: Dictionary of Resilient Function parameters.
    :param patt: Pattern to remove from beginning of parameters in 'params'.
    """
    params = {}
    for (key, val) in kwargs.copy().items():
        val = kwargs.pop(key)

        if isinstance(key, list):
            key = [ResilientComponent.get_select_param(val) for val in val]
        elif isinstance(val, dict):
            val = val.get("name")
        kwargs[key] = val.rstrip().lstrip() if isinstance(val, str) else val
        params[snake_to_pascal(key.rsplit(PARAM_PREFIX, 1)[1])] = val.rstrip().lstrip() \
            if isinstance(val, str) and key.lower().startswith(PARAM_PREFIX) else val

    # If any entry has "None" string change to None value for params.
    for key, val in params.items():
        if isinstance(val, str) and val.lower() == 'none':
            params[key] = None

    return params

def snake_to_pascal(param):
    """ Convert a parameter name from snake_case to PascalCase as used for AWS IAM api parameters.

    :param word: Dictionary of Resilient Function parameters.
    :return: Converted  string.
    """
    return ''.join(x.capitalize() or '_' for x in param.split('_'))

def validate_opts(func):
    """"Check options set correctly.
    Checks that the parameters are set and that they aren't set to an empty value.

    :param func: Resilient Function instance reference
    """
    for param in MANDATORY_CONFIG_PARAMS:
        param_value = func.options.get(param, None)
        LOG.info(param_value)
        if param_value is None:
            raise Exception("Mandatory config setting '{}' not set.".format(param))
        if param_value in ('', "\'\'"):
            raise ValueError("Invalid value for config setting '{}'.".format(param))


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