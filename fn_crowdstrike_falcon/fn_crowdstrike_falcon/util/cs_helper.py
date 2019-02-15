# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""CrowdStrikeHelper Module"""

import logging
import datetime
import time
import requests


class CrowdStrikeHelper(object):
    """A helper class for fn_crowdstrike_falcon"""

    app_config_section = "fn_crowdstrike_falcon"
    class_vars_loaded = False
    oauth2_base_url, oauth2_cid, oauth2_key, oauth2_token, bauth_base_url, bauth_api_uuid, bauth_api_key, request_timeout, ping_delay = None, None, None, None, None, None, None, None, None
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
        cls.ping_delay = cls.__get_config_option(app_configs, "cs_falcon_ping_delay", True)
        cls.ping_timeout = cls.__get_config_option(app_configs, "cs_falcon_ping_timeout", True)

        # Set defaults ping_delay=5s and ping_timeout=120s
        if not cls.ping_delay:
            cls.ping_delay = 5
        else:
            cls.ping_delay = int(cls.ping_delay)

        if not cls.ping_timeout:
            cls.ping_timeout = 120
        else:
            cls.ping_timeout = int(cls.ping_timeout)

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

    @staticmethod
    def is_workflow_terminated(workflow_instance_id, res_client):
        """Function to check if the current workflow has been terminated via the UI"""
        resp = res_client.get("/workflow_instances/{0}".format(workflow_instance_id))
        wf_status = resp.get("status")
        return True if wf_status == "terminated" else False

    @classmethod
    def should_timeout(cls, start_time):
        """Return if the time running is longer than the timeout"""
        return (time.time() - start_time) > cls.ping_timeout

    @classmethod
    def get_device_status(cls, device_id):
        """Wait for x seconds then get and return the status of the device in CrowdStrike

        :param device_id: Unique CrowdStrike ID of the device
        """
        log = logging.getLogger(__name__)

        log.info("Waiting for %s seconds. Then getting the device status for device_id %s", cls.ping_delay, device_id)
        time.sleep(cls.ping_delay)

        get_device_details_url = "{0}{1}".format(cls.bauth_base_url, "/devices/entities/devices/v1")
        get_device_details_payload = {
            "ids": device_id
        }

        get_device_details_response = cls.cs_api_request(
            method="GET",
            url=get_device_details_url,
            basicauth=(cls.bauth_api_uuid, cls.bauth_api_key),
            params=get_device_details_payload)

        device_details = get_device_details_response.get("resources")

        if device_details is None:
            return {
                "error": True,
                "err_msg": "Could not get device status for device_id {0}.".format(device_id)
            }

        return {
            "status": device_details[0].get("status")
        }

    @classmethod
    def get_oauth2_token(cls):
        """Calls /oauth2/token endpoint and sets CrowdStrikeHelper.oauth2_token to the new token"""
        log = logging.getLogger(__name__)

        # Set request url, headers and data
        get_oauth2_token_url = "{0}{1}".format(cls.oauth2_base_url, "/oauth2/token")
        get_oauth2_headers = {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

        # As per CS APIs, this must be url-encoded string with client_id and client_secret
        get_oauth2_token_data = "client_id={0}&client_secret={1}".format(cls.oauth2_cid, cls.oauth2_key)

        log.info("Requesting new oauth2 Token from %s", get_oauth2_token_url)

        get_oauth2_token_response = cls.cs_api_request(
            method="POST",
            url=get_oauth2_token_url,
            data=get_oauth2_token_data,
            headers=get_oauth2_headers)

        # Handle custom error
        if get_oauth2_token_response.get("error"):
            raise ValueError("Error getting new oauth2 Token from CrowdStrike: {0}".format(get_oauth2_token_response.get("err_msg")))

        # Set the new token
        cls.oauth2_token = get_oauth2_token_response.get("access_token")

        log.info("New oauth2 Token set successfully")

    @classmethod
    def cs_api_request(cls, method, url, headers=None, basicauth=None, params=None, data=None, json_data=None):
        """Method to handle resquests to CrowdStrike APIs"""
        log = logging.getLogger(__name__)

        response, return_value = None, None

        SUPPORTED_METHODS = ["GET", "POST"]

        if method not in SUPPORTED_METHODS:
            raise ValueError("{0} is not a supported CrowdStrike API Request. Supported methods are: {1}".format(method, SUPPORTED_METHODS))

        headers = cls.json_header if headers is None else headers

        try:
            log.debug("%s CrowdStrike API Request. url: %s headers: %s data: %s", method, url, headers, data)

            if method == "GET":
                response = requests.get(url, auth=basicauth, headers=headers, params=params)
                response.raise_for_status()
                return_value = response.json()

            elif method == "POST":
                response = requests.post(url, auth=basicauth, headers=headers, params=params, data=data, json=json_data)
                response.raise_for_status()
                return_value = response.json()

            log.debug("%s Request successful", method)

        except requests.exceptions.Timeout:
            err_msg = "{0} CrowdStrike API Request timed out".format(method)
            raise ValueError(err_msg)

        except requests.exceptions.TooManyRedirects:
            err_msg = "Too Many Redirects for: {0}".format(url)
            raise ValueError(err_msg)

        except requests.exceptions.HTTPError as err:
            if err.response.content:
                response_content = response.json()
                response_errors = response_content.get("errors")
                response_error_code = response_errors[0].get("code")

                if response_errors and len(response_errors) > 0 and (response_error_code == 403 or response_error_code == 409):
                    return_value = {
                        "error": True,
                        "err_code": response_errors[0].get("code"),
                        "err_msg": response_errors[0].get("message"),
                    }
                    return return_value

            raise ValueError(err)

        except requests.exceptions.RequestException as err:
            raise ValueError(err)

        return return_value
