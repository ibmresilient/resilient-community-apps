# (c) Copyright IBM Corp. 2018. All Rights Reserved.

from twython import Twython


class TwythonFacade: 

    def __init__(self,api_key, api_secret,log):
        """

        :param api_key: The API KEY for a Twitter Developer App
        :param api_secret: The API Secret for a Twitter Developer App.

        Both of these values are used to acquire a OAuth2 Access Token,
        :param log:
        """
        self.log = log
        self.twitter_auth = Twython(api_key, api_secret, oauth_version=2)
        log.info(api_key)
        self.access_token = self.twitter_auth.obtain_access_token()
        self.twitter = Twython(api_key, access_token=self.access_token)

        log.info("Access_Token is {}".format(self.access_token))
        del api_secret, self.twitter_auth


        
        log.info("Deleted API Secret")

    def search_for_tweets(self, query=None, count=None):
        if count is None:
            count = 15

        return self.twitter.search(q=self.form_query_string(query), result_type='popular', count=count)

    def form_query_string(self, tags_to_search):
        """
        :param: tags_to_search - String
        :return:
        """

        if isinstance(tags_to_search, list):
            if (len(tags_to_search) > 1):

                return ",".join(tags_to_search).replace(',', ' OR ')
        print("Result is "+str(tags_to_search))
        return tags_to_search



