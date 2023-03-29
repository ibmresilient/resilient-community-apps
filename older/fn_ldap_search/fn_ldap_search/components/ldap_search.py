# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to execute queries against an LDAP server """

# Set up:
# Destination: a Queue named "ldap".
# Manual Action: Execute a query against an LDAP server.

import logging
import json
import re

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import ldap3
from ldap3 import Server, Connection, ALL
from ldap3.core.exceptions import LDAPSocketOpenError, LDAPNoSuchObjectResult, LDAPInvalidCredentialsResult, \
    LDAPInvalidFilterError, LDAPAttributeError, LDAPObjectClassError
from ldap3.utils.conv import escape_filter_chars, to_unicode
from ldap3.utils.config import get_config_parameter

LOG = logging.getLogger(__name__)
LDAP_PORT_DEF = 389
LDAP_PORT_SSL = 636
LDAP_AUTH_TYPES = ["ANONYMOUS", "SIMPLE", "NTLM", "SASL"]
LDAP_AUTH_DEF = "ANONYMOUS"

class FunctionComponent(ResilientComponent):


    """Component that implements Resilient function 'ldap_search'

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
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ldap_search", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ldap_search", {})

    def validate_params(self, search_params):
        """"Check mandatory fields

        Do a number of checks on input fields.

        """
        if search_params is None:
            raise Exception("LDAP query requires parameters dictionary to be set")

        for k in search_params:
            if re.match('^search_filter$', k) and not search_params[k]:
                raise ValueError("LDAP query requires '{}' parameter to be a non empty value".format(k))
            else:
                if re.match('^search_filter$', k):
                    # Do some basic checks on filter.
                    if not re.match('^\(.*\)$', search_params[k]):
                        # Outer parentheses not found thus invalid filter
                        raise ValueError("LDAP search filter invalid format")
                    if not search_params[k].count('(') == search_params[k].count(')'):
                        # The count of '(' and ')' characters need to match in filter.
                        raise LDAPInvalidFilterError("Invalid filter because of unmatched parentheses.")

    def update_param_fields(self, search_params):
        """"Update %param% fields

        Escape some characters in search_params[search_filter].
        If search_params[search_filter] hash key has %param% set in it's value, update
        value replacing %param% with actual escaped value from param.


        """
        for k in search_params:
            if re.match('^search_filter$', k):
                # Escape some characters in search_filter which might cause LDAP injection.
                search_params[k] = self.escape_chars(search_params[k])
            # Search for "%ldap_param% token in parameter.
            if re.search("%ldap_param%", search_params[k]):
                # Only allow "%ldap_param% in search_filter field.
                if re.match('^search_filter$', k):
                    if "param" not in search_params:
                        raise Exception ("The parameter '{}' contains string token '%ldap_param%' but parameter '{}' "
                                         "is blank.".format(k, "param"))
                    else:
                        # Insert escaped param value in filter, need to escape any backslashes X 2 for regex.
                        search_params[k] = re.sub("%ldap_param%", search_params["param"].replace('\\', '\\\\'), search_params[k])
                        LOG.debug(('Transformed parameter'+k+' to '+search_params[k]))
                else:
                    raise Exception(
                        "The string %ldap_param% not allowed in parameter '{}' ".format(k))


    def get_creds(self):
        """"Get LDAP credentials from configuration settings.

        Validates user, password and auth values from config file to
        setup the credentials.

        Returns a tuple value.

        """
        ldap_user = self.options.get("user", "").strip('\'"')
        ldap_domain = self.options.get("domain", "")
        ldap_password = self.options.get("password", "")
        ldap_auth = self.options.get("auth", "")
        ldap_user_split = None

        if ldap_auth.upper() not in LDAP_AUTH_TYPES:
            raise ValueError("Invalid value for 'auth' configuration setting")

        if ldap_auth.upper() == "SASL":
            raise Exception("Connection using SASL authentication not currently implemented.")

        if ldap_user and '\\' in ldap_user:
            # User can have a domain value pre-pended if connecting to Active Directory server.
            ldap_user_split = ldap_user.split("\\")
            if len(ldap_user_split) > 2:
                # If '\' character appears more than once throw error.
                raise ValueError("Invalid value '{}' for 'user'.".format(ldap_user))
            if len(ldap_user_split[1]) == 0:
                raise ValueError("Invalid empty value for user after the '\\' character in 'user' config option.")
            if len(ldap_user_split[0]) == 0:
                raise ValueError("Invalid empty value for domain before the '\\' character in 'user' config option.")

        if (not ldap_user and ldap_password) or (ldap_user and not ldap_password):
            raise Exception("User and password required to be set as a pair.")

        if ldap_auth.upper() in LDAP_AUTH_TYPES:
            ldap_auth = ldap_auth.upper()
        else:
            ldap_auth = LDAP_AUTH_DEF

        if (ldap_user and ldap_password) and (ldap_auth.upper() == "ANONYMOUS"):
            raise Exception("If 'user' and 'password' values are both set 'auth=ANONYMOUS' is not allowed.")
        elif (not ldap_user and not ldap_password) and (ldap_auth.upper() != "ANONYMOUS"):
            raise Exception("Empty 'user' and 'password' values can only be used with 'auth=ANONYMOUS'.")


        if ldap_domain or ldap_auth.upper() == "NTLM":
            # Looks like we are pointing at an Active Directory server.(Note: AD can also use auth='SIMPLE').
            if (not ldap_domain and not ldap_user_split):
                # If we got here 'auth' = 'NTLM' but no domain specified in 'domain' or 'user'.
                raise Exception("Connection using AD requires a 'domain' to be specified.")
            elif ldap_domain and not ldap_user_split:
                # If we got here 'domain' is set and no domain specified in 'user' configuration option.
                # Prepend domain to user.
                ldap_user = "{}\\{}".format(ldap_domain, ldap_user)
            elif ldap_domain and len(ldap_user_split) == 2:
                # Check to see if ldap_domain and ldap_user_split[0] match.
                if ldap_domain.upper() != ldap_user_split[0].upper():
                    raise Exception("Conflicting domain names '{}' and '{}' specified for credentials."
                                    .format(ldap_domain, ldap_user_split[0]))


        return(ldap_user, ldap_password, ldap_auth)

    def str_to_bool(self, str):
        """"Convert unicode string to equivalent boolean value

        Converts a "true" or "false" string to a boolean value , string is case insensitive.

        """
        if str.lower() == 'true':
            return True
        elif str.lower() == 'false':
            return False
        else:
            raise ValueError

    def escape_chars(self, str, encoding=None):
        """ Escape some characters in filter.

        Escape a set of characters in the filter string to help to mitigate against possibility of injection.
        This has a subset of characters escaped in ldap3 function escape_filter_chars.

        """
        if encoding is None:
            encoding = get_config_parameter('DEFAULT_ENCODING')

        str = to_unicode(str, encoding)
        escaped_str = str.replace('\\', '\\5c')
        escaped_str = escaped_str.replace('*', '\\2a')
        escaped_str = escaped_str.replace('\x00', '\\00')

        return escaped_str

    def setup_ldap_connection(self):
        """ Setup LDAP server connection

        Setups up LDAP server and connection objects using LDAP server credentials obtained from the config file.
        Adds the LDAP connection as a class property.

        """
        if "server" in self.options:
            ldap_server = self.options["server"]
        else:
            raise Exception("Mandatory config setting 'server' not set.")
        ldap_port = int(self.options["port"] or LDAP_PORT_DEF)
        if "use_ssl" in self.options:
            ldap_use_ssl = self.str_to_bool(self.options["use_ssl"])
        else:
            raise Exception("Credentials parameter 'use_ssl' not set.")
        if ldap_use_ssl and (ldap_port != LDAP_PORT_SSL):
            # Should be port 636 for encrypted connections.
            raise Exception("If 'use_ssl' set to 'True' the port needs to be set to '{}'".format(LDAP_PORT_SSL))
        else:
            ldap_port = int(self.options["port"] or LDAP_PORT_DEF)

            ldap_user, ldap_password, ldap_auth = self.get_creds()

        if "connect_timeout" in self.options:
            connect_timeout = int(self.options["connect_timeout"])
        else:
            LOG.debug(type(self.options["connect_timeout"]))
            raise Exception("Mandatory config setting 'connect_timeout' not set.")

        try:
            # Create LDAP Server object.
            LOG.debug("Create LDAP server object")
            server = Server(ldap_server, port=ldap_port, get_info=ALL, use_ssl=ldap_use_ssl, connect_timeout=connect_timeout )
            # Connect to the LDAP server.

            connection = Connection(server, user=ldap_user, password=ldap_password, authentication=ldap_auth,
                                        auto_bind=True, return_empty_attributes=True, raise_exceptions=True)

        # Catch some specific exceptions
        except (LDAPSocketOpenError, LDAPInvalidCredentialsResult) as e:
            raise e

        # Catch any additional errors not specifically checked for
        except Exception as e:
            raise Exception("Could not connect to LDAP server %s, Exception %s", ldap_server, e)

        try:
            connection
        except Exception as e:
            raise Exception("No LDAP connection returned for server %s, Exception $s",ldap_server, e)

        return connection

    def run_search(self, search_params, connection):
        """ Run LDAP search/query

        Run LDAP search using input parameters and return result.

        """
        results = None
        return_empty_attributes = True

        search_base = search_params.get("search_base")
        search_filter = search_params.get("search_filter")
        search_attributes = search_params.get("search_attributes")

        if search_attributes and search_attributes is not None:
            attributes = search_attributes.split(',')
            search_attributes = [str(attr) for attr in attributes]


        # Do LDAP search
        LOG.debug("Do LDAP search")
        with connection as conn:

            LOG.debug("LDAP query with base: {0}, filter: {1}, attributes: {2}".format(search_base, search_filter, search_attributes))
            try:
                conn.search(search_base,
                            search_filter,
                            attributes=search_attributes)

                entries = conn.entries

            # Catch some specific exceptions
            except (LDAPNoSuchObjectResult, LDAPObjectClassError, LDAPInvalidFilterError, LDAPAttributeError) as e:
                raise e

            # Catch any errors not specifically tested for.
            except Exception as e:
                raise Exception("Could not perform a query on LDAP connection, got Exception %s",  e)

            try:
                entries
            except NameError:
                raise Exception("No LDAP entry returned")

            if entries is None:
                LOG.info("LDAP query returned None")
                results = {"entries": None}
            else:
                # List of entries.
                entries = json.loads(conn.response_to_json())["entries"]
                LOG.info("Result contains %s entries", len(entries))
                # Each entry has 'dn' and dict of 'attributes'.  Move attributes to the top level for easier processing.
                for entry in entries:
                    LOG.debug(json.dumps(entry))
                    entry.update(entry.pop("attributes", None))
                results = {"entries": entries}

        return results


    @function("ldap_search")
    def _ldap_search_function(self, event, *args, **kwargs):
        """Resilient Function: entry point """
        try:
            # Get the function parameters:
            ldap_search_base = kwargs.get("ldap_search_base")  # text
            ldap_search_filter = self.get_textarea_param(kwargs.get("ldap_search_filter"))  # textarea
            ldap_search_attributes = kwargs.get("ldap_search_attributes")  # text
            ldap_param = kwargs.get("ldap_param")  # text

            LOG.info("ldap_search_base: %s", ldap_search_base)
            LOG.info("ldap_search_filter: %s", ldap_search_filter)
            LOG.info("ldap_search_attributes: %s", ldap_search_attributes)
            LOG.info("ldap_param: %s", ldap_param)

            search_params = {'search_base': ldap_search_base, 'search_filter': ldap_search_filter,
                             'search_attributes': ldap_search_attributes}
            if ldap_param:
                # Escape 'param' parameter.
                search_params.setdefault('param', escape_filter_chars(ldap_param))
            yield StatusMessage("Starting...")
            self.validate_params(search_params)
            self.update_param_fields(search_params)
            connection = self.setup_ldap_connection()
            yield StatusMessage("Running LDAP query...")
            results = self.run_search(search_params, connection)
            yield StatusMessage("done...")
            LOG.debug(json.dumps(results))
            # Produce a FunctionResult with the return value.
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
