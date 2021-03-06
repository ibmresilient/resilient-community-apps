# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import json
import re
from ldap3 import ALL_ATTRIBUTES
from ldap3.core.exceptions import LDAPSocketOpenError
from ldap3.utils.conv import escape_filter_chars
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper

PACKAGE_NAME = "fn_ldap_utilities"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ldap_utilities_search''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("ldap_utilities_search")
    def _ldap_utilities_search_function(self, event, *args, **kwargs):
        """Function: Resilient Function to do a search or query against an LDAP server."""

        ##############################################
        def replace_ldap_param(ldap_param_value=None, ldap_search_filter=""):

            re_pattern = "%ldap_param%"

            # if "ldap_param" in ldap_search_filter:

            if re.search(re_pattern, ldap_search_filter) is not None:
                if ldap_param_value is None:
                    raise ValueError("The LDAP Search Filter '{0}' contains the key '%ldap_param%' but no value has been given for ldap_search_param.".format(ldap_search_filter))

                else:
                    # Insert escaped param value in filter, need to escape any backslashes X 2 for regex.
                    ldap_search_filter = re.sub(re_pattern, ldap_param_value.replace('\\', '\\\\'), ldap_search_filter)

            return ldap_search_filter
        ##############################################


        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'ldap_utilities_search' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            ldap_domain_name = kwargs.get("ldap_domain_name")  # text
            ldap_search_attributes = kwargs.get("ldap_search_attributes")  # text
            ldap_search_param = kwargs.get("ldap_search_param")  # text
            ldap_search_base = kwargs.get("ldap_search_base")  # text
            ldap_search_filter = self.get_textarea_param(kwargs.get("ldap_search_filter"))  # textarea

            log = logging.getLogger(__name__)
            log.info("ldap_domain_name: %s", ldap_domain_name)
            log.info("ldap_search_attributes: %s", ldap_search_attributes)
            log.info("ldap_search_param: %s", ldap_search_param)
            log.info("ldap_search_base: %s", ldap_search_base)
            log.info("ldap_search_filter: %s", ldap_search_filter)
            yield StatusMessage("Function Inputs OK")


            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(self.options, ldap_domain_name)
            log.info("[app.config] -ldap_server: %s", helper.LDAP_SERVER)
            #log.info("[app.config] -ldap_pas: %s", helper.LDAP_PAS)
            log.info("[app.config] -ldap_user_dn: %s", helper.LDAP_USER_DN)
            yield StatusMessage("Appconfig Settings OK")


            ##############################################
            # If search_attributes is not specified, request that ALL_ATTRIBUTES for the DN be returned
            if ldap_search_attributes is None:
                ldap_search_attributes = ALL_ATTRIBUTES
            else:
                ldap_search_attributes = [str(attr) for attr in ldap_search_attributes.split(',')]

            if ldap_search_param is not None:
                # Escape special chars from the search_param
                ldap_search_param = escape_filter_chars(ldap_search_param)

            ldap_search_filter = replace_ldap_param(ldap_search_param, ldap_search_filter)

            # Instansiate LDAP Server and Connection
            conn = helper.get_ldap_connection()

            try:
                # Bind to the connection
                conn.bind()
            except Exception as err:
                raise ValueError("Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {0}".format(err))

            try:
                # Inform user
                yield StatusMessage("Connected to {0}".format("Active Directory" if helper.LDAP_IS_ACTIVE_DIRECTORY else "LDAP Server"))

                res = None
                entries = []
                success = False

                yield StatusMessage("Attempting to Search")

                res = conn.search(
                    search_base=ldap_search_base,
                    search_filter=ldap_search_filter,
                    attributes=ldap_search_attributes)

                if res and len(conn.entries) > 0:

                    entries = json.loads(conn.response_to_json())["entries"]
                    log.info("Result contains %s entries", len(entries))

                    # Each entry has 'dn' and dict of 'attributes'. Move attributes to the top level for easier processing.
                    for entry in entries:
                        entry.update(entry.pop("attributes", None))

                    yield StatusMessage("{0} entries found".format(len(entries)))
                    success = True

                else:
                    yield StatusMessage("No entries found")
                    success = False

            except LDAPSocketOpenError:
                success = False
                raise ValueError("Invalid Search Base", ldap_search_base)

            except Exception as err:
                success = False
                raise ValueError("Could not Search the LDAP Server. Ensure 'ldap_search_base' is valid", err)

            finally:
                # Unbind connection
                conn.unbind()

            ##############################################


            results = {
                "success": success,
                "domain_name": ldap_domain_name,
                "entries": entries
            }

            yield StatusMessage("Finished 'ldap_utilities_search' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
