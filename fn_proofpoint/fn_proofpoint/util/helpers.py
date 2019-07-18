# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
"""Helper functions"""


def get_config_option(options, option_name, optional=False):
    """Given option_name, check and return it if it is in appconfig.
       Raises ValueError if it is missing and mandatory
    """
    option = options.get(option_name)

    if not option and not optional:
        raise ValueError('"{0}" is mandatory and is not set in the app.config file'.format(option_name))

    return option
