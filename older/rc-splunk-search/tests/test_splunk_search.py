"""System Integration Tests for Splunk Search component"""
from __future__ import print_function

import os.path
import pytest
import query_runner.components.splunk_search

config_data = query_runner.components.splunk_search.config_section_data()

@pytest.mark.usefixtures("configure_resilient")
class TestSplunkSearchIntegrationTests:
    """ System tests for the Splunk Search component """
    # Appliance Configuration Requirements
    destinations = ("splunk",)

    def test_load(self, circuits_app, new_incident):
        """ Successful value lookup """
        # Just a placeholder test to at least verify component installs and runs
        pass
