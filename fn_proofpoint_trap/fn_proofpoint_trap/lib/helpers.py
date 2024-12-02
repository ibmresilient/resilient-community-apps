# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

""" Helper functions for Resilient circuits Functions supporting ProofPoint TRAP """

from resilient_circuits.actions_component import ResilientComponent

CONFIG_DATA_SECTION = "fn_proofpoint_trap"

MANDATORY_CONFIG_PARAMS = [
    "base_url",
    "api_key",
    "polling_interval",
    "startup_interval",
    "state",
    "host_categories"
]

def transform_kwargs(kwargs):
    """"Update kwargs dictionary.
    This function will perform following actions:
        - Copy kwargs to a new 'params' dict which will be used to call the apis.
        - Strip whitespaces from beginning and end of parametrs in 'kwargs' and 'params' taking into
          account lists or dicts.
        - Remove "trap_" from beginning of parameters in 'params'.
        - Convert any case insensitive "None" values to None in 'params'.
    :param kwargs: Dictionary of Resilient Function parameters.

     """
    params = {}

    # Remove  "sep_" from the kwargs key names.
    for (key, value) in kwargs.copy().items():
        value = kwargs.pop(key)

        if isinstance(key, list):
            key = [ResilientComponent.get_select_param(val) for val in value]
        elif isinstance(value, dict):
            value = value.get("name")
        kwargs[key] = value.rstrip().lstrip() if isinstance(value, str)  else value
        params[key.split('_', 1)[1]] = value.rstrip().lstrip() if isinstance(value, str) \
                                                                and value.lower().startswith("trap_") else value

    # If any entry has "None" string change to None value for params.
    for key, value in params.items():
        if isinstance(value, str) and value.lower() == 'none':
            params[key] = None

    return params

def validate_opts(func):
    """"Check options set correctly.

    :param func: Resilient Function instance reference

     """
    for param in MANDATORY_CONFIG_PARAMS:
        param_value = func.options.get(param, None)

        if param_value is None:
            raise Exception("Mandatory config setting '{}' not set.".format(param))
        if not param_value:
            raise ValueError("Invalid value for config setting '{}'.".format(param))
