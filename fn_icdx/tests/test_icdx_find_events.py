# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
import json
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock import patch
import mock

from fn_icdx.util.amqp_facade import AmqpFacade
from fn_icdx.util.helper import ICDXHelper
from amqpmock import AmqpFacadeMock, mocked_call, is_json
import pika
PACKAGE_NAME = "fn_icdx"
FUNCTION_NAME = "icdx_find_events"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_icdx_find_events_function(circuits, function_params, timeout=30):
    # Fire a message to the function
    evt = SubmitTestFunction("icdx_find_events", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("icdx_find_events_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestIcdxFindEvents:
    """ Tests for the icdx_utilities_find_events function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("icdx_search_request, expected_results", [
        ({"type": "text", "content": json.dumps({
              "id" : 1,
              "start"  : "-14d",
              "end"    : "-7d",
              "where"  : "type_id = 8031",
              "filter" : "threat.type_id = 1 OR threat.type_id = 4",
              "fields" : ["time",
                          "device_name",
                          "device_ip",
                          "threat.name",
                          "threat.type_id",
                          "threat.risk_id",
                          "file.name"
              ],
              "limit"  : 100
              })}, {"value": "xyz"}),
        ({"type": "text", "content": json.dumps({
               "id" : 1,
               "start"  : "-24h",
               "where"  : "type_id = 8031",
               "fields" : ["time", "device_name",
               "device_ip"
               ,"device_uuid"],
               "limit"  : 2,
               "next":"2a10ab40-0afc-11e5-dcda-00000000f8d8"
               })}, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, icdx_search_request, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "icdx_search_request": icdx_search_request
        }
        # Mock acquiring the config options, all config options are set to '10' or 10
        with patch.object(ICDXHelper, "get_config_option", lambda x, y,z=None: "10", True):
            # Mock both the AMQP connection and the channel
            with patch('pika.BlockingConnection') as mock_block, \
                    patch.object(pika.BlockingConnection, 'channel') as mock_block_channel:
                # Mock the actual AMQP call
                with patch.object(AmqpFacade, 'call') as mock_amqp:
                    mock_amqp.return_value = mocked_call(payload=json.dumps(icdx_search_request['content']), success=True,operation='find_events')

                    mock_block.return_value = mock.Mock()
                    mock_block_channel.return_value = mock.Mock()
                    results = call_icdx_find_events_function(circuits_app, function_params)
                    assert(results['success'] == True)

    @pytest.mark.parametrize("icdx_search_request, expected_results", [
        ({"type": "text", "content": json.dumps({
            "id": 1,
            "start": "-14d",
            "end": "-7d",
            "where": "type_id = 8031",
            "filter": "threat.type_id = 1 OR threat.type_id = 4",
            "fields": ["time",
                       "device_name",
                       "device_ip",
                       "threat.name",
                       "threat.type_id",
                       "threat.risk_id",
                       "file.name"
                       ],
            "limit": 100
        })}, {"value": "xyz"}),
        ({"type": "text", "content": json.dumps({
            "id": 1,
            "start": "-24h",
            "where": "type_id = 8031",
            "fields": ["time", "device_name",
                       "device_ip"
                , "device_uuid"],
            "limit": 2,
            "next": "2a10ab40-0afc-11e5-dcda-00000000f8d8"
        })}, {"value": "xyz"})
    ])
    def test_failure(self, circuits_app, icdx_search_request, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "icdx_search_request": icdx_search_request
        }
        # Mock acquiring the config options, all config options are set to '10' or 10
        with patch.object(ICDXHelper, "get_config_option", lambda x, y,z=None: "10", True):
            # Mock both the AMQP connection and the channel
            with patch('pika.BlockingConnection') as mock_block, \
                    patch.object(pika.BlockingConnection, 'channel') as mock_block_channel:
                # Mock the actual AMQP call
                with patch.object(AmqpFacade, 'call') as mock_amqp:
                    mock_amqp.return_value = mocked_call(payload=json.dumps(icdx_search_request['content']),
                                                         success=False, operation='find_events')

                    mock_block.return_value = mock.Mock()
                    mock_block_channel.return_value = mock.Mock()
                    results = call_icdx_find_events_function(circuits_app, function_params)
                    assert (results['success'] == False)

    @pytest.mark.parametrize("icdx_search_request, expected_results", [
        ({"type": "text", "content": json.dumps({
            "id": 1,
            "start": "-14d",
            "end": "-7d",
            "where": "type_id = 8031",
            "filter": "threat.type_id = 1 OR threat.type_id = 4",
            "fields": ["time",
                       "device_name",
                       "device_ip",
                       "threat.name",
                       "threat.type_id",
                       "threat.risk_id",
                       "file.name"
                       ],
            "limit": 100
        })}, {"value": "xyz"}),
        ({"type": "text", "content": json.dumps({

            "start": "-24h",
            "where": "type_id = 8031",
            "fields": ["time", "device_name",
                       "device_ip"
                , "device_uuid"],
            "limit": 2,
            "next": "2a10ab40-0afc-11e5-dcda-00000000f8d8"
        })}, {"value": "xyz"})
    ])
    def test_payload_validation(self, circuits_app, icdx_search_request, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "icdx_search_request": icdx_search_request
        }
        # Mock acquiring the config options, all config options are set to '10' or 10
        with patch.object(ICDXHelper, "get_config_option", lambda x, y,z=None: "10", True):
            # Mock both the AMQP connection and the channel
            with patch('pika.BlockingConnection') as mock_block, \
                    patch.object(pika.BlockingConnection, 'channel') as mock_block_channel:
                # Mock the actual AMQP call
                with patch.object(AmqpFacade, 'call') as mock_amqp:
                    if "id" not in json.loads(icdx_search_request['content']):
                        '''
                        If the "ID" attribute is missing from the payload
                        The function will return rather than raise an exception
                        but empty results are returned 
                        '''

                        mock_amqp.return_value = mocked_call(payload=json.dumps(icdx_search_request['content']),
                                                             success=False, operation='find_events')

                        mock_block.return_value = mock.Mock()
                        mock_block_channel.return_value = mock.Mock()
                        results = call_icdx_find_events_function(circuits_app, function_params)
                        assert(results['success'] == False)
                        assert (results['num_of_results'] == 0)

                    else:
                        mock_amqp.return_value = mocked_call(payload=json.dumps(icdx_search_request['content']),
                                                             success=False, operation='find_events')

                        mock_block.return_value = mock.Mock()
                        mock_block_channel.return_value = mock.Mock()
                        results = call_icdx_find_events_function(circuits_app, function_params)
                        assert (results['success'] == False)


    def test_amqp_client_success(self):
        amqp_client = AmqpFacadeMock()
        result, status_code = amqp_client.call(payload=json.dumps({"id": 1}), success=True)
        assert(status_code == 200)

    def test_amqp_client_failure(self):
        amqp_client = AmqpFacadeMock()
        result, status_code = amqp_client.call(payload=json.dumps({"id": 1}), success=False)
        assert(status_code == 204)