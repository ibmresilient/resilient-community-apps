"""System Integration Tests for REST Query component"""
from __future__ import print_function

import os.path
import pytest
import query_runner.components.rest_query

config_data = query_runner.components.rest_query.config_section_data()

@pytest.mark.usefixtures("configure_resilient")
class TestRESTIntegrationTests:
    """ System tests for the REST Query component """
    # Appliance Configuration Requirements
    destinations = ("rest",)

    def test_load(self, circuits_app, new_incident):
        """ Successful value lookup """
        # Just a placeholder test to at least verify component installs and runs
        pass
