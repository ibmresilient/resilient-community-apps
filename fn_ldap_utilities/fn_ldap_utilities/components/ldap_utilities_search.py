# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

""" Resilient functions component to execute queries against an LDAP server """

import logging
import json
import re

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import ldap3
from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPSocketOpenError, LDAPNoSuchObjectResult, LDAPInvalidCredentialsResult, \
    LDAPInvalidFilterError, LDAPAttributeError, LDAPObjectClassError
from ldap3.utils.conv import escape_filter_chars, to_unicode
from ldap3.utils.config import get_config_parameter

from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ldap_utilities_search'

      The Function does an LDAP lookup and takes the following parameters:
          ldap_search_base , ldap_search_filter, ldap_search_attributes and ldap_param

      An example of a set of query parameter might look like the following:

              ldap_search_base = "dc=example,dc=com"
              ldap_search_filter = "(&(objectClass=person)(|(uid={%ldap_param%})(uid=newton)))"
              ldap_search_attributes = "uid,cn,sn,mail,telephoneNumber"
              ldap_param = artifact.value # Assigned value 'einstein' during run.

      The LDAP lookup will return a result in JSON format with an entry consisting of a dn and a set of
      attributes for each result.

          {
            "entries": [
                  {"dn': "entry1_dn1_value", "entry1_attribute2", "entry1_attribute3", ... },
                  {"dn": "entry2_dn2_value", "entry2_attribute2", "entry2_attribute3", ... }
                  ...
            ]
          }

      An example of a returned result (Note: some attributes can be arrays):

      'entries': [{"dn": "uid=newton,dc=example,dc=com", "telephoneNumber": [], "uid": ["newton"],
      "mail": ["newton@ldap.forumsys.com"], "sn": ["Newton"], "cn": ["Isaac Newton"]},
      {"dn": "uid=einstein,dc=example,dc=com", "telephoneNumber": ["314-159-2653"], "uid": ["einstein"],
      "mail": ["einstein@ldap.forumsys.com"], "sn": ["Einstein"], "cn": ["Albert Einstein"]}]
    """

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ldap_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ldap_utilities", {})

    @function("ldap_utilities_search")
    def _ldap_utilities_search_function(self, event, *args, **kwargs):
        """Resilient Function: entry point """

        LOG = logging.getLogger(__name__)

        def escape_chars(str, encoding=None):
          """ Escape some characters in filter.

          Escape a set of characters in the filter string to help to mitigate against possibility of injection.
          This has a subset of characters escaped in ldap3 function escape_filter_chars.

          """
          if encoding is None:
              encoding = get_config_parameter('DEFAULT_ENCODING')

          str = to_unicode(str, encoding)
          escaped_str = str.replace('\\', '\\5c')
          escaped_str = escaped_str.replace('*', '\\2a')
          escaped_str = escaped_str.replace('\x00', '\\00')

          return escaped_str

        def validate_params(search_params):
          """"Check mandatory fields

          Do a number of checks on input fields.

          """
          for k in search_params:
            if re.match(r'^search_filter$', k):
                # Do some basic checks on filter.
                if not re.match(r'^\(.*\)$', search_params[k]):
                    # Outer parentheses not found thus invalid filter
                    raise ValueError("LDAP search filter invalid format")
                if not search_params[k].count('(') == search_params[k].count(')'):
                    # The count of '(' and ')' characters need to match in filter.
                    raise LDAPInvalidFilterError("Invalid filter because of unmatched parentheses.")

        def update_param_fields(search_params):
          """"Update %ldap_param% fields

          Escape some characters in search_params[search_filter].
          If search_params[search_filter] hash key has %ldap_param% set in it's value, update
          value replacing %param% with actual escaped value from param.

          """
          for k in search_params:
            if re.match('^search_filter$', k):
              # Escape some characters in search_filter which might cause LDAP injection.
              search_params[k] = escape_chars(search_params[k])

              # Search for "%ldap_param% token in parameter.
              if re.search("%ldap_param%", search_params[k]):

                # Only allow "%ldap_param% in search_filter field.
                if re.match('^search_filter$', k):
                  
                  if "param" not in search_params:
                    raise Exception ("The parameter '{}' contains string token '%ldap_param%' but the input '{}' is blank.".format(k, "ldap_search_param"))
                  
                  else:
                    # Insert escaped param value in filter, need to escape any backslashes X 2 for regex.
                    search_params[k] = re.sub("%ldap_param%", search_params["param"].replace('\\', '\\\\'), search_params[k])
                    LOG.debug(('Transformed parameter'+k+' to '+search_params[k]))
                
                else:
                  raise Exception("The string %ldap_param% not allowed in parameter '{}' ".format(k))

          return search_params

        try:
            yield StatusMessage("Starting ldap_utilities_search")

            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(self.options)
            yield StatusMessage("Appconfig Settings OK")

            # Get function inputs
            input_ldap_search_base = helper.get_function_input(kwargs, "ldap_search_base") # text (required)
            input_ldap_search_filter = self.get_textarea_param(kwargs.get("ldap_search_filter"))  # textarea (required)
            input_ldap_search_attributes = helper.get_function_input(kwargs, "ldap_search_attributes", optional=True)  # text (optional)
            input_ldap_search_param = helper.get_function_input(kwargs, "ldap_search_param", optional=True)  # text (optional)

            if input_ldap_search_attributes is None:
              input_ldap_search_attributes = ""
            else:
              attributes = input_ldap_search_attributes.split(',')
              input_ldap_search_attributes = [str(attr) for attr in attributes]

            yield StatusMessage("Function Inputs OK")

            search_params = {
              'search_base': input_ldap_search_base, 
              'search_filter': input_ldap_search_filter,
              'search_attributes': input_ldap_search_attributes
            }

            if input_ldap_search_param:
              # Escape 'param' parameter.
              search_params.setdefault('param', escape_filter_chars(input_ldap_search_param))
            
            yield StatusMessage("Validating LDAP Parameters")
            validate_params(search_params)
            search_params = update_param_fields(search_params)

            # Instansiate LDAP Server and Connection
            c = helper.get_ldap_connection()

            try:
              # Bind to the connection
              c.bind()
            except Exception as e:
              raise ValueError("Cannot connect to LDAP Server. Ensure credentials are correct")

            # Inform user
            msg = ""
            if helper.LDAP_IS_ACTIVE_DIRECTORY:
              msg = "Connected to {0}".format("Active Directory")
            else:
              msg = "Connected to {0}".format("LDAP Server")
            yield StatusMessage(msg)

            res = False
            entries = []
            success = False

            try:
              yield StatusMessage("Attempting to Search")
              res = c.search(search_params["search_base"], search_params["search_filter"], attributes=search_params["search_attributes"])

              if res and len(c.entries) > 0:

                entries = json.loads(c.response_to_json())["entries"]
                LOG.info("Result contains %s entries", len(entries))

                # Each entry has 'dn' and dict of 'attributes'. Move attributes to the top level for easier processing.
                for entry in entries:
                  LOG.debug(json.dumps(entry))
                  entry.update(entry.pop("attributes", None))
            
                yield StatusMessage("{0} entries found".format(len(entries)))
                success = True

              else:
                yield StatusMessage("No entries found")
                success = False

            except Exception:
              success = False
              raise ValueError("Could not Search the LDAP Server. Ensure 'ldap_search_base' is valid")

            finally:
              # Unbind connection
              c.unbind()

            results = {
              "success": success,
              "entries": entries
            }

            LOG.info("Completed")
            LOG.debug(json.dumps(results))

            # Produce a FunctionResult with the return value.
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()