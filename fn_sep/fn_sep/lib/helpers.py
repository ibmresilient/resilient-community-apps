# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

""" Helper functions for Resilient circuits Functions supporting Symantec SEP """

from __future__ import print_function
import logging
import re
from textwrap import dedent

from resilient_circuits.actions_component import ResilientComponent

LOG = logging.getLogger(__name__)


def transform_kwargs(kwargs):
    """"Update kwargs dictionary.

    :param kwargs: Dictionary of Resilient Function parameters.

     """
    params = {}

    # Remove  "sep_" from the kwargs key names.
    for (k, v) in kwargs.copy().items():
            v = kwargs.pop(k)

            if isinstance(k, list):
                k =  [ResilientComponent.get_select_param(val) for val in v]
            elif isinstance(v, dict):
                v =  v.get("name")
            kwargs[k] = v.rstrip().lstrip() if isinstance(v, str)  else v
            params[re.split('_', k, 1)[1]] = v.rstrip().lstrip() if isinstance(v, str)  else v

    # If any entry has "None" string change to None value.
    for k, v in kwargs.items():
        if type(v) == str and v.lower() == 'none':
            params[k] = None

    return params