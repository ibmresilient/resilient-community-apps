# (c) Copyright IBM Corp. 2018. All Rights Reserved.

# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import requests

class FunctionPayload:
  """Class that contains the payload sent back to UI and available in the post-processing script"""
  def __init__(self, inputs):
    self.success = True
    self.inputs = {}
    self.pastebin_link = None

    for input in inputs:
      self.inputs[input] = inputs[input]
  
  def as_dict(self):
    """Return this class as a Dictionary"""
    return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_create_pastebin"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_pastebin", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_pastebin", {})

    @function("fn_create_pastebin")
    def _fn_create_pastebin_function(self, event, *args, **kwargs):
        """Function: Function that dumps any text/code to pastebin.com and returns a link to that paste"""

        log = logging.getLogger(__name__)

        # Login URL for Pastebin
        PASTEBIN_LOGIN_URL = "https://pastebin.com/api/api_login.php"

        # POST URL for Pastebin
        PASTEBIN_POST_URL = "https://pastebin.com/api/api_post.php"

        def get_config_option(option_name, optional=False):
          """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
          option = self.options.get(option_name)

          if not option and optional is False:
            err = "'{0}' is mandatory and is not set in ~/.resilient/app.config file. You must set this value to run this function".format(option_name)
            raise ValueError(err)
          else:
            return option
        
        def get_function_input(inputs, input_name, optional=False):
          """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
          input = inputs.get(input_name)

          if input is None and optional is False:
            err = "'{0}' is a mandatory function input".format(input_name)
            raise ValueError(err)
          else:
            return input
        
        def get_pastebin_api_dev_key(api_dev_key, api_user_name, login_url):
            """Gets the api_dev_key from Pastebin. This essentially creates a session so the paste is
            created under that user account"""

            response = requests.post(login_url, data={
              "api_dev_key": api_dev_key,
              "api_user_name": api_user_name,
              "api_user_password": str(get_config_option("pastebin_api_user_password"))
            })

            if response and response.content:
              # If there is an error, fail
              if "Bad API request" in response.content:
                payload.success = False
                raise ValueError(response.content)

              # If success, return the api key
              else:
                return response.content

            else:
              raise ValueError("No response from Pastebin. Check your connection")

        try:

            # Get API Key from app.config file
            PASTEBIN_API_DEV_KEY = str(get_config_option("pastebin_api_dev_key"))

            # Get the Pastebin username, its optional, if defined, will log the user in, then create the paste
            PASTEBIN_API_USER_NAME = str(get_config_option("pastebin_api_user_name", True))

            # Get the API user key, so we can create a paste under this users account
            PASTEBIN_API_USER_KEY = None if PASTEBIN_API_USER_NAME is None else get_pastebin_api_dev_key(PASTEBIN_API_DEV_KEY, PASTEBIN_API_USER_NAME, PASTEBIN_LOGIN_URL)

            # Get the function inputs:
            inputs = {
              "pastebin_code": get_function_input(kwargs, "pastebin_code"), # text (required)
              "pastebin_name": get_function_input(kwargs, "pastebin_name", True), # text (optional)
              "pastebin_format": get_function_input(kwargs, "pastebin_format", True), # text (optional)
              "pastebin_privacy": get_function_input(kwargs, "pastebin_privacy", True), # text (optional)
              "pastebin_expiration": get_function_input(kwargs, "pastebin_expiration", True) # text (optional)
            }

            # Create payload dict with inputs
            payload = FunctionPayload(inputs)

            yield StatusMessage("Function Inputs OK")

            # Set the required request data
            pastebin_request_data = {
              "api_option": "paste",
              "api_dev_key": PASTEBIN_API_DEV_KEY,
              "api_paste_code": payload.inputs["pastebin_code"].encode("utf8")
            }

            # Set the optional request data
            if PASTEBIN_API_USER_KEY:
              pastebin_request_data["api_user_key"] = PASTEBIN_API_USER_KEY

            if payload.inputs["pastebin_name"]:
              pastebin_request_data["api_paste_name"] = payload.inputs["pastebin_name"]
            
            if payload.inputs["pastebin_format"]:
              pastebin_request_data["api_paste_format"] = payload.inputs["pastebin_format"]
            
            if payload.inputs["pastebin_privacy"]:
              pastebin_request_data["api_paste_private"] = payload.inputs["pastebin_privacy"]
            
            if payload.inputs["pastebin_expiration"]:
              pastebin_request_data["api_paste_expire_date"] = payload.inputs["pastebin_expiration"]

            yield StatusMessage("Creating the Paste")

            # Call the POST and get response
            response = requests.post(PASTEBIN_POST_URL, data=pastebin_request_data)

            if response and response.content:
              # If there is an error, fail
              if "Bad API request" in response.content:
                payload.success = False
                yield FunctionError(response.content)

              # If success, set the link
              else:
                payload.pastebin_link = response.content

            else:
              payload.success = False
              yield FunctionError("No response from Pastebin. Check your connection")

            # Send payload back to Appliance
            results = payload.as_dict()

            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()