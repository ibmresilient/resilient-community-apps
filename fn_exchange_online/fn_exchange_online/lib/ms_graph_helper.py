# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

import logging
from resilient_circuits import FunctionError
from resilient_lib import OAuth2ClientCredentialsSession

log = logging.getLogger(__name__)

class MSGraphHelper(object):
    """
    Helper object MSGraphHelper.
    """
    def __init__(self, ms_graph_token_url, ms_graph_url, tenant_id, client_id, client_secret, proxies=None):
        self.__ms_graph_token_url = ms_graph_token_url.format(tenant_id)
        self.__ms_graph_url = ms_graph_url
        self.__tenant_id = tenant_id
        self.__client_id = client_id,
        self.__client_secret = client_secret
        self.__proxies = proxies
        self.__ms_graph_session = self.authenticate()

    def authenticate(self):
        """
        Authenticate and get oauth2 token for the session.
        """
        return OAuth2ClientCredentialsSession(url=self.__ms_graph_token_url,
                                              client_id=self.__client_id,
                                              client_secret=self.__client_secret,
                                              scope=['.default'],
                                              proxies=self.__proxies)

    def get_user_profile(self, email_address):
        """
        Query MS Graph user profile endpoint using the MS graph session.
        :param email_address: email address of the user profile requested
        :return: requests response from the users/profile endpoint
        """
        ms_graph_user_profile_url = u'{0}/users/{1}'.format(self.__ms_graph_url, email_address)
        response = self.__ms_graph_session.get(ms_graph_user_profile_url)

        # User not found (404) is a valid "error" so don't return error for that.
        if response.status_code >= 300 and response.status_code != 404:
            raise FunctionError("Invalid response from Microsoft Graph when trying to get user profile.")

        return response