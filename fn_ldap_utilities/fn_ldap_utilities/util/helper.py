class LDAPUtilitiesHelper:

  def str_to_bool(self, str):
    """Convert unicode string to equivalent boolean value. Converts a "true" or "false" string to a boolean value , string is case insensitive."""
    if str.lower() == 'true':
        return True
    elif str.lower() == 'false':
        return False
    else:
        raise ValueError

  def get_config_option(self, option_name, optional=False):
    """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
    option = self.options.get(option_name)

    if option is None and optional is False:
      err = "'{0}' is mandatory and is not set in ~/.resilient/appconfig file. You must set this value to run this function".format(option_name)
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

    self.LDAP_SERVER = self.get_config_option("ldap_server")
    self.LDAP_PORT = int(self.get_config_option("ldap_port"))
    self.LDAP_USE_SSL = self.str_to_bool(self.get_config_option("ldap_use_ssl"))
    self.LDAP_AUTH = self.get_config_option("ldap_auth")
    self.LDAP_USER_DN = self.get_config_option("ldap_user_dn")
    self.LDAP_PASSWORD = self.get_config_option("ldap_password")
    self.LDAP_IS_ACTIVE_DIRECTORY = self.str_to_bool(self.get_config_option("ldap_is_active_directory"))
    self.LDAP_CONNECT_TIMEOUT = int(self.get_config_option("ldap_connect_timeout"))
    self.LDAP_DOMAIN = self.get_config_option("ldap_domain", True)
