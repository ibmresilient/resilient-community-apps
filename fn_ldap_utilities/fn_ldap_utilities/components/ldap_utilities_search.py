# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

""" SOAR functions component to execute queries against an LDAP server """

from logging import getLogger
from json import loads
from re import search, sub
from resilient_lib import validate_fields
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from ldap3 import ALL_ATTRIBUTES
from ldap3.core.exceptions import LDAPSocketOpenError
from ldap3.utils.conv import escape_filter_chars
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper, get_domains_list
from fn_ldap_utilities.util.ldap_utils import LDAPDomains

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'ldap_utilities_search'

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
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.domains_list = get_domains_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.domains_list = get_domains_list(opts)

    @function("ldap_utilities_search")
    def _ldap_utilities_search_function(self, event, *args, **kwargs):
        """SOAR Function: entry point """

        def replace_ldap_param(ldap_param_value=None, ldap_search_filter=""):

            re_pattern = "%ldap_param%"

            if search(re_pattern, ldap_search_filter):
                if not ldap_param_value:
                    raise ValueError("The LDAP Search Filter '{}' contains the key '%ldap_param%' but no value has been given for ldap_search_param.".format(
                        ldap_search_filter))
                else:
                    # Insert escaped param value in filter, need to escape any backslashes X 2 for regex.
                    ldap_search_filter = sub(
                        re_pattern, ldap_param_value.replace('\\', '\\\\'), ldap_search_filter)

            return ldap_search_filter

        try:
            yield StatusMessage("Starting ldap_utilities_search")

            # Validate that required fields are given
            validate_fields(["ldap_search_base", "ldap_search_filter"], kwargs)

            # Get function inputs
            ldap_domain_name = kwargs.get("ldap_domain_name") # text
            input_ldap_search_base = kwargs.get("ldap_search_base") # text (required)
            input_ldap_search_filter = self.get_textarea_param(kwargs.get("ldap_search_filter")) # textarea (required)
            input_ldap_search_attributes = kwargs.get("ldap_search_attributes", ALL_ATTRIBUTES) # text (optional)
            input_ldap_search_param = kwargs.get("ldap_search_param") # text (optional)

            if input_ldap_search_attributes and input_ldap_search_attributes is not ALL_ATTRIBUTES:
                input_ldap_search_attributes = [str(attr) for attr in input_ldap_search_attributes.split(',')]

            if input_ldap_search_param:
                # Escape special chars from the search_param
                input_ldap_search_param = escape_filter_chars(input_ldap_search_param)

            LOG.info("LDAP Domain Name: %s", ldap_domain_name)
            LOG.info("LDAP Search Base: %s", input_ldap_search_base)
            LOG.info("LDAP Search Filter: %s", input_ldap_search_filter)
            LOG.info("LDAP Search Attributes: %s", input_ldap_search_attributes)
            LOG.info("LDAP Search Param: %s", input_ldap_search_param)

            yield StatusMessage("Function Inputs OK")

            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(LDAPDomains.ldap_domain_name_test(ldap_domain_name, self.domains_list))
            yield StatusMessage("Appconfig Settings OK")

            input_ldap_search_filter = replace_ldap_param(input_ldap_search_param, input_ldap_search_filter)

            # Instansiate LDAP Server and Connection
            conn = helper.get_ldap_connection()

            try:
                # Bind to the connection
                conn.bind()
            except Exception as err:
                raise ValueError("Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {}".format(err))

            try:
                # Inform user
                yield StatusMessage("Connected to {}".format("Active Directory" if helper.LDAP_IS_ACTIVE_DIRECTORY else "LDAP Server"))

                entries = []
                success = False

                yield StatusMessage("Attempting to Search")

                res = conn.search(
                    search_base=input_ldap_search_base,
                    search_filter=input_ldap_search_filter,
                    attributes=input_ldap_search_attributes)

                if res and len(conn.entries) > 0:
                    entries = loads(conn.response_to_json())["entries"]
                    LOG.info("Result contains %s entries", len(entries))

                    # Each entry has 'dn' and dict of 'attributes'. Move attributes to the top level for easier processing.
                    for entry in entries:
                        entry.update(entry.pop("attributes", None))

                    yield StatusMessage("{0} entries found".format(len(entries)))
                    success = True

                else:
                    yield StatusMessage("No entries found")

            except LDAPSocketOpenError:
                raise ValueError("Invalid Search Base", input_ldap_search_base)

            except Exception as err:
                raise ValueError("Could not Search the LDAP Server. Ensure 'ldap_search_base' is valid", err)

            finally:
                # Unbind connection
                conn.unbind()

            results = {
                "success": success,
                "entries": entries
            }

            LOG.info("Completed")
            LOG.debug("RESULTS: %s", results)

            # Produce a FunctionResult with the return value.
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
