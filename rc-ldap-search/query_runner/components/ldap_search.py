"""Action Module circuits component to update incidents from LDAP searches"""
from pkg_resources import Requirement, resource_filename
import logging
from datetime import datetime
import time
import copy
import json
from string import Template
import resilient_circuits.template_functions as template_functions
from query_runner.lib.query_action import QueryRunner
import ldap3
from ldap3 import Server, Connection, STRING_TYPES
import ast
try:
    basestring
except NameError:
    basestring = str

LOG = logging.getLogger(__name__)
CONFIG_DATA_SECTION = 'AD'
LDAP_DEFAULT_PORT = 389
LDAP_AUTH_TYPES = {"ANONYMOUS": ldap3.ANONYMOUS,
                   "SIMPLE": ldap3.SIMPLE,
                   "SASL": ldap3.SASL,
                   "NTLM": ldap3.NTLM}

# Active Directory domains
DOMAIN_CLIENT = "CLIENT"

def config_section_data():
    """sample config data for use in app.config"""
    section_config_fn = resource_filename(Requirement("rc-ldap-search"), "query_runner/data/app.config.ldap")
    query_dir = resource_filename(Requirement("rc-ldap-search"), "query_runner/data/queries_ldap")

    with open(section_config_fn, 'r') as section_config_file:
        section_config = Template(section_config_file.read())
        return section_config.safe_substitute(directory=query_dir)

class LDAPIncidentUpdate(QueryRunner):
    """ Acknowledges and fires off new query requests """

    def __init__(self, opts):
        query_options = opts.get(CONFIG_DATA_SECTION, {})
        super(LDAPIncidentUpdate, self).__init__(opts, query_options, run_search,
                                                 wait_for_complete=True)


#############################
# Functions for running Query
#############################
def run_search(options, query_definition, event_message):
    """ Run LDAP search and return result """
    # Read the LDAP configuration options
    ldap_server = options["server"]
    ldap_port = int(options["port"] or LDAP_DEFAULT_PORT)
    ldap_user = options["user"]
    ldap_password = options["password"]
    ldap_ssl = options["ssl"] == "True"  # anything else is false
    ldap_auth = LDAP_AUTH_TYPES[options["auth"] or "ANONYMOUS"]
    results = None
    # CLIENT Active Directory
    client_ad_server = Server(ldap_server,
                              ldap_port,
                              get_info=ldap3.ALL, use_ssl=options["ssl"] == "True",
                              connect_timeout=3)

    client_ad_creds = (ldap_user,
                       ldap_password,
                       ldap_auth)

    if query_definition.params is None:
        raise Exception("LDAP query requires 'search_base' parameter")
    search_base = query_definition.params.get("search_base")
    if search_base is None:
        raise Exception("LDAP query requires 'search_base' parameter")

    query_definition_attributes = query_definition.params.get("attributes")

    ldap_attributes = ldap3.ALL_ATTRIBUTES
    return_empty_attributes = True
    if query_definition_attributes and query_definition_attributes is not None:
        ldap_attributes = ast.literal_eval(query_definition_attributes)
        return_empty_attributes = False

    # Connect to the LDAP server
    LOG.debug("LDAP connect")
    with Connection(client_ad_server,
                    user=client_ad_creds[0],
                    password=client_ad_creds[1],
                    authentication=client_ad_creds[2],
                    auto_bind=True,
                    return_empty_attributes=return_empty_attributes) as conn:

        LOG.debug("LDAP search {0} / {1} / {2}".format(search_base, query_definition.query, ldap_attributes))
        conn.search(search_base,
                    query_definition.query,
                    attributes=ldap_attributes)

        entries = conn.entries
        if entries is None:
            LOG.info("LDAP query returned None")
            results = {"entries": None}
            if query_definition.default:
                mapdata = copy.deepcopy(event_message)
                mapdata.update(query_definition.vars)
                mapdata.update({"query": query_definition.query})
                default_template = json.dumps({"entries": [query_definition.default]}, indent=2)
                default_rendered = template_functions.render_json(default_template, mapdata)
                results = default_rendered
        else:
            # List of entries.
            entries = json.loads(conn.response_to_json())["entries"]
            LOG.info("Result contains %s entries", len(entries))
            # Each entry has 'dn' and dict of 'attributes'.  Move attributes to the top level for easier processing.
            for entry in entries:
                entry.update(entry.pop("attributes", None))
            results = {"entries": entries}

    LOG.debug(json.dumps(results, indent=2))
    return results
# end run_search
