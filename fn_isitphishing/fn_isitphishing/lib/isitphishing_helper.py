# (c) Copyright IBM Corp. 2025. All Rights Reserved.
# -*- coding: utf-8 -*-
"""
This module contains helper functions for the IsItPhishing function.
"""

from cachetools import TTLCache, cached
from resilient_lib import OAuth2ClientCredentialsSession

CACHE_TTL = 60 * 45     # 2700 seconds = 45 mins

class IsItPhishingHelper():
    """
    Helper class for the IsItPhishing function.
    """

    def __init__(self, phishing_url: str, oauth_url: str,
                 client_id: str, client_secret: str,
                 proxies: dict = None):
        self.phishing_url = phishing_url
        self.auth_url = oauth_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.proxies = proxies

    @cached(cache=TTLCache(maxsize=1, ttl=CACHE_TTL))
    def authenticate(self, client_id, client_secret):
        """
        Authenticate and get oauth2 token for the session.
        """
        session = OAuth2ClientCredentialsSession(url=self.auth_url,
                                                 client_id=client_id,
                                                 client_secret=client_secret,
                                                 scope=None,
                                                 proxies=self.proxies)

        return session.access_token if session else None
