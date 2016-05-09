#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Action Module circuits component to post a tweet to Twitter"""

from __future__ import print_function
import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent, ActionMessage
from twitter import *
LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'twitterpost'


class TwitterPostComponent(ResilientComponent):
    """Action modules component to post a tweet when called"""

    # This component posts a tweet to Twitter

    def __init__(self, opts):
        super(TwitterPostComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})
        LOG.debug(self.options)

        # The queue name can be specified in the config file,
        # or default to 'twitterpost'
        self.channel = "actions." + self.options.get("queue", "twitterpost")

    @handler()
    def _post_tweet(self, event, *args, **kwargs):
        """The @handler() annotation without an event name makes this
           a default handler - for all events on this component's queue.
           This will be called with some "internal" events from Circuits,
           so you must declare the method with the generic parameters
           (event, *args, **kwargs), and ignore any messages that are not
           from the Actions module.
        """

        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return

        # Get the incident ID and tweet body
        incident = event.message["incident"]
        inc_id = incident["id"]
        properties = event.message['properties']
        tweet_body = properties['tweet_body']

        print('the tweet is:', tweet_body)
        twitter = Twitter(auth=OAuth(self.options['oauth_token'],
                                     self.options['oauth_secret'],
                                     self.options['consumer_key'],
                                     self.options['consumer_secret']))
        twitter.statuses.update(status=str(tweet_body))

        # Log output
        LOG.info("Posted tweet to twitter! :D", inc_id)

        yield "User updated!"
        # end _post_tweet
