# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import get_mock_config
from mock import mock, patch, MagicMock
from twython.api import Twython
from fn_twitter_most_popular.util.twython_facade import TwythonFacade


PACKAGE_NAME = "fn_twitter_most_popular"
FUNCTION_NAME = "twitter_most_popular_tweets"

# Read the default configuration-data section from the package
#config_data = get_config_data(PACKAGE_NAME)
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_twitter_most_popular_tweets_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("twitter_most_popular_tweets", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("twitter_most_popular_tweets_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestTwitterMostPopularTweets:
    """ Tests for the twitter_most_popular_tweets function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("twitter_search_tweet_string, twitter_search_tweet_count, expected_results", [
        ({"type": "text", 'content': '{\n"hashtags":[ "Malware"]\n}'}, 123, {"value": "xyz"}),
        ({"type": "text", 'content': '{\n"hashtags":[ "Botnet", "Cybersecurity", "Malware"]\n}'}, 123, {"value": "xyz"}),
        ({"type": "text", 'content': '{\n"hashtags":[ "Викрито ", "хакера"]\n}'}, 123, {"value": "xyz"})

    ])
    def test_success(self, circuits_app, twitter_search_tweet_string, twitter_search_tweet_count, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "twitter_search_tweet_string": twitter_search_tweet_string,
            "twitter_search_tweet_count": twitter_search_tweet_count
        }

        result_mock = MagicMock()
        result_mock = [{
            "value":"mock"
        },
        {
            "value": "mock"
        },
        ]
        with patch.object(TwythonFacade, "__init__", lambda x,api_key,api_secret, log,client_args: None) as mock_session1:
            with patch.object(TwythonFacade, "search_for_tweets",
                              lambda x, query, count: result_mock):

                results = call_twitter_most_popular_tweets_function(circuits_app, function_params)
                assert(results["success"] is True)
