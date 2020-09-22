# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
import logging
from resilient_lib import OAuth2ClientCredentialsSession
from resilient_lib.components.integration_errors import IntegrationError

LOG = logging.getLogger(__name__)
DEFAULT_SCOPE = 'https://graph.microsoft.com/.default'

class MSGraphHelper(object):
    """
    Helper object MSGraphHelper.
    """
    def __init__(self, ms_graph_token_url, ms_graph_url, tenant_id, client_id, client_secret, proxies=None):
        self.ms_graph_token_url = ms_graph_token_url.format(tenant=tenant_id)
        self.ms_graph_url = ms_graph_url
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.proxies = proxies
        self.ms_graph_session = self.authenticate()

    @staticmethod
    def check_ms_graph_response_code(status_code):
        """
        Check that the request status code: raise an integration error if great than 300 and code is "not found"
        :param status_code: request statues code
        :return:
        """
        if status_code >= 300 and status_code != 404:
            raise IntegrationError("Invalid response from Microsoft Graph API call.")

    def authenticate(self):
        """
        Authenticate and get oauth2 token for the session.
        """
        return OAuth2ClientCredentialsSession(url=self.ms_graph_token_url,
                                              client_id=self.client_id,
                                              client_secret=self.client_secret,
                                              scope=DEFAULT_SCOPE,
                                              proxies=self.proxies)

