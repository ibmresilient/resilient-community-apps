# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper
from ast import literal_eval
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups

PACKAGE_NAME = "fn_ldap_utilities"
FN_NAME = "ldap_utilities_add"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ldap_utilities_add'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.ldap_attribute_name_values
            -   fn_inputs.ldap_dn
            -   fn_inputs.
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["ldap_dn"], fn_inputs)

        helper = LDAPUtilitiesHelper(self.app_configs._asdict())

        inputs = fn_inputs._asdict()

        try:
            # Try converting input to an array
            attribute_list = literal_eval("{{ {0} }}".format(inputs.get("ldap_attribute_name_values"))) \
                if inputs.get("ldap_attribute_name_values") else {}
        except Exception:
            raise ValueError("""ldap_attribute_name_values incorrectly specified e.g. "attribute1": "value1", "attribute2": "value2" """)

        try:
            group_list = literal_eval(inputs.get("ldap_multiple_group_dn")) \
                if inputs.get("ldap_multiple_group_dn") else []
        except Exception:
            raise ValueError("""ldap_multiple_group_dn incorrectly specified e.g. "['cn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']" """)

        self.LOG.info("attribute_list: %s", attribute_list)
        self.LOG.info("group_list: %s", group_list)
        # Instantiate LDAP Server and Connection
        c = helper.get_ldap_connection()

        try:
            # Bind to the connection
            c.bind()
        except Exception as err:
            raise ValueError("Cannot connect to LDAP Server. Ensure credentials are correct. Error: %s", str(err))

        # Inform user
        msg = "Connected to server {0}".format(self.app_configs.ldap_server)
        yield self.status_message(msg)

        try:
            yield self.status_message("Attempting to execute add")

            c.add(fn_inputs.ldap_dn, attributes=attribute_list)
            result = c.result
        except Exception as err:
            raise ValueError("Unable to add: %s", fn_inputs.ldap_dn)

        try:
            if result.get('description', '') == 'success' and group_list:
                yield self.status_message("Attempting to execute group add")
                ad_add_members_to_groups(c, [fn_inputs.ldap_dn], group_list, True)
        except Exception as err:
            raise ValueError("Unable to add: %s to group(s): %s", fn_inputs.ldap_dn, group_list)

        finally:
            # Unbind connection
            c.unbind()

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(result)
        # yield FunctionResult({}, success=False, reason="Bad call")
