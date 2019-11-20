# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

""" Helper functions for Resilient circuits Functions supporting Symantec SEP """
from __future__ import print_function
import logging
import sys
import datetime
import tempfile
from resilient_circuits.actions_component import ResilientComponent

LOG = logging.getLogger(__name__)
CONFIG_DATA_SECTION = "fn_aws_iam"
PARAM_PREFIX = CONFIG_DATA_SECTION.split('_', 1)[1]+'_'

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
    # Pattern to strip from beginning of parameter e.g. 'aws_iam_'.
    pattern = PARAM_PREFIX+'_'

    # Remove  "aws_iam_" from the kwargs key names.
    for (k, v) in kwargs.copy().items():
        v = kwargs.pop(k)

        if isinstance(k, list):
            k = [ResilientComponent.get_select_param(val) for val in v]
        elif isinstance(v, dict):
            v = v.get("name")
        kwargs[k] = v.rstrip().lstrip() if isinstance(v, str) else v
        params[snake_to_pascal(k.rsplit(PARAM_PREFIX,1)[1])] = v.rstrip().lstrip() if isinstance(v, str) \
                                                                and k.lower().startswith(PARAM_PREFIX) else v

    # If any entry has "None" string change to None value for params.
    for k, v in params.items():
        if isinstance(v, str) and v.lower() == 'none':
            params[k] = None

    return params

def snake_to_pascal(param):
    """
    Convert a paramater name from snake_case to PascalCase as used for AWS IAM api parameters.

    :param word: Dictionary of Resilient Function parameters.
    :return: Converted  string.

    """
    return ''.join(x.capitalize() or '_' for x in param.split('_'))