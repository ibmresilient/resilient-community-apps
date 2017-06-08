"""System Integration Tests for Active Directory LDAP Search component"""
from __future__ import print_function

import os.path
import pytest
import query_runner.components.ldap_search

config_data = query_runner.components.ldap_search.config_section_data()

@pytest.mark.usefixtures("configure_resilient")
class TestLDAPSearchIntegrationTests:
    """ System tests for the LDAP Search component """
    # Appliance Configuration Requirements
    destinations = ("ldap",)

    def test_load(self, circuits_app, new_incident):
        """ Successful value lookup """
        # Just a placeholder test to at least verify component installs and runs
        pass
