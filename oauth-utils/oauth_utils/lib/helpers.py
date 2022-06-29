# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Helper functions for the Outbound email app"""
import configparser
import argparse
import os
import sys
from six import string_types

if sys.version_info[0] == 3:
    from urllib.parse import urlencode
else:
    from urllib import urlencode

DEFAULT_CONFIG_FILENAME = "app.config"


def get_config_file(filename=None):
    """
    Helper: get the location of the configuration file
    * Use the location specified in $APP_CONFIG_FILE, if set
    * Otherwise if filename path specified in args exist in the current working use as config file.
    * Otherwise if default config file name exists in current work directory use as config file.
    * Otherwise use path in ~/.resilient/ directory

    :param filename: The filename to use for the app config file.
    """
    # The config file location should usually be set in the environment
    # First check environment, then cwd, then ~/.resilient/app.config
    env_app_config_file = os.environ.get("APP_CONFIG_FILE", None)

    if not env_app_config_file:
        if not filename:
            # If file not specified use default value.
            filename = DEFAULT_CONFIG_FILENAME
        # If the filename exists in local directory use as config file name.
        if os.path.exists(filename):
            config_file = filename
        else:
            # Use default config file in ~/.resilient/app.config.
            config_file = os.path.expanduser(os.path.join("~", ".resilient", filename))

    else:
        config_file = env_app_config_file

    if not os.path.isfile(config_file):
        print("ERROR: The app.config file {} does not exist.".format(config_file))
        os._exit(0)

    return config_file

def set_configs(script_args):
    """
    Set the config values in a dict if using discrete arguments instead of an
    app.config.

    :param script_args: Parsed cli parameters.
    :return: dictionary of all the configs.
    """
    script_args.scope, script_args.client_id, script_args.client_secret,
    script_args.token_url, script_args.auth_url
    opts = {
        "scope": script_args.scope,
        "client_id": script_args.client_id,
        "client_secret": script_args.client_secret,
        "token_url": script_args.token_url,
        "auth_url": script_args.auth_url
    }
    return opts

def get_configs(path_config_file=None, app_name=None):
    """
    Gets all the configs that are defined in the app.config file
    Uses the path to the config file from the parameter
    Or uses the `get_config_file()` method in resilient if None

    :param path_config_file: path to the app.config to parse
    :return: dictionary of all the configs in the app.config file
    """
    opts = {}
    a_name = app_name
    a_count = 0
    if not path_config_file:
        path_config_file = get_config_file()

    config = configparser.ConfigParser()
    config.read(path_config_file)

    if config:
        for section in config.sections():
            if section.startswith("fn_") and a_name is None:
                app_name = section
                if a_count:
                    print("\nThere is more that one SOAR app defined in the app.config file")
                    print("Please use the [-a|--app_name] option to select the SOAR app.\n")
                    os._exit(0)
                else:
                    a_count += 1
            items = dict((item.lower(), config.get(section, item)) for item in config.options(section))
            opts.update({section: items})

    if app_name is None:
        raise ValueError("There is no function defined in app.config.")

    return opts[app_name]

def validate_fields(field_list, kwargs):
    """
    Ensure each mandatory field in ``field_list`` is present in ``kwargs``.
    Throw ValueError if not.

    ``field_list`` can be a list/tuple of ``strings``

    ``kwargs`` can be a dict.

    :param field_list: List of the mandatory fields.
    :param kwargs: A dict of all the fields to search.
    :raises ValueError: if a field is missing

    """

    mandatory_fields = field_list
    provided_fields = kwargs
    mandatory_err_msg = "'{0}' is mandatory and is not set. You must set this value to run this function"

    if not isinstance(mandatory_fields, list):
        raise ValueError("'field_list' must be of type list, not {0}".format(type(mandatory_fields)))

    if not isinstance(provided_fields, dict):
        try:
            provided_fields = provided_fields._asdict()
        except AttributeError:
            raise ValueError("'kwargs' must be of type dict or namedtuple, not {0}".format(type(provided_fields)))

    # Validate that mandatory fields exist + are not  blank
    for field in mandatory_fields:
        # If the field value is a defined empty str, raise an error
        if isinstance(provided_fields.get(field), string_types):
            if not provided_fields.get(field):
                raise ValueError(mandatory_err_msg.format(field))

        if provided_fields.get(field) is None:
            raise ValueError(mandatory_err_msg.format(field))
