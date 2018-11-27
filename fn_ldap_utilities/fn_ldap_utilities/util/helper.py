# (c) Copyright IBM Corp. 2018. All Rights Reserved.
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE

class LDAPUtilitiesHelper:

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

  def get_ldap_connection(self):
    try:
      server = Server(self.LDAP_SERVER, port=self.LDAP_PORT, get_info=ALL, use_ssl=self.LDAP_USE_SSL, connect_timeout=self.LDAP_CONNECT_TIMEOUT)
      connection = Connection(server, user=self.LDAP_USER_DN, password=self.LDAP_PASSWORD, authentication=self.LDAP_AUTH, return_empty_attributes=True, raise_exceptions=True)
      return connection
    except:
      raise ValueError('Cannot connect to LDAP Server. Ensure credentials are correct')
  
  def __init__(self, options):
    LDAP_AUTH_TYPES = ["ANONYMOUS", "SIMPLE", "NTLM", "SASL"]

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

    if self.LDAP_AUTH.upper() not in LDAP_AUTH_TYPES:
      raise ValueError("Invalid value for 'LDAP_AUTH' configuration setting")

    if self.LDAP_AUTH.upper() == "SASL":
      raise Exception("Connection using SASL authentication not currently implemented.")

    # Check user
    if self.LDAP_USER_DN and '\\' in self.LDAP_USER_DN:
      # User can have a domain value pre-pended if connecting to Active Directory server.
      ldap_user_split = self.LDAP_USER_DN.split("\\")
      if len(ldap_user_split) > 2:
          # If '\' character appears more than once throw error.
          raise ValueError("Invalid value '{}' for 'user'.".format(self.LDAP_USER_DN))
      if len(ldap_user_split[1]) == 0:
          raise ValueError("Invalid empty value for user after the '\\' character in 'user' config option.")
      if len(ldap_user_split[0]) == 0:
          raise ValueError("Invalid empty value for domain before the '\\' character in 'user' config option.")
    
    # Check user + password combo
    if (self.LDAP_USER_DN and self.LDAP_PASSWORD) and (self.LDAP_AUTH.upper() == "ANONYMOUS"):
      raise ValueError("If 'user' and 'password' values are both set 'auth=ANONYMOUS' is not allowed.")
    elif (not self.LDAP_USER_DN and not self.LDAP_PASSWORD) and (self.LDAP_AUTH.upper() != "ANONYMOUS"):
      raise ValueError("Empty 'user' and 'password' values can only be used with 'auth=ANONYMOUS'.")
    
    if self.LDAP_DOMAIN or self.LDAP_AUTH.upper() == "NTLM":
      # Looks like we are pointing at an Active Directory server.(Note: AD can also use auth='SIMPLE').
      if (not self.LDAP_DOMAIN and not ldap_user_split):
        # If we got here 'auth' = 'NTLM' but no domain specified in 'domain' or 'user'.
        raise Exception("Connection using AD requires a 'domain' to be specified.")
      elif self.LDAP_DOMAIN and not ldap_user_split:
        # If we got here 'domain' is set and no domain specified in 'user' configuration option.
        # Prepend domain to user.
        self.LDAP_USER_DN = "{}\\{}".format(self.LDAP_DOMAIN, self.LDAP_USER_DN)
      elif self.LDAP_DOMAIN and len(ldap_user_split) == 2:
        # Check to see if self.LDAP_DOMAIN and ldap_user_split[0] match.
        if self.LDAP_DOMAIN.upper() != ldap_user_split[0].upper():
          raise Exception("Conflicting domain names '{}' and '{}' specified for credentials.".format(self.LDAP_DOMAIN, ldap_user_split[0]))