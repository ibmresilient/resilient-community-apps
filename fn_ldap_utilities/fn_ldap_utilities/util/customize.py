# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""Generate the Resilient customizations required for fn_ldap_utilities"""

import base64
import os
import io
try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the fn_ldap_utilities package
    """
    return {
        "package": u"fn_ldap_utilities",
        "message_destinations": [u"fn_ldap_utilities"],
        "functions": [u"ldap_utilities_add", u"ldap_utilities_add_to_groups", u"ldap_utilities_remove_from_groups", u"ldap_utilities_search", u"ldap_utilities_set_password", u"ldap_utilities_toggle_access", u"ldap_utilities_update"],
        "workflows": [],
        "actions": [],
        "incident_fields": [u"ldap_base_dn", u"ldap_domain_name"],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [u"ldap_query_results"],
        "automatic_tasks": [],
        "scripts": [u"No search results"],
        "playbooks": [u"example_ldap_utilities_add", u"example_ldap_utilities_add_users_to_groups", u"example_ldap_utilities_remove_users_from_groups", u"example_ldap_utilities_search", u"example_ldap_utilities_set_password", u"example_ldap_utilities_toggle_access", u"example_ldap_utilities_update"]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 48.2.16

    Contents:
    - Message Destinations:
        - fn_ldap_utilities
    - Functions:
        - ldap_utilities_add
        - ldap_utilities_add_to_groups
        - ldap_utilities_remove_from_groups
        - ldap_utilities_search
        - ldap_utilities_set_password
        - ldap_utilities_toggle_access
        - ldap_utilities_update
    - Playbooks:
        - example_ldap_utilities_add
        - example_ldap_utilities_add_users_to_groups
        - example_ldap_utilities_remove_users_from_groups
        - example_ldap_utilities_search
        - example_ldap_utilities_set_password
        - example_ldap_utilities_toggle_access
        - example_ldap_utilities_update
    - Incident Fields:
        - ldap_base_dn
        - ldap_domain_name
    - Data Tables:
        - ldap_query_results
    - Scripts:
        - No search results
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)