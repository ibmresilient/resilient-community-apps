"""System Integration Tests for Ariel Query component"""
from __future__ import print_function

import os.path
import pytest
import query_runner.components.ariel_query

config_data = query_runner.components.ariel_query.config_section_data()

@pytest.mark.usefixtures("configure_resilient")
class TestQRadarSearchIntegrationTests:
    """ System tests for the Ariel Query component """
    # Appliance Configuration Requirements
    destinations = ("ariel",)

    def test_load(self, circuits_app, new_incident):
        """ Successful value lookup """
        # Just a placeholder test to at least verify component installs and runs
        pass
