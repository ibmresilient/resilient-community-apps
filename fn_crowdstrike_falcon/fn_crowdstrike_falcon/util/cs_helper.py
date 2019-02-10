# (c) Copyright IBM Corp. 2019. All Rights Reserved.
"""CrowdStrikeHelper Module"""

import logging
import datetime


class CrowdStrikeHelper(object):
    """A helper class for fn_crowdstrike_falcon"""

    app_config_section = "fn_crowdstrike_falcon"
    class_vars_loaded = False
    oauth2_base_url, oauth2_cid, oauth2_key, bauth_base_url, bauth_api_uuid, bauth_api_key, request_timeout, ping_delay = None, None, None, None, None, None, None, None
    json_header = {"Content-Type": "application/json"}

    def __init__(self, app_configs):

        log = logging.getLogger(__name__)
        log.debug("Initializing CrowdStrikeHelper")

        if not self.class_vars_loaded:
            self.load_class_variables(app_configs)

        log.debug("CrowdStrikeHelper initialized")

    @classmethod
    def load_class_variables(cls, app_configs):
        """Loads class variables from app.config file"""
        log = logging.getLogger(__name__)
        log.debug("Setting static class variables from app.configs")
        cls.oauth2_base_url = cls.__get_config_option(app_configs, "cs_falcon_oauth2_base_url")
        cls.oauth2_cid = cls.__get_config_option(app_configs, "cs_falcon_oauth2_cid")
        cls.oauth2_key = cls.__get_config_option(app_configs, "cs_falcon_oauth2_key")
        cls.bauth_base_url = cls.__get_config_option(app_configs, "cs_falcon_bauth_base_url")
        cls.bauth_api_uuid = cls.__get_config_option(app_configs, "cs_falcon_bauth_api_uuid")
        cls.bauth_api_key = cls.__get_config_option(app_configs, "cs_falcon_bauth_api_key")
        cls.request_timeout = cls.__get_config_option(app_configs, "cs_falcon_request_timeout")
        cls.ping_delay = cls.__get_config_option(app_configs, "cs_falcon_ping_delay")
        cls.class_vars_set = True

    @staticmethod
    def __get_config_option(app_configs, option_name, optional=False, placeholder=None):
        """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
        option = app_configs.get(option_name)
        err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(option_name)

        if not option and optional is False:
            raise ValueError(err)
        elif optional is False and placeholder is not None and option == placeholder:
            raise ValueError(err)
        else:
            return option

    @staticmethod
    def get_function_input(inputs, input_name, optional=False):
        """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""

        log = logging.getLogger(__name__)
        log.debug("Trying to get function input: %s from %s. optional = %s", input_name, inputs, optional)

        the_input = inputs.get(input_name)

        if the_input is None and optional is False:
            err = "'{0}' is a mandatory function input".format(input_name)
            raise ValueError(err)
        else:
            log.debug("Got function input: %s", input_name)
            return the_input

    @staticmethod
    def timestamp_to_ms_epoch(str_timestamp, timestamp_format="%Y-%m-%dT%H:%M:%SZ"):
        """Converts a String Timestamp to an int in milliseconds since 1970 epoch, a format that
        Resilient DateTime field type accepts"""

        epoch = datetime.datetime(1970, 1, 1)
        utc_time = datetime.datetime.strptime(str_timestamp, timestamp_format)
        return int((utc_time - epoch).total_seconds() * 1000.0)
