# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import inspect
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_twitter_most_popular.util.twython_facade import TwythonFacade


class FunctionPayload:
    """Class that contains the payload sent back to UI and available in the post-processing script"""

    def __init__(self, inputs):
        self.success = True
        self.inputs = {}
        self.tweets = None

        for input in inputs:
            self.inputs[input] = inputs[input]

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'twitter_most_popular_tweets"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_twitter_most_popular", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_twitter_most_popular", {})

    @function("twitter_most_popular_tweets")
    def _twitter_most_popular_tweets_function(self, event, *args, **kwargs):
        """Function: A function with targets the Twitter Search API. Takes in an input of a multiple possible hashtags and a number of Tweets to be returned and contacts the Twitter Search API to return the results. Requires Twitter Access Key and Secret to obtain a OAuth2 read-only token."""


        # Inner Function used to get config:

        def get_config_option(option_name, optional=False):
            """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
            option = self.options.get(option_name)

            if not option and optional is False:
                err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(
                    option_name)
                raise ValueError(err)
            else:
                return option

        def setup_proxies(http_proxy, https_proxy):
            if http_proxy is None and https_proxy is None:
                return None
            else:
                client_args = {
                    'proxies': {
                        'http': http_proxy,
                        'https': https_proxy,
                    }
                }
                return client_args

        try:
            # Get the function parameters:
            twitter_search_tweet_string = self.get_textarea_param(kwargs.get("twitter_search_tweet_string"))  # textarea
            twitter_search_tweet_count = kwargs.get("twitter_search_tweet_count")  # number
            yield StatusMessage("starting...")
            log = logging.getLogger(__name__)
            log.info("twitter_search_tweet_string: %s", twitter_search_tweet_string)
            log.info("twitter_search_tweet_count: %s", twitter_search_tweet_count)

            query = json.loads(twitter_search_tweet_string)["hashtags"]
            # Create payload dict with inputs
            payload = FunctionPayload({
                "twitter_search_tweet_string": query,
                "twitter_search_tweet_count": twitter_search_tweet_count
            })

            log.info("Setting up Twython")
            twitter = TwythonFacade(api_key=get_config_option(option_name="twitter_api_key"), api_secret=get_config_option(option_name="twitter_api_secret"), log=log, client_args=setup_proxies(get_config_option(option_name="twitter_proxy_http", optional=True),get_config_option(option_name="twitter_proxy_https", optional=True)))
            yield StatusMessage("Config Inputs Gathered. Sending Search request")
            payload.tweets = twitter.search_for_tweets(query=query, count=twitter_search_tweet_count)

            if len(payload.tweets) > 0:
                yield StatusMessage("Got results back")

            else:
                yield StatusMessage("Got no results.")
                payload.success = False
            yield StatusMessage("Complete")


            # Produce a FunctionResult with the results
            yield FunctionResult(payload.as_dict())
        except Exception:
            yield FunctionError()