# -*- coding: utf-8 -*-

"""Action Module circuits component to post a tweet to Twitter"""

import logging
from circuits.core.handlers import handler
from resilient_circuits.actions_component import ResilientComponent
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

    @handler("post_to_twitter")
    def _post_tweet(self, event, *args, **kwargs):
        # Get the incident ID and tweet body
        properties = event.message['properties']
        tweet_body = properties['tweet_body']

        LOG.info(u'the tweet is: %s', tweet_body)
        twitter = Twitter(auth=OAuth(self.options['oauth_token'],
                                     self.options['oauth_secret'],
                                     self.options['consumer_key'],
                                     self.options['consumer_secret']))
        twitter.statuses.update(status=unicode(tweet_body))

        # Log output
        LOG.info("Posted tweet to twitter! :D")

        yield "Tweet Posted"
    # end _post_tweet
