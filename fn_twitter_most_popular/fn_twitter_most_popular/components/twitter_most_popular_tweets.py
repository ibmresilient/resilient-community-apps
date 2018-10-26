# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


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
        try:
            # Get the function parameters:
            twitter_search_tweet_string = self.get_textarea_param(kwargs.get("twitter_search_tweet_string"))  # textarea
            twitter_search_tweet_count = kwargs.get("twitter_search_tweet_count")  # number

            log = logging.getLogger(__name__)
            log.info("twitter_search_tweet_string: %s", twitter_search_tweet_string)
            log.info("twitter_search_tweet_count: %s", twitter_search_tweet_count)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()