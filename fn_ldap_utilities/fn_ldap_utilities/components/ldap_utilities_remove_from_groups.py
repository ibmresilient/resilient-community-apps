# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from resilient_lib import validate_fields
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper
from ast import literal_eval
from ldap3.extend.microsoft.removeMembersFromGroups import ad_remove_members_from_groups as ad_remove_members_from_groups

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'ldap_utilities_remove_from_groups"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ldap_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ldap_utilities", {})

    @function("ldap_utilities_remove_from_groups")
    def _ldap_utilities_remove_from_groups_function(self, event, *args, **kwargs):
        """Function: A function that allows you to remove multiple from multiple groups"""

        try:
            yield StatusMessage("Starting ldap_utilities_remove_from_groups")

            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(self.options)
            yield StatusMessage("Appconfig Settings OK")

            # Validate that required fields are given
            validate_fields(["ldap_multiple_user_dn", "ldap_multiple_group_dn"], kwargs)

            # Get function inputs
            input_ldap_multiple_user_dn_asString = kwargs.get("ldap_multiple_user_dn") # text (required) [string repersentation of an array]
            input_ldap_multiple_group_dn_asString = kwargs.get("ldap_multiple_group_dn") # text (required) [string repersentation of an array]

            yield StatusMessage("Function Inputs OK")

            if not helper.LDAP_IS_ACTIVE_DIRECTORY:
                raise FunctionError(
                    "This function only supports an Active Directory connection. Make sure ldap_is_active_directory is set to True in the app.config file")

            try:
                # Try converting input to an array
                input_ldap_multiple_user_dn = literal_eval(input_ldap_multiple_user_dn_asString)
                input_ldap_multiple_group_dn = literal_eval(input_ldap_multiple_group_dn_asString)

            except Exception:
                raise ValueError(
                    """input_ldap_multiple_user_dn and input_ldap_multiple_group_dn must be a string repersenation of an array e.g. "['dn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']" """)

            # Instansiate LDAP Server and Connection
            c = helper.get_ldap_connection()

            try:
                # Bind to the connection
                c.bind()
            except Exception as err:
                raise ValueError("Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {}".format(err))

            # Inform user
            yield StatusMessage("Connected to Active Directory")

            res = False
            users_dn = []

            try:
                yield StatusMessage("Attempting to remove user(s) from group(s)")
                # Perform the removeMermbersFromGroups operation
                res = ad_remove_members_from_groups(
                    c, input_ldap_multiple_user_dn, input_ldap_multiple_group_dn, True)

                # Return list of users that were removed, and ignore users that do not exist, not valid, or not member of group
                if res and "changes" in c.request:
                    users_dn = c.request["changes"][0]["attribute"]["value"]

            except Exception:
                raise ValueError("Ensure all group DNs exist")

            finally:
                # Unbind connection
                c.unbind()

            results = {
                "success": res,
                "users_dn": users_dn if len(users_dn) > 0 else None,
                "groups_dn": input_ldap_multiple_group_dn
            }

            LOG.info("Completed")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
