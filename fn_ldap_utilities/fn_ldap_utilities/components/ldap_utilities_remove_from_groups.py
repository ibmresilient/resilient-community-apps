# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper
from ast import literal_eval
from ldap3.extend.microsoft.removeMembersFromGroups import ad_remove_members_from_groups as ad_remove_members_from_groups

PACKAGE_NAME = "fn_ldap_utilities"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ldap_utilities_remove_from_groups''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("ldap_utilities_remove_from_groups")
    def _ldap_utilities_remove_from_groups_function(self, event, *args, **kwargs):
        """Function: A function that allows you to remove multiple from multiple groups"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'ldap_utilities_remove_from_groups' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            ldap_domain_name = kwargs.get("ldap_domain_name")  # text
            ldap_multiple_user_dn = kwargs.get("ldap_multiple_user_dn")  # text
            ldap_multiple_group_dn = kwargs.get("ldap_multiple_group_dn")  # text

            log = logging.getLogger(__name__)
            log.info("ldap_domain_name: %s", ldap_domain_name)
            log.info("ldap_multiple_user_dn: %s", ldap_multiple_user_dn)
            log.info("ldap_multiple_group_dn: %s", ldap_multiple_group_dn)
            yield StatusMessage("Function Inputs OK")


            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(self.options, ldap_domain_name)
            log.info("[app.config] -ldap_server: %s", helper.LDAP_SERVER)
            log.info("[app.config] -ldap_user_dn: %s", helper.LDAP_USER_DN)
            yield StatusMessage("Appconfig Settings OK")


            ##############################################

            if not helper.LDAP_IS_ACTIVE_DIRECTORY:
              raise FunctionError("This function only supports an Active Directory connection. Make sure ldap_is_active_directory is set to True in the app.config file")

            try:
              # Try converting input to an array
              ldap_multiple_user_dn = literal_eval(ldap_multiple_user_dn)
              ldap_multiple_group_dn = literal_eval(ldap_multiple_group_dn)

            except Exception:
              raise ValueError("""ldap_multiple_user_dn and ldap_multiple_group_dn must be a string repersenation of an array e.g. "['dn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']" """)

            # Instansiate LDAP Server and Connection
            c = helper.get_ldap_connection()

            try:
              # Bind to the connection
              c.bind()
            except Exception as err:
              raise ValueError("Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {0}".format(err))

            
            # Inform user
            msg = "Connected to {0}".format("Active Directory")
            yield StatusMessage(msg)

            res = False
            users_dn = []
            try:
              yield StatusMessage("Attempting to remove user(s) from group(s)")
              # perform the removeMermbersFromGroups operation
              res = ad_remove_members_from_groups(c, ldap_multiple_user_dn, ldap_multiple_group_dn, True)
              # Test: res = 'ad_remove_members_from_groups(c, ' + str(ldap_multiple_user_dn) + ', ' + str(ldap_multiple_group_dn) + ', True)'
              
              # Return list of users that were removed, and ignore users that do not exist, not valid, or not member of group
              if res and "changes" in c.request:
                users_dn = c.request["changes"][0]["attribute"]["value"]

            except Exception:
              raise ValueError("Ensure all group DNs exist")

            finally:
              # Unbind connection
              c.unbind()

            ##############################################


            results = {
                "success": res,
                "domain_name": ldap_domain_name,
                "users_dn": users_dn if len(users_dn) > 0 else None,
                "groups_dn": ldap_multiple_group_dn
            }

            yield StatusMessage("Finished 'ldap_utilities_remove_from_groups' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
