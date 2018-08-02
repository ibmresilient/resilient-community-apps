# (c) Copyright IBM Corp. 2018. All Rights Reserved.
import requests

class ServiceNowHelper:

  def str_to_bool(self, str):
    """Convert unicode string to equivalent boolean value. Converts a "true" or "false" string to a boolean value , string is case insensitive."""
    if str.lower() == 'true':
        return True
    elif str.lower() == 'false':
        return False
    else:
        raise ValueError("{} is not a boolean".format(str))

  def get_config_option(self, option_name, optional=False):
    """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
    option = self.options.get(option_name)

    if option is None and optional is False:
      err = "'{0}' is mandatory and is not set in ~/.resilient/app.config file. You must set this value to run this function".format(option_name)
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
  
  def POST(self, url, data, auth=None, headers={"Content-Type":"application/xml","Accept":"application/xml"}):
    if auth is None:
      auth = self.SN_AUTH
    
    url = self.SN_API_URL + url
    
    try:
      response = requests.post(url, auth=auth, headers=headers, data=data)
    except Exception:
      raise ValueError("ServiceNow POST failed. Check url and credentials")

    return response

  def __init__(self, options):
    self.options = options

    self.SN_API_URL = self.get_config_option("sn_api_url")
    self.SN_USERNAME = str(self.get_config_option("sn_username"))
    
    # Handle password surrounded by '
    pwd = str(self.get_config_option("sn_password"))
    if pwd.startswith("'") and pwd.endswith("'"):
      self.SN_PASSWORD = pwd[1:-1]
    else:
      self.SN_PASSWORD = pwd
    
    self.SN_AUTH = (self.SN_USERNAME, self.SN_PASSWORD)

