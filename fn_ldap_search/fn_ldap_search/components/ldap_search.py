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
    LDAPInvalidFilterError
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
        search_base , search_filter, search_attributes

    An example of a set of query parameter might look like the following:

            search_base = "dc=example,dc=com"
            search_filter = "(&(objectClass=person)(|(uid={%param%})(uid=newton)))"
            search_attributes = "uid,cn,sn,mail,telephoneNumber"
            param = artifact.value # Assigned value 'einstein' during run.

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

    def validate_params(self):
        """"Check mandatory fields

        Do a number of checks on input fields.

        """
        if self.search_params is None:
            raise Exception("LDAP query requires parameters dictionary to be set")
        for k in self.search_params:
            if re.match('^search_', k) and not self.search_params[k]:
                raise ValueError("LDAP query requires '{}' parameter to be a non empty value".format(k))
            else:
                if re.match('^search_filter$', k):
                    # Do some basic checks on filter.
                    if not re.match('^\(.*\)$',self.search_params[k]):
                        # Outer parentheses not found thus invalid filter
                        raise ValueError("LDAP search filter invalid format")
                    if not self.search_params[k].count('(') == self.search_params[k].count(')'):
                        # The count of '(' and ')' characters need to match in filter.
                        raise LDAPInvalidFilterError("Invalid filter because of unmatched parentheses.")

    def update_param_fields(self):
        """"Update %param% fields

        Escape some characters in self.search_params[search_filter].
        If self.search_params[search_filter] hash key has %param% set in it's value, update
        value replacing %param% with actual escaped value from param.


        """
        for k in self.search_params:
            if re.match('^search_filter$', k):
                # Escape some characters in search_filter which might cause LDAP injection.
                self.search_params[k] = self.escape_chars(self.search_params[k])
            # Search for "%param% token in parameter.
            if re.search("%param%", self.search_params[k]):
                # Only allow "%param% in search_attributes field.
                if re.match('^search_filter$', k):
                    if not self.search_params["param"]:
                        raise Exception ("The parameter '{}' contains string token '%param%' but parameter '{}' is blank".format(k, "param"))
                    else:
                        # Insert escaped param value in filter, need to escape any backslashes X 2 for regex.
                        self.search_params[k] = re.sub("%param%", self.search_params["param"].replace('\\', '\\\\'), self.search_params[k])
                        LOG.debug(('Transformed parameter'+k+' to '+self.search_params[k]))
                else:
                    raise Exception(
                        "The string %param% not allowed in parameter '{}' ".format(k))


    def get_creds(self):
        """"Get LDAP credentials from configuration settings.

        Validates user, password and auth values from config file to
        setup the credentials.

        Returns a tuple value.

        """
        ldap_user = self.options.get("user", "")
        ldap_domain = self.options.get("domain", "")
        ldap_password = self.options.get("password", "")
        ldap_auth = self.options.get("auth", "")

        if ldap_auth.upper() not in LDAP_AUTH_TYPES:
            raise ValueError("Invalid value for 'auth' configuration setting")

        if ldap_auth.upper() == "SASL":
            raise Exception("Connection using SASL authentication not currently implemented.")

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

        if ldap_auth.upper() == "NTLM":
            if not ldap_domain:
                raise Exception("Connection using NTLM requires a 'domain' to be specified.")
            else:
                # Add domain to user if NTLM
                ldap_user = "{}\\{}".format(ldap_domain, ldap_user)

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

        try:
            # Create LDAP Server object.
            LOG.debug("Create LDAP server object")
            server = Server(ldap_server, port=ldap_port, get_info=ALL, use_ssl=ldap_use_ssl, connect_timeout=3 )
            # Connect to the LDAP server.

            self.connection = Connection(server, user=ldap_user, password=ldap_password, authentication=ldap_auth,
                                        auto_bind=True, return_empty_attributes=True, raise_exceptions=True)

        except LDAPSocketOpenError as e:
            raise Exception("Could not connect to LDAP server %s - SocketOpenError %s", ldap_server, e)

        except LDAPInvalidCredentialsResult as e:
            raise Exception("Invalid credentials used for server LDAP server %s, Exception %s", ldap_server, e)
        # Catch any additional errors not specifically checked for
        except Exception as e:
            raise Exception("Could not connect to LDAP server %s, Exception %s", ldap_server, e)

        try:
            self.connection
        except Exception as e:
            raise Exception("No LDAP connection returned for server %s, Exception $s",ldap_server, e)

    def run_search(self):
        """ Run LDAP search/query

        Run LDAP search using input parameters and return result.

        """
        results = None
        return_empty_attributes = True

        search_base = self.search_params.get("search_base")
        search_filter = self.search_params.get("search_filter")
        search_attributes = self.search_params.get("search_attributes")

        if search_attributes and search_attributes is not None:
            attributes = search_attributes.split(',')
            search_attributes = [str(attr) for attr in attributes]


        # Do LDAP search
        LOG.debug("Do LDAP search")
        with self.connection as conn:

            LOG.debug("LDAP query with base: {0}, filter: {1}, attributes: {2}".format(search_base, search_filter, search_attributes))
            try:
                conn.search(search_base,
                            search_filter,
                            attributes=search_attributes)

                entries = conn.entries

            except LDAPNoSuchObjectResult as e:
                raise Exception("Returned no such object from LDAP query, with Exception %s", e)

            except LDAPInvalidFilterError as e:
                raise Exception("Got a malformed from LDAP query, with Exception %s",  e)
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
            search_base = kwargs.get("search_base")  # text
            search_filter = self.get_textarea_param(kwargs.get("search_filter"))  # textarea
            search_attributes = kwargs.get("search_attributes")  # text
            param = kwargs.get("param")  # text

            LOG.info("search_base: %s", search_base)
            LOG.info("search_filter: %s", search_filter)
            LOG.info("search_attributes: %s", search_attributes)
            LOG.info("param: %s", param)

            self.search_params = {'search_base': search_base, 'search_filter': search_filter,
                                  'search_attributes': search_attributes}
            if param:
                # Escape 'param' parameter.
                self.search_params.setdefault('param', escape_filter_chars(param))
            yield StatusMessage("Starting...")
            self.validate_params()
            self.update_param_fields()
            self.setup_ldap_connection()
            yield StatusMessage("Running LDAP query...")
            results = self.run_search()
            yield StatusMessage("done...")
            LOG.debug(json.dumps(results))
            # Produce a FunctionResult with the return value.
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
