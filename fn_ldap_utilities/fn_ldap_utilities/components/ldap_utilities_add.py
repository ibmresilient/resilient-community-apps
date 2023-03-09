# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from ast import literal_eval
from logging import getLogger
from resilient_circuits import ResilientComponent, function, FunctionResult, StatusMessage, handler, FunctionError
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper, get_domains_list, PACKAGE_NAME
from resilient_lib import IntegrationError, validate_fields, ResultPayload
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups
from ldap3.core.exceptions import LDAPObjectClassError, LDAPEntryAlreadyExistsResult
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper
from fn_ldap_utilities.util.ldap_utils import LDAPDomains

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements function 'ldap_utilities_add'"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.domains_list = get_domains_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.domains_list = get_domains_list(opts)

    @function("ldap_utilities_add")
    def _ldap_utilities_add_function(self, event, *args, **kwargs):
        """Function: A function that allows you to add users, groups and organizational units to LDAP"""

        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage(f"Starting 'ldap_utilities_add' running in workflow '{wf_instance_id}'")

            # Validate that required fields are given
            validate_fields(["ldap_dn"], kwargs)

            ldap_domain_name = kwargs.get("ldap_domain_name", "") # text
            ldap_dn = kwargs.get("ldap_dn") # text (required)
            attribute_list = kwargs.get("ldap_attribute_name_values") # text
            group_list = kwargs.get("ldap_multiple_group_dn") # text

            try:
                # Try converting input to an dictionary
                attribute_list = literal_eval("{{ {} }}".format(attribute_list))\
                    if attribute_list else {'objectClass': 'user'}
            except Exception:
                raise IntegrationError('ldap_attribute_name_values incorrectly specified e.g. "attribute1": "value1", "attribute2": "value2", "objectClass": "Users"')

            try:
                group_list = literal_eval(group_list) if group_list else []
            except Exception:
                raise IntegrationError("""ldap_multiple_group_dn incorrectly specified e.g. "['cn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']" """)

            LOG.info("LDAP Domain Name: %s", ldap_domain_name)
            LOG.info("LDAP DN: %s", ldap_dn)
            LOG.info("ldap_attribute_name_values: %s", attribute_list)
            LOG.info("ldap_multiple_group_dn: %s", group_list)

            # Initiate variable, so that it does not error when called
            conn = ""

            # Instansiate helper (which gets appconfigs from file)
            ldap = LDAPDomains(self.opts)
            helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(ldap_domain_name, self.domains_list))

            # Instantiate LDAP Server and Connection
            conn = helper.get_ldap_connection()
            try:
                # Bind to the connection
                conn.bind()
            except Exception as err:
                raise ValueError(f"Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {err}")

            # Inform user
            yield StatusMessage(f"Connected to {'Active Directory' if helper.LDAP_IS_ACTIVE_DIRECTORY else 'LDAP Server'}")

            try:
                yield StatusMessage("Attempting to execute add")

                conn.add(ldap_dn, attributes=attribute_list)
                result = conn.result

                try:
                    if result.get('description', '') == 'success' and group_list:
                        yield StatusMessage("Attempting to execute group add")
                        ad_add_members_to_groups(conn, [ldap_dn], group_list, True)
                except Exception as err:
                    raise IntegrationError(f"Unable to add: {ldap_dn} to group(s): {group_list}")
            except LDAPObjectClassError:
                raise ValueError("objectClass is needed in attribute input, EX: 'objectClass': 'user'")
            except LDAPEntryAlreadyExistsResult:
                raise ValueError("User already exists")
            except Exception as err:
                LOG.debug(f'Error: {err}')
                raise ValueError("Ensure dn is correct")
            finally:
                # Unbind connection
                if conn:
                    conn.unbind()

            # Initialize ResultPayload object
            rp = ResultPayload(PACKAGE_NAME, **kwargs)
            if result.get('description', '') == 'success':
                results = rp.done(True, result)
            else:
                results = rp.done(False, result)

            yield StatusMessage(f"Finished 'ldap_utilities_add' running in workflow '{wf_instance_id}'")

            # success
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
