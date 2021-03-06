# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE
import string
import random

PACKAGE_NAME = "fn_ldap_utilities"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ldap_utilities_set_password''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("ldap_utilities_set_password")
    def _ldap_utilities_set_password_function(self, event, *args, **kwargs):
        """Function: A function that allows you to set a new password for an LDAP entry given the entry's DN"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'ldap_utilities_set_password' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            ldap_domain_name = kwargs.get("ldap_domain_name")  # text
            ldap_new_password = kwargs.get("ldap_new_password")  # text
            ldap_dn = kwargs.get("ldap_dn")  # text
            ldap_new_auto_password_len = kwargs.get("ldap_new_auto_password_len")  # text
            ldap_return_new_password = kwargs.get("ldap_return_new_password")  # boolean

            log = logging.getLogger(__name__)
            log.info("ldap_domain_name: %s", ldap_domain_name)
            log.info("ldap_new_password: %s", ldap_new_password)
            log.info("ldap_dn: %s", ldap_dn)
            log.debug("ldap_new_auto_pasxxxxx_len: %s", ldap_new_auto_password_len)
            log.info("ldap_return_new_pasxxxxx: %s", ldap_return_new_password)
            yield StatusMessage("Function Inputs OK")
            

            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(self.options, ldap_domain_name)
            log.info("[app.config] -ldap_server: %s", helper.LDAP_SERVER)
            log.info("[app.config] -ldap_user_dn: %s", helper.LDAP_USER_DN)
            yield StatusMessage("Appconfig Settings OK")


            ##############################################

            # Instansiate LDAP Server and Connection
            c = helper.get_ldap_connection()

            try:
              # Bind to the connection
              c.bind()
            except Exception as err:
              raise ValueError("Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {0}".format(err))
            
            # Inform user
            msg = ""
            if helper.LDAP_IS_ACTIVE_DIRECTORY:
              msg = "Connected to {0}".format("Active Directory")
            else:
              msg = "Connected to {0}".format("LDAP Server")
            yield StatusMessage(msg)

            # If ldap_new_password empty, auto-generate pwd with length ldap_new_auto_password_len. If ldap_new_auto_password_len empty, creates 8 char length pwd.
            if ldap_new_password is None or ldap_new_password == '':
              if ldap_new_auto_password_len is None or not ldap_new_auto_password_len.isnumeric():
                ldap_new_password = generate_password(8)
              else:                
                ldap_new_password = generate_password(int(ldap_new_auto_password_len))

            res = False
            try:
              yield StatusMessage("Attempting to change password")
              if helper.LDAP_IS_ACTIVE_DIRECTORY:
                res = c.extend.microsoft.modify_password(str(ldap_dn), ldap_new_password)
                # Test: res = 'c.extend.microsoft.modify_password(' + str(ldap_dn) + ', ' + str(ldap_new_password) + ')'
              else:
                res = c.modify(ldap_dn, {'userPassword': [(MODIFY_REPLACE, [ldap_new_password])]})
                # Test: res = 'c.modify(' + str(ldap_dn) + ', {userPassword: [(MODIFY_REPLACE, [' + str(ldap_new_password) + '])]})'

            except Exception:
              raise ValueError("Could not change password. Check ldap_dn and ldap_new_password are valid")

            finally:
              # Unbind connection
              c.unbind()

            if not ldap_return_new_password:
              ldap_new_password = '********'
            
            ##############################################


            results = {
                "success": res,
                "domain_name": ldap_domain_name,
                "user_dn": ldap_dn,
                "new_password": ldap_new_password
            }

            yield StatusMessage("Finished 'ldap_utilities_set_password' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()


def generate_password(pwd_len=8):
    # Random password generator
    pwd = [random.choice(string.digits),random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase),random.choice('*#$%&/-_!?')] + random.choices(string.digits+string.ascii_letters+'*#$%&/-_!?', k=pwd_len-4)
    random.shuffle(pwd)
    return ''.join(pwd) 