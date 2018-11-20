# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

'''
tested with pytest --resilient_app_config=/path/to/.resilient/app.config
'''
PACKAGE_NAME = "fn_geocoding"
FUNCTION_NAME = "geocoding"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_geocoding_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("geocoding", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("geocoding_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestGeocoding:
    """ Tests for the geocoding function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("geocoding_source, geocoding_data, expected_results", [
        ('latlng', "42.3656119,-71.0805841", "75 Binney St, Cambridge, MA 02142, USA"),
        ('address', "75 Binney St, Cambridge, MA 02142, USA", "42.3656119,-71.0805841")
    ])
    def test_success(self, circuits_app, geocoding_source, geocoding_data, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "geocoding_source": geocoding_source,
            "geocoding_data": geocoding_data
        }
        results = call_geocoding_function(circuits_app, function_params)
        print (results)
        if geocoding_source == 'address':
            result = "{},{}".format(results['response']['results'][0]['geometry']['location']['lat'],
                               results['response']['results'][0]['geometry']['location']['lng'])
        elif geocoding_source == 'latlng':
            result = results['response']['results'][0]['formatted_address']

        assert(expected_results == result)