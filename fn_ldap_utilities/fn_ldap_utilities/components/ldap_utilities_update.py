# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from resilient_lib import validate_fields, ResultPayload
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper, get_domains_list, PACKAGE_NAME
from fn_ldap_utilities.util.ldap_utils import LDAPDomains
from ldap3 import MODIFY_REPLACE
from ast import literal_eval

LOG = getLogger(__name__)
class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'ldap_utilities_update"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.domains_list = get_domains_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.domains_list = get_domains_list(opts)

    @function("ldap_utilities_update")
    def _ldap_utilities_update_function(self, event, *args, **kwargs):
        """Function: A function that updates the attribute of a DN with a new value"""

        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'ldap_utilities_update' running in workflow '{}'".format(wf_instance_id))

            # Validate that required fields are given
            validate_fields(["ldap_dn", "ldap_attribute_name", "ldap_attribute_values"], kwargs)

            # Get function inputs
            ldap_domain_name = kwargs.get("ldap_domain_name", "") # text
            input_ldap_dn = kwargs.get("ldap_dn") # text (required)
            input_ldap_attribute_name = kwargs.get("ldap_attribute_name") # text (required)
            input_ldap_attribute_values_asString = kwargs.get("ldap_attribute_values") # text (required) [string repersentation of an array]

            LOG.info("LDAP Domain Name: %s", ldap_domain_name)
            LOG.info("LDAP DN: %s", input_ldap_dn)
            LOG.info("LDAP Attribute name: %s", input_ldap_attribute_name)
            LOG.info("LDAP Attribute Value: %s", input_ldap_attribute_values_asString)

            yield StatusMessage("Function Inputs OK")

            # Instansiate helper (which gets appconfigs from file)
            ldap = LDAPDomains(self.opts)
            helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(ldap_domain_name, self.domains_list))
            yield StatusMessage("Appconfig Settings OK")

            try:
                # Try converting input to an array
                input_ldap_attribute_values = literal_eval(input_ldap_attribute_values_asString)
            except Exception as err:
                LOG.debug("Error: {}".format(err))
                raise ValueError(
                    """input_ldap_attribute_values must be a string repersenation of an array e.g. "['stringValue1, 1234, 'stringValue2']" """)

            # Instansiate LDAP Server and Connection
            c = helper.get_ldap_connection()

            try:
                # Bind to the connection
                c.bind()
            except Exception as err:
                raise ValueError("Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {}".format(err))

            # Inform user
            yield StatusMessage("Connected to {}".format("Active Directory" if helper.LDAP_IS_ACTIVE_DIRECTORY else "LDAP Server"))

            try:
                yield StatusMessage("Attempting to update {}".format(input_ldap_attribute_name))
                # Perform the Modify operation
                res = c.modify(input_ldap_dn, {input_ldap_attribute_name: [(MODIFY_REPLACE, input_ldap_attribute_values)]})

            except Exception as err:
                LOG.debug("Error: {}".format(err))
                raise ValueError("Failed to update. Ensure 'ldap_dn' is valid and the update meets your LDAP CONSTRAINTS")

            finally:
                # Unbind connection
                c.unbind()

            # Initialize ResultPayload object
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            results = rp.done(res, None)
            results["attribute_name"] = input_ldap_attribute_name
            results["attribute_values"] = input_ldap_attribute_values
            results["user_dn"] = input_ldap_dn

            yield StatusMessage("Finished 'ldap_utilities_update' running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
