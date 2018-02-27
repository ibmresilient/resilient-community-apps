# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import ldap3
from ldap3 import Server, Connection, ALL

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ldap_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("functions_ldap_search", {})
        self.ldap_port_def = 389
        self.ldap_auth_def = "ANONYMOUS"
        self.ldap_auth_types = ["ANONYMOUS", "SIMPLE"]

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("functions_ldap_search", {})

    def str_to_bool(self, str):
        """"Convert unicode string to equivalent boolean value"""
        if str.lower() == 'true':
            return True
        elif str.lower() == 'false':
            return False
        else:
            raise ValueError

    def setup_ldap_connection(self):
        """ Setup LDAP server connection """
        # Read the LDAP configuration options

        ldap_server = self.options["server"]
        ldap_port = int(self.options["port"] or self.ldap_port_def)
        ldap_user = self.options["user"]
        ldap_password = self.options["password"]
        ldap_use_ssl = self.str_to_bool(self.options["use_ssl"])
        if self.options["auth"].upper() in self.ldap_auth_types:
            ldap_auth = self.options["auth"].upper()
        else:
            ldap_auth = self.ldap_auth_def

        try:
            # Create LDAP Server object
            LOG.debug("Create LDAP server object")
            server = Server(ldap_server, port=ldap_port, get_info=ALL, use_ssl=ldap_use_ssl, connect_timeout=3 )
            # Connect to the LDAP server

            self.connection = Connection(server, user=ldap_user, password=ldap_password, authentication=ldap_auth,
                                        auto_bind=True, return_empty_attributes=True, raise_exceptions=True)
        except Exception as e:
            LOG.debug("Could not connect to LDAP server %s, Exception %s", ldap_server, e)

        try:
            self.connection
        except Exception as e:
            raise Exception("No LDAP connection returned for server %s, Exception $s",ldap_server, e)


    def run_search(self):
        """ Run LDAP search and return result """

        results = None
        return_empty_attributes = True

        if self.search_params is None:
            raise Exception("LDAP query requires 'search_base' parameter")
        search_base = self.search_params.get("search_base")
        if search_base is None:
            raise Exception("LDAP query requires 'search_base' parameter")
        search_filter = self.search_params.get("search_filter")
        if search_filter is None:
            raise Exception("LDAP query requires 'search_filter' parameter")
        search_attributes = self.search_params.get("search_attributes")

        if search_attributes and search_attributes is not None:
            attributes = search_attributes.split(',')
            search_attributes = [str(attr) for attr in attributes]


        # Do LDAP search
        LOG.debug("Do LDAP search")
        with self.connection  as conn:

            LOG.debug("LDAP query with base: {0}, filter: {1}, attributes: {2}".format(search_base, search_filter, search_attributes))
            try:
                conn.search(search_base,
                            search_filter,
                            attributes=search_attributes)

                entries = conn.entries
            except Exception as e:
                LOG.debug("Could not perform a query on LDAP connection got Exception %s",  e)

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
        """Function: """
        try:
            # Get the function parameters:
            search_base = kwargs.get("search_base")  # text
            search_filter = self.get_textarea_param(kwargs.get("search_filter"))  # textarea
            search_attributes = kwargs.get("search_attributes")  # text

            LOG.info("search_base: %s", search_base)
            LOG.info("search_filter: %s", search_filter)
            LOG.info("search_attributes: %s", search_attributes)

            self.search_params = {'search_base': search_base, 'search_filter': search_filter,
                                  'search_attributes': search_attributes}

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("Starting...")
            yield StatusMessage("Setting up lDAP connection...")
            self.setup_ldap_connection()
            yield StatusMessage("Running LDAP query...")
            results = self.run_search()
            yield StatusMessage("done...")
            LOG.debug(json.dumps(results))
            # Produce a FunctionResult with the return value
            yield FunctionResult({"value": results})
        except Exception:
            yield FunctionError()
