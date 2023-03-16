# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
""" SOAR functions component to execute queries against an LDAP server """

from json import loads
from re import search, sub

from ldap3 import ALL_ATTRIBUTES
from ldap3.core.exceptions import LDAPInvalidFilterError, LDAPSocketOpenError
from ldap3.utils.conv import escape_filter_chars
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import validate_fields

from fn_ldap_utilities.util.helper import (PACKAGE_NAME, LDAPUtilitiesHelper,
                                           get_domains_list)
from fn_ldap_utilities.util.ldap_utils import LDAPDomains

FN_NAME = "ldap_utilities_search"
MAX_returned_results = 1000

class FunctionComponent(AppFunctionComponent):
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
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.domains_list = get_domains_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: A function that allows the user to search LDAP.
        Inputs:
            -   fn_inputs.ldap_domain_name
            -   fn_inputs.ldap_search_base
            -   fn_inputs.ldap_search_base
            -   fn_inputs.ldap_search_filter
            -   fn_inputs.ldap_search_attributes
            -   fn_inputs.ldap_search_param
            -   fn_inputs.ldap_search_max_return
        """

        def replace_ldap_param(ldap_param_value=None, ldap_search_filter=""):

            re_pattern = "%ldap_param%"

            if search(re_pattern, ldap_search_filter):
                if not ldap_param_value:
                    raise ValueError(f"The LDAP Search Filter '{ldap_search_filter}' contains the key '%ldap_param%' but no value has been given for ldap_search_param.")
                else:
                    # Insert escaped param value in filter, need to escape any backslashes X 2 for regex.
                    ldap_search_filter = sub(
                        re_pattern, ldap_param_value.replace('\\', '\\\\'), ldap_search_filter)

            return ldap_search_filter

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate that required fields are given
        validate_fields(["ldap_search_base", "ldap_search_filter"], fn_inputs)

        # Get function inputs
        ldap_domain_name = getattr(fn_inputs, "ldap_domain_name", "") # text
        input_ldap_search_base = getattr(fn_inputs, "ldap_search_base") # text (required)
        input_ldap_search_filter = self.get_textarea_param(getattr(fn_inputs, "ldap_search_filter")) # textarea (required)
        input_ldap_search_attributes = getattr(fn_inputs, "ldap_search_attributes", ALL_ATTRIBUTES) # text (optional)
        input_ldap_search_param = getattr(fn_inputs, "ldap_search_param") # text (optional)
        max_return = getattr(fn_inputs, "ldap_search_max_return", MAX_returned_results)

        if input_ldap_search_attributes and input_ldap_search_attributes is not ALL_ATTRIBUTES:
            input_ldap_search_attributes = [str(attr) for attr in input_ldap_search_attributes.split(',')]

        if input_ldap_search_param:
            # Escape special chars from the search_param
            input_ldap_search_param = escape_filter_chars(input_ldap_search_param)

        self.LOG.info(f"LDAP Domain Name: {ldap_domain_name}")
        self.LOG.info(f"LDAP Search Base: {input_ldap_search_base}")
        self.LOG.info(f"LDAP Search Filter: {input_ldap_search_filter}")
        self.LOG.info(f"LDAP Search Attributes: {input_ldap_search_attributes}")
        self.LOG.info(f"LDAP Search Param: {input_ldap_search_param}")
        self.LOG.info(f"LDAP Search Max Return: {max_return}")

        # Initiate variable, so that it does not error when called
        conn = ""

        # Instansiate helper (which gets appconfigs from file)
        ldap = LDAPDomains(self.opts)
        helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(ldap_domain_name, self.domains_list))

        input_ldap_search_filter = replace_ldap_param(input_ldap_search_param, input_ldap_search_filter)

        # Instansiate LDAP Server and Connection
        conn = helper.get_ldap_connection()

        try:
            # Bind to the connection
            conn.bind()
        except Exception as err:
            raise ValueError(f"Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {err}")

        try:
            # Inform user
            yield self.status_message(f"Connected to {'Active Directory' if helper.LDAP_IS_ACTIVE_DIRECTORY else 'LDAP Server'}")

            entries = []
            success = False

            yield self.status_message("Attempting to Search")

            res = conn.search(
                search_base=input_ldap_search_base,
                search_filter=input_ldap_search_filter,
                attributes=input_ldap_search_attributes
            )

            if res and len(conn.entries) > 0:
                entries = loads(conn.response_to_json())["entries"]
                self.LOG.info("Result contains %s entries", len(entries))

                # Each entry has 'dn' and dict of 'attributes'. Move attributes to the top level for easier processing.
                for entry in entries:
                    entry.update(entry.pop("attributes", None))

                yield self.status_message(f"{len(entries)} entries found")
                success = True

            else:
                yield self.status_message("No entries found")

        except LDAPSocketOpenError as err:
            self.LOG.debug(f"Error: {err}")
            raise ValueError("Invalid Search Base", input_ldap_search_base)
        except LDAPInvalidFilterError as err:
            self.LOG.debug(f"Error: {err}")
            raise ValueError("Invalid search filter", input_ldap_search_filter)
        except Exception as err:
            raise ValueError("Could not Search the LDAP Server. Ensure 'ldap_search_base' is valid", err)

        finally:
            # Unbind connection
            conn.unbind()

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the return value.
        yield FunctionResult({"entries": entries}, success=success)
