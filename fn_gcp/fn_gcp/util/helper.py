# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
class GCPHelper:

  def str_to_bool(self, str):
    """Convert unicode string to equivalent boolean value. Converts a "true" or "false" string to a boolean value , string is case insensitive."""
    if str.lower() == 'true':
        return True
    elif str.lower() == 'false':
        return False
    else:
        raise ValueError

  def get_config_option(self, option_name, optional=False):
    """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
    option = self.options.get(option_name)

    if option is None and optional is False:
      err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function properly".format(option_name)
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

  def setup_config(self):
    HTTP_PROXY = self.get_config_option("gcp_http_proxy", True)
    HTTPS_PROXY = self.get_config_option("gcp_https_proxy", True)

    GCP_REGION = self.get_config_option("gcp_region")
    GCP_PROJECT_ID = self.get_config_option("gcp_project_id")
    GCP_FUNCTION_NAME = self.get_config_option("gcp_function_name")
    return HTTPS_PROXY, HTTP_PROXY, GCP_REGION, GCP_PROJECT_ID, GCP_FUNCTION_NAME

  def setup_proxies(self, proxies, http_proxy, https_proxy):
    if http_proxy:
        proxies["http"] = http_proxy
    if https_proxy:
        proxies["https"] = https_proxy
    if len(proxies) == 0:
        proxies = None
    return proxies

  def __init__(self, options):
    self.options = options