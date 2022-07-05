# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from ast import literal_eval
from logging import getLogger
from resilient_lib import validate_fields, ResultPayload
from fn_ldap_utilities.util.ldap_utils import LDAPDomains
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper, get_domains_list, PACKAGE_NAME
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as ad_add_members_to_groups
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'ldap_utilities_add_to_groups'"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.domains_list = get_domains_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.domains_list = get_domains_list(opts)

    @function("ldap_utilities_add_to_groups")
    def _ldap_utilities_add_to_groups_function(self, event, *args, **kwargs):
        """Function: A function that allows adding multiple users to multiple groups"""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'ldap_utilities_add_to_groups' running in workflow '{}'".format(wf_instance_id))

            # Validate that required fields are given
            validate_fields(["ldap_multiple_user_dn", "ldap_multiple_group_dn"], kwargs)

            # Get function inputs
            ldap_domain_name = kwargs.get("ldap_domain_name", "") # text
            input_ldap_multiple_user_dn_asString = kwargs.get("ldap_multiple_user_dn") # text (required) [string repersentation of an array]
            input_ldap_multiple_group_dn_asString = kwargs.get("ldap_multiple_group_dn") # text (required) [string repersentation of an array]

            LOG.info("LDAP Domain Name: %s", ldap_domain_name)
            LOG.info("LDAP User DN: %s", input_ldap_multiple_user_dn_asString)
            LOG.info("LDAP Group DN: %s", input_ldap_multiple_group_dn_asString)

            yield StatusMessage("Function Inputs OK")

            # Instansiate helper (which gets appconfigs from file)
            ldap = LDAPDomains(self.opts)
            helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(ldap_domain_name, self.domains_list))
            yield StatusMessage("Appconfig Settings OK")

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
                raise ValueError(
                    "Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {}".format(err))

            # Inform user
            yield StatusMessage("Connected to Active Directory")

            try:
                yield StatusMessage("Attempting to add user(s) to group(s)")
                # Perform the removeMermbersFromGroups operation
                res = ad_add_members_to_groups(c, input_ldap_multiple_user_dn, input_ldap_multiple_group_dn, True)

            except Exception as err:
                LOG.debug("Error: {}".format(err))
                raise ValueError("Ensure all user and group DNs exist")

            finally:
                # Unbind connection
                c.unbind()

            # Initialize ResultPayload object
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            results = rp.done(res, None)
            results["users_dn"] = input_ldap_multiple_user_dn,
            results["groups_dn"] = input_ldap_multiple_group_dn

            yield StatusMessage("Finished 'ldap_utilities_add_to_groups' running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
