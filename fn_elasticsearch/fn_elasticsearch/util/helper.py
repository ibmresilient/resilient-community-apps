# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use


class ElasticSearchHelper():

    def get_config_option(self, option_name, optional=False):
        """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
        option = self.options.get(option_name)

        if option is None and optional is False:
            err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(
                option_name)
            raise ValueError(err)
        else:
            return option

    def get_function_input(self, inputs, input_name, optional=False):
        """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
        input = inputs.get(input_name)

        if input is None and optional is False:
            err = "'{0}' is a mandatory function input".format(input_name)
            raise ValueError(err)
        else:
            return input

    def __init__(self, options):
        self.options = options
